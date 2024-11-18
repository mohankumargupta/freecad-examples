import FreeCAD
from FreeCAD import Document
import importSVG
from document import createDocumentAndBody



def create():
    doc, body = createDocumentAndBody()
    from freecad import module_io
    #module_io.OpenInsertObject("importSVG", "applications/stencil-creator/twitter.svg", "insert", doc.Name)
    importSVG.insert("applications/stencil-creator/twitter_inkscaped.svg", doc.Name)
    return doc

if __name__ == "__main__":
    create()