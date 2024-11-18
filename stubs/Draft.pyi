"""
Provide the Draft Workbench public programming interface.

The Draft module offers tools to create and manipulate 2D objects.
The functions in this file must be usable without requiring the
graphical user interface.
These functions can be used as the backend for the graphical commands
defined in `DraftTools.py`.
"""
import FreeCAD as App
from __future__ import annotations
from draftfunctions.array import array
from draftfunctions.cut import cut
from draftfunctions.downgrade import downgrade
from draftfunctions.draftify import draftify
from draftfunctions.dxf import getDXF
from draftfunctions.dxf import get_dxf
from draftfunctions.extrude import extrude
from draftfunctions.fuse import fuse
from draftfunctions.heal import heal
from draftfunctions.join import join_two_wires
from draftfunctions.join import join_two_wires as joinTwoWires
from draftfunctions.join import join_wires as joinWires
from draftfunctions.join import join_wires
from draftfunctions.mirror import mirror
from draftfunctions.move import copy_moved_edges
from draftfunctions.move import copy_moved_edges as copyMovedEdges
from draftfunctions.move import move
from draftfunctions.move import move_edge as moveEdge
from draftfunctions.move import move_edge
from draftfunctions.move import move_vertex as moveVertex
from draftfunctions.move import move_vertex
from draftfunctions.offset import offset
from draftfunctions.rotate import copy_rotated_edges as copyRotatedEdges
from draftfunctions.rotate import copy_rotated_edges
from draftfunctions.rotate import rotate
from draftfunctions.rotate import rotate_edge as rotateEdge
from draftfunctions.rotate import rotate_edge
from draftfunctions.rotate import rotate_vertex as rotateVertex
from draftfunctions.rotate import rotate_vertex
from draftfunctions.scale import copy_scaled_edges as copyScaledEdges
from draftfunctions.scale import copy_scaled_edges
from draftfunctions.scale import scale
from draftfunctions.scale import scale_edge as scaleEdge
from draftfunctions.scale import scale_edge
from draftfunctions.scale import scale_vertex
from draftfunctions.scale import scale_vertex as scaleVertex
from draftfunctions.split import split
from draftfunctions.svg import getSVG
from draftfunctions.svg import get_svg
from draftfunctions.upgrade import upgrade
from draftmake.make_arc_3points import make_arc_3points
from draftmake.make_array import makeArray
from draftmake.make_array import make_array
from draftmake.make_bezcurve import make_bezcurve
from draftmake.make_bezcurve import make_bezcurve as makeBezCurve
from draftmake.make_block import make_block as makeBlock
from draftmake.make_block import make_block
from draftmake.make_bspline import make_bspline as makeBSpline
from draftmake.make_bspline import make_bspline
from draftmake.make_circle import make_circle as makeCircle
from draftmake.make_circle import make_circle
from draftmake.make_circulararray import make_circular_array
from draftmake.make_clone import make_clone
from draftmake.make_clone import make_clone as clone
from draftmake.make_copy import make_copy
from draftmake.make_copy import make_copy as makeCopy
from draftmake.make_dimension import makeAngularDimension
from draftmake.make_dimension import makeDimension
from draftmake.make_dimension import make_angular_dimension
from draftmake.make_dimension import make_dimension
from draftmake.make_dimension import make_linear_dimension
from draftmake.make_dimension import make_linear_dimension_obj
from draftmake.make_dimension import make_radial_dimension_obj
from draftmake.make_ellipse import make_ellipse as makeEllipse
from draftmake.make_ellipse import make_ellipse
from draftmake.make_facebinder import make_facebinder as makeFacebinder
from draftmake.make_facebinder import make_facebinder
from draftmake.make_fillet import make_fillet
from draftmake.make_hatch import make_hatch
from draftmake.make_label import makeLabel
from draftmake.make_label import make_label
from draftmake.make_layer import make_layer
from draftmake.make_line import make_line
from draftmake.make_line import make_line as makeLine
from draftmake.make_orthoarray import make_ortho_array
from draftmake.make_orthoarray import make_ortho_array2d
from draftmake.make_orthoarray import make_rect_array
from draftmake.make_orthoarray import make_rect_array2d
from draftmake.make_patharray import makePathArray
from draftmake.make_patharray import make_path_array
from draftmake.make_patharray import make_path_twisted_array
from draftmake.make_point import make_point as makePoint
from draftmake.make_point import make_point
from draftmake.make_pointarray import makePointArray
from draftmake.make_pointarray import make_point_array
from draftmake.make_polararray import make_polar_array
from draftmake.make_polygon import make_polygon
from draftmake.make_polygon import make_polygon as makePolygon
from draftmake.make_rectangle import make_rectangle
from draftmake.make_rectangle import make_rectangle as makeRectangle
from draftmake.make_shape2dview import make_shape2dview
from draftmake.make_shape2dview import make_shape2dview as makeShape2DView
from draftmake.make_shapestring import make_shapestring
from draftmake.make_shapestring import make_shapestring as makeShapeString
from draftmake.make_sketch import make_sketch as makeSketch
from draftmake.make_sketch import make_sketch
from draftmake.make_text import convertDraftTexts
from draftmake.make_text import convert_draft_texts
from draftmake.make_text import makeText
from draftmake.make_text import make_text
from draftmake.make_wire import make_wire as makeWire
from draftmake.make_wire import make_wire
from draftmake.make_wpproxy import make_workingplaneproxy
from draftmake.make_wpproxy import make_workingplaneproxy as makeWorkingPlaneProxy
from draftobjects.array import Array as _Array
from draftobjects.array import Array
from draftobjects.base import DraftObject as _DraftObject
from draftobjects.base import DraftObject
from draftobjects.bezcurve import BezCurve as _BezCurve
from draftobjects.bezcurve import BezCurve
from draftobjects.block import Block as _Block
from draftobjects.block import Block
from draftobjects.bspline import BSpline
from draftobjects.bspline import BSpline as _BSpline
from draftobjects.circle import Circle as _Circle
from draftobjects.circle import Circle
from draftobjects.clone import Clone
from draftobjects.clone import Clone as _Clone
from draftobjects.dimension import AngularDimension
from draftobjects.dimension import AngularDimension as _AngularDimension
from draftobjects.dimension import LinearDimension as _Dimension
from draftobjects.dimension import LinearDimension
from draftobjects.draftlink import DraftLink
from draftobjects.draftlink import DraftLink as _DraftLink
from draftobjects.ellipse import Ellipse as _Ellipse
from draftobjects.ellipse import Ellipse
from draftobjects.facebinder import Facebinder as _Facebinder
from draftobjects.facebinder import Facebinder
from draftobjects.fillet import Fillet
from draftobjects.hatch import Hatch
from draftobjects.label import Label
from draftobjects.label import Label as DraftLabel
from draftobjects.layer import Layer as _VisGroup
from draftobjects.layer import Layer
from draftobjects.patharray import PathArray
from draftobjects.patharray import PathArray as _PathArray
from draftobjects.point import Point as _Point
from draftobjects.point import Point
from draftobjects.pointarray import PointArray
from draftobjects.pointarray import PointArray as _PointArray
from draftobjects.polygon import Polygon as _Polygon
from draftobjects.polygon import Polygon
from draftobjects.rectangle import Rectangle
from draftobjects.rectangle import Rectangle as _Rectangle
from draftobjects.shape2dview import Shape2DView
from draftobjects.shape2dview import Shape2DView as _Shape2DView
from draftobjects.shapestring import ShapeString
from draftobjects.shapestring import ShapeString as _ShapeString
from draftobjects.text import Text as DraftText
from draftobjects.text import Text
from draftobjects.wire import Wire
from draftobjects.wire import Wire as _Wire
from draftobjects.wpproxy import WorkingPlaneProxy
from draftutils.groups import getGroupContents
from draftutils.groups import getGroupNames
from draftutils.groups import getMovableChildren
from draftutils.groups import get_group_contents
from draftutils.groups import get_group_names
from draftutils.groups import get_movable_children
from draftutils.groups import get_windows
from draftutils.groups import is_group
from draftutils.groups import ungroup
from draftutils.gui_utils import apply_current_style
from draftutils.gui_utils import autogroup
from draftutils.gui_utils import dim_dash
from draftutils.gui_utils import dim_dash as dimDash
from draftutils.gui_utils import dim_symbol as dimSymbol
from draftutils.gui_utils import dim_symbol
from draftutils.gui_utils import end_all_events
from draftutils.gui_utils import format_object as formatObject
from draftutils.gui_utils import format_object
from draftutils.gui_utils import get_3d_view
from draftutils.gui_utils import get_3d_view as get3DView
from draftutils.gui_utils import get_bbox
from draftutils.gui_utils import get_diffuse_color
from draftutils.gui_utils import get_selection as getSelection
from draftutils.gui_utils import get_selection
from draftutils.gui_utils import get_selection_ex
from draftutils.gui_utils import get_selection_ex as getSelectionEx
from draftutils.gui_utils import load_texture
from draftutils.gui_utils import load_texture as loadTexture
from draftutils.gui_utils import remove_hidden
from draftutils.gui_utils import remove_hidden as removeHidden
from draftutils.gui_utils import select
from draftutils.utils import argb_to_rgba
from draftutils.utils import compare_objects as compareObjects
from draftutils.utils import compare_objects
from draftutils.utils import filter_objects_for_modifiers
from draftutils.utils import filter_objects_for_modifiers as filterObjectsForModifiers
from draftutils.utils import get_clone_base as getCloneBase
from draftutils.utils import get_clone_base
from draftutils.utils import get_objects_of_type as getObjectsOfType
from draftutils.utils import get_objects_of_type
from draftutils.utils import get_param
from draftutils.utils import get_param as getParam
from draftutils.utils import get_param_type
from draftutils.utils import get_param_type as getParamType
from draftutils.utils import get_real_name as getRealName
from draftutils.utils import get_real_name
from draftutils.utils import get_rgb
from draftutils.utils import get_rgb as getrgb
from draftutils.utils import get_rgba_tuple
from draftutils.utils import get_type
from draftutils.utils import get_type as getType
from draftutils.utils import is_clone as isClone
from draftutils.utils import is_clone
from draftutils.utils import is_closed_edge as isClosedEdge
from draftutils.utils import is_closed_edge
from draftutils.utils import load_svg_patterns as loadSvgPatterns
from draftutils.utils import load_svg_patterns
from draftutils.utils import precision
from draftutils.utils import print_shape
from draftutils.utils import print_shape as printShape
from draftutils.utils import rgba_to_argb
from draftutils.utils import set_param
from draftutils.utils import set_param as setParam
from draftutils.utils import shapify
from draftutils.utils import string_encode_coin
from draftutils.utils import string_encode_coin as stringencodecoin
from draftutils.utils import svg_patterns as svgpatterns
from draftutils.utils import svg_patterns
from draftutils.utils import tolerance
from draftutils.utils import type_check
from draftutils.utils import type_check as typecheck
from draftviewproviders.view_base import ViewProviderDraft
from draftviewproviders.view_base import ViewProviderDraft as _ViewProviderDraft
from draftviewproviders.view_base import ViewProviderDraftAlt as _ViewProviderDraftAlt
from draftviewproviders.view_base import ViewProviderDraftAlt
from draftviewproviders.view_base import ViewProviderDraftPart as _ViewProviderDraftPart
from draftviewproviders.view_base import ViewProviderDraftPart
from draftviewproviders.view_draftlink import ViewProviderDraftLink
from draftviewproviders.view_draftlink import ViewProviderDraftLink as _ViewProviderDraftLink
__all__ = ['AngularDimension', 'App', 'Array', 'BSpline', 'BezCurve', 'Block', 'Circle', 'Clone', 'DraftLabel', 'DraftLink', 'DraftObject', 'DraftText', 'Ellipse', 'Facebinder', 'Fillet', 'Hatch', 'Label', 'Layer', 'LinearDimension', 'PathArray', 'Point', 'PointArray', 'Polygon', 'Rectangle', 'Shape2DView', 'ShapeString', 'Text', 'ViewProviderDraft', 'ViewProviderDraftAlt', 'ViewProviderDraftLink', 'ViewProviderDraftPart', 'Wire', 'WorkingPlaneProxy', 'apply_current_style', 'argb_to_rgba', 'array', 'arrowtypes', 'autogroup', 'clone', 'compareObjects', 'compare_objects', 'convertDraftTexts', 'convert_draft_texts', 'copyMovedEdges', 'copyRotatedEdges', 'copyScaledEdges', 'copy_moved_edges', 'copy_rotated_edges', 'copy_scaled_edges', 'cut', 'dimDash', 'dimSymbol', 'dim_dash', 'dim_symbol', 'downgrade', 'draftify', 'end_all_events', 'extrude', 'filterObjectsForModifiers', 'filter_objects_for_modifiers', 'formatObject', 'format_object', 'fuse', 'get3DView', 'getCloneBase', 'getDXF', 'getGroupContents', 'getGroupNames', 'getMovableChildren', 'getObjectsOfType', 'getParam', 'getParamType', 'getRealName', 'getSVG', 'getSelection', 'getSelectionEx', 'getType', 'get_3d_view', 'get_bbox', 'get_clone_base', 'get_diffuse_color', 'get_dxf', 'get_group_contents', 'get_group_names', 'get_movable_children', 'get_objects_of_type', 'get_param', 'get_param_type', 'get_real_name', 'get_rgb', 'get_rgba_tuple', 'get_selection', 'get_selection_ex', 'get_svg', 'get_type', 'get_windows', 'getrgb', 'gui', 'heal', 'isClone', 'isClosedEdge', 'is_clone', 'is_closed_edge', 'is_group', 'joinTwoWires', 'joinWires', 'join_two_wires', 'join_wires', 'loadSvgPatterns', 'loadTexture', 'load_svg_patterns', 'load_texture', 'makeAngularDimension', 'makeArray', 'makeBSpline', 'makeBezCurve', 'makeBlock', 'makeCircle', 'makeCopy', 'makeDimension', 'makeEllipse', 'makeFacebinder', 'makeLabel', 'makeLine', 'makePathArray', 'makePoint', 'makePointArray', 'makePolygon', 'makeRectangle', 'makeShape2DView', 'makeShapeString', 'makeSketch', 'makeText', 'makeWire', 'makeWorkingPlaneProxy', 'make_angular_dimension', 'make_arc_3points', 'make_array', 'make_bezcurve', 'make_block', 'make_bspline', 'make_circle', 'make_circular_array', 'make_clone', 'make_copy', 'make_dimension', 'make_ellipse', 'make_facebinder', 'make_fillet', 'make_hatch', 'make_label', 'make_layer', 'make_line', 'make_linear_dimension', 'make_linear_dimension_obj', 'make_ortho_array', 'make_ortho_array2d', 'make_path_array', 'make_path_twisted_array', 'make_point', 'make_point_array', 'make_polar_array', 'make_polygon', 'make_radial_dimension_obj', 'make_rect_array', 'make_rect_array2d', 'make_rectangle', 'make_shape2dview', 'make_shapestring', 'make_sketch', 'make_text', 'make_wire', 'make_workingplaneproxy', 'mirror', 'move', 'moveEdge', 'moveVertex', 'move_edge', 'move_vertex', 'offset', 'precision', 'printShape', 'print_shape', 'removeHidden', 'remove_hidden', 'rgba_to_argb', 'rotate', 'rotateEdge', 'rotateVertex', 'rotate_edge', 'rotate_vertex', 'scale', 'scaleEdge', 'scaleVertex', 'scale_edge', 'scale_vertex', 'select', 'setParam', 'set_param', 'shapify', 'split', 'string_encode_coin', 'stringencodecoin', 'svg_patterns', 'svgpatterns', 'tolerance', 'type_check', 'typecheck', 'ungroup', 'upgrade']
__author__: str = 'Yorik van Havre, Werner Mayer, Martin Burbaum, Ken Cline, Dmitry Chigrin, Daniel Falck'
__title__: str = 'FreeCAD Draft Workbench'
__url__: str = 'https://www.freecad.org'
arrowtypes: list = ['Dot', 'Circle', 'Arrow', 'Tick', 'Tick-2']
gui: bool = False
