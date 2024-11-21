
import FreeCAD as App
from FreeCAD import Vector
import pytest

@pytest.fixture 
def freecad_document():
   doc_name = "Untitles"
   doc = App.newDocument(doc_name)
   yield doc
   App.closeDocument(doc_name)

@pytest.fixture 
def sketch():
   doc_name = "Untitled"
   doc = App.newDocument(doc_name)
   sketch = doc.addObject('Sketcher::SketchObject', 'Sketch')
   yield sketch
   App.closeDocument(doc_name)

@pytest.fixture 
def document_and_sketches():
   doc_name = "Untitled"
   doc = App.newDocument(doc_name)
   sketch1 = doc.addObject('Sketcher::SketchObject', 'Sketch1')
   sketch2 = doc.addObject('Sketcher::SketchObject', 'Sketch2')
   yield doc, sketch1,sketch2
   App.closeDocument(doc_name)