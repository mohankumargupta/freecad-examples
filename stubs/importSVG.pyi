"""
Provides support for importing and exporting SVG files.

It enables importing/exporting objects directly to/from the 3D document
but doesn't handle the SVG output from the TechDraw module.

Currently it only reads the following entities:
* paths, lines, circular arcs, rects, circles, ellipses, polygons, polylines.

Currently unsupported:
* use, image.
"""
from Base import Vector
import Draft as Draft
import DraftVecUtils as DraftVecUtils
import FreeCAD as FreeCAD
from __future__ import annotations
from draftutils.messages import _err
from draftutils.messages import _msg
from draftutils.messages import _wrn
from draftutils import params
from draftutils.translate import translate
from draftutils import utils
from io import open as pyopen
import math as math
import os as os
import re as re
import xml as xml
__all__ = ['Draft', 'DraftVecUtils', 'FreeCAD', 'Vector', 'arccenter2end', 'arcend2center', 'draftui', 'export', 'getContents', 'getcolor', 'getrgb', 'getsize', 'gui', 'insert', 'makewire', 'math', 'open', 'os', 'params', 'pyopen', 're', 'svgHandler', 'svgcolors', 'svgcolorslower', 'transformCopyShape', 'translate', 'utils', 'xml']
class svgHandler(xml.sax.handler.ContentHandler):
    """
    Parse SVG files and create FreeCAD objects.
    """
    def __init__(self):
        ...
    def applyTrans(self, sh):
        """
        Apply transformation to the shape and return the new shape.
        
                Parameters
                ----------
                sh : Part.Shape or Draft.Dimension
                    Object to be transformed
                
        """
    def characters(self, content):
        """
        Read characters from the given string.
        """
    def endElement(self, name):
        """
        Finish processing the element indicated by the name.
        
                Parameters
                ----------
                name : str
                    The name of the element
                
        """
    def format(self, obj):
        """
        Apply styles to the object if the graphical interface is up.
        """
    def getMatrix(self, tr):
        """
        Return a FreeCAD matrix from an SVG transform attribute.
        
                Parameters
                ----------
                tr : str
                    The type of transform: 'matrix', 'translate', 'scale',
                    'rotate', 'skewX', 'skewY' and its value
        
                Returns
                -------
                Base::Matrix4D
                    The translated matrix.
                
        """
    def startElement(self, name, attrs):
        """
        Re-organize data into a nice clean dictionary.
        
                Parameters
                ----------
                name : str
                    Name of the element: 'path', 'rect', 'line', 'polyline',
                    'polygon', 'ellipse', 'circle', 'text', 'tspan', 'symbol'
                attrs : iterable
                    Dictionary of content of the elements
                
        """
    def translateVec(self, vec, mat):
        """
        Translate (move) a point or vector by a matrix.
        
                Parameters
                ----------
                vec : Base::Vector3
                    The original vector
                mat : Base::Matrix4D
                    The translation matrix, from which only the elements 14, 24, 34
                    are used.
                
        """
def arccenter2end(center, rx, ry, angle1, angledelta, xrotation = 0.0):
    """
    Calculate start and end points, and flags of an arc.
    
        Calculate start and end points, and flags of an arc given in
        ``center parametrization``.
        See http://www.w3.org/TR/SVG/implnote.html#ArcImplementationNotes
    
        Parameters
        ----------
        center : Base::Vector3
            Coordinates of the center of the ellipse.
        rx : float
            Radius of the ellipse, semi-major axis in the X direction
        ry : float
            Radius of the ellipse, semi-minor axis in the Y direction
        angle1 : float
            Initial angle in radians
        angledelta : float
            Additional angle in radians
        xrotation : float, optional
            Default 0. Rotation around the Z axis
    
        Returns
        -------
        v1, v2, largerc, sweep
            Tuple indicating the end points of the arc, and two boolean values
            indicating whether the arc is less than 180 degrees or not,
            and whether the angledelta is negative.
        
    """
