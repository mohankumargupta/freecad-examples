"""
This module is the Sketcher module.
"""
from __future__ import annotations
__all__ = ['Constraint', 'ExternalGeometryExtension', 'ExternalGeometryFacade', 'GeometryFacade', 'Sketch', 'SketchGeometryExtension']
class Constraint(Base.Persistence):
    """
    With this object you can handle sketches
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __delattr__(self, name):
        """
        Implement delattr(self, name).
        """
    def __getattribute__(self, name):
        """
        Return getattr(self, name).
        """
    def __repr__(self):
        """
        Return repr(self).
        """
    def __setattr__(self, name, value):
        """
        Implement setattr(self, name, value).
        """
class ExternalGeometryExtension(Part.GeometryExtension):
    """
    Describes a ExternalGeometryExtension
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def setFlag(*args, **kwargs):
        """
        sets the given bit to true/false.
        """
    @staticmethod
    def testFlag(*args, **kwargs):
        """
        returns a boolean indicating whether the given bit is set.
        """
    def __delattr__(self, name):
        """
        Implement delattr(self, name).
        """
    def __getattribute__(self, name):
        """
        Return getattr(self, name).
        """
    def __repr__(self):
        """
        Return repr(self).
        """
    def __setattr__(self, name, value):
        """
        Implement setattr(self, name, value).
        """
class ExternalGeometryFacade(Base.BaseClass):
    """
    Describes a GeometryFacade
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def deleteExtensionOfName(*args, **kwargs):
        """
        Deletes all extensions of the indicated name.
        """
    @staticmethod
    def deleteExtensionOfType(*args, **kwargs):
        """
        Deletes all extensions of the indicated type.
        """
    @staticmethod
    def getExtensionOfName(*args, **kwargs):
        """
        Gets the first geometry extension of the name indicated by the string.
        """
    @staticmethod
    def getExtensionOfType(*args, **kwargs):
        """
        Gets the first geometry extension of the type indicated by the string.
        """
    @staticmethod
    def getExtensions(*args, **kwargs):
        """
        Returns a list with information about the geometry extensions.
        """
    @staticmethod
    def hasExtensionOfName(*args, **kwargs):
        """
        Returns a boolean indicating whether a geometry extension with the name indicated as a string exists.
        """
    @staticmethod
    def hasExtensionOfType(*args, **kwargs):
        """
        Returns a boolean indicating whether a geometry extension of the type indicated as a string exists.
        """
    @staticmethod
    def mirror(*args, **kwargs):
        """
        Performs the symmetrical transformation of this geometric object
        """
    @staticmethod
    def rotate(*args, **kwargs):
        """
        Rotates this geometric object at angle Ang (in radians) about axis
        """
    @staticmethod
    def scale(*args, **kwargs):
        """
        Applies a scaling transformation on this geometric object with a center and scaling factor
        """
    @staticmethod
    def setExtension(*args, **kwargs):
        """
        Sets a geometry extension of the indicated type.
        """
    @staticmethod
    def setFlag(*args, **kwargs):
        """
        Sets the given bit to true/false.
        """
    @staticmethod
    def testFlag(*args, **kwargs):
        """
        Returns a boolean indicating whether the given bit is set.
        """
    @staticmethod
    def transform(*args, **kwargs):
        """
        Applies a transformation to this geometric object
        """
    @staticmethod
    def translate(*args, **kwargs):
        """
        Translates this geometric object
        """
    def __delattr__(self, name):
        """
        Implement delattr(self, name).
        """
    def __getattribute__(self, name):
        """
        Return getattr(self, name).
        """
    def __repr__(self):
        """
        Return repr(self).
        """
    def __setattr__(self, name, value):
        """
        Implement setattr(self, name, value).
        """
class GeometryFacade(Base.BaseClass):
    """
    Describes a GeometryFacade
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def deleteExtensionOfName(*args, **kwargs):
        """
        Deletes all extensions of the indicated name.
        """
    @staticmethod
    def deleteExtensionOfType(*args, **kwargs):
        """
        Deletes all extensions of the indicated type.
        """
    @staticmethod
    def getExtensionOfName(*args, **kwargs):
        """
        Gets the first geometry extension of the name indicated by the string.
        """
    @staticmethod
    def getExtensionOfType(*args, **kwargs):
        """
        Gets the first geometry extension of the type indicated by the string.
        """
    @staticmethod
    def getExtensions(*args, **kwargs):
        """
        Returns a list with information about the geometry extensions.
        """
    @staticmethod
    def hasExtensionOfName(*args, **kwargs):
        """
        Returns a boolean indicating whether a geometry extension with the name indicated as a string exists.
        """
    @staticmethod
    def hasExtensionOfType(*args, **kwargs):
        """
        Returns a boolean indicating whether a geometry extension of the type indicated as a string exists.
        """
    @staticmethod
    def mirror(*args, **kwargs):
        """
        Performs the symmetrical transformation of this geometric object
        """
    @staticmethod
    def rotate(*args, **kwargs):
        """
        Rotates this geometric object at angle Ang (in radians) about axis
        """
    @staticmethod
    def scale(*args, **kwargs):
        """
        Applies a scaling transformation on this geometric object with a center and scaling factor
        """
    @staticmethod
    def setExtension(*args, **kwargs):
        """
        Sets a geometry extension of the indicated type.
        """
    @staticmethod
    def setGeometryMode(*args, **kwargs):
        """
        Sets the given bit to true/false.
        """
    @staticmethod
    def testGeometryMode(*args, **kwargs):
        """
        Returns a boolean indicating whether the given bit is set.
        """
    @staticmethod
    def transform(*args, **kwargs):
        """
        Applies a transformation to this geometric object
        """
    @staticmethod
    def translate(*args, **kwargs):
        """
        Translates this geometric object
        """
    def __delattr__(self, name):
        """
        Implement delattr(self, name).
        """
    def __getattribute__(self, name):
        """
        Return getattr(self, name).
        """
    def __repr__(self):
        """
        Return repr(self).
        """
    def __setattr__(self, name, value):
        """
        Implement setattr(self, name, value).
        """
