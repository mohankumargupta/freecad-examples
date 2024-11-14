import FreeCAD as App
import FreeCADGui as Gui

freecad_file = "example001b.FCstd"
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