def arcend2center(lastvec, currentvec, rx, ry, xrotation = 0.0, correction = False):
    """
    Calculate the possible centers for an arc in endpoint parameterization.
    
        Calculate (positive and negative) possible centers for an arc given in
        ``endpoint parametrization``.
        See http://www.w3.org/TR/SVG/implnote.html#ArcImplementationNotes
    
        the sweepflag is interpreted as: sweepflag <==>  arc is travelled clockwise
    
        Parameters
        ----------
        lastvec : Base::Vector3
            First point of the arc.
        currentvec : Base::Vector3
            End point (current) of the arc.
        rx : float
            Radius of the ellipse, semi-major axis in the X direction.
        ry : float
            Radius of the ellipse, semi-minor axis in the Y direction.
        xrotation : float, optional
            Default is 0. Rotation around the Z axis, in radians (CCW).
        correction : bool, optional
            Default is `False`. If it is `True`, the radii will be scaled
            by a factor.
    
        Returns
        -------
        list, (float, float)
            A tuple that consists of one list, and a tuple of radii.
        [(positive), (negative)], (rx, ry)
            The first element of the list is the positive tuple,
            the second is the negative tuple.
        [(Base::Vector3, float, float),
        (Base::Vector3, float, float)], (float, float)
            Types
        [(vcenter+, angle1+, angledelta+),
        (vcenter-, angle1-, angledelta-)], (rx, ry)
            The first element of the list is the positive tuple,
            consisting of center, angle, and angle increment;
            the second element is the negative tuple.
        
    """
def export(exportList, filename):
    """
    Export the SVG file with a given list of objects.
    
        The objects must be derived from Part::Feature, in order to be processed
        and exported.
    
        Parameters
        ----------
        exportList : list
            List of document objects to export.
        filename : str
            Path to the new file.
    
        Returns
        -------
        None
            If `exportList` doesn't have shapes to export.
        
    """
def getContents(filename, tag, stringmode = False):
    """
    Get the contents of all occurrences of the given tag in the file.
    
        Parameters
        ----------
        filename : str
            A filename to scan for tags.
        tag : str
            An SVG tag to find inside a file, for example, `some`
            in <some id="12">information</some>
        stringmode : bool, optional
            The default is False.
            If False, `filename` is a path to a file.
            If True, `filename` is already a pointer to an open file.
    
        Returns
        -------
        dict
            A dictionary with tagids and the information associated with that id
            results[tagid] = information
        
    """
def getcolor(color):
    """
    Check if the given string is an RGB value, or if it is a named color.
    
        Parameters
        ----------
        color : str
            Color in hexadecimal format, long '#12ab9f' or short '#1af'
    
        Returns
        -------
        tuple
        (r, g, b, a)
            RGBA float tuple, where each value is between 0.0 and 1.0.
        
    """
def getrgb(color):
    """
    Return an RGB hexadecimal string '#00aaff' from a FreeCAD color.
    
        Parameters
        ----------
        color : App::Color::Color
            FreeCAD color.
    
        Returns
        -------
        str
            The hexadecimal string representation of the color '#00aaff'.
        
    """
def getsize(length, mode = 'discard', base = 1):
    """
    Parse the length string containing number and unit.
    
        Parameters
        ----------
        length : str
            The length is a string, including sign, exponential notation,
            and unit: '+56215.14565E+6mm', '-23.156e-2px'.
        mode : str, optional
            One of 'discard', 'tuple', 'css90.0', 'css96.0', 'mm90.0', 'mm96.0'.
            'discard' (default), it discards the unit suffix, and extracts
                a number from the given string.
            'tuple', return number and unit as a tuple
            'css90.0', convert the unit to pixels assuming 90 dpi
            'css96.0', convert the unit to pixels assuming 96 dpi
            'mm90.0', convert the unit to millimeters assuming 90 dpi
            'mm96.0', convert the unit to millimeters assuming 96 dpi
        base : float, optional
            A base to scale the length.
    
        Returns
        -------
        float
            The numeric value of the length, as is, or transformed to
            millimeters or pixels.
        float, string
            A tuple with the numeric value, and the unit if `mode='tuple'`.
        
    """
def insert(filename, docname):
    """
    Get an active document and parse using the svgHandler().
    
        If no document exist, it is created.
    
        Parameters
        ----------
        filename : str
            The path to the filename to be opened.
        docname : str
            The name of the active App::Document if one exists, or
            of the new one created.
    
        Returns
        -------
        App::Document
            The active FreeCAD document, or the document created if none exists,
            with the parsed information.
        
    """
def makewire(path, checkclosed = False, donttry = False):
    """
    Try to make a wire out of the list of edges.
    
        If the wire functions fail or the wire is not closed,
        if required the TopoShapeCompoundPy::connectEdgesToWires()
        function is used.
    
        Parameters
        ----------
        path : Part.Edge
            A collection of edges
        checkclosed : bool, optional
            Default is `False`.
        donttry : bool, optional
            Default is `False`. If it's `True` it won't try to check
            for a closed path.
    
        Returns
        -------
        Part::Wire
            A wire created from the ordered edges.
        Part::Compound
            A compound made of the edges, but unable to form a wire.
        
    """
