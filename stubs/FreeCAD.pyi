"""
The functions in the FreeCAD module allow working with documents.
The FreeCAD instance provides a list of references of documents which
can be addressed by a string. Hence the document name must be unique.

The document has the read-only attribute FileName which points to the
file the document should be stored to.
"""
from App import Document
from App import DocumentObject
from App import DocumentObjectExtension
from App import DocumentObjectGroup
from App import Extension
from App import ExtensionContainer
from App import GeoFeature
from App import GeoFeatureGroupExtension
from App import GroupExtension
from App import LinkBaseExtension
from App import Material
from App import MeasureManager
from App import Metadata
from App import OriginGroupExtension
from App import PropertyContainer
from App import StringHasher
from App import StringID
from Base import Axis
from Base import BoundBox
from Base import Matrix
from Base import Placement
from Base import Rotation
from Base import Vector
import Units as Units
import __FreeCADBase__ as Base
import __FreeCADConsole__ as Console
import __Translate__ as Qt
from __future__ import annotations
from __main__ import FCADLogger as Logger
from __main__ import PropertyType
from __main__ import ReturnType
from __main__ import ScaleType
from __main__ import removeFromPath as _importFromFreeCAD
import typing
__all__ = ['ActiveDocument', 'Axis', 'Base', 'BoundBox', 'ConfigDump', 'ConfigGet', 'ConfigSet', 'Console', 'Document', 'DocumentObject', 'DocumentObjectExtension', 'DocumentObjectGroup', 'Extension', 'ExtensionContainer', 'GeoFeature', 'GeoFeatureGroupExtension', 'GroupExtension', 'GuiUp', 'LinkBaseExtension', 'Logger', 'Material', 'Matrix', 'MeasureManager', 'Metadata', 'OriginGroupExtension', 'ParamGet', 'Placement', 'PropertyContainer', 'PropertyType', 'Qt', 'ReturnType', 'Rotation', 'ScaleType', 'StringHasher', 'StringID', 'Units', 'Vector', 'Version', 'activeDocument', 'addDocumentObserver', 'addExportType', 'addImportType', 'changeExportModule', 'changeImportModule', 'checkAbort', 'checkLinkDepth', 'closeActiveTransaction', 'closeDocument', 'getActiveTransaction', 'getDependentObjects', 'getDocument', 'getExportType', 'getHelpDir', 'getHomePath', 'getImportType', 'getLibraryDir', 'getLinksTo', 'getLogLevel', 'getResourceDir', 'getTempPath', 'getUserAppDataDir', 'getUserCachePath', 'getUserConfigDir', 'getUserMacroDir', 'isRestoring', 'listDocuments', 'loadFile', 'newDocument', 'open', 'openDocument', 'removeDocumentObserver', 'saveParameter', 'setActiveDocument', 'setActiveTransaction', 'setLogLevel']
def ConfigDump(*args, **kwargs):
    """
    Dump the configuration to the output.
    """
def ConfigGet(*args, **kwargs):
    """
    ConfigGet(string) -- Get the value for the given key.
    """
def ConfigSet(*args, **kwargs):
    """
    ConfigSet(string, string) -- Set the given key to the given value.
    """
def ParamGet(*args, **kwargs):
    """
    Get parameters by path
    """
def Version(*args, **kwargs):
    """
    Print the version to the output.
    """
def activeDocument() -> object or None:
    """
    Return the active document or None if there is no one.
    """
def addDocumentObserver() -> None:
    """
    Add an observer to get notified about changes on documents.
    """
def addExportType(*args, **kwargs):
    """
    Register filetype for export
    """
def addImportType(*args, **kwargs):
    """
    Register filetype for import
    """
def changeExportModule(*args, **kwargs):
    """
    Change the export module name of a registered filetype
    """
def changeImportModule(*args, **kwargs):
    """
    Change the import module name of a registered filetype
    """
