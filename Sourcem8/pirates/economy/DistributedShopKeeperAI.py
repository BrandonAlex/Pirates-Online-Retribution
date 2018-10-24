# STUB

from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistributedShopKeeperAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedShopKeeperAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)

    # requestPurchaseRepair(uint32) airecv clsend
    # requestPurchaseOverhaul(uint32) airecv clsend
    # requestSellShip(uint32) airecv clsend
    # requestSellItem(uint32, uint32, uint16, uint16) airecv clsend
    # requestAccessoriesList(uint32) airecv clsend
    # requestJewelryList(uint32) airecv clsend
    # requestTattooList(uint32) airecv clsend
    # requestAccessories(Accessory [], Accessory []) airecv clsend
    # requestJewelry(JewelryInfo [], JewelryInfo []) airecv clsend
    # requestAccessoryEquip(Accessory []) airecv clsend
    # requestJewelryEquip(Jewelry []) airecv clsend
    # requestTattooEquip(Tattoo []) airecv clsend
    # requestTattoo(TattooInfo [], TattooInfo []) airecv clsend
    # requestBarber(uint32, uint8) airecv clsend
    # requestStowaway(string) airecv clsend
    # makeSaleResponse(uint32) ownrecv
    # responseShipRepair(uint32) ownrecv
    # makeTattooResponse(uint16, uint16, bool) ownrecv
    # makeBarberResponse(uint32, uint8, bool) ownrecv
    # responseClothingList(uint32, uint32 [][]) ownrecv
    # responseTattooList(uint32, TattooInfo []) ownrecv
    # responseJewelryList(uint32, JewelryInfo []) ownrecv
