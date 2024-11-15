import FreeCAD as App
import FreeCADGui as Gui


freecad_file = "examples/example004.FCstd"
#freecad_file = "example002a.FCstd"
# Open FreeCAD

Gui.showMainWindow()
doc = App.openDocument(freecad_file)
App.setActiveDocument(doc.Name)
Gui.activateWorkbench("PartDesignWorkbench")

Gui.runCommand('Std_OrthographicCamera',1)

view = Gui.activeDocument().activeView()
view.viewIsometric()
view.fitAll()





#view = doc.ActiveView

#Gui.SendMsgToActiveView("ViewFit")
Gui.exec_loop()

