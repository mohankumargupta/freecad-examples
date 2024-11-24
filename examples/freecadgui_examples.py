

import FreeCAD as App
import FreeCADGui as Gui

#from example001a import create
#from example001b import create
from example001c import create
#from example004 import create
#from example005 import create
#from example006 import create
#from example007 import create
#from stencil import create
#from stencil_paddle import create
#from johnshirt_footrest import create


#freecad_file = "examples/example004.FCstd"
#freecad_file = "example002a.FCstd"
# Open FreeCAD

Gui.showMainWindow()
doc = create()
App.setActiveDocument(doc.Name)
Gui.activateWorkbench("PartDesignWorkbench")

Gui.runCommand('Std_OrthographicCamera',1)

view = Gui.activeDocument().activeView()
view.viewIsometric()
view.fitAll()
App.ActiveDocument.getObject("Body").Visibility = True

#Gui.Selection.addSelection('Unnamed','Body','Origin.')
#Gui.Selection.clearSelection()


#view = doc.ActiveView

#Gui.SendMsgToActiveView("ViewFit")
Gui.exec_loop()

