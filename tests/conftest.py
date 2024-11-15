
import FreeCAD as App
from FreeCAD import Vector
import pytest

@pytest.fixture 
def freecad_document():
   doc_name = "boo"
   doc = App.newDocument(doc_name)
   yield doc
   App.closeDocument(doc_name)