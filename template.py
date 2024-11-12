import FreeCAD as App
import FreeCADGui as Gui
import Part # type: ignore
import Sketcher  # type: ignore
from document import createDocument, save_as
from const import Constraints

doc, body, sketch = createDocument()

# Use body and sketch here

save_as(doc, __file__)

