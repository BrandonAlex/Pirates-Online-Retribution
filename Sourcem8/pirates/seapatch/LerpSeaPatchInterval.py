from CLerpSeaPatchInterval import CLerpSeaPatchInterval

class LerpSeaPatchInterval(CLerpSeaPatchInterval):
    lerpNum = 1

    def __init__(self, name, duration, blendType, patch, initial, target):
        if name == None:
            name = 'LerpSeaPatchInterval-%d' % self.lerpNum
            LerpSeaPatchInterval.lerpNum += 1

        blendType = self.stringBlendType(blendType)
        if target == None:
            target = SeaPatchRoot()

        CLerpSeaPatchInterval.__init__(self, name, duration, blendType, patch, initial, target)