def checkAbort(*args, **kwargs):
    """
    checkAbort() -- check for user abort in length operation.
    
    This only works if there is an active sequencer (or ProgressIndicator in Python).
    There is an active sequencer during document restore and recomputation. User may
    abort the operation by pressing the ESC key. Once detected, this function will
    trigger a Base.FreeCADAbort exception.
    """
def checkLinkDepth(*args, **kwargs):
    """
    checkLinkDepth(depth) -- check link recursion depth
    """
def closeActiveTransaction(*args, **kwargs):
    """
    closeActiveTransaction(abort=False) -- commit or abort current active transaction
    """
def closeDocument(string) -> None:
    """
    Close the document with a given name.
    """
def getActiveTransaction(*args, **kwargs):
    """
    return the current active transaction name and ID
    """
def getDependentObjects(*args, **kwargs):
    """
    Return a list of dependent objects including the given objects.
    
    options: can have the following bit flags,
             1: to sort the list in topological order.
             2: to exclude dependency of Link type object.
    """
def getDocument(string) -> typing.Any:
    """
    Get a document by its name or raise an exception
    if there is no document with the given name.
    """
def getExportType(*args, **kwargs):
    """
    Get the name of the module that can export the filetype
    """
def getHelpDir(*args, **kwargs):
    """
    Get the directory of the documentation
    """
def getHomePath(*args, **kwargs):
    """
    Get the home path, i.e. the parent directory of the executable
    """
def getImportType(*args, **kwargs):
    """
    Get the name of the module that can import the filetype
    """
def getLibraryDir(*args, **kwargs):
    """
    Get the directory of all extension modules
    """
def getLinksTo(*args, **kwargs):
    """
    getLinksTo(obj,options=0,maxCount=0) -- return the objects linked to 'obj'
    
    options: 1: recursive, 2: check link array. Options can combine.
    maxCount: to limit the number of links returned
    """
def getLogLevel(*args, **kwargs):
    """
    getLogLevel(tag) -- Get the log level of a string tag
    """
def getResourceDir(*args, **kwargs):
    """
    Get the root directory of all resources
    """
def getTempPath(*args, **kwargs):
    """
    Get the root directory of cached files
    """
def getUserAppDataDir(*args, **kwargs):
    """
    Get the root directory of application data
    """
def getUserCachePath(*args, **kwargs):
    """
    Get the root path of cached files
    """
def getUserConfigDir(*args, **kwargs):
    """
    Get the root path of user config files
    """
def getUserMacroDir(bool = False) -> str:
    """
    Get the directory of the user's macro directory
    If parameter is False (the default) it returns the standard path in theuser's home directory, otherwise it returns the user-defined path.
    """
def isRestoring() -> bool:
    """
    Test if the application is opening some document
    """
def listDocuments(sort = False) -> list:
    """
    Return a list of names of all documents, optionally sort in dependency order.
    """
def loadFile(*args, **kwargs) -> None:
    """
    Loads an arbitrary file by delegating to the given Python module:
    * If no module is given it will be determined by the file extension.
    * If more than one module can load a file the first one will be taken.
    * If no module exists to load the file an exception will be raised.
    """
def newDocument(name, label = None, hidden = False, temp = False) -> typing.Any:
    """
    Create a new document with a given name.
    
    name: unique document name which is checked automatically.
    label: optional user changeable label for the document.
    hidden: whether to hide document 3D view.
    temp: mark the document as temporary so that it will not be saved
    """
def open(*args, **kwargs):
    """
    See openDocument(string)
    """
def openDocument(filepath, hidden = False) -> typing.Any:
    """
    Create a document and load the project file into the document.
    
    filepath: file path to an existing file. If the file doesn't exist
              or the file cannot be loaded an I/O exception is thrown.
              In this case the document is kept alive.
    hidden: whether to hide document 3D view.
    """
def removeDocumentObserver() -> None:
    """
    Remove an added document observer.
    """
