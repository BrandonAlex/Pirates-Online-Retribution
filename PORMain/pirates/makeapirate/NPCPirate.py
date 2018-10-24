from panda3d.core import GeomNode
from direct.showbase import DirectObject
import random

class NPCPirate(DirectObject.DirectObject):

    def __init__(self, pirate, dna = None):
        self.pirate = pirate
        self.dna = dna


    def delete(self):
        del self.pirate
        del self.dna


    def setupHead(self):
        return None
        geom = self.pirate.getGeomNode()
        self.headIdx = 0
        self.heads = []
        if not geom.findAllMatches('**/head_a').isEmpty():
            self.heads.append(geom.findAllMatches('**/head_a'))

        if not geom.findAllMatches('**/head_b').isEmpty():
            self.heads.append(geom.findAllMatches('**/head_b'))

        if not geom.findAllMatches('**/head_c').isEmpty():
            self.heads.append(geom.findAllMatches('**/head_c'))

        if not geom.findAllMatches('**/head_d').isEmpty():
            self.heads.append(geom.findAllMatches('**/head_d'))

        if not geom.findAllMatches('**/head_e').isEmpty():
            self.heads.append(geom.findAllMatches('**/head_e'))

        self.numHeads = len(self.heads)


    def setupBody(self):
        return None
        geom = self.pirate.getGeomNode()
        self.bodys = []
        self.bodyIdx = 0
        self.body = geom.findAllMatches('**/body_*')
        self.bodys.append(geom.findAllMatches('**/body_torso_base'))
        self.bodys.append(geom.findAllMatches('**/body_hand_left'))
        self.bodys.append(geom.findAllMatches('**/body_hand_right'))
        self.bodys.append(geom.findAllMatches('**/body_legs_base'))
        self.bodys.append(geom.findAllMatches('**/body_foot_left'))
        self.bodys.append(geom.findAllMatches('**/body_foot_right'))


    def setupClothes(self):
        return None
        geom = self.pirate.getGeomNode()
        self.accIdx = 0
        self.accs = []
        self.accs.append(geom.findAllMatches('**/acc_none*'))
        if not geom.findAllMatches('**/acc_neckerchief*').isEmpty():
            self.accs.append(geom.findAllMatches('**/acc_neckerchief*'))

        if not geom.findAllMatches('**/acc_bangle*').isEmpty():
            self.accs.append(geom.findAllMatches('**/acc_bangle*'))

        self.shirtIdx = 0
        self.shirts = []
        self.shirts.append(geom.findAllMatches('**/shirt_none*'))
        if not geom.findAllMatches('**/shirt_short_sleeve1*').isEmpty():
            self.shirts.append(geom.findAllMatches('**/shirt_short_sleeve1*'))

        if not geom.findAllMatches('**/shirt_tanktop*').isEmpty():
            self.shirts.append(geom.findAllMatches('**/shirt_tanktop*'))

        if not geom.findAllMatches('**/shirt_no_sleeve*').isEmpty():
            self.shirts.append(geom.findAllMatches('**/shirt_no_sleeve*'))

        self.vestIdx = 0
        self.vests = []
        self.vests.append(geom.findAllMatches('**/vest_none*'))
        if not geom.findAllMatches('**/vest_open*').isEmpty():
            self.vests.append(geom.findAllMatches('**/vest_open*'))

        if not geom.findAllMatches('**/vest_closed*').isEmpty():
            self.vests.append(geom.findAllMatches('**/vest_closed*'))

        if not geom.findAllMatches('**/vest_loose*').isEmpty():
            self.vests.append(geom.findAllMatches('**/vest_loose*'))

        self.coatIdx = 0
        self.coats = []
        self.coats.append(geom.findAllMatches('**/coat_none*'))
        if not geom.findAllMatches('**/coat_long*').isEmpty():
            self.coats.append(geom.findAllMatches('**/coat_long*'))

        self.pantIdx = 0
        self.pants = []
        self.pants.append(geom.findAllMatches('**/pant_none*'))
        if not geom.findAllMatches('**/pant_untucked*').isEmpty():
            self.pants.append(geom.findAllMatches('**/pant_untucked*'))

        if not geom.findAllMatches('**/pant_short*').isEmpty():
            self.pants.append(geom.findAllMatches('**/pant_short*'))

        if not geom.findAllMatches('**/pant_skirt*').isEmpty():
            self.pants.append(geom.findAllMatches('**/pant_skirt*'))

        self.shoeIdx = 0
        self.shoes = []
        self.shoes.append(geom.findAllMatches('**/shoe_none*'))
        if not geom.findAllMatches('**/shoe_short*').isEmpty():
            self.shoes.append(geom.findAllMatches('**/shoe_short*'))

        if not geom.findAllMatches('**/shoe_work*').isEmpty():
            self.shoes.append(geom.findAllMatches('**/shoe_work*'))

        if not geom.findAllMatches('**/shoe_medium*').isEmpty():
            self.shoes.append(geom.findAllMatches('**/shoe_medium*'))

        if not geom.findAllMatches('**/shoe_knee_high*').isEmpty():
            self.shoes.append(geom.findAllMatches('**/shoe_knee_high*'))



    def handleClothesHiding(self):
        pass


    def showClothes(self):
        return None
        self.body.unstash()
        for i in xrange(0, len(self.accs)):
            if i != self.accIdx:
                self.accs[i].stash()
                continue

        self.accs[self.accIdx].unstash()
        for i in xrange(0, len(self.shirts)):
            if i != self.shirtIdx:
                self.shirts[i].stash()
                continue

        self.shirts[self.shirtIdx].unstash()
        for i in xrange(0, len(self.vests)):
            if i != self.vestIdx:
                self.vests[i].stash()
                continue

        self.vests[self.vestIdx].unstash()
        for i in xrange(0, len(self.coats)):
            if i != self.coatIdx:
                self.coats[i].stash()
                continue

        self.coats[self.coatIdx].unstash()
        for i in xrange(0, len(self.pants)):
            if i != self.pantIdx:
                self.pants[i].stash()
                continue

        self.pants[self.pantIdx].unstash()
        for i in xrange(0, len(self.shoes)):
            if i != self.shoeIdx:
                self.shoes[i].stash()
                continue

        self.shoes[self.shoeIdx].unstash()
        if self.shoeIdx:
            self.bodys[4].stash()
            self.bodys[5].stash()



    def showHead(self):
        return None
        for i in xrange(0, self.numHeads):
            if i != self.headIdx:
                self.heads[i].stash()
                continue

        if self.numHeads:
            self.heads[self.headIdx].unstash()



    def resetPick(self):
        return None
        self.headIdx = 0


    def randomPick(self):
        return None
        if self.numHeads:
            cList = range(0, self.numHeads)
            cList.remove(self.headIdx)
            self.headIdx = random.choice(cList)



    def initialParts(self):
        return None
        self.showHead()
        self.showClothes()


    def setFromDNA(self):
        return None
        self.initialParts()
