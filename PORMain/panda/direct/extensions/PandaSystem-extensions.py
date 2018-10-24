
    def getSystems(self):
        l = []
        for i in xrange(self.getNumSystems()):
            l.append(self.getSystem(l))
        return l