def saveParameter(config = 'User parameter') -> None:
    """
    Save parameter set to file. The default set is 'User parameter'
    """
def setActiveDocument(*args, **kwargs):
    """
    setActiveDocement(string) -> None
    
    Set the active document by its name.
    """
def setActiveTransaction(*args, **kwargs):
    """
    setActiveTransaction(name, persist=False) -- setup active transaction with the given name
    
    name: the transaction name
    persist(False): by default, if the calling code is inside any invocation of a command, it
                    will be auto closed once all commands within the current stack exists. To
                    disable auto closing, set persist=True
    Returns the transaction ID for the active transaction. An application-wide
    active transaction causes any document changes to open a transaction with
    the given name and ID.
    """
def setLogLevel(*args, **kwargs):
    """
    setLogLevel(tag, level) -- Set the log level for a string tag.
    'level' can either be string 'Log', 'Msg', 'Wrn', 'Error', or an integer value
    """
ActiveDocument = None
GuiUp: int = 0
__ModDirs__: list = ['C:\\Users\\Mohan\\Downloads\\FreeCAD_weekly-builds-39153-conda-Windows-x86_64-py311\\Mod\\AddonManager', 'C:\\Users\\Mohan\\Downloads\\FreeCAD_weekly-builds-39153-conda-Windows-x86_64-py311\\Mod\\Assembly', 'C:\\Users\\Mohan\\Downloads\\FreeCAD_weekly-builds-39153-conda-Windows-x86_64-py311\\Mod\\BIM', 'C:\\Users\\Mohan\\Downloads\\FreeCAD_weekly-builds-39153-conda-Windows-x86_64-py311\\Mod\\CAM', 'C:\\Users\\Mohan\\Downloads\\FreeCAD_weekly-builds-39153-conda-Windows-x86_64-py311\\Mod\\Draft', 'C:\\Users\\Mohan\\Downloads\\FreeCAD_weekly-builds-39153-conda-Windows-x86_64-py311\\Mod\\Fem', 'C:\\Users\\Mohan\\Downloads\\FreeCAD_weekly-builds-39153-conda-Windows-x86_64-py311\\Mod\\Help', 'C:\\Users\\Mohan\\Downloads\\FreeCAD_weekly-builds-39153-conda-Windows-x86_64-py311\\Mod\\Idf', 'C:\\Users\\Mohan\\Downloads\\FreeCAD_weekly-builds-39153-conda-Windows-x86_64-py311\\Mod\\Import', 'C:\\Users\\Mohan\\Downloads\\FreeCAD_weekly-builds-39153-conda-Windows-x86_64-py311\\Mod\\Inspection', 'C:\\Users\\Mohan\\Downloads\\FreeCAD_weekly-builds-39153-conda-Windows-x86_64-py311\\Mod\\Material', 'C:\\Users\\Mohan\\Downloads\\FreeCAD_weekly-builds-39153-conda-Windows-x86_64-py311\\Mod\\Measure', 'C:\\Users\\Mohan\\Downloads\\FreeCAD_weekly-builds-39153-conda-Windows-x86_64-py311\\Mod\\Mesh', 'C:\\Users\\Mohan\\Downloads\\FreeCAD_weekly-builds-39153-conda-Windows-x86_64-py311\\Mod\\MeshPart', 'C:\\Users\\Mohan\\Downloads\\FreeCAD_weekly-builds-39153-conda-Windows-x86_64-py311\\Mod\\OpenSCAD', 'C:\\Users\\Mohan\\Downloads\\FreeCAD_weekly-builds-39153-conda-Windows-x86_64-py311\\Mod\\Part', 'C:\\Users\\Mohan\\Downloads\\FreeCAD_weekly-builds-39153-conda-Windows-x86_64-py311\\Mod\\PartDesign', 'C:\\Users\\Mohan\\Downloads\\FreeCAD_weekly-builds-39153-conda-Windows-x86_64-py311\\Mod\\Plot', 'C:\\Users\\Mohan\\Downloads\\FreeCAD_weekly-builds-39153-conda-Windows-x86_64-py311\\Mod\\Points', 'C:\\Users\\Mohan\\Downloads\\FreeCAD_weekly-builds-39153-conda-Windows-x86_64-py311\\Mod\\ReverseEngineering', 'C:\\Users\\Mohan\\Downloads\\FreeCAD_weekly-builds-39153-conda-Windows-x86_64-py311\\Mod\\Robot', 'C:\\Users\\Mohan\\Downloads\\FreeCAD_weekly-builds-39153-conda-Windows-x86_64-py311\\Mod\\Show', 'C:\\Users\\Mohan\\Downloads\\FreeCAD_weekly-builds-39153-conda-Windows-x86_64-py311\\Mod\\Sketcher', 'C:\\Users\\Mohan\\Downloads\\FreeCAD_weekly-builds-39153-conda-Windows-x86_64-py311\\Mod\\Spreadsheet', 'C:\\Users\\Mohan\\Downloads\\FreeCAD_weekly-builds-39153-conda-Windows-x86_64-py311\\Mod\\Start', 'C:\\Users\\Mohan\\Downloads\\FreeCAD_weekly-builds-39153-conda-Windows-x86_64-py311\\Mod\\Surface', 'C:\\Users\\Mohan\\Downloads\\FreeCAD_weekly-builds-39153-conda-Windows-x86_64-py311\\Mod\\TechDraw', 'C:\\Users\\Mohan\\Downloads\\FreeCAD_weekly-builds-39153-conda-Windows-x86_64-py311\\Mod\\Test', 'C:\\Users\\Mohan\\Downloads\\FreeCAD_weekly-builds-39153-conda-Windows-x86_64-py311\\Mod\\Tux', 'C:\\Users\\Mohan\\Downloads\\FreeCAD_weekly-builds-39153-conda-Windows-x86_64-py311\\Mod\\Web']
__cmake__: list = ['BUILD_ADDONMGR', 'BUILD_ASSEMBLY', 'BUILD_BIM', 'BUILD_CAM', 'BUILD_DRAFT', 'BUILD_DYNAMIC_LINK_PYTHON', 'BUILD_ENABLE_CXX_STD', 'BUILD_FEM', 'BUILD_FEM_NETGEN', 'BUILD_FEM_VTK', 'BUILD_FLAT_MESH', 'BUILD_GUI', 'BUILD_HELP', 'BUILD_IDF', 'BUILD_IMPORT', 'BUILD_INSPECTION', 'BUILD_MATERIAL', 'BUILD_MEASURE', 'BUILD_MESH', 'BUILD_MESH_PART', 'BUILD_OPENSCAD', 'BUILD_PART', 'BUILD_PART_DESIGN', 'BUILD_PLOT', 'BUILD_POINTS', 'BUILD_REVERSEENGINEERING', 'BUILD_ROBOT', 'BUILD_SHOW', 'BUILD_SKETCHER', 'BUILD_SMESH', 'BUILD_SPREADSHEET', 'BUILD_START', 'BUILD_SURFACE', 'BUILD_TECHDRAW', 'BUILD_TEST', 'BUILD_TUX', 'BUILD_WEB', 'BUILD_WITH_CONDA']
__unit_test__: list = ['TestAddonManagerApp', 'TestAssemblyWorkbench', 'TestCAMApp', 'TestDraft', 'TestFemApp', 'TestMaterialsApp', 'MeshTestsApp', 'TestPartApp', 'TestPartDesignApp', 'TestSketcherApp', 'TestSpreadsheet', 'TestSurfaceApp', 'TestTechDrawApp', 'BaseTests', 'UnitTests', 'Document', 'Metadata', 'StringHasher', 'UnicodeTests', 'TestPythonSyntax']
