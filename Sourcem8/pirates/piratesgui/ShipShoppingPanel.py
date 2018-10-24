# File: S (Python 2.4)

from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from pirates.ship import ShipGlobals
from pirates.piratesgui import PiratesGuiGlobals
from pirates.piratesbase import PiratesGlobals
from pirates.piratesgui.ShipFrameShopping import ShipFrameShopping
from pirates.piratesbase import PLocalizer
from pirates.band.DistributedBandMember import DistributedBandMember
from pirates.piratesgui.ShipSelectionPanel import ShipSelectionPanel
from pirates.distributed import InteractGlobals

class ShipShoppingPanel(ShipSelectionPanel):
    notify = directNotify.newCategory('ShipShoppingPanel')

    def __init__(self, title, doneCallback, mode):
        ShipSelectionPanel.__init__(self, title, doneCallback)
        self.initialiseoptions(ShipShoppingPanel)
        self.mode = mode


    def updateShip(self, shipId):
        frame = self.getFrame(shipId)
        if frame is not None:
            frameCallback = frame['command']
            frameIndex = self.getFrameIndex(frame)
            self.removeFrame(frame)
            self.addOwnShip(shipId, frameCallback, frameIndex, repaired = True)
            interactNPC = base.cr.interactionMgr.getCurrent()
            if interactNPC is not None:
                repairButtonState = DGG.DISABLED
                for frames in self.shipFrames.itervalues():
                    for frame in frames:
                        shipOV = frame.snapShot['shipOV']
                        if shipOV is not None:
                            if shipOV.Hp < shipOV.maxHp:
                                repairButtonState = DGG.NORMAL

                        shipOV.Hp < shipOV.maxHp


                for button in interactNPC.interactGUI.optionButtons:
                    if button['extraArgs'][0] == InteractGlobals.REPAIR:
                        if repairButtonState == DGG.NORMAL:
                            button['text_fg'] = PiratesGuiGlobals.TextFG1
                            button['image_color'] = VBase4(1.0, 1.0, 1.0, 1.0)
                        else:
                            button['text_fg'] = VBase4(0.29999999999999999, 0.25, 0.20000000000000001, 1.0)
                            button['image_color'] = VBase4(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1.0)
                        button['state'] = repairButtonState
                        continue





    def addOwnShip(self, shipId, callback, index = None, repaired = False):
        shipOV = base.cr.getOwnerView(shipId)
        if not shipOV:
            return None

        shipFrame = ShipFrameShopping(parent = self.scrollFrame.getCanvas(), relief = None, shipId = shipId, shipName = shipOV.name, shipClass = shipOV.shipClass, mode = self.mode, command = callback, extraArgs = [
            shipId])
        if repaired:
            shipOV.setHealthState(100.0)
            [ min(1, x) * 100 for x in shipOV.mastStates ]

        shipFrame.enableStatsOV(shipOV)
        self.addFrame(shipFrame, index)
