"""
The functions in this module allow working with mesh objects.
A set of functions are provided for reading in registered mesh
file formats to either a new or existing document.

open(string) -- Create a new document and a Mesh feature
                to load the file into the document.
insert(string, string) -- Create a Mesh feature to load
                          the file into the given document.
Mesh() -- Create an empty mesh object.

"""
from __future__ import annotations
__all__ = ['Edge', 'Facet', 'Feature', 'Mesh', 'MeshPoint']
class Edge(PyObjectBase):
    """
    Edge in mesh
    This is an edge of a facet in a MeshObject. You can get it by e.g. iterating over the facets of a
    mesh and calling getEdge(index).
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def intersectWithEdge(Edge) -> list:
        """
        Get a list of intersection points with another edge.
        """
    @staticmethod
    def isCollinear(Edge) -> bool:
        """
        Checks if the two edges are collinear.
        """
    @staticmethod
    def isParallel(Edge) -> bool:
        """
        Checks if the two edges are parallel.
        """
    @staticmethod
    def unbound(*args, **kwargs):
        """
        method unbound()
        Cut the connection to a MeshObject. The edge becomes
        free and is more or less a simple edge.
        After calling unbound() no topological operation will
        work!
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
class Facet(PyObjectBase):
    """
    Facet in mesh
    This is a facet in a MeshObject. You can get it by e.g. iterating a
    mesh. The facet has a connection to its mesh and allows therefore
    topological operations. It is also possible to create an unbounded facet e.g. to create
    a mesh. In this case the topological operations will fail. The same is
    when you cut the bound to the mesh by calling unbound().
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def getEdge(int) -> Edge:
        """
        Returns the edge of the facet.
        """
    @staticmethod
    def intersect(Facet) -> list:
        """
        Get a list of intersection points with another triangle.
        """
    @staticmethod
    def isDeformed(*args, **kwargs):
        """
        isDegenerated(MinAngle, MaxAngle) -> boolean
        Returns true if the facet is deformed, otherwise false.
        A triangle is considered deformed if an angle is less than MinAngle
        or higher than MaxAngle.
        The two angles are given in radian.
        """
    @staticmethod
    def isDegenerated(*args, **kwargs) -> boolean:
        """
        Returns true if the facet is degenerated, otherwise false.
        """
    @staticmethod
    def unbound(*args, **kwargs):
        """
        method unbound()
        Cut the connection to a MeshObject. The facet becomes
        free and is more or less a simple facet.
        After calling unbound() no topological operation will
        work!
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
class Feature(App.GeoFeature):
    """
    The Mesh::Feature class handles meshes.
    The Mesh.MeshFeature() function is for internal use only and cannot be used to create instances of this class.
    Therefore you must have a reference to a document, e.g. 'd' then you can create an instance with
    d.addObject("Mesh::Feature").
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def countFacets(*args, **kwargs):
        """
        Return the number of facets of the mesh object
        """
    @staticmethod
    def countPoints(*args, **kwargs):
        """
        Return the number of vertices of the mesh object
        """
    @staticmethod
    def decimate(*args, **kwargs):
        """
        Decimate the mesh
                         decimate(tolerance(Float), reduction(Float))
                         tolerance: maximum error
                         reduction: reduction factor must be in the range [0.0,1.0]
                         Example:
                         mesh.decimate(0.5, 0.1) # reduction by up to 10 percent
                         mesh.decimate(0.5, 0.9) # reduction by up to 90 percent
        
                         or
        
                         decimate(targwt size(int))
                         mesh.decimate(mesh.CountFacets/2)
        """
    @staticmethod
    def fixDegenerations(*args, **kwargs):
        """
        Remove degenerated facets
        """
    @staticmethod
    def fixIndices(*args, **kwargs):
        """
        Repair any invalid indices
        """
    @staticmethod
    def fixSelfIntersections(*args, **kwargs):
        """
        Repair self-intersections
        """
    @staticmethod
    def harmonizeNormals(*args, **kwargs):
        """
        Adjust wrong oriented facets
        """
    @staticmethod
    def removeDuplicatedFacets(*args, **kwargs):
        """
        Remove duplicated facets
        """
    @staticmethod
    def removeDuplicatedPoints(*args, **kwargs):
        """
        Remove duplicated points
        """
    @staticmethod
    def removeFoldsOnSurface(*args, **kwargs):
        """
        Remove folds on surfaces
        """
    @staticmethod
    def removeInvalidPoints(*args, **kwargs):
        """
        Remove points with invalid coordinates (NaN)
        """
    @staticmethod
    def removeNonManifoldPoints(*args, **kwargs):
        """
        Remove non-manifold points
        """
    @staticmethod
    def removeNonManifolds(*args, **kwargs):
        """
        Remove non-manifolds
        """
    @staticmethod
    def smooth(*args, **kwargs):
        """
        Smooth the mesh data
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
class MeshPoint(PyObjectBase):
    """
    Point in mesh
    This is a point in a MeshObject. You can get it by e.g. iterating a
    mesh. The point has a connection to its mesh and allows therefore
    topological operations. It is also possible to create an unbounded mesh point e.g. to create
    a mesh. In this case the topological operations will fail. The same is
    when you cut the bound to the mesh by calling unbound().
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def unbound(*args, **kwargs):
        """
        method unbound()
        Cut the connection to a MeshObject. The point becomes
        free and is more or less a simple vector/point.
        After calling unbound() no topological operation will
        work!
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
Mesh = MeshObject
