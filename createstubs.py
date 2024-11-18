import FreeCAD as App
import runpy
import pybind11_stubgen
import sys

import Draft
import importSVG
import Sketcher
import Part


modules=["Draft", "importSVG","Part", "Sketcher"]

for i in range(len(modules)):
    sys.argv = ["pybind11_stubgen", modules[i]]
    runpy.run_module("pybind11_stubgen", run_name='__main__')