class Sketch(Base.Persistence):
    """
    With this objects you can handle constraint sketches
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def addConstraint(*args, **kwargs):
        """
        add an constraint object to the sketch
        """
    @staticmethod
    def addGeometry(*args, **kwargs):
        """
        add a geometric object to the sketch
        """
    @staticmethod
    def clear(*args, **kwargs):
        """
        clear the sketch
        """
    @staticmethod
    def movePoint(*args, **kwargs):
        """
                  to another location.
                  It moves the specified point (or curve) to the given location by adding some
                  temporary weak constraints and solve the sketch.
                  This method is mostly used to allow the user to drag some portions of the sketch
                  in real time by e.g. the mouse and it works only for underconstrained portions of
                  the sketch.
                  The argument 'relative', if present, states if the new location is given
                  relatively to the current one.
        """
    @staticmethod
    def solve(*args, **kwargs):
        """
        solve the actual set of geometry and constraints
        """
    def __delattr__(self, name):
        """
        Implement delattr(self, name).
        """
    def __getattribute__(self, name):
        """
        Return getattr(self, name).
        """
    def __repr__(self):
        """
        Return repr(self).
        """
    def __setattr__(self, name, value):
        """
        Implement setattr(self, name, value).
        """
class SketchGeometryExtension(Part.GeometryExtension):
    """
    Describes a SketchGeometryExtension
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def setGeometryMode(*args, **kwargs):
        """
        Sets the given bit to true/false.
        """
    @staticmethod
    def testGeometryMode(*args, **kwargs):
        """
        Returns a boolean indicating whether the given bit is set.
        """
    def __delattr__(self, name):
        """
        Implement delattr(self, name).
        """
    def __getattribute__(self, name):
        """
        Return getattr(self, name).
        """
    def __repr__(self):
        """
        Return repr(self).
        """
    def __setattr__(self, name, value):
        """
        Implement setattr(self, name, value).
        """
