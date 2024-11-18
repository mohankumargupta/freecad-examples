import FreeCAD
from FreeCAD import Document
import importSVG

def create():
    doc: Document = FreeCAD.newDocument()
    importSVG.insert("applications/stencil-creator/twitter.svg", doc.Name)

if __name__ == "__main__":
    create()