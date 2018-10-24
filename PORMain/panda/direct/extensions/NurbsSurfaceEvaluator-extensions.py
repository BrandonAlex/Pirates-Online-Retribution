
    """
    NurbsSurfaceEvaluator-extensions module: contains methods to extend
    functionality of the NurbsSurfaceEvaluator class
    """

    def getUKnots(self):
        """Returns the U knot vector as a Python list of floats"""
        knots = []
        for i in xrange(self.getNumUKnots()):
            knots.append(self.getUKnot(i))
        return knots

    def getVKnots(self):
        """Returns the V knot vector as a Python list of floats"""
        knots = []
        for i in xrange(self.getNumVKnots()):
            knots.append(self.getVKnot(i))
        return knots

    def getVertices(self, relTo = None):
        """Returns the vertices as a 2-d Python list of Vec4's, relative
        to the indicated space if given."""

        verts = []
        for ui in xrange(self.getNumUVertices()):
            v = []
            if relTo:
                for vi in xrange(self.getNumVVertices()):
                    v.append(self.getVertex(ui, vi, relTo))
            else:
                for vi in xrange(self.getNumVVertices()):
                    v.append(self.getVertex(ui, vi))
            verts.append(v)
            
        return verts
