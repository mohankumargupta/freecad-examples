import FreeCAD as App
import FreeCADGui as Gui

#from example004 import create
from example005 import create


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




#view = doc.ActiveView

#Gui.SendMsgToActiveView("ViewFit")
Gui.exec_loop()

