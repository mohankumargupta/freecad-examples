"""
This is a module working with shapes.
"""
from Attacher import AttachEngine
import BRepFeat as BRepFeat
import BRepOffsetAPI as BRepOffsetAPI
from Base import Precision
import ChFi2d as ChFi2d
import Geom2d as Geom2d
import GeomPlate as GeomPlate
import HLRBRep as HLRBRep
import ShapeFix as ShapeFix
import ShapeUpgrade as ShapeUpgrade
from __future__ import annotations
__all__ = ['Arc', 'ArcOfCircle', 'ArcOfConic', 'ArcOfEllipse', 'ArcOfHyperbola', 'ArcOfParabola', 'AttachEngine', 'BRepFeat', 'BRepOffsetAPI', 'BSplineCurve', 'BSplineSurface', 'BezierCurve', 'BezierSurface', 'BodyBase', 'ChFi2d', 'Circle', 'CompSolid', 'Compound', 'Cone', 'Conic', 'Cylinder', 'Edge', 'Ellipse', 'Face', 'Feature', 'Geom2d', 'GeomPlate', 'GeometryBoolExtension', 'GeometryDoubleExtension', 'GeometryIntExtension', 'GeometryStringExtension', 'HLRBRep', 'Hyperbola', 'Line', 'LineSegment', 'OCCConstructionError', 'OCCDimensionError', 'OCCDomainError', 'OCCError', 'OCCRangeError', 'OCC_VERSION', 'OffsetCurve', 'OffsetSurface', 'Parabola', 'Part2DObject', 'Plane', 'PlateSurface', 'Point', 'Precision', 'RectangularTrimmedSurface', 'Shape', 'ShapeFix', 'ShapeUpgrade', 'Shell', 'Solid', 'Sphere', 'SurfaceOfExtrusion', 'SurfaceOfRevolution', 'Toroid', 'Vertex', 'Wire']
class Arc(TrimmedCurve):
    """
    Describes a portion of a curve
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
class ArcOfCircle(ArcOfConic):
    """
    Describes a portion of a circle
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
class ArcOfConic(TrimmedCurve):
    """
    Describes a portion of a conic
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
class ArcOfEllipse(ArcOfConic):
    """
    Describes a portion of an ellipse
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
class ArcOfHyperbola(ArcOfConic):
    """
    Describes a portion of an hyperbola
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
class ArcOfParabola(ArcOfConic):
    """
    Describes a portion of an parabola
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
class BSplineCurve(BoundedCurve):
    """
    Describes a B-Spline curve in 3D space
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def __reduce__():
        """
        Serialization of Part.BSplineCurve objects
        """
    @staticmethod
    def approximate(*args, **kwargs):
        """
        Replaces this B-Spline curve by approximating a set of points.
                            The function accepts keywords as arguments.
        
                            approximate(Points = list_of_points)
        
                            Optional arguments :
        
                            DegMin = integer (3) : Minimum degree of the curve.
                            DegMax = integer (8) : Maximum degree of the curve.
                            Tolerance = float (1e-3) : approximating tolerance.
                            Continuity = string ('C2') : Desired continuity of the curve.
                            Possible values : 'C0','G1','C1','G2','C2','C3','CN'
        
                            LengthWeight = float, CurvatureWeight = float, TorsionWeight = float
                            If one of these arguments is not null, the functions approximates the
                            points using variational smoothing algorithm, which tries to minimize
                            additional criterium:
                            LengthWeight*CurveLength + CurvatureWeight*Curvature + TorsionWeight*Torsion
                                                Continuity must be C0, C1(with DegMax >= 3) or C2(with DegMax >= 5).
        
                            Parameters = list of floats : knot sequence of the approximated points.
                            This argument is only used if the weights above are all null.
        
                            ParamType = string ('Uniform','Centripetal' or 'ChordLength')
                            Parameterization type. Only used if weights and Parameters above aren't specified.
        
                            Note : Continuity of the spline defaults to C2. However, it may not be applied if
                            it conflicts with other parameters ( especially DegMax ).
        """
    @staticmethod
    def buildFromPoles(*args, **kwargs):
        """
        Builds a B-Spline by a list of poles.
                            arguments: poles (sequence of Base.Vector), [periodic (default is False), degree (default is 3), interpolate (default is False)]
        
                            Examples:
                            from FreeCAD import Base
                            import Part
                            V = Base.Vector
                            poles = [V(-2, 2, 0),V(0, 2, 1),V(2, 2, 0),V(2, -2, 0),V(0, -2, 1),V(-2, -2, 0)]
        
                            # non-periodic spline
                            n=Part.BSplineCurve()
                            n.buildFromPoles(poles)
                            Part.show(n.toShape())
        
                            # periodic spline
                            n=Part.BSplineCurve()
                            n.buildFromPoles(poles, True)
                            Part.show(n.toShape())
        """
    @staticmethod
    def buildFromPolesMultsKnots(*args, **kwargs):
        """
        Builds a B-Spline by a lists of Poles, Mults, Knots.
                        arguments: poles (sequence of Base.Vector), [mults , knots, periodic, degree, weights (sequence of float), CheckRational]
        
                        Examples:
                        from FreeCAD import Base
                        import Part
                        V=Base.Vector
                        poles=[V(-10,-10),V(10,-10),V(10,10),V(-10,10)]
        
                        # non-periodic spline
                        n=Part.BSplineCurve()
                        n.buildFromPolesMultsKnots(poles,(3,1,3),(0,0.5,1),False,2)
                        Part.show(n.toShape())
        
                        # periodic spline
                        p=Part.BSplineCurve()
                        p.buildFromPolesMultsKnots(poles,(1,1,1,1,1),(0,0.25,0.5,0.75,1),True,2)
                        Part.show(p.toShape())
        
                        # periodic and rational spline
                        r=Part.BSplineCurve()
                        r.buildFromPolesMultsKnots(poles,(1,1,1,1,1),(0,0.25,0.5,0.75,1),True,2,(1,0.8,0.7,0.2))
                        Part.show(r.toShape())
        """
    @staticmethod
    def getCardinalSplineTangents(*args, **kwargs):
        """
        Compute the tangents for a Cardinal spline
        """
    @staticmethod
    def getKnot(*args, **kwargs):
        """
        Get a knot of the B-Spline curve.
        """
    @staticmethod
    def getKnots(*args, **kwargs):
        """
        Get all knots of the B-Spline curve.
        """
    @staticmethod
    def getMultiplicities(*args, **kwargs):
        """
        Returns the multiplicities table M of the knots of this B-Spline curve.
        """
    @staticmethod
    def getMultiplicity(*args, **kwargs):
        """
        Returns the multiplicity of the knot of index
        from the knots table of this B-Spline curve.
        """
    @staticmethod
    def getPole(*args, **kwargs):
        """
        Get a pole of the B-Spline curve.
        """
    @staticmethod
    def getPoles(*args, **kwargs):
        """
        Get all poles of the B-Spline curve.
        """
    @staticmethod
    def getPolesAndWeights(*args, **kwargs):
        """
        Returns the table of poles and weights in homogeneous coordinates.
        """
    @staticmethod
    def getResolution(*args, **kwargs):
        """
        Computes for this B-Spline curve the parametric tolerance (UTolerance)
        for a given 3D tolerance (Tolerance3D).
        If f(t) is the equation of this B-Spline curve, the parametric tolerance
        ensures that:
        |t1-t0| < UTolerance =""==> |f(t1)-f(t0)| < Tolerance3D
        """
    @staticmethod
    def getWeight(*args, **kwargs):
        """
        Get a weight of the B-Spline curve.
        """
    @staticmethod
    def getWeights(*args, **kwargs):
        """
        Get all weights of the B-Spline curve.
        """
    @staticmethod
    def increaseDegree(*args, **kwargs):
        """
        increase(Int=Degree)
        Increases the degree of this B-Spline curve to Degree.
        As a result, the poles, weights and multiplicities tables
        are modified; the knots table is not changed. Nothing is
        done if Degree is less than or equal to the current degree.
        """
    @staticmethod
    def increaseMultiplicity(*args, **kwargs):
        """
                        increaseMultiplicity(int start, int end, int mult)
                        Increases multiplicity of knots up to mult.
        
                        index: the index of a knot to modify (1-based)
                        start, end: index range of knots to modify.
                        If mult is lower or equal to the current multiplicity nothing is done. If mult is higher than the degree the degree is used.
        """
    @staticmethod
    def incrementMultiplicity(*args, **kwargs):
        """
                        Raises multiplicity of knots by mult.
        
                        start, end: index range of knots to modify.
        """
    @staticmethod
    def insertKnot(u, mult = 1, tol = 0.0):
        """
                        Inserts a knot value in the sequence of knots. If u is an existing knot the
                        multiplicity is increased by mult.
        """
    @staticmethod
    def insertKnots(list_of_floats, list_of_ints, tol = 0.0, bool_add = True):
        """
                        Inserts a set of knots values in the sequence of knots.
        
                        For each u = list_of_floats[i], mult = list_of_ints[i]
        
                        If u is an existing knot the multiplicity is increased by mult if bool_add is
                        True, otherwise increased to mult.
        
                        If u is not on the parameter range nothing is done.
        
                        If the multiplicity is negative or null nothing is done. The new multiplicity
                        is limited to the degree.
        
                        The tolerance criterion for knots equality is the max of Epsilon(U) and ParametricTolerance.
        """
    @staticmethod
    def interpolate(*args, **kwargs):
        """
        Replaces this B-Spline curve by interpolating a set of points.
                            The function accepts keywords as arguments.
        
                            interpolate(Points = list_of_points)
        
                            Optional arguments :
        
                            PeriodicFlag = bool (False) : Sets the curve closed or opened.
                            Tolerance = float (1e-6) : interpolating tolerance
        
                            Parameters : knot sequence of the interpolated points.
                            If not supplied, the function defaults to chord-length parameterization.
                            If PeriodicFlag == True, one extra parameter must be appended.
        
                            EndPoint Tangent constraints :
        
                            InitialTangent = vector, FinalTangent = vector
                            specify tangent vectors for starting and ending points
                            of the BSpline. Either none, or both must be specified.
        
                            Full Tangent constraints :
        
                            Tangents = list_of_vectors, TangentFlags = list_of_bools
                            Both lists must have the same length as Points list.
                            Tangents specifies the tangent vector of each point in Points list.
                            TangentFlags (bool) activates or deactivates the corresponding tangent.
                            These arguments will be ignored if EndPoint Tangents (above) are also defined.
        
                            Note : Continuity of the spline defaults to C2. However, if periodic, or tangents
                            are supplied, the continuity will drop to C1.
        """
    @staticmethod
    def isClosed(*args, **kwargs):
        """
        Returns true if the distance between the start point and end point of
                            this B-Spline curve is less than or equal to gp::Resolution().
        """
    @staticmethod
    def isPeriodic(*args, **kwargs):
        """
        Returns true if this BSpline curve is periodic.
        """
    @staticmethod
    def isRational(*args, **kwargs):
        """
        Returns true if this B-Spline curve is rational.
                            A B-Spline curve is rational if, at the time of construction,
                            the weight table has been initialized.
        """
    @staticmethod
    def join(*args, **kwargs):
        """
        Build a new spline by joining this and a second spline.
        """
    @staticmethod
    def makeC1Continuous(tol = 1e-6, ang_tol = 1e-7):
        """
                            Reduces as far as possible the multiplicities of the knots of this BSpline
                            (keeping the geometry). It returns a new BSpline, which could still be C0.
                            tol is a geometrical tolerance.
                            The tol_ang is angular tolerance, in radians. It sets tolerable angle mismatch
                            of the tangents on the left and on the right to decide if the curve is G1 or
                            not at a given point.
        """
    @staticmethod
    def movePoint(U, P, Index1, Index2):
        """
                        Moves the point of parameter U of this B-Spline curve to P.
        Index1 and Index2 are the indexes in the table of poles of this B-Spline curve
        of the first and last poles designated to be moved.
        
        Returns: (FirstModifiedPole, LastModifiedPole). They are the indexes of the
        first and last poles which are effectively modified.
        """
    @staticmethod
    def removeKnot(Index, M, tol):
        """
                            Reduces the multiplicity of the knot of index Index to M.
                            If M is equal to 0, the knot is removed.
                            With a modification of this type, the array of poles is also modified.
                            Two different algorithms are systematically used to compute the new
                            poles of the curve. If, for each pole, the distance between the pole
                            calculated using the first algorithm and the same pole calculated using
                            the second algorithm, is less than Tolerance, this ensures that the curve
                            is not modified by more than Tolerance. Under these conditions, true is
                            returned; otherwise, false is returned.
        
                            A low tolerance is used to prevent modification of the curve.
                            A high tolerance is used to 'smooth' the curve.
        """
    @staticmethod
    def scaleKnotsToBounds(*args, **kwargs):
        """
        Scales the knots list to fit the specified bounds.
                            The shape of the curve is not modified.
                            bspline_curve.scaleKnotsToBounds(u0, u1)
                            Default arguments are (0.0, 1.0)
        """
    @staticmethod
    def segment(u1, u2):
        """
                            Modifies this B-Spline curve by segmenting it.
        """
    @staticmethod
    def setKnot(*args, **kwargs):
        """
        Set a knot of the B-Spline curve.
        """
    @staticmethod
    def setKnots(*args, **kwargs):
        """
        Set knots of the B-Spline curve.
        """
    @staticmethod
    def setNotPeriodic(*args, **kwargs):
        """
        Changes this B-Spline curve into a non-periodic curve.
        If this curve is already non-periodic, it is not modified.
        """
    @staticmethod
    def setOrigin(*args, **kwargs):
        """
        Assigns the knot of index Index in the knots table
        as the origin of this periodic B-Spline curve. As a consequence,
        the knots and poles tables are modified.
        """
    @staticmethod
    def setPeriodic(*args, **kwargs):
        """
        Changes this B-Spline curve into a periodic curve.
        """
    @staticmethod
    def setPole(*args, **kwargs):
        """
        Modifies this B-Spline curve by assigning P
        to the pole of index Index in the poles table.
        """
    @staticmethod
    def setWeight(*args, **kwargs):
        """
        Set a weight of the B-Spline curve.
        """
    @staticmethod
    def toBezier(*args, **kwargs):
        """
        Build a list of Bezier splines.
        """
    @staticmethod
    def toBiArcs(*args, **kwargs):
        """
        Build a list of arcs and lines to approximate the B-spline.
                            toBiArcs(tolerance) -> list.
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
class BSplineSurface(GeometrySurface):
    """
    Describes a B-Spline surface in 3D space
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def approximate(*args, **kwargs):
        """
        Replaces this B-Spline surface by approximating a set of points.
                            This method uses keywords :
                            - Points = 2Darray of points (or floats, in combination with X0, dX, Y0, dY)
                            - DegMin (int), DegMax (int)
                            - Continuity = 0,1 or 2 (for C0, C1, C2)
                            - Tolerance (float)
                            - X0, dX, Y0, dY (floats) with Points = 2Darray of floats
                            - ParamType = 'Uniform','Centripetal' or 'ChordLength'
                            - LengthWeight, CurvatureWeight, TorsionWeight (floats)
                            (with this smoothing algorithm, continuity C1 requires DegMax >= 3 and C2, DegMax >=5)
        
                            Possible combinations :
                            - approximate(Points, DegMin, DegMax, Continuity, Tolerance)
                            - approximate(Points, DegMin, DegMax, Continuity, Tolerance, X0, dX, Y0, dY)
                            With explicit keywords :
                            - approximate(Points, DegMin, DegMax, Continuity, Tolerance, ParamType)
                            - approximate(Points, DegMax, Continuity, Tolerance, LengthWeight, CurvatureWeight, TorsionWeight)
        """
    @staticmethod
    def bounds(*args, **kwargs):
        """
        Returns the parametric bounds (U1, U2, V1, V2) of this B-Spline surface.
        """
    @staticmethod
    def buildFromNSections(*args, **kwargs):
        """
        Builds a B-Spline from a list of control curves
        """
    @staticmethod
    def buildFromPolesMultsKnots(*args, **kwargs):
        """
        Builds a B-Spline by a lists of Poles, Mults and Knots
                            arguments: poles (sequence of sequence of Base.Vector), umults, vmults, [uknots, vknots, uperiodic, vperiodic, udegree, vdegree, weights (sequence of sequence of float)]
        """
    @staticmethod
    def exchangeUV(*args, **kwargs):
        """
        Exchanges the u and v parametric directions on this B-Spline surface.
                            As a consequence:
                            -- the poles and weights tables are transposed,
                            -- the knots and multiplicities tables are exchanged,
                            -- degrees of continuity and rational, periodic and uniform
                               characteristics are exchanged and
                            -- the orientation of the surface is reversed.
        """
    @staticmethod
    def getPole(*args, **kwargs):
        """
        Returns the pole of index (UIndex,VIndex) of this B-Spline surface.
        """
    @staticmethod
    def getPoles(*args, **kwargs):
        """
        Returns the table of poles of this B-Spline surface.
        """
    @staticmethod
    def getPolesAndWeights(*args, **kwargs):
        """
        Returns the table of poles and weights in homogeneous coordinates.
        """
    @staticmethod
    def getResolution(*args, **kwargs):
        """
        Computes two tolerance values for this B-Spline surface, based on the
                            given tolerance in 3D space Tolerance3D. The tolerances computed are:
                            -- UTolerance in the u parametric direction and
                            -- VTolerance in the v parametric direction.
        
                            If f(u,v) is the equation of this B-Spline surface, UTolerance and
                            VTolerance guarantee that:
                            |u1 - u0| < UTolerance
                            |v1 - v0| < VTolerance
                            ====> ||f(u1, v1) - f(u2, v2)|| < Tolerance3D
        """
    @staticmethod
    def getUKnot(*args, **kwargs):
        """
        Returns, for this B-Spline surface, in the u parametric direction
                            the knot of index UIndex of the knots table.
        """
    @staticmethod
    def getUKnots(*args, **kwargs):
        """
        Returns, for this B-Spline surface, the knots table
                            in the u parametric direction
        """
    @staticmethod
    def getUMultiplicities(*args, **kwargs):
        """
        Returns, for this B-Spline surface, the table of
                            multiplicities in the u parametric direction
        """
    @staticmethod
    def getUMultiplicity(*args, **kwargs):
        """
        Returns, for this B-Spline surface, the multiplicity of
                            the knot of index UIndex in the u parametric direction.
        """
    @staticmethod
    def getVKnot(*args, **kwargs):
        """
        Returns, for this B-Spline surface, in the v parametric direction
                            the knot of index VIndex of the knots table.
        """
    @staticmethod
    def getVKnots(*args, **kwargs):
        """
        Returns, for this B-Spline surface, the knots table
                            in the v parametric direction
        """
    @staticmethod
    def getVMultiplicities(*args, **kwargs):
        """
        Returns, for this B-Spline surface, the table of
                            multiplicities in the v parametric direction
        """
    @staticmethod
    def getVMultiplicity(*args, **kwargs):
        """
        Returns, for this B-Spline surface, the multiplicity of
                            the knot of index VIndex in the v parametric direction.
        """
    @staticmethod
    def getWeight(*args, **kwargs):
        """
        Return the weight of the pole of index (UIndex,VIndex)
                            in the poles table for this B-Spline surface.
        """
    @staticmethod
    def getWeights(*args, **kwargs):
        """
        Returns the table of weights of the poles for this B-Spline surface.
        """
    @staticmethod
    def increaseDegree(*args, **kwargs):
        """
        increase(Int=UDegree, int=VDegree)
                            Increases the degrees of this B-Spline surface to UDegree and VDegree
                            in the u and v parametric directions respectively.
                            As a result, the tables of poles, weights and multiplicities are modified.
                            The tables of knots is not changed.
        
                            Note: Nothing is done if the given degree is less than or equal to the
                            current degree in the corresponding parametric direction.
        """
    @staticmethod
    def increaseUMultiplicity(*args, **kwargs):
        """
        Increases the multiplicity in the u direction.
        """
    @staticmethod
    def increaseVMultiplicity(*args, **kwargs):
        """
        Increases the multiplicity in the v direction.
        """
    @staticmethod
    def incrementUMultiplicity(*args, **kwargs):
        """
        Increment the multiplicity in the u direction
        """
    @staticmethod
    def incrementVMultiplicity(*args, **kwargs):
        """
        Increment the multiplicity in the v direction
        """
    @staticmethod
    def insertUKnot(*args, **kwargs):
        """
        insertUKnote(float U, int Index, float Tolerance) - Insert or override a knot
        """
    @staticmethod
    def insertUKnots(*args, **kwargs):
        """
        insertUKnote(List of float U, List of float Mult, float Tolerance) - Inserts knots.
        """
    @staticmethod
    def insertVKnot(*args, **kwargs):
        """
        insertUKnote(float V, int Index, float Tolerance) - Insert or override a knot.
        """
    @staticmethod
    def insertVKnots(*args, **kwargs):
        """
        insertUKnote(List of float V, List of float Mult, float Tolerance) - Inserts knots.
        """
    @staticmethod
    def interpolate(points):
        """
                            interpolate(zpoints, X0, dX, Y0, dY)
        
                            Replaces this B-Spline surface by interpolating a set of points.
                            The resulting surface is of degree 3 and continuity C2.
                            Arguments:
                            a 2 dimensional array of vectors, that the surface passes through
                            or
                            a 2 dimensional array of floats with the z values,
                            the x starting point X0 (float),
                            the x increment dX (float),
                            the y starting point Y0 and increment dY
        """
    @staticmethod
    def isUClosed(*args, **kwargs):
        """
        Checks if this surface is closed in the u parametric direction.
                            Returns true if, in the table of poles the first row and the last
                            row are identical.
        """
    @staticmethod
    def isUPeriodic(*args, **kwargs):
        """
        Returns true if this surface is periodic in the u parametric direction.
        """
    @staticmethod
    def isURational(*args, **kwargs):
        """
        Returns false if the equation of this B-Spline surface is polynomial
                            (e.g. non-rational) in the u or v parametric direction.
                            In other words, returns false if for each row of poles, the associated
                            weights are identical
        """
    @staticmethod
    def isVClosed(*args, **kwargs):
        """
        Checks if this surface is closed in the v parametric direction.
                            Returns true if, in the table of poles the first column and the
                            last column are identical.
        """
    @staticmethod
    def isVPeriodic(*args, **kwargs):
        """
        Returns true if this surface is periodic in the v parametric direction.
        """
    @staticmethod
    def isVRational(*args, **kwargs):
        """
        Returns false if the equation of this B-Spline surface is polynomial
                            (e.g. non-rational) in the u or v parametric direction.
                            In other words, returns false if for each column of poles, the associated
                            weights are identical
        """
    @staticmethod
    def movePoint(*args, **kwargs):
        """
        Moves the point of parameters (U, V) of this B-Spline surface to P.
                            UIndex1, UIndex2, VIndex1 and VIndex2 are the indexes in the poles
                            table of this B-Spline surface, of the first and last poles which
                            can be moved in each parametric direction.
                            The returned indexes UFirstIndex, ULastIndex, VFirstIndex and
                            VLastIndex are the indexes of the first and last poles effectively
                            modified in each parametric direction.
                            In the event of incompatibility between UIndex1, UIndex2, VIndex1,
                            VIndex2 and the values U and V:
                            -- no change is made to this B-Spline surface, and
                            -- UFirstIndex, ULastIndex, VFirstIndex and VLastIndex are set to
                               null.
        """
    @staticmethod
    def removeUKnot(*args, **kwargs):
        """
        Reduces to M the multiplicity of the knot of index Index in the given
                        parametric direction. If M is 0, the knot is removed.
                        With a modification of this type, the table of poles is also modified.
                        Two different algorithms are used systematically to compute the new
                        poles of the surface. For each pole, the distance between the pole
                        calculated using the first algorithm and the same pole calculated using
                        the second algorithm, is checked. If this distance is less than Tolerance
                        it ensures that the surface is not modified by more than Tolerance.
                        Under these conditions, the function returns true; otherwise, it returns
                        false.
        
                        A low tolerance prevents modification of the surface. A high tolerance
                        'smoothes' the surface.
        """
    @staticmethod
    def removeVKnot(*args, **kwargs):
        """
        Reduces to M the multiplicity of the knot of index Index in the given
                        parametric direction. If M is 0, the knot is removed.
                        With a modification of this type, the table of poles is also modified.
                        Two different algorithms are used systematically to compute the new
                        poles of the surface. For each pole, the distance between the pole
                        calculated using the first algorithm and the same pole calculated using
                        the second algorithm, is checked. If this distance is less than Tolerance
                        it ensures that the surface is not modified by more than Tolerance.
                        Under these conditions, the function returns true; otherwise, it returns
                        false.
        
                        A low tolerance prevents modification of the surface. A high tolerance
                        'smoothes' the surface.
        """
    @staticmethod
    def reparametrize(*args, **kwargs):
        """
        Returns a reparametrized copy of this surface
        """
    @staticmethod
    def scaleKnotsToBounds(*args, **kwargs):
        """
        Scales the U and V knots lists to fit the specified bounds.
                            The shape of the surface is not modified.
                            bspline_surf.scaleKnotsToBounds(u0, u1, v0, v1)
                            Default arguments are 0.0, 1.0, 0.0, 1.0
        """
    @staticmethod
    def segment(*args, **kwargs):
        """
        Modifies this B-Spline surface by segmenting it between U1 and U2 in the
                            u parametric direction and between V1 and V2 in the v parametric direction.
                            Any of these values can be outside the bounds of this surface, but U2 must
                            be greater than U1 and V2 must be greater than V1.
        
                            All the data structure tables of this B-Spline surface are modified but the
                            knots located between U1 and U2 in the u parametric direction, and between
                            V1 and V2 in the v parametric direction are retained.
                            The degree of the surface in each parametric direction is not modified.
        """
    @staticmethod
    def setPole(*args, **kwargs):
        """
        Modifies this B-Spline surface by assigning P to the pole of
                            index (UIndex, VIndex) in the poles table.
                            The second syntax allows you also to change the weight of the
                            modified pole. The weight is set to Weight. This syntax must
                            only be used for rational surfaces.
                            Modifies this B-Spline curve by assigning P to the pole of
                            index Index in the poles table.
        """
    @staticmethod
    def setPoleCol(*args, **kwargs):
        """
        Modifies this B-Spline surface by assigning values to all or part
                            of the column of poles of index VIndex, of this B-Spline surface.
                            You can also change the weights of the modified poles. The weights
                            are set to the corresponding values of CPoleWeights.
                            These syntaxes must only be used for rational surfaces.
        """
    @staticmethod
    def setPoleRow(*args, **kwargs):
        """
        Modifies this B-Spline surface by assigning values to all or part
                            of the row of poles of index VIndex, of this B-Spline surface.
                            You can also change the weights of the modified poles. The weights
                            are set to the corresponding values of CPoleWeights.
                            These syntaxes must only be used for rational surfaces.
        """
    @staticmethod
    def setUKnot(*args, **kwargs):
        """
        Modifies this B-Spline surface by assigning the value K to the knot of index
                            UIndex of the knots table corresponding to the u parametric direction.
                            This modification remains relatively local, since K must lie between the values
                            of the knots which frame the modified knot.
        
                            You can also increase the multiplicity of the modified knot to M. Note however
                            that it is not possible to decrease the multiplicity of a knot with this function.
        """
    @staticmethod
    def setUKnots(*args, **kwargs):
        """
        Changes all knots of this B-Spline surface in the u parametric
                            direction. The multiplicity of the knots is not modified.
        """
    @staticmethod
    def setUNotPeriodic(*args, **kwargs):
        """
        Changes this B-Spline surface into a non-periodic one in the u parametric direction.
                            If this B-Spline surface is already non-periodic in the given parametric direction,
                            it is not modified.
                            If this B-Spline surface is periodic in the given parametric direction, the boundaries
                            of the surface are not given by the first and last rows (or columns) of poles (because
                            the multiplicity of the first knot and of the last knot in the given parametric direction
                            are not modified, nor are they equal to Degree+1, where Degree is the degree of this
                            B-Spline surface in the given parametric direction). Only the function Segment ensures
                            this property.
        
                            Note: the poles and knots tables are modified.
        """
    @staticmethod
    def setUOrigin(*args, **kwargs):
        """
        Assigns the knot of index Index in the knots table
                            in the u parametric direction to be the origin of
                            this periodic B-Spline surface. As a consequence,
                            the knots and poles tables are modified.
        """
    @staticmethod
    def setUPeriodic(*args, **kwargs):
        """
        Modifies this surface to be periodic in the u parametric direction.
                            To become periodic in a given parametric direction a surface must
                            be closed in that parametric direction, and the knot sequence relative
                            to that direction must be periodic.
                            To generate this periodic sequence of knots, the functions FirstUKnotIndex
                            and LastUKnotIndex are used to compute I1 and I2. These are the indexes,
                            in the knot array associated with the given parametric direction, of the
                            knots that correspond to the first and last parameters of this B-Spline
                            surface in the given parametric direction. Hence the period is:
        
                            Knots(I1) - Knots(I2)
        
                            As a result, the knots and poles tables are modified.
        """
    @staticmethod
    def setVKnot(*args, **kwargs):
        """
        Modifies this B-Spline surface by assigning the value K to the knot of index
                            VIndex of the knots table corresponding to the v parametric direction.
                            This modification remains relatively local, since K must lie between the values
                            of the knots which frame the modified knot.
        
                            You can also increase the multiplicity of the modified knot to M. Note however
                            that it is not possible to decrease the multiplicity of a knot with this function.
        """
    @staticmethod
    def setVKnots(*args, **kwargs):
        """
        Changes all knots of this B-Spline surface in the v parametric
                            direction. The multiplicity of the knots is not modified.
        """
    @staticmethod
    def setVNotPeriodic(*args, **kwargs):
        """
        Changes this B-Spline surface into a non-periodic one in the v parametric direction.
                            If this B-Spline surface is already non-periodic in the given parametric direction,
                            it is not modified.
                            If this B-Spline surface is periodic in the given parametric direction, the boundaries
                            of the surface are not given by the first and last rows (or columns) of poles (because
                            the multiplicity of the first knot and of the last knot in the given parametric direction
                            are not modified, nor are they equal to Degree+1, where Degree is the degree of this
                            B-Spline surface in the given parametric direction). Only the function Segment ensures
                            this property.
        
                            Note: the poles and knots tables are modified.
        """
    @staticmethod
    def setVOrigin(*args, **kwargs):
        """
        Assigns the knot of index Index in the knots table
                            in the v parametric direction to be the origin of
                            this periodic B-Spline surface. As a consequence,
                            the knots and poles tables are modified.
        """
    @staticmethod
    def setVPeriodic(*args, **kwargs):
        """
        Modifies this surface to be periodic in the v parametric direction.
                            To become periodic in a given parametric direction a surface must
                            be closed in that parametric direction, and the knot sequence relative
                            to that direction must be periodic.
                            To generate this periodic sequence of knots, the functions FirstUKnotIndex
                            and LastUKnotIndex are used to compute I1 and I2. These are the indexes,
                            in the knot array associated with the given parametric direction, of the
                            knots that correspond to the first and last parameters of this B-Spline
                            surface in the given parametric direction. Hence the period is:
        
                            Knots(I1) - Knots(I2)
        
                            As a result, the knots and poles tables are modified.
        """
    @staticmethod
    def setWeight(*args, **kwargs):
        """
        Modifies this B-Spline surface by assigning the value Weight to the weight
                            of the pole of index (UIndex, VIndex) in the poles tables of this B-Spline
                            surface.
        
                            This function must only be used for rational surfaces.
        """
    @staticmethod
    def setWeightCol(*args, **kwargs):
        """
        Modifies this B-Spline surface by assigning values to all or part of the
                            weights of the column of poles of index VIndex of this B-Spline surface.
        
                            The modified part of the column of weights is defined by the bounds
                            of the array CPoleWeights.
        
                            This function must only be used for rational surfaces.
        """
    @staticmethod
    def setWeightRow(*args, **kwargs):
        """
        Modifies this B-Spline surface by assigning values to all or part of the
                            weights of the row of poles of index UIndex of this B-Spline surface.
        
                            The modified part of the row of weights is defined by the bounds of the
                            array CPoleWeights.
        
                            This function must only be used for rational surfaces.
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
class BezierCurve(BoundedCurve):
    """
    Describes a rational or non-rational Bezier curve:
                    -- a non-rational Bezier curve is defined by a table of poles (also called control points)
                    -- a rational Bezier curve is defined by a table of poles with varying weights
    
                    Constructor takes no arguments.
    
                    Example usage:
                        p1 = Base.Vector(-1, 0, 0)
                        p2 = Base.Vector(0, 1, 0.2)
                        p3 = Base.Vector(1, 0, 0.4)
                        p4 = Base.Vector(0, -1, 1)
    
                        bc = BezierCurve()
                        bc.setPoles([p1, p2, p3, p4])
                        curveShape = bc.toShape()
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def getPole(*args, **kwargs):
        """
        Get a pole of the Bezier curve.
        """
    @staticmethod
    def getPoles(*args, **kwargs):
        """
        Get all poles of the Bezier curve.
        """
    @staticmethod
    def getResolution(*args, **kwargs):
        """
        Computes for this Bezier curve the parametric tolerance (UTolerance)
        for a given 3D tolerance (Tolerance3D).
        If f(t) is the equation of this Bezier curve, the parametric tolerance
        ensures that:
        |t1-t0| < UTolerance =""==> |f(t1)-f(t0)| < Tolerance3D
        """
    @staticmethod
    def getWeight(*args, **kwargs):
        """
        Get a weight of the Bezier curve.
        """
    @staticmethod
    def getWeights(*args, **kwargs):
        """
        Get all weights of the Bezier curve.
        """
    @staticmethod
    def increase(Int = ...):
        """
        Increases the degree of this Bezier curve to Degree.
        As a result, the poles and weights tables are modified.
        """
    @staticmethod
    def insertPoleAfter(*args, **kwargs):
        """
        Inserts after the pole of index.
        """
    @staticmethod
    def insertPoleBefore(*args, **kwargs):
        """
        Inserts before the pole of index.
        """
    @staticmethod
    def interpolate(*args, **kwargs):
        """
        Interpolates a list of constraints.
                        Each constraint is a list of a point and some optional derivatives
                        An optional list of parameters can be passed. It must be of same size as constraint list.
                        Otherwise, a simple uniform parametrization is used.
                        Example :
                        bezier.interpolate([[pt1, deriv11, deriv12], [pt2,], [pt3, deriv31]], [0, 0.4, 1.0])
        """
    @staticmethod
    def isClosed(*args, **kwargs):
        """
        Returns true if the distance between the start point and end point of
                            this Bezier curve is less than or equal to gp::Resolution().
        """
    @staticmethod
    def isPeriodic(*args, **kwargs):
        """
        Returns false.
        """
    @staticmethod
    def isRational(*args, **kwargs):
        """
        Returns false if the weights of all the poles of this Bezier curve are equal.
        """
    @staticmethod
    def removePole(*args, **kwargs):
        """
        Removes the pole of index Index from the table of poles of this Bezier curve.
        If this Bezier curve is rational, it can become non-rational.
        """
    @staticmethod
    def segment(*args, **kwargs):
        """
        Modifies this Bezier curve by segmenting it.
        """
    @staticmethod
    def setPole(*args, **kwargs):
        """
        Set a pole of the Bezier curve.
        """
    @staticmethod
    def setPoles(*args, **kwargs):
        """
        Set the poles of the Bezier curve.
        
                        Takes a list of 3D Base.Vector objects.
        """
    @staticmethod
    def setWeight(*args, **kwargs):
        """
        (id, weight) Set a weight of the Bezier curve.
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
class BezierSurface(GeometrySurface):
    """
    Describes a rational or non-rational Bezier surface
                    -- A non-rational Bezier surface is defined by a table of poles (also known as control points).
                    -- A rational Bezier surface is defined by a table of poles with varying associated weights.
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def bounds(*args, **kwargs):
        """
        Returns the parametric bounds (U1, U2, V1, V2) of this Bezier surface.
        """
    @staticmethod
    def exchangeUV(*args, **kwargs):
        """
        Exchanges the u and v parametric directions on this Bezier surface.
                            As a consequence:
                            -- the poles and weights tables are transposed,
                            -- degrees, rational characteristics and so on are exchanged between
                               the two parametric directions, and
                            -- the orientation of the surface is reversed.
        """
    @staticmethod
    def getPole(*args, **kwargs):
        """
        Get a pole of index (UIndex,VIndex) of the Bezier surface.
        """
    @staticmethod
    def getPoles(*args, **kwargs):
        """
        Get all poles of the Bezier surface.
        """
    @staticmethod
    def getResolution(*args, **kwargs):
        """
        Computes two tolerance values for this Bezier surface, based on the
                            given tolerance in 3D space Tolerance3D. The tolerances computed are:
                            -- UTolerance in the u parametric direction and
                            -- VTolerance in the v parametric direction.
        
                            If f(u,v) is the equation of this Bezier surface, UTolerance and VTolerance
                            guarantee that:
                            |u1 - u0| < UTolerance
                            |v1 - v0| < VTolerance
                            ====> ||f(u1, v1) - f(u2, v2)|| < Tolerance3D
        """
    @staticmethod
    def getWeight(*args, **kwargs):
        """
        Get a weight of the pole of index (UIndex,VIndex)
                            of the Bezier surface.
        """
    @staticmethod
    def getWeights(*args, **kwargs):
        """
        Get all weights of the Bezier surface.
        """
    @staticmethod
    def increase(Int = ..., Int = ...):
        """
                            Increases the degree of this Bezier surface in the two
                            parametric directions.
        """
    @staticmethod
    def insertPoleColAfter(*args, **kwargs):
        """
        Inserts into the table of poles of this surface, after the column
                            of poles of index.
                            If this Bezier surface is non-rational, it can become rational if
                            the weights associated with the new poles are different from each
                            other, or collectively different from the existing weights in the
                            table.
        """
    @staticmethod
    def insertPoleColBefore(*args, **kwargs):
        """
        Inserts into the table of poles of this surface, before the column
                            of poles of index.
                            If this Bezier surface is non-rational, it can become rational if
                            the weights associated with the new poles are different from each
                            other, or collectively different from the existing weights in the
                            table.
        """
    @staticmethod
    def insertPoleRowAfter(*args, **kwargs):
        """
        Inserts into the table of poles of this surface, after the row
                            of poles of index.
                            If this Bezier surface is non-rational, it can become rational if
                            the weights associated with the new poles are different from each
                            other, or collectively different from the existing weights in the
                            table.
        """
    @staticmethod
    def insertPoleRowBefore(*args, **kwargs):
        """
        Inserts into the table of poles of this surface, before the row
                            of poles of index.
                            If this Bezier surface is non-rational, it can become rational if
                            the weights associated with the new poles are different from each
                            other, or collectively different from the existing weights in the
                            table.
        """
    @staticmethod
    def isUClosed(*args, **kwargs):
        """
        Checks if this surface is closed in the u parametric direction.
                            Returns true if, in the table of poles the first row and the last
                            row are identical.
        """
    @staticmethod
    def isUPeriodic(*args, **kwargs):
        """
        Returns false.
        """
    @staticmethod
    def isURational(*args, **kwargs):
        """
        Returns false if the equation of this Bezier surface is polynomial
                            (e.g. non-rational) in the u or v parametric direction.
                            In other words, returns false if for each row of poles, the associated
                            weights are identical
        """
    @staticmethod
    def isVClosed(*args, **kwargs):
        """
        Checks if this surface is closed in the v parametric direction.
                            Returns true if, in the table of poles the first column and the
                            last column are identical.
        """
    @staticmethod
    def isVPeriodic(*args, **kwargs):
        """
        Returns false.
        """
    @staticmethod
    def isVRational(*args, **kwargs):
        """
        Returns false if the equation of this Bezier surface is polynomial
                            (e.g. non-rational) in the u or v parametric direction.
                            In other words, returns false if for each column of poles, the associated
                            weights are identical
        """
    @staticmethod
    def removePoleCol(*args, **kwargs):
        """
        removePoleRow(int=VIndex)
                            Removes the column of poles of index VIndex from the table of
                            poles of this Bezier surface.
                            If this Bezier curve is rational, it can become non-rational.
        """
    @staticmethod
    def removePoleRow(int = ...):
        """
                            Removes the row of poles of index UIndex from the table of
                            poles of this Bezier surface.
                            If this Bezier curve is rational, it can become non-rational.
        """
    @staticmethod
    def segment(double = ..., double = ..., double = ..., double = ...):
        """
                            Modifies this Bezier surface by segmenting it between U1 and U2
                            in the u parametric direction, and between V1 and V2 in the v
                            parametric direction.
                            U1, U2, V1, and V2 can be outside the bounds of this surface.
        
                            -- U1 and U2 isoparametric Bezier curves, segmented between
                               V1 and V2, become the two bounds of the surface in the v
                               parametric direction (0. and 1. u isoparametric curves).
                            -- V1 and V2 isoparametric Bezier curves, segmented between
                               U1 and U2, become the two bounds of the surface in the u
                               parametric direction (0. and 1. v isoparametric curves).
        
                            The poles and weights tables are modified, but the degree of
                            this surface in the u and v parametric directions does not
                            change.U1 can be greater than U2, and V1 can be greater than V2.
                            In these cases, the corresponding parametric direction is inverted.
                            The orientation of the surface is inverted if one (and only one)
                            parametric direction is inverted.
        """
    @staticmethod
    def setPole(*args, **kwargs):
        """
        Set a pole of the Bezier surface.
        """
    @staticmethod
    def setPoleCol(*args, **kwargs):
        """
        Set the column of poles of the Bezier surface.
        """
    @staticmethod
    def setPoleRow(*args, **kwargs):
        """
        Set the row of poles of the Bezier surface.
        """
    @staticmethod
    def setWeight(*args, **kwargs):
        """
        Set the weight of pole of the index (UIndex, VIndex)
                            for the Bezier surface.
        """
    @staticmethod
    def setWeightCol(*args, **kwargs):
        """
        Set the weights of the poles in the column of poles
                            of index VIndex of the Bezier surface.
        """
    @staticmethod
    def setWeightRow(*args, **kwargs):
        """
        Set the weights of the poles in the row of poles
                            of index UIndex of the Bezier surface.
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
class BodyBase(Feature):
    """
    Base class of all Body objects
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
class Circle(Conic):
    """
    Describes a circle in 3D space
    To create a circle there are several ways:
    Part.Circle()
        Creates a default circle with center (0,0,0) and radius 1
    
    Part.Circle(Circle)
        Creates a copy of the given circle
    
    Part.Circle(Circle, Distance)
        Creates a circle parallel to given circle at a certain distance
    
    Part.Circle(Center,Normal,Radius)
        Creates a circle defined by center, normal direction and radius
    
    Part.Circle(Point1,Point2,Point3)
        Creates a circle defined by three non-linear points
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
class CompSolid(Shape):
    """
    TopoShapeCompSolid is the OpenCasCade topological compound solid wrapper
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def add(*args, **kwargs):
        """
        Add a solid to the compound.
        add(solid)
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
class Compound(Shape):
    """
    Create a compound out of a list of shapes
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def add(*args, **kwargs):
        """
        Add a shape to the compound.
        add(shape)
        """
    @staticmethod
    def connectEdgesToWires(*args, **kwargs):
        """
        Build a compound of wires out of the edges of this compound.
        connectEdgesToWires([Shared = True, Tolerance = 1e-7]) -> Compound
        --
        If Shared is True  connection is performed only when adjacent edges share the same vertex.
        If Shared is False connection is performed only when ends of adjacent edges are at distance less than Tolerance.
        """
    @staticmethod
    def setFaces(*args, **kwargs):
        """
        A shape is created from points and triangles and set to this object
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
class Cone(GeometrySurface):
    """
    Describes a cone in 3D space
                    To create a cone there are several ways:
                    Part.Cone()
                        Creates a default cone with radius 1
    
                    Part.Cone(Cone)
                        Creates a copy of the given cone
    
                    Part.Cone(Cone, Distance)
                        Creates a cone parallel to given cone at a certain distance
    
                    Part.Cone(Point1,Point2,Radius1,Radius2)
                        Creates a cone defined by two points and two radii
                        The axis of the cone is the line passing through
                        Point1 and Poin2.
                        Radius1 is the radius of the section passing through
                        Point1 and Radius2 the radius of the section passing
                        through Point2.
    
                    Part.Cone(Point1,Point2,Point3,Point4)
                        Creates a cone passing through three points Point1,
                        Point2 and Point3.
                        Its axis is defined by Point1 and Point2 and the radius of
                        its base is the distance between Point3 and its axis.
                        The distance between Point and the axis is the radius of
                        the section passing through Point4.
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
class Conic(Curve):
    """
    Describes an abstract conic in 3d space
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
class Cylinder(GeometrySurface):
    """
    Describes a cylinder in 3D space
                    To create a cylinder there are several ways:
                    Part.Cylinder()
                        Creates a default cylinder with center (0,0,0) and radius 1
    
                    Part.Cylinder(Cylinder)
                        Creates a copy of the given cylinder
    
                    Part.Cylinder(Cylinder, Distance)
                        Creates a cylinder parallel to given cylinder at a certain distance
    
                    Part.Cylinder(Point1,Point2,Point2)
                        Creates a cylinder defined by three non-linear points
    
                    Part.Cylinder(Circle)
                        Creates a cylinder by a circular base
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
class Edge(Shape):
    """
    TopoShapeEdge is the OpenCasCade topological edge wrapper
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def centerOfCurvatureAt(*args, **kwargs):
        """
        Get the center of curvature at the given parameter [First|Last] if defined
        centerOfCurvatureAt(paramval) -> Vector
        """
    @staticmethod
    def countNodes(*args, **kwargs):
        """
        Returns the number of nodes of the 3D polygon of the edge.
        """
    @staticmethod
    def curvatureAt(*args, **kwargs):
        """
        Get the curvature at the given parameter [First|Last] if defined
        curvatureAt(paramval) -> Float
        """
    @staticmethod
    def curveOnSurface(*args, **kwargs):
        """
        Returns the 2D curve, the surface, the placement and the parameter range of index idx.
        curveOnSurface(idx) -> None or tuple
        --
        Returns None if index idx is out of range.
        Returns a 5-items tuple of a curve, a surface, a placement, first parameter and last parameter.
        """
    @staticmethod
    def derivative1At(*args, **kwargs):
        """
        Get the first derivative at the given parameter value along the Edge if it is defined
        derivative1At(paramval) -> Vector
        --
        Args:
            paramval (float or int): The parameter value along the Edge at which to
                determine the first derivative e.g:
        
                x = Part.makeCircle(1, FreeCAD.Vector(0,0,0), FreeCAD.Vector(0,0,1), 0, 90)
                y = x.derivative1At(x.FirstParameter + 0.5 * (x.LastParameter - x.FirstParameter))
        
                y is the Vector (-0.7071067811865475, 0.7071067811865476, 0.0)
        
                Values with magnitude greater than the Edge length return
                values of the first derivative on the curve extrapolated
                beyond its length. This may not be valid for all Edges.
                Negative values similarly return a first derivative on the
                curve extrapolated backwards (before the start point of the
                Edge). For example, using the same shape as above:
        
                >>> x.derivative1At(x.FirstParameter + 3.5*(x.LastParameter - x.FirstParameter))
                Vector (0.7071067811865477, 0.7071067811865474, 0.0)
        
                Which gives the same result as
        
                >>> x.derivative1At(x.FirstParameter -0.5*(x.LastParameter - x.FirstParameter))
                Vector (0.7071067811865475, 0.7071067811865476, 0.0)
        
                Since it is a circle
        
        Returns:
            Vector: representing the first derivative to the Edge at the
               given location along its length (or extrapolated length)
        """
    @staticmethod
    def derivative2At(*args, **kwargs):
        """
        Get the second derivative at the given parameter value along the Edge if it is defined
        derivative2At(paramval) -> Vector
        --
        Args:
            paramval (float or int): The parameter value along the Edge at which to
                determine the second derivative e.g:
        
                x = Part.makeCircle(1, FreeCAD.Vector(0,0,0), FreeCAD.Vector(0,0,1), 0, 90)
                y = x.derivative2At(x.FirstParameter + 0.5 * (x.LastParameter - x.FirstParameter))
        
                y is the Vector (-0.7071067811865476, -0.7071067811865475, 0.0)
        
                Values with magnitude greater than the Edge length return
                values of the second derivative on the curve extrapolated
                beyond its length. This may not be valid for all Edges.
                Negative values similarly return a second derivative on the
                curve extrapolated backwards (before the start point of the
                Edge). For example, using the same shape as above:
        
                >>> x.derivative2At(x.FirstParameter + 3.5*(x.LastParameter - x.FirstParameter))
                Vector (-0.7071067811865474, 0.7071067811865477, 0.0)
        
                Which gives the same result as
        
                >>> x.derivative2At(x.FirstParameter -0.5*(x.LastParameter - x.FirstParameter))
                Vector (-0.7071067811865476, 0.7071067811865475, 0.0)
        
                Since it is a circle
        
        Returns:
            Vector: representing the second derivative to the Edge at the
               given location along its length (or extrapolated length)
        """
    @staticmethod
    def derivative3At(*args, **kwargs):
        """
        Get the third derivative at the given parameter value along the Edge if it is defined
        derivative3At(paramval) -> Vector
        --
        Args:
            paramval (float or int): The parameter value along the Edge at which to
                determine the third derivative e.g:
        
                x = Part.makeCircle(1, FreeCAD.Vector(0,0,0), FreeCAD.Vector(0,0,1), 0, 90)
                y = x.derivative3At(x.FirstParameter + 0.5 * (x.LastParameter - x.FirstParameter))
        
                y is the Vector (0.7071067811865475, -0.7071067811865476, -0.0)
        
                Values with magnitude greater than the Edge length return
                values of the third derivative on the curve extrapolated
                beyond its length. This may not be valid for all Edges.
                Negative values similarly return a third derivative on the
                curve extrapolated backwards (before the start point of the
                Edge). For example, using the same shape as above:
        
                >>> x.derivative3At(x.FirstParameter + 3.5*(x.LastParameter - x.FirstParameter))
                Vector (-0.7071067811865477, -0.7071067811865474, 0.0)
        
                Which gives the same result as
        
                >>> x.derivative3At(x.FirstParameter -0.5*(x.LastParameter - x.FirstParameter))
                Vector (-0.7071067811865475, -0.7071067811865476, 0.0)
        
                Since it is a circle
        
        Returns:
            Vector: representing the third derivative to the Edge at the
               given location along its length (or extrapolated length)
        """
    @staticmethod
    def discretize(*args, **kwargs):
        """
        Discretizes the edge and returns a list of points.
        discretize(kwargs) -> list
        --
        The function accepts keywords as argument:
        discretize(Number=n) => gives a list of 'n' equidistant points
        discretize(QuasiNumber=n) => gives a list of 'n' quasi equidistant points (is faster than the method above)
        discretize(Distance=d) => gives a list of equidistant points with distance 'd'
        discretize(Deflection=d) => gives a list of points with a maximum deflection 'd' to the edge
        discretize(QuasiDeflection=d) => gives a list of points with a maximum deflection 'd' to the edge (faster)
        discretize(Angular=a,Curvature=c,[Minimum=m]) => gives a list of points with an angular deflection of 'a'
                                            and a curvature deflection of 'c'. Optionally a minimum number of points
                                            can be set which by default is set to 2.
        
        Optionally you can set the keywords 'First' and 'Last' to define a sub-range of the parameter range
        of the edge.
        
        If no keyword is given then it depends on whether the argument is an int or float.
        If it's an int then the behaviour is as if using the keyword 'Number', if it's float
        then the behaviour is as if using the keyword 'Distance'.
        
        Example:
        
        import Part
        e=Part.makeCircle(5)
        p=e.discretize(Number=50,First=3.14)
        s=Part.Compound([Part.Vertex(i) for i in p])
        Part.show(s)
        
        
        p=e.discretize(Angular=0.09,Curvature=0.01,Last=3.14,Minimum=100)
        s=Part.Compound([Part.Vertex(i) for i in p])
        Part.show(s)
        """
    @staticmethod
    def firstVertex(*args, **kwargs):
        """
        Returns the Vertex of orientation FORWARD in this edge.
        firstVertex([Orientation=False]) -> Vertex
        --
        If there is none a Null shape is returned.
        Orientation = True : taking into account the edge orientation
        """
    @staticmethod
    def getParameterByLength(*args, **kwargs):
        """
        Get the value of the primary parameter at the given distance along the cartesian length of the edge.
        getParameterByLength(pos, [tolerance = 1e-7]) -> Float
        --
        Args:
            pos (float or int): The distance along the length of the edge at which to
                determine the primary parameter value. See help for the FirstParameter or
                LastParameter properties for more information on the primary parameter.
                If the given value is positive, the distance from edge start is used.
                If the given value is negative, the distance from edge end is used.
            tol (float): Computing tolerance. Optional, defaults to 1e-7.
        
        Returns:
            paramval (float): the value of the primary parameter defining the edge at the
                given position along its cartesian length.
        """
    @staticmethod
    def isSeam(*args, **kwargs):
        """
        Checks whether the edge is a seam edge.
        isSeam(Face)
        """
    @staticmethod
    def lastVertex(*args, **kwargs):
        """
        Returns the Vertex of orientation REVERSED in this edge.
        lastVertex([Orientation=False]) -> Vertex
        --
        If there is none a Null shape is returned.
        Orientation = True : taking into account the edge orientation
        """
    @staticmethod
    def normalAt(*args, **kwargs):
        """
        Get the normal direction at the given parameter value along the Edge if it is defined
        normalAt(paramval) -> Vector
        --
        Args:
            paramval (float or int): The parameter value along the Edge at which to
                determine the normal direction e.g:
        
                x = Part.makeCircle(1, FreeCAD.Vector(0,0,0), FreeCAD.Vector(0,0,1), 0, 90)
                y = x.normalAt(x.FirstParameter + 0.5 * (x.LastParameter - x.FirstParameter))
        
                y is the Vector (-0.7071067811865476, -0.7071067811865475, 0.0)
        
                Values with magnitude greater than the Edge length return
                values of the normal on the curve extrapolated beyond its
                length. This may not be valid for all Edges. Negative values
                similarly return a normal on the curve extrapolated backwards
                (before the start point of the Edge). For example, using the
                same shape as above:
        
                >>> x.normalAt(x.FirstParameter + 3.5*(x.LastParameter - x.FirstParameter))
                Vector (-0.7071067811865474, 0.7071067811865477, 0.0)
        
                Which gives the same result as
        
                >>> x.normalAt(x.FirstParameter -0.5*(x.LastParameter - x.FirstParameter))
                Vector (-0.7071067811865476, 0.7071067811865475, 0.0)
        
                Since it is a circle
        
        Returns:
            Vector: representing the normal to the Edge at the given
               location along its length (or extrapolated length)
        """
    @staticmethod
    def parameterAt(*args, **kwargs):
        """
        Get the parameter at the given vertex if lying on the edge
        parameterAt(Vertex) -> Float
        """
    @staticmethod
    def parameters(*args, **kwargs):
        """
        Get the list of parameters of the tessellation of an edge.
        parameters([face]) -> list
        --
        If the edge is part of a face then this face is required as argument.
        An exception is raised if the edge has no polygon.
        """
    @staticmethod
    def split(*args, **kwargs):
        """
        Splits the edge at the given parameter values and builds a wire out of it
        split(paramval) -> Wire
        --
        Args:
            paramval (float or list_of_floats): The parameter values along the Edge at which to
                split it e.g:
        
                edge = Part.makeCircle(1, FreeCAD.Vector(0,0,0), FreeCAD.Vector(0,0,1), 0, 90)
                wire = edge.split([0.5, 1.0])
        
        Returns:
            Wire: wire made up of two Edges
        """
    @staticmethod
    def tangentAt(*args, **kwargs):
        """
        Get the tangent direction at the given primary parameter value along the Edge if it is defined
        tangentAt(paramval) -> Vector
        --
        Args:
            paramval (float or int): The parameter value along the Edge at which to
                determine the tangent direction e.g:
        
                x = Part.makeCircle(1, FreeCAD.Vector(0,0,0), FreeCAD.Vector(0,0,1), 0, 90)
                y = x.tangentAt(x.FirstParameter + 0.5 * (x.LastParameter - x.FirstParameter))
        
                y is the Vector (-0.7071067811865475, 0.7071067811865476, 0.0)
        
                Values with magnitude greater than the Edge length return
                values of the tangent on the curve extrapolated beyond its
                length. This may not be valid for all Edges. Negative values
                similarly return a tangent on the curve extrapolated backwards
                (before the start point of the Edge). For example, using the
                same shape as above:
        
                >>> x.tangentAt(x.FirstParameter + 3.5*(x.LastParameter - x.FirstParameter))
                Vector (0.7071067811865477, 0.7071067811865474, 0.0)
        
                Which gives the same result as
        
                >>> x.tangentAt(x.FirstParameter -0.5*(x.LastParameter - x.FirstParameter))
                Vector (0.7071067811865475, 0.7071067811865476, 0.0)
        
                Since it is a circle
        
        Returns:
            Vector: representing the tangent to the Edge at the given
               location along its length (or extrapolated length)
        """
    @staticmethod
    def valueAt(*args, **kwargs):
        """
        Get the value of the cartesian parameter value at the given parameter value along the Edge
        valueAt(paramval) -> Vector
        --
        Args:
            paramval (float or int): The parameter value along the Edge at which to
                determine the value in terms of the main parameter defining
                the edge, what the parameter value is depends on the type of
                edge. See  e.g:
        
                For a circle value
        
                x = Part.makeCircle(1, FreeCAD.Vector(0,0,0), FreeCAD.Vector(0,0,1), 0, 90)
                y = x.valueAt(x.FirstParameter + 0.5 * (x.LastParameter - x.FirstParameter))
        
                y is theVector (0.7071067811865476, 0.7071067811865475, 0.0)
        
                Values with magnitude greater than the Edge length return
                values on the curve extrapolated beyond its length. This may
                not be valid for all Edges. Negative values similarly return
                a parameter value on the curve extrapolated backwards (before the
                start point of the Edge). For example, using the same shape
                as above:
        
                >>> x.valueAt(x.FirstParameter + 3.5*(x.LastParameter - x.FirstParameter))
                Vector (0.7071067811865474, -0.7071067811865477, 0.0)
        
                Which gives the same result as
        
                >>> x.valueAt(x.FirstParameter -0.5*(x.LastParameter - x.FirstParameter))
                Vector (0.7071067811865476, -0.7071067811865475, 0.0)
        
                Since it is a circle
        
        Returns:
            Vector: representing the cartesian location on the Edge at the given
               distance along its length (or extrapolated length)
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
class Ellipse(Conic):
    """
    Describes an ellipse in 3D space
                    To create an ellipse there are several ways:
                    Part.Ellipse()
                        Creates an ellipse with major radius 2 and minor radius 1 with the
                        center in (0,0,0)
    
                    Part.Ellipse(Ellipse)
                        Create a copy of the given ellipse
    
                    Part.Ellipse(S1,S2,Center)
                        Creates an ellipse centered on the point Center, where
                        the plane of the ellipse is defined by Center, S1 and S2,
                        its major axis is defined by Center and S1,
                        its major radius is the distance between Center and S1, and
                        its minor radius is the distance between S2 and the major axis.
    
                    Part.Ellipse(Center,MajorRadius,MinorRadius)
                        Creates an ellipse with major and minor radii MajorRadius and
                        MinorRadius, and located in the plane defined by Center and
                        the normal (0,0,1)
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
class Face(Shape):
    """
    TopoShapeFace is the OpenCasCade topological face wrapper
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def addWire(*args, **kwargs):
        """
        Adds a wire to the face.
        addWire(wire)
        """
    @staticmethod
    def countNodes(*args, **kwargs):
        """
        Returns the number of nodes of the triangulation.
        """
    @staticmethod
    def countTriangles(*args, **kwargs):
        """
        Returns the number of triangles of the triangulation.
        """
    @staticmethod
    def curvatureAt(*args, **kwargs):
        """
        Get the curvature at the given parameter [0|Length] if defined
        curvatureAt(u,v) -> Float
        """
    @staticmethod
    def curveOnSurface(*args, **kwargs):
        """
        Returns the curve associated to the edge in the parametric space of the face.
        curveOnSurface(Edge) -> (curve, min, max) or None
        --
        If this curve exists then a tuple of curve and parameter range is returned.
        Returns None if this curve  does not exist.
        """
    @staticmethod
    def cutHoles(*args, **kwargs):
        """
        Cut holes in the face.
        cutHoles(list_of_wires)
        """
    @staticmethod
    def derivative1At(*args, **kwargs):
        """
        Get the first derivative at the given parameter [0|Length] if defined
        derivative1At(u,v) -> (vectorU,vectorV)
        """
    @staticmethod
    def derivative2At(*args, **kwargs):
        """
        Vector = d2At(pos) - Get the second derivative at the given parameter [0|Length] if defined
        derivative2At(u,v) -> (vectorU,vectorV)
        """
    @staticmethod
    def getUVNodes(*args, **kwargs):
        """
        Get the list of (u,v) nodes of the tessellation
        getUVNodes() -> list
        --
        An exception is raised if the face is not triangulated.
        """
    @staticmethod
    def isPartOfDomain(*args, **kwargs):
        """
        Check if a given (u,v) pair is inside the domain of a face
        isPartOfDomain(u,v) -> bool
        """
    @staticmethod
    def makeEvolved(*args, **kwargs):
        """
        Profile along the spine
        """
    @staticmethod
    def makeHalfSpace(*args, **kwargs):
        """
        Make a half-space solid by this face and a reference point.
        makeHalfSpace(pos) -> Shape
        """
    @staticmethod
    def makeOffset(*args, **kwargs):
        """
        Offset the face by a given amount.
        makeOffset(dist) -> Face
        --
        Returns Compound of Wires. Deprecated - use makeOffset2D instead.
        """
    @staticmethod
    def normalAt(*args, **kwargs):
        """
        Get the normal vector at the given parameter [0|Length] if defined
        normalAt(pos) -> Vector
        """
    @staticmethod
    def tangentAt(*args, **kwargs):
        """
        Get the tangent in u and v isoparametric at the given point if defined
        tangentAt(u,v) -> Vector
        """
    @staticmethod
    def validate(*args, **kwargs):
        """
        Validate the face.
        validate()
        """
    @staticmethod
    def valueAt(*args, **kwargs):
        """
        Get the point at the given parameter [0|Length] if defined
        valueAt(u,v) -> Vector
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
    This is the father of all shape object classes
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def getElementHistory(*args, **kwargs):
        """
        getElementHistory(name,recursive=True,sameType=False,showName=False) - returns the element mapped name history
        
        name: mapped element name belonging to this shape
        recursive: if True, then track back the history through other objects till the origin
        sameType: if True, then stop trace back when element type changes
        showName: if False, return the owner object, or else return a tuple of object name and label
        
        If not recursive, then return tuple(sourceObject, sourceElementName, [intermediateNames...]),
        otherwise return a list of tuple.
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
class GeometryBoolExtension(GeometryExtension):
    """
    A GeometryExtension extending geometry objects with a boolean.
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
class GeometryDoubleExtension(GeometryExtension):
    """
    A GeometryExtension extending geometry objects with a double.
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
class GeometryIntExtension(GeometryExtension):
    """
    A GeometryExtension extending geometry objects with an int.
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
class GeometryStringExtension(GeometryExtension):
    """
    A GeometryExtension extending geometry objects with a string.
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
class Hyperbola(Conic):
    """
    Describes an hyperbola in 3D space
                    To create a hyperbola there are several ways:
                    Part.Hyperbola()
                        Creates an hyperbola with major radius 2 and minor radius 1 with the
                        center in (0,0,0)
    
                    Part.Hyperbola(Hyperbola)
                        Create a copy of the given hyperbola
    
                    Part.Hyperbola(S1,S2,Center)
                        Creates an hyperbola centered on the point Center, where
                        the plane of the hyperbola is defined by Center, S1 and S2,
                        its major axis is defined by Center and S1,
                        its major radius is the distance between Center and S1, and
                        its minor radius is the distance between S2 and the major axis.
    
                    Part.Hyperbola(Center,MajorRadius,MinorRadius)
                        Creates an hyperbola with major and minor radii MajorRadius and
                        MinorRadius, and located in the plane defined by Center and
                        the normal (0,0,1)
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
class Line(Curve):
    """
    Describes an infinite line
    To create a line there are several ways:
    Part.Line()
        Creates a default line
    
    Part.Line(Line)
        Creates a copy of the given line
    
    Part.Line(Point1,Point2)
        Creates a line that goes through two given points
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
class LineSegment(TrimmedCurve):
    """
    Describes a line segment
    To create a line segment there are several ways:
    Part.LineSegment()
        Creates a default line segment
    
    Part.LineSegment(LineSegment)
        Creates a copy of the given line segment
    
    Part.LineSegment(Point1,Point2)
        Creates a line segment that goes through two given points
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def setParameterRange(*args, **kwargs):
        """
        Set the parameter range of the underlying line geometry
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
class OCCConstructionError(OCCDomainError):
    pass
class OCCDimensionError(OCCDomainError):
    pass
class OCCDomainError(OCCError):
    pass
class OCCError(Base.FreeCADError):
    pass
class OCCRangeError(OCCDomainError):
    pass
class OffsetCurve(Curve):
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
class OffsetSurface(GeometrySurface):
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
class Parabola(Conic):
    """
    Describes a parabola in 3D space
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def compute(p1, p2, p3):
        """
                            The three points must lie on a plane parallel to xy plane and must not be collinear
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
class Part2DObject(Feature):
    """
    This object represents a 2D Shape in a 3D World
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
class Plane(GeometrySurface):
    """
    Describes an infinite plane
    To create a plane there are several ways:
    Part.Plane()
        Creates a default plane with base (0,0,0) and normal (0,0,1)
    
    Part.Plane(Plane)
        Creates a copy of the given plane
    
    Part.Plane(Plane, Distance)
        Creates a plane parallel to given plane at a certain distance
    
    Part.Plane(Location,Normal)
        Creates a plane with a given location and normal
    
    Part.Plane(Point1,Point2,Point3)
        Creates a plane defined by three non-linear points
    
    Part.Plane(A,B,C,D)
        Creates a plane from its cartesian equation
        Ax+By+Cz+D=0
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
class PlateSurface(GeometrySurface):
    """
    Represents a plate surface in FreeCAD. Plate surfaces can be defined by specifying points or curves as constraints, and they can also be approximated to B-spline surfaces using the makeApprox method. This class is commonly used in CAD modeling for creating surfaces that represent flat or curved plates, such as sheet metal components or structural elements.
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def makeApprox(*args, **kwargs):
        """
        Approximate the plate surface to a B-Spline surface
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
class Point(Geometry):
    """
    Describes a point
    To create a point there are several ways:
    Part.Point()
        Creates a default point
    
    Part.Point(Point)
        Creates a copy of the given point
    
    Part.Point(Vector)
        Creates a line for the given coordinates
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def toShape(*args, **kwargs):
        """
        Create a vertex from this point.
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
class RectangularTrimmedSurface(GeometrySurface):
    """
    Describes a portion of a surface (a patch) limited by two values of the
    u parameter in the u parametric direction, and two values of the v parameter in the v parametric
    direction. The domain of the trimmed surface must be within the domain of the surface being trimmed.
    
    The trimmed surface is defined by:
    - the basis surface, and
    - the values (umin, umax) and (vmin, vmax) which limit it in the u and v parametric directions.
    
    The trimmed surface is built from a copy of the basis surface. Therefore, when the basis surface
    is modified the trimmed surface is not changed. Consequently, the trimmed surface does not
    necessarily have the same orientation as the basis surface.
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def setTrim(*args, **kwargs):
        """
        Modifies this patch by changing the trim values applied to the original surface
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
class Shape(Data.ComplexGeoData):
    """
    TopoShape is the OpenCasCade topological shape wrapper.
    Sub-elements such as vertices, edges or faces are accessible as:
    * Vertex#, where # is in range(1, number of vertices)
    * Edge#, where # is in range(1, number of edges)
    * Face#, where # is in range(1, number of faces)
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def ancestorsOfType(*args, **kwargs):
        """
        For a sub-shape of this shape get its ancestors of a type.
        ancestorsOfType(shape, shape type) -> list
        """
    @staticmethod
    def check(*args, **kwargs):
        """
        Checks the shape and report errors in the shape structure.
        check([runBopCheck = False])
        --
        This is a more detailed check as done in isValid().
        if runBopCheck is True, a BOPCheck analysis is also performed.
        """
    @staticmethod
    def childShapes(*args, **kwargs):
        """
        Return a list of sub-shapes that are direct children of this shape.
        childShapes([cumOri=True, cumLoc=True]) -> list
        --
         * If cumOri is true, the function composes all
           sub-shapes with the orientation of this shape.
         * If cumLoc is true, the function multiplies all
           sub-shapes by the location of this shape, i.e. it applies to
           each sub-shape the transformation that is associated with this shape.
        """
    @staticmethod
    def cleaned(*args, **kwargs):
        """
        This creates a cleaned copy of the shape with the triangulation removed.
        clean()
        --
        This can be useful to reduce file size when exporting as a BREP file.
        Warning: Use the cleaned shape with care because certain algorithms may work incorrectly
        if the shape has no internal triangulation any more.
        """
    @staticmethod
    def clearCache(*args, **kwargs):
        """
        Clear internal sub-shape cache
        """
    @staticmethod
    def common(*args, **kwargs):
        """
        Intersection of this and a given (list of) topo shape.
        common(tool) -> Shape
          or
        common((tool1,tool2,...),[tolerance=0.0]) -> Shape
        --
        Supports:
        - Fuzzy Boolean operations (global tolerance for a Boolean operation)
        - Support of multiple arguments for a single Boolean operation (s1 AND (s2 OR s3))
        - Parallelization of Boolean Operations algorithm
        
        OCC 6.9.0 or later is required.
        """
    @staticmethod
    def complement(*args, **kwargs):
        """
        Computes the complement of the orientation of this shape,
        i.e. reverses the interior/exterior status of boundaries of this shape.
        complement()
        """
    @staticmethod
    def copy(*args, **kwargs):
        """
        Create a copy of this shape
        copy(copyGeom=True, copyMesh=False) -> Shape
        --
        If copyMesh is True, triangulation contained in original shape will be
        copied along with geometry.
        If copyGeom is False, only topological objects will be copied, while
        geometry and triangulation will be shared with original shape.
        """
    @staticmethod
    def countElement(*args, **kwargs):
        """
        Returns the count of a type of element
        countElement(type) -> int
        """
    @staticmethod
    def cut(*args, **kwargs):
        """
        Difference of this and a given (list of) topo shape
        cut(tool) -> Shape
          or
        cut((tool1,tool2,...),[tolerance=0.0]) -> Shape
        --
        Supports:
        - Fuzzy Boolean operations (global tolerance for a Boolean operation)
        - Support of multiple arguments for a single Boolean operation
        - Parallelization of Boolean Operations algorithm
        
        OCC 6.9.0 or later is required.
        """
    @staticmethod
    def defeaturing(*args, **kwargs):
        """
        Remove a feature defined by supplied faces and return a new shape.
        defeaturing(shapeList) -> Shape
        --
        The parameter is a list of faces.
        """
    @staticmethod
    def distToShape(*args, **kwargs):
        """
        Find the minimum distance to another shape.
        distToShape(shape, tol=1e-7) -> (dist, vectors, infos)
        --
        dist is the minimum distance, in mm (float value).
        
        vectors is a list of pairs of App.Vector. Each pair corresponds to solution.
        Example: [(App.Vector(2.0, -1.0, 2.0), App.Vector(2.0, 0.0, 2.0)),
        (App.Vector(2.0, -1.0, 2.0), App.Vector(2.0, -1.0, 3.0))]
        First vector is a point on self, second vector is a point on s.
        
        infos contains additional info on the solutions. It is a list of tuples:
        (topo1, index1, params1, topo2, index2, params2)
        
            topo1, topo2 are strings identifying type of BREP element: 'Vertex',
            'Edge', or 'Face'.
        
            index1, index2 are indexes of the elements (zero-based).
        
            params1, params2 are parameters of internal space of the elements. For
            vertices, params is None. For edges, params is one float, u. For faces,
            params is a tuple (u,v).
        """
    @staticmethod
    def dumpToString(*args, **kwargs):
        """
        Dump information about the shape to a string.
        dumpToString() -> string
        """
    @staticmethod
    def dumps(*args, **kwargs):
        """
        Serialize the content of this shape to a string in BREP format.
        """
    @staticmethod
    def exportBinary(*args, **kwargs):
        """
        Export the content of this shape in binary format to a file.
        exportBinary(filename)
        """
    @staticmethod
    def exportBrep(*args, **kwargs):
        """
        Export the content of this shape to an BREP file.
        exportBrep(filename)
        --
        BREP is an OpenCasCade native format.
        """
    @staticmethod
    def exportBrepToString(*args, **kwargs):
        """
        Export the content of this shape to a string in BREP format.
        exportBrepToString() -> string
        --
        BREP is an OpenCasCade native format.
        """
    @staticmethod
    def exportIges(*args, **kwargs):
        """
        Export the content of this shape to an IGES file.
        exportIges(filename)
        """
    @staticmethod
    def exportStep(*args, **kwargs):
        """
        Export the content of this shape to an STEP file.
        exportStep(filename)
        """
    @staticmethod
    def exportStl(*args, **kwargs):
        """
        Export the content of this shape to an STL mesh file.
        exportStl(filename)
        """
    @staticmethod
    def extrude(*args, **kwargs):
        """
        Extrude the shape along a vector.
        extrude(vector) -> Shape
        --
        Shp2 = Shp1.extrude(App.Vector(0,0,10)) - extrude the shape 10 mm in the +Z direction.
        """
    @staticmethod
    def findPlane(*args, **kwargs):
        """
        return a plane if the shape is planar
        findPlane(tol=None) -> Shape
        """
    @staticmethod
    def findSubShape(*args, **kwargs):
        """
                          Find sub shape and return the shape type name and index. If not found,
                          then return (None, 0)
        """
    @staticmethod
    def findSubShapesWithSharedVertex(shape, needName = False, checkGeometry = True, tol = 1e-7, atol = 1e-12) -> Shape:
        """
                          shape: input elementary shape, currently only support Face, Edge, or Vertex
        
                          needName: if True, return a list of tuple(name, shape), or else return a list
                          of shapes.
        
                          checkGeometry: whether to compare geometry
        
                          tol: distance tolerance
        
                          atol: angular tolerance
        
                          Search sub shape by checking vertex coordinates and comparing the underlying
                          geometries, This can find shapes that are copied. It currently only works with
                          elementary shapes, Face, Edge, Vertex.
        """
    @staticmethod
    def fix(*args, **kwargs):
        """
        Tries to fix a broken shape.
        fix(working precision, minimum precision, maximum precision) -> bool
        --
        True is returned if the operation succeeded, False otherwise.
        """
    @staticmethod
    def fixTolerance(*args, **kwargs):
        """
        Sets (enforces) tolerances in a shape to the given value
        fixTolerance(value, [ShapeType=Shape])
        --
        ShapeType = Vertex : only vertices are set
        ShapeType = Edge   : only edges are set
        ShapeType = Face   : only faces are set
        ShapeType = Wire   : to have edges and their vertices set
        ShapeType = other value : all (vertices,edges,faces) are set
        """
    @staticmethod
    def fuse(*args, **kwargs):
        """
        Union of this and a given (list of) topo shape.
        fuse(tool) -> Shape
          or
        fuse((tool1,tool2,...),[tolerance=0.0]) -> Shape
        --
        Union of this and a given list of topo shapes.
        
        Supports (OCCT 6.9.0 and above):
        - Fuzzy Boolean operations (global tolerance for a Boolean operation)
        - Support of multiple arguments for a single Boolean operation
        - Parallelization of Boolean Operations algorithm
        
        Beginning from OCCT 6.8.1 a tolerance value can be specified.
        """
    @staticmethod
    def generalFuse(*args, **kwargs):
        """
        Run general fuse algorithm (GFA) between this and given shapes.
        generalFuse(list_of_other_shapes, [fuzzy_value = 0.0]) -> (result, map)
        --
        list_of_other_shapes: shapes to run the algorithm against (the list is
        effectively prepended by 'self').
        
        fuzzy_value: extra tolerance to apply when searching for interferences, in
        addition to tolerances of the input shapes.
        
        Returns a tuple of 2: (result, map).
        
        result is a compound containing all the pieces generated by the algorithm
        (e.g., for two spheres, the pieces are three touching solids). Pieces that
        touch share elements.
        
        map is a list of lists of shapes, providing the info on which children of
        result came from which argument. The length of list is equal to length of
        list_of_other_shapes + 1. First element is a list of pieces that came from
        shape of this, and the rest are those that come from corresponding shapes in
        list_of_other_shapes.
        hint: use isSame method to test shape equality
        
        Parallelization of Boolean Operations algorithm
        
        OCC 6.9.0 or later is required.
        """
    @staticmethod
    def getChildShapes(*args, **kwargs):
        """
                          Return a list of child sub-shapes of given type.
        
                          shapetype: the type of requesting sub shapes
                          avoidtype: optional shape type to skip when exploring
        """
    @staticmethod
    def getElement(*args, **kwargs):
        """
        Returns a SubElement
        getElement(elementName, [silent = False]) -> Face | Edge | Vertex
        elementName:  SubElement name - i.e. 'Edge1', 'Face3' etc. 
                      Accepts TNP mitigation mapped names as well
        silent:  True to suppress the exception throw if the shape isn't found.
        """
    @staticmethod
    def getElementHistory(*args, **kwargs):
        """
        getElementHistory(name) - returns the element mapped name history
        
                          name: mapped element name belonging to this shape
        
                          Returns tuple(sourceShapeTag, sourceName, [intermediateNames...]),
                          or None if no history.
        """
    @staticmethod
    def getTolerance(*args, **kwargs):
        """
        Determines a tolerance from the ones stored in a shape
        getTolerance(mode, ShapeType=Shape) -> float
        --
        mode = 0 : returns the average value between sub-shapes,
        mode > 0 : returns the maximal found,
        mode < 0 : returns the minimal found.
        ShapeType defines what kinds of sub-shapes to consider:
        Shape (default) : all : Vertex, Edge, Face,
        Vertex : only vertices,
        Edge   : only edges,
        Face   : only faces,
        Shell  : combined Shell + Face, for each face (and containing
                 shell), also checks edge and Vertex
        """
    @staticmethod
    def globalTolerance(*args, **kwargs):
        """
        Returns the computed tolerance according to the mode
        globalTolerance(mode) -> float
        --
        mode = 0 : average
        mode > 0 : maximal
        mode < 0 : minimal
        """
    @staticmethod
    def hashCode(*args, **kwargs):
        """
        This value is computed from the value of the underlying shape reference and the location.
        hashCode() -> int
        --
        Orientation is not taken into account.
        """
    @staticmethod
    def importBinary(*args, **kwargs):
        """
        Import the content to this shape of a string in BREP format.
        importBinary(filename)
        """
    @staticmethod
    def importBrep(*args, **kwargs):
        """
        Load the shape from a file in BREP format.
        importBrep(filename)
        """
    @staticmethod
    def importBrepFromString(*args, **kwargs):
        """
        Load the shape from a string that keeps the content in BREP format.
        importBrepFromString(string, [displayProgressBar=True])
        --
        importBrepFromString(str,False) to not display a progress bar.
        """
    @staticmethod
    def inTolerance(*args, **kwargs):
        """
        Determines which shapes have a tolerance within a given interval
        inTolerance(value, [ShapeType=Shape]) -> ShapeList
        --
        ShapeType is interpreted as in the method getTolerance
        """
    @staticmethod
    def isClosed(*args, **kwargs):
        """
        Checks if the shape is closed.
        isClosed() -> bool
        --
        If the shape is a shell it returns True if it has no free boundaries (edges).
        If the shape is a wire it returns True if it has no free ends (vertices).
        (Internal and External sub-shepes are ignored in these checks)
        If the shape is an edge it returns True if its vertices are the same.
        """
    @staticmethod
    def isCoplanar(*args, **kwargs):
        """
        Checks if this shape is coplanar with the given shape.
        isCoplanar(shape,tol=None) -> bool
        """
    @staticmethod
    def isEqual(*args, **kwargs):
        """
        Checks if both shapes are equal.
                This means geometry, placement and orientation are equal.
        isEqual(shape) -> bool
        """
    @staticmethod
    def isInfinite(*args, **kwargs):
        """
        Checks if this shape has an infinite expansion.
        isInfinite() -> bool
        """
    @staticmethod
    def isInside(*args, **kwargs):
        """
        Checks whether a point is inside or outside the shape.
        isInside(point, tolerance, checkFace) => Boolean
        --
        checkFace indicates if the point lying directly on a face is considered to be inside or not
        """
    @staticmethod
    def isNull(*args, **kwargs):
        """
        Checks if the shape is null.
        isNull() -> bool
        """
    @staticmethod
    def isPartner(*args, **kwargs):
        """
        Checks if both shapes share the same geometry.
        Placement and orientation may differ.
        isPartner(shape) -> bool
        """
    @staticmethod
    def isSame(*args, **kwargs):
        """
        Checks if both shapes share the same geometry
                and placement. Orientation may differ.
        isSame(shape) -> bool
        """
    @staticmethod
    def isValid(*args, **kwargs):
        """
        Checks if the shape is valid, i.e. neither null, nor empty nor corrupted.
        isValid() -> bool
        """
    @staticmethod
    def limitTolerance(*args, **kwargs):
        """
        Limits tolerances in a shape
        limitTolerance(tmin, [tmax=0, ShapeType=Shape]) -> bool
        --
        tmin = tmax -> as fixTolerance (forces)
        tmin = 0   -> maximum tolerance will be tmax
        tmax = 0 or not given (more generally, tmax < tmin) ->
        tmax ignored, minimum will be tmin
        else, maximum will be max and minimum will be min
        ShapeType = Vertex : only vertices are set
        ShapeType = Edge   : only edges are set
        ShapeType = Face   : only faces are set
        ShapeType = Wire   : to have edges and their vertices set
        ShapeType = other value : all (vertices,edges,faces) are set
        Returns True if at least one tolerance of the sub-shape has been modified
        """
    @staticmethod
    def loads(*args, **kwargs):
        """
        Deserialize the content of this shape from a string in BREP format.
        """
    @staticmethod
    def makeChamfer(*args, **kwargs):
        """
        Make chamfer.
        makeChamfer(radius,edgeList) -> Shape
        or
        makeChamfer(radius1,radius2,edgeList) -> Shape
        """
    @staticmethod
    def makeEvolved(*args, **kwargs):
        """
        Profile along the spine
        """
    @staticmethod
    def makeFillet(*args, **kwargs):
        """
        Make fillet.
        makeFillet(radius,edgeList) -> Shape
        or
        makeFillet(radius1,radius2,edgeList) -> Shape
        """
    @staticmethod
    def makeOffset2D(*args, **kwargs):
        """
        makes an offset shape (2d offsetting).
        makeOffset2D(offset, [join = 0, fill = False, openResult = false, intersection =
        false]) -> Shape
        --
        The function supports keyword
        arguments. Input shape (self) can be edge, wire, face, or a compound of those.
        
        * offset: distance to expand the shape by. Negative value will shrink the
        shape.
        
        * join: method of offsetting non-tangent joints. 0 = arcs, 1 = tangent, 2 =
        intersection
        
        * fill: if true, the output is a face filling the space covered by offset. If
        false, the output is a wire.
        
        * openResult: affects the way open wires are processed. If False, an open wire
        is made. If True, a closed wire is made from a double-sided offset, with rounds
        around open vertices.
        
        * intersection: affects the way compounds are processed. If False, all children
        are offset independently. If True, and children are edges/wires, the children
        are offset in a collective manner. If compounding is nested, collectiveness
        does not spread across compounds (only direct children of a compound are taken
        collectively).
        
        Returns: result of offsetting (wire or face or compound of those). Compounding
        structure follows that of source shape.
        """
    @staticmethod
    def makeOffsetShape(*args, **kwargs):
        """
        makes an offset shape (3d offsetting).
        makeOffsetShape(offset, tolerance, [inter = False, self_inter = False,
        offsetMode = 0, join = 0, fill = False]) -> Shape
        --
        The function supports keyword arguments.
        
        * offset: distance to expand the shape by. Negative value will shrink the
        shape.
        
        * tolerance: precision of approximation.
        
        * inter: (parameter to OCC routine; not implemented)
        
        * self_inter: (parameter to OCC routine; not implemented)
        
        * offsetMode: 0 = skin; 1 = pipe; 2 = recto-verso
        
        * join: method of offsetting non-tangent joints. 0 = arcs, 1 = tangent, 2 =
        intersection
        
        * fill: if true, offsetting a shell is to yield a solid
        
        Returns: result of offsetting.
        """
    @staticmethod
    def makeParallelProjection(*args, **kwargs):
        """
        Parallel projection of an edge or wire on this shape
        makeParallelProjection(shape, dir) -> Shape
        """
    @staticmethod
    def makePerspectiveProjection(*args, **kwargs):
        """
        Perspective projection of an edge or wire on this shape
        makePerspectiveProjection(shape, pnt) -> Shape
        """
    @staticmethod
    def makeShapeFromMesh(*args, **kwargs):
        """
        Make a compound shape out of mesh data.
        makeShapeFromMesh((vertex,facets),tolerance) -> Shape
        --
        Note: This should be used for rather small meshes only.
        """
    @staticmethod
    def makeThickness(*args, **kwargs):
        """
        Hollow a solid according to given thickness and faces.
        makeThickness(List of faces, Offset (Float), Tolerance (Float)) -> Shape
        --
        A hollowed solid is built from an initial solid and a set of faces on this solid,
        which are to be removed. The remaining faces of the solid become the walls of
        the hollowed solid, their thickness defined at the time of construction.
        """
    @staticmethod
    def makeWires(*args, **kwargs):
        """
        make wire(s) using the edges of this shape
        makeWires([op=None])
        --
        The function will sort any edges inside the current shape, and connect them
        into wire. If more than one wire is found, then it will make a compound out of
        all found wires.
        
        This function is element mapping aware. If the input shape has non-zero Tag,
        it will map any edge and vertex element name inside the input shape into the
        itself.
        
        op: an optional string to be appended when auto generates element mapping.
        """
    @staticmethod
    def mapShapes(generated, modified, op = ''):
        """
                          generate element names with user defined mapping
        
                          generated: a list of tuple(src, dst) that indicating src shape or shapes
                          generates dst shape or shapes. Note that the dst shape or shapes
                          must be sub-shapes of this shape.
                          modified: a list of tuple(src, dst) that indicating src shape or shapes
                          modifies into dst shape or shapes. Note that the dst shape or
                          shapes must be sub-shapes of this shape.
                          op: optional string prefix to append before the mapped sub element names
        """
    @staticmethod
    def mapSubElement(*args, **kwargs):
        """
        mapSubElement(shape|[shape...], op='') - maps the sub element of other shape
        
                          shape:  other shape or sequence of shapes to map the sub-elements
                          op:     optional string prefix to append before the mapped sub element names
        """
    @staticmethod
    def mirror(*args, **kwargs):
        """
        Mirror this shape on a given plane.
        mirror(base, norm) -> Shape
        --
        The plane is given with its base point and its normal direction.
        """
    @staticmethod
    def multiFuse(*args, **kwargs):
        """
        Union of this and a given list of topo shapes.
        multiFuse((tool1,tool2,...),[tolerance=0.0]) -> Shape
        --
        Supports (OCCT 6.9.0 and above):
        - Fuzzy Boolean operations (global tolerance for a Boolean operation)
        - Support of multiple arguments for a single Boolean operation
        - Parallelization of Boolean Operations algorithm
        
        Beginning from OCCT 6.8.1 a tolerance value can be specified.
        Deprecated: use fuse() instead.
        """
    @staticmethod
    def nullify(*args, **kwargs):
        """
        Destroys the reference to the underlying shape stored in this shape.
        As a result, this shape becomes null.
        nullify()
        """
    @staticmethod
    def oldFuse(*args, **kwargs):
        """
        Union of this and a given topo shape (old algorithm).
        oldFuse(tool) -> Shape
        """
    @staticmethod
    def optimalBoundingBox(*args, **kwargs):
        """
        Get the optimal bounding box
        optimalBoundingBox([useTriangulation = True, useShapeTolerance = False]) -> bound box
        """
    @staticmethod
    def overTolerance(*args, **kwargs):
        """
        Determines which shapes have a tolerance over the given value
        overTolerance(value, [ShapeType=Shape]) -> ShapeList
        --
        ShapeType is interpreted as in the method getTolerance
        """
    @staticmethod
    def project(*args, **kwargs):
        """
        Project a list of shapes on this shape
        project(shapeList) -> Shape
        """
    @staticmethod
    def proximity(*args, **kwargs):
        """
        Returns two lists of Face indexes for the Faces involved in the intersection.
        proximity(shape,[tolerance]) -> (selfFaces, shapeFaces)
        """
    @staticmethod
    def read(*args, **kwargs):
        """
        Read in an IGES, STEP or BREP file.
        read(filename)
        """
    @staticmethod
    def reflectLines(*args, **kwargs):
        """
        Build projection or reflect lines of a shape according to a view direction.
        reflectLines(ViewDir, [ViewPos, UpDir, EdgeType, Visible, OnShape]) -> Shape (Compound of edges)
        --
        This algorithm computes the projection of the shape in the ViewDir direction.
        If OnShape is False(default), the returned edges are flat on the XY plane defined by
        ViewPos(origin) and UpDir(up direction).
        If OnShape is True, the returned edges are the corresponding 3D reflect lines located on the shape.
        EdgeType is a string defining the type of result edges :
        - IsoLine : isoparametric line
        - OutLine : outline (silhouette) edge
        - Rg1Line : smooth edge of G1-continuity between two surfaces
        - RgNLine : sewn edge of CN-continuity on one surface
        - Sharp : sharp edge (of C0-continuity)
        If Visible is True (default), only visible edges are returned.
        If Visible is False, only invisible edges are returned.
        """
    @staticmethod
    def removeInternalWires(*args, **kwargs):
        """
        Removes internal wires (also holes) from the shape.
        removeInternalWires(minimalArea) -> bool
        """
    @staticmethod
    def removeShape(*args, **kwargs):
        """
        Remove a sub-shape and return a new shape.
        removeShape(shapeList) -> Shape
        --
        The parameter is a list of shapes.
        """
    @staticmethod
    def removeSplitter(*args, **kwargs):
        """
        Removes redundant edges from the B-REP model
        removeSplitter() -> Shape
        """
    @staticmethod
    def replaceShape(*args, **kwargs):
        """
        Replace a sub-shape with a new shape and return a new shape.
        replaceShape(tupleList) -> Shape
        --
        The parameter is in the form list of tuples with the two shapes.
        """
    @staticmethod
    def reverse(*args, **kwargs):
        """
        Reverses the orientation of this shape.
        reverse()
        """
    @staticmethod
    def reversed(*args, **kwargs):
        """
        Reverses the orientation of a copy of this shape.
        reversed() -> Shape
        """
    @staticmethod
    def revolve(*args, **kwargs):
        """
        Revolve the shape around an Axis to a given degree.
        revolve(base, direction, angle)
        --
        Part.revolve(App.Vector(0,0,0),App.Vector(0,0,1),360) - revolves the shape around the Z Axis 360 degree.
        
        Hints: Sometimes you want to create a rotation body out of a closed edge or wire.
        Example:
        from FreeCAD import Base
        import Part
        V=Base.Vector
        
        e=Part.Ellipse()
        s=e.toShape()
        r=s.revolve(V(0,0,0),V(0,1,0), 360)
        Part.show(r)
        
        However, you may possibly realize some rendering artifacts or that the mesh
        creation seems to hang. This is because this way the surface is created twice.
        Since the curve is a full ellipse it is sufficient to do a rotation of 180 degree
        only, i.e. r=s.revolve(V(0,0,0),V(0,1,0), 180)
        
        Now when rendering this object you may still see some artifacts at the poles. Now the
        problem seems to be that the meshing algorithm doesn't like to rotate around a point
        where there is no vertex.
        
        The idea to fix this issue is that you create only half of the ellipse so that its shape
        representation has vertexes at its start and end point.
        
        from FreeCAD import Base
        import Part
        V=Base.Vector
        
        e=Part.Ellipse()
        s=e.toShape(e.LastParameter/4,3*e.LastParameter/4)
        r=s.revolve(V(0,0,0),V(0,1,0), 360)
        Part.show(r)
        """
    @staticmethod
    def rotate(*args, **kwargs):
        """
        Apply the rotation (base,dir,degree) to the current location of this shape
        rotate(base,dir,degree)
        --
        Shp.rotate(App.Vector(0,0,0),App.Vector(0,0,1),180) - rotate the shape around the Z Axis 180 degrees.
        """
    @staticmethod
    def rotated(*args, **kwargs):
        """
        Create a new shape with rotation.
        rotated(base,dir,degree) -> shape
        """
    @staticmethod
    def scale(*args, **kwargs):
        """
        Apply scaling with point and factor to this shape.
        scale(factor,[base=App.Vector(0,0,0)])
        """
    @staticmethod
    def scaled(*args, **kwargs):
        """
        Create a new shape with scale.
        scaled(factor,[base=App.Vector(0,0,0)]) -> shape
        """
    @staticmethod
    def section(*args, **kwargs):
        """
        Section of this with a given (list of) topo shape.
        section(tool,[approximation=False]) -> Shape
          or
        section((tool1,tool2,...),[tolerance=0.0, approximation=False]) -> Shape
        --
        If approximation is True, section edges are approximated to a C1-continuous BSpline curve.
        
        Supports:
        - Fuzzy Boolean operations (global tolerance for a Boolean operation)
        - Support of multiple arguments for a single Boolean operation (s1 AND (s2 OR s3))
        - Parallelization of Boolean Operations algorithm
        
        OCC 6.9.0 or later is required.
        """
    @staticmethod
    def sewShape(*args, **kwargs):
        """
        Sew the shape if there is a gap.
        sewShape()
        """
    @staticmethod
    def slice(*args, **kwargs):
        """
        Make single slice of this shape.
        slice(direction, distance) --> Wires
        """
    @staticmethod
    def slices(*args, **kwargs):
        """
        Make slices of this shape.
        slices(direction, distancesList) --> Wires
        """
    @staticmethod
    def tessellate(*args, **kwargs):
        """
        Tessellate the shape and return a list of vertices and face indices
        tessellate() -> (vertex,facets)
        """
    @staticmethod
    def toNurbs(*args, **kwargs):
        """
        Conversion of the complete geometry of a shape into NURBS geometry.
        toNurbs() -> Shape
        --
        For example, all curves supporting edges of the basis shape are converted
        into B-spline curves, and all surfaces supporting its faces are converted
        into B-spline surfaces.
        """
    @staticmethod
    def transformGeometry(*args, **kwargs):
        """
        Apply geometric transformation on this or a copy the shape.
        transformGeometry(matrix) -> Shape
        --
        This method returns a new shape.
        The transformation to be applied is defined as a 4x4 matrix.
        The underlying geometry of the following shapes may change:
        - a curve which supports an edge of the shape, or
        - a surface which supports a face of the shape;
        
        For example, a circle may be transformed into an ellipse when
        applying an affinity transformation. It may also happen that
        the circle then is represented as a B-spline curve.
        
        The transformation is applied to:
        - all the curves which support edges of the shape, and
        - all the surfaces which support faces of the shape.
        
        Note: If you want to transform a shape without changing the
        underlying geometry then use the methods translate or rotate.
        """
    @staticmethod
    def transformShape(*args, **kwargs):
        """
        Apply transformation on a shape without changing the underlying geometry.
        transformShape(Matrix,[boolean copy=False, checkScale=False]) -> None
        --
        If checkScale is True, it will use transformGeometry if non-uniform
        scaling is detected.
        """
    @staticmethod
    def transformed(*args, **kwargs):
        """
        Create a new transformed shape
        transformed(Matrix,copy=False,checkScale=False,op=None) -> shape
        """
    @staticmethod
    def translate(*args, **kwargs):
        """
        Apply the translation to the current location of this shape.
        translate(vector)
        """
    @staticmethod
    def translated(*args, **kwargs):
        """
        Create a new shape with translation
        translated(vector) -> shape
        """
    @staticmethod
    def writeInventor(*args, **kwargs):
        """
        Write the mesh in OpenInventor format to a string.
        writeInventor() -> string
        """
    def __delattr__(self, name):
        """
        Implement delattr(self, name).
        """
    def __getattribute__(self, name):
        """
        Return getattr(self, name).
        """
    def __hash__(self):
        """
        Return hash(self).
        """
    def __repr__(self):
        """
        Return repr(self).
        """
    def __setattr__(self, name, value):
        """
        Implement setattr(self, name, value).
        """
