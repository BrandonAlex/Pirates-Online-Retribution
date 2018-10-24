from panda3d.direct import CMotionTrail
from panda3d.core import GeomNode
# STUB


class CMotionTrailVertex:
    def __init__(self):
        pass

class CMotionTrailFrame:
    def __init__(self):
        pass


class CMotionTrail:

    def __init__(self):
        pass

    def reset(self):
        pass

    def resetVertexList(self):
        pass

    def enable(self, enable):
        pass

    def setGeomNode(self, node):
        pass

    def addVertex(self, vertex, start_color, end_color, v):
        pass

    def setParameters(self, sampling_time, time_window, use_texture, calculate_relative_matrix, use_nurbs, resolution_distance):
        pass

    def checkForUpdate(self, current_time):
        pass

    def updateMotionTrail(self, current_time, transform):
        pass

    def beginGeometry(self):
        pass

    def endGeometry(self):
        pass

    def addGeometryQuad(self, v0, v1, v2, v3, c0, c1, c2, c3, t0, t1, t2, t3):
        pass
