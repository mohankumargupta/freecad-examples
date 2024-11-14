from pathlib import Path
import FreeCAD as App

from const import Plane

def createDocument():
    doc = App.newDocument()
    body = doc.addObject('PartDesign::Body', 'Body')
    sketch = doc.addObject('Sketcher::SketchObject', 'Sketch')
    return doc, body, sketch

def createDocumentAndBody():
    doc = App.newDocument()
    body = doc.addObject('PartDesign::Body', 'Body')
    return doc, body

def createSketch(doc:App.Document, name, plane: Plane = Plane.XY):
    sketch = doc.addObject('Sketcher::SketchObject', name)
    match plane:
        case Plane.YZ:
            yz_plane = doc.getObject('YZ_Plane')
            sketch.AttachmentSupport = [(yz_plane, '')]
            sketch.MapMode = 'FlatFace'

        case Plane.XY:
            return

        case _:
            return

    return sketch

def save_as(doc, fullpath):
    path = Path(fullpath)
    filename_without_extension = path.with_suffix("").name
    old = Path(f"{filename_without_extension}.FCStd")
    if old.exists():
        old.unlink()
    doc.saveAs(f"{filename_without_extension}.FCStd")