class Shell(Shape):
    """
    Create a shell out of a list of faces
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def add(*args, **kwargs):
        """
        Add a face to the shell.
        add(face)
        """
    @staticmethod
    def getBadEdges(*args, **kwargs):
        """
        Get bad edges as compound.
        getBadEdges() -> compound
        """
    @staticmethod
    def getFreeEdges(*args, **kwargs):
        """
        Get free edges as compound.
        getFreeEdges() -> compound
        """
    @staticmethod
    def makeHalfSpace(*args, **kwargs):
        """
        Make a half-space solid by this shell and a reference point.
        makeHalfSpace(point) -> Solid
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
class Solid(Shape):
    """
    Part.Solid(shape): Create a solid out of shells of shape. If shape is a compsolid, the overall volume solid is created.
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def getMomentOfInertia(*args, **kwargs):
        """
        computes the moment of inertia of the material system about the axis A.
        getMomentOfInertia(point,direction) -> Float
        """
    @staticmethod
    def getRadiusOfGyration(*args, **kwargs):
        """
        Returns the radius of gyration of the current system about the axis A.
        getRadiusOfGyration(point,direction) -> Float
        """
    @staticmethod
    def offsetFaces(*args, **kwargs):
        """
        Extrude single faces of the solid.
        offsetFaces(facesTuple, offset) -> Solid
        or
        offsetFaces(dict) -> Solid
        --
        Example:
        solid.offsetFaces((solid.Faces[0],solid.Faces[1]), 1.5)
        
        solid.offsetFaces({solid.Faces[0]:1.0,solid.Faces[1]:2.0})
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
class Sphere(GeometrySurface):
    """
    Describes a sphere in 3D space
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
class SurfaceOfExtrusion(GeometrySurface):
    """
    Describes a surface of linear extrusion
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
class SurfaceOfRevolution(GeometrySurface):
    """
    Describes a surface of revolution
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
class Toroid(GeometrySurface):
    """
    Describes a toroid in 3D space
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
class Vertex(Shape):
    """
    TopoShapeVertex is the OpenCasCade topological vertex wrapper
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
class Wire(Shape):
    """
    TopoShapeWire is the OpenCasCade topological wire wrapper
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def add(*args, **kwargs):
        """
        Add an edge to the wire
        add(edge)
        """
    @staticmethod
    def approximate(*args, **kwargs):
        """
        Approximate B-Spline-curve from this wire
        approximate([Tol2d,Tol3d=1e-4,MaxSegments=10,MaxDegree=3]) -> BSpline
        """
    @staticmethod
    def discretize(*args, **kwargs):
        """
        Discretizes the wire and returns a list of points.
        discretize(kwargs) -> list
        --
        The function accepts keywords as argument:
        discretize(Number=n) => gives a list of 'n' equidistant points
        discretize(QuasiNumber=n) => gives a list of 'n' quasi equidistant points (is faster than the method above)
        discretize(Distance=d) => gives a list of equidistant points with distance 'd'
        discretize(Deflection=d) => gives a list of points with a maximum deflection 'd' to the wire
        discretize(QuasiDeflection=d) => gives a list of points with a maximum deflection 'd' to the wire (faster)
        discretize(Angular=a,Curvature=c,[Minimum=m]) => gives a list of points with an angular deflection of 'a'
                                            and a curvature deflection of 'c'. Optionally a minimum number of points
                                            can be set which by default is set to 2.
        
        Optionally you can set the keywords 'First' and 'Last' to define a sub-range of the parameter range
        of the wire.
        
        If no keyword is given then it depends on whether the argument is an int or float.
        If it's an int then the behaviour is as if using the keyword 'Number', if it's float
        then the behaviour is as if using the keyword 'Distance'.
        
        Example:
        
        import Part
        V=App.Vector
        
        e1=Part.makeCircle(5,V(0,0,0),V(0,0,1),0,180)
        e2=Part.makeCircle(5,V(10,0,0),V(0,0,1),180,360)
        w=Part.Wire([e1,e2])
        
        p=w.discretize(Number=50)
        s=Part.Compound([Part.Vertex(i) for i in p])
        Part.show(s)
        
        
        p=w.discretize(Angular=0.09,Curvature=0.01,Minimum=100)
        s=Part.Compound([Part.Vertex(i) for i in p])
        Part.show(s)
        """
    @staticmethod
    def fixWire(*args, **kwargs):
        """
        Fix wire
        fixWire([face, tolerance])
        --
        A face and a tolerance can optionally be supplied to the algorithm:
        """
    @staticmethod
    def makeEvolved(*args, **kwargs):
        """
        Profile along the spine
        """
    @staticmethod
    def makeHomogenousWires(*args, **kwargs):
        """
        Make this and the given wire homogeneous to have the same number of edges
        makeHomogenousWires(wire) -> Wire
        """
    @staticmethod
    def makeOffset(*args, **kwargs):
        """
        Offset the shape by a given amount. DEPRECATED - use makeOffset2D instead.
        """
    @staticmethod
    def makePipe(*args, **kwargs):
        """
        Make a pipe by sweeping along a wire.
        makePipe(profile) -> Shape
        """
    @staticmethod
    def makePipeShell(*args, **kwargs):
        """
        Make a loft defined by a list of profiles along a wire.
        makePipeShell(shapeList,[isSolid=False,isFrenet=False,transition=0]) -> Shape
        --
        Transition can be 0 (default), 1 (right corners) or 2 (rounded corners).
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
OCC_VERSION: str = '7.8.1'