def open(filename):
    """
    Open filename and parse using the svgHandler().
    
        Parameters
        ----------
        filename : str
            The path to the filename to be opened.
    
        Returns
        -------
        App::Document
            The new FreeCAD document object created, with the parsed information.
        
    """
def transformCopyShape(shape, m):
    """
    Apply transformation matrix m on given shape.
    
        Since OCCT 6.8.0 transformShape can be used to apply certain
        non-orthogonal transformations on shapes. This way a conversion
        to BSplines in transformGeometry can be avoided.
    
        @sa: Part::TopoShape::transformGeometry(), TopoShapePy::transformGeometry()
        @sa: Part::TopoShape::transformShape(), TopoShapePy::transformShape()
    
        Parameters
        ----------
        shape : Part::TopoShape
            A given shape
        m : Base::Matrix4D
            A transformation matrix
    
        Returns
        -------
        shape : Part::TopoShape
            The shape transformed by the matrix
        
    """
__author__: str = 'Yorik van Havre, Sebastian Hoogen'
__title__: str = 'FreeCAD Draft Workbench - SVG importer/exporter'
__url__: str = 'https://www.freecad.org'
draftui = None
gui: bool = False
svgcolors: dict = {'Pink': (255, 192, 203), 'Blue': (0, 0, 255), 'Honeydew': (240, 255, 240), 'Purple': (128, 0, 128), 'Fuchsia': (255, 0, 255), 'LawnGreen': (124, 252, 0), 'Amethyst': (153, 102, 204), 'Crimson': (220, 20, 60), 'White': (255, 255, 255), 'NavajoWhite': (255, 222, 173), 'Cornsilk': (255, 248, 220), 'Bisque': (255, 228, 196), 'PaleGreen': (152, 251, 152), 'Brown': (165, 42, 42), 'DarkTurquoise': (0, 206, 209), 'DarkGreen': (0, 100, 0), 'MediumOrchid': (186, 85, 211), 'Chocolate': (210, 105, 30), 'PapayaWhip': (255, 239, 213), 'Olive': (128, 128, 0), 'Silver': (192, 192, 192), 'PeachPuff': (255, 218, 185), 'Plum': (221, 160, 221), 'DarkGoldenrod': (184, 134, 11), 'SlateGrey': (112, 128, 144), 'MintCream': (245, 255, 250), 'CornflowerBlue': (100, 149, 237), 'Gold': (255, 215, 0), 'HotPink': (255, 105, 180), 'DarkBlue': (0, 0, 139), 'LimeGreen': (50, 205, 50), 'DeepSkyBlue': (0, 191, 255), 'DarkKhaki': (189, 183, 107), 'LightGrey': (211, 211, 211), 'Yellow': (255, 255, 0), 'Gainsboro': (220, 220, 220), 'MistyRose': (255, 228, 225), 'SandyBrown': (244, 164, 96), 'DeepPink': (255, 20, 147), 'Magenta': (255, 0, 255), 'AliceBlue': (240, 248, 255), 'DarkCyan': (0, 139, 139), 'DarkSlateGrey': (47, 79, 79), 'GreenYellow': (173, 255, 47), 'DarkOrchid': (153, 50, 204), 'OliveDrab': (107, 142, 35), 'Chartreuse': (127, 255, 0), 'Peru': (205, 133, 63), 'Orange': (255, 165, 0), 'Red': (255, 0, 0), 'Wheat': (245, 222, 179), 'LightCyan': (224, 255, 255), 'LightSeaGreen': (32, 178, 170), 'BlueViolet': (138, 43, 226), 'LightSlateGrey': (119, 136, 153), 'Cyan': (0, 255, 255), 'MediumPurple': (147, 112, 219), 'MidnightBlue': (25, 25, 112), 'FireBrick': (178, 34, 34), 'PaleTurquoise': (175, 238, 238), 'PaleGoldenrod': (238, 232, 170), 'Gray': (128, 128, 128), 'MediumSeaGreen': (60, 179, 113), 'Moccasin': (255, 228, 181), 'Ivory': (255, 255, 240), 'DarkSlateBlue': (72, 61, 139), 'Beige': (245, 245, 220), 'Green': (0, 128, 0), 'SlateBlue': (106, 90, 205), 'Teal': (0, 128, 128), 'Azure': (240, 255, 255), 'LightSteelBlue': (176, 196, 222), 'DimGrey': (105, 105, 105), 'Tan': (210, 180, 140), 'AntiqueWhite': (250, 235, 215), 'SkyBlue': (135, 206, 235), 'GhostWhite': (248, 248, 255), 'MediumTurquoise': (72, 209, 204), 'FloralWhite': (255, 250, 240), 'LavenderBlush': (255, 240, 245), 'SeaGreen': (46, 139, 87), 'Lavender': (230, 230, 250), 'BlanchedAlmond': (255, 235, 205), 'DarkOliveGreen': (85, 107, 47), 'DarkSeaGreen': (143, 188, 143), 'SpringGreen': (0, 255, 127), 'Navy': (0, 0, 128), 'Orchid': (218, 112, 214), 'SaddleBrown': (139, 69, 19), 'IndianRed': (205, 92, 92), 'Snow': (255, 250, 250), 'SteelBlue': (70, 130, 180), 'MediumSlateBlue': (123, 104, 238), 'Black': (0, 0, 0), 'LightBlue': (173, 216, 230), 'Turquoise': (64, 224, 208), 'MediumVioletRed': (199, 21, 133), 'DarkViolet': (148, 0, 211), 'DarkGray': (169, 169, 169), 'Salmon': (250, 128, 114), 'DarkMagenta': (139, 0, 139), 'Tomato': (255, 99, 71), 'WhiteSmoke': (245, 245, 245), 'Goldenrod': (218, 165, 32), 'MediumSpringGreen': (0, 250, 154), 'DodgerBlue': (30, 144, 255), 'Aqua': (0, 255, 255), 'ForestGreen': (34, 139, 34), 'LemonChiffon': (255, 250, 205), 'LightSlateGray': (119, 136, 153), 'SlateGray': (112, 128, 144), 'LightGray': (211, 211, 211), 'Indigo': (75, 0, 130), 'CadetBlue': (95, 158, 160), 'LightYellow': (255, 255, 224), 'DarkOrange': (255, 140, 0), 'PowderBlue': (176, 224, 230), 'RoyalBlue': (65, 105, 225), 'Sienna': (160, 82, 45), 'Thistle': (216, 191, 216), 'Lime': (0, 255, 0), 'Seashell': (255, 245, 238), 'DarkRed': (139, 0, 0), 'LightSkyBlue': (135, 206, 250), 'YellowGreen': (154, 205, 50), 'Aquamarine': (127, 255, 212), 'LightCoral': (240, 128, 128), 'DarkSlateGray': (47, 79, 79), 'Khaki': (240, 230, 140), 'DarkGrey': (169, 169, 169), 'BurlyWood': (222, 184, 135), 'LightGoldenrodYellow': (250, 250, 210), 'MediumBlue': (0, 0, 205), 'DarkSalmon': (233, 150, 122), 'RosyBrown': (188, 143, 143), 'LightSalmon': (255, 160, 122), 'PaleVioletRed': (219, 112, 147), 'Coral': (255, 127, 80), 'Violet': (238, 130, 238), 'Grey': (128, 128, 128), 'LightGreen': (144, 238, 144), 'Linen': (250, 240, 230), 'OrangeRed': (255, 69, 0), 'DimGray': (105, 105, 105), 'Maroon': (128, 0, 0), 'LightPink': (255, 182, 193), 'MediumAquamarine': (102, 205, 170), 'OldLace': (253, 245, 230)}
svgcolorslower: dict = {'pink': (255, 192, 203), 'blue': (0, 0, 255), 'honeydew': (240, 255, 240), 'purple': (128, 0, 128), 'fuchsia': (255, 0, 255), 'lawngreen': (124, 252, 0), 'amethyst': (153, 102, 204), 'crimson': (220, 20, 60), 'white': (255, 255, 255), 'navajowhite': (255, 222, 173), 'cornsilk': (255, 248, 220), 'bisque': (255, 228, 196), 'palegreen': (152, 251, 152), 'brown': (165, 42, 42), 'darkturquoise': (0, 206, 209), 'darkgreen': (0, 100, 0), 'mediumorchid': (186, 85, 211), 'chocolate': (210, 105, 30), 'papayawhip': (255, 239, 213), 'olive': (128, 128, 0), 'silver': (192, 192, 192), 'peachpuff': (255, 218, 185), 'plum': (221, 160, 221), 'darkgoldenrod': (184, 134, 11), 'slategrey': (112, 128, 144), 'mintcream': (245, 255, 250), 'cornflowerblue': (100, 149, 237), 'gold': (255, 215, 0), 'hotpink': (255, 105, 180), 'darkblue': (0, 0, 139), 'limegreen': (50, 205, 50), 'deepskyblue': (0, 191, 255), 'darkkhaki': (189, 183, 107), 'lightgrey': (211, 211, 211), 'yellow': (255, 255, 0), 'gainsboro': (220, 220, 220), 'mistyrose': (255, 228, 225), 'sandybrown': (244, 164, 96), 'deeppink': (255, 20, 147), 'magenta': (255, 0, 255), 'aliceblue': (240, 248, 255), 'darkcyan': (0, 139, 139), 'darkslategrey': (47, 79, 79), 'greenyellow': (173, 255, 47), 'darkorchid': (153, 50, 204), 'olivedrab': (107, 142, 35), 'chartreuse': (127, 255, 0), 'peru': (205, 133, 63), 'orange': (255, 165, 0), 'red': (255, 0, 0), 'wheat': (245, 222, 179), 'lightcyan': (224, 255, 255), 'lightseagreen': (32, 178, 170), 'blueviolet': (138, 43, 226), 'lightslategrey': (119, 136, 153), 'cyan': (0, 255, 255), 'mediumpurple': (147, 112, 219), 'midnightblue': (25, 25, 112), 'firebrick': (178, 34, 34), 'paleturquoise': (175, 238, 238), 'palegoldenrod': (238, 232, 170), 'gray': (128, 128, 128), 'mediumseagreen': (60, 179, 113), 'moccasin': (255, 228, 181), 'ivory': (255, 255, 240), 'darkslateblue': (72, 61, 139), 'beige': (245, 245, 220), 'green': (0, 128, 0), 'slateblue': (106, 90, 205), 'teal': (0, 128, 128), 'azure': (240, 255, 255), 'lightsteelblue': (176, 196, 222), 'dimgrey': (105, 105, 105), 'tan': (210, 180, 140), 'antiquewhite': (250, 235, 215), 'skyblue': (135, 206, 235), 'ghostwhite': (248, 248, 255), 'mediumturquoise': (72, 209, 204), 'floralwhite': (255, 250, 240), 'lavenderblush': (255, 240, 245), 'seagreen': (46, 139, 87), 'lavender': (230, 230, 250), 'blanchedalmond': (255, 235, 205), 'darkolivegreen': (85, 107, 47), 'darkseagreen': (143, 188, 143), 'springgreen': (0, 255, 127), 'navy': (0, 0, 128), 'orchid': (218, 112, 214), 'saddlebrown': (139, 69, 19), 'indianred': (205, 92, 92), 'snow': (255, 250, 250), 'steelblue': (70, 130, 180), 'mediumslateblue': (123, 104, 238), 'black': (0, 0, 0), 'lightblue': (173, 216, 230), 'turquoise': (64, 224, 208), 'mediumvioletred': (199, 21, 133), 'darkviolet': (148, 0, 211), 'darkgray': (169, 169, 169), 'salmon': (250, 128, 114), 'darkmagenta': (139, 0, 139), 'tomato': (255, 99, 71), 'whitesmoke': (245, 245, 245), 'goldenrod': (218, 165, 32), 'mediumspringgreen': (0, 250, 154), 'dodgerblue': (30, 144, 255), 'aqua': (0, 255, 255), 'forestgreen': (34, 139, 34), 'lemonchiffon': (255, 250, 205), 'lightslategray': (119, 136, 153), 'slategray': (112, 128, 144), 'lightgray': (211, 211, 211), 'indigo': (75, 0, 130), 'cadetblue': (95, 158, 160), 'lightyellow': (255, 255, 224), 'darkorange': (255, 140, 0), 'powderblue': (176, 224, 230), 'royalblue': (65, 105, 225), 'sienna': (160, 82, 45), 'thistle': (216, 191, 216), 'lime': (0, 255, 0), 'seashell': (255, 245, 238), 'darkred': (139, 0, 0), 'lightskyblue': (135, 206, 250), 'yellowgreen': (154, 205, 50), 'aquamarine': (127, 255, 212), 'lightcoral': (240, 128, 128), 'darkslategray': (47, 79, 79), 'khaki': (240, 230, 140), 'darkgrey': (169, 169, 169), 'burlywood': (222, 184, 135), 'lightgoldenrodyellow': (250, 250, 210), 'mediumblue': (0, 0, 205), 'darksalmon': (233, 150, 122), 'rosybrown': (188, 143, 143), 'lightsalmon': (255, 160, 122), 'palevioletred': (219, 112, 147), 'coral': (255, 127, 80), 'violet': (238, 130, 238), 'grey': (128, 128, 128), 'lightgreen': (144, 238, 144), 'linen': (250, 240, 230), 'orangered': (255, 69, 0), 'dimgray': (105, 105, 105), 'maroon': (128, 0, 0), 'lightpink': (255, 182, 193), 'mediumaquamarine': (102, 205, 170), 'oldlace': (253, 245, 230)}
