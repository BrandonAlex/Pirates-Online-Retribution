from pandac.PandaModules import *
from pirates.uberdog.UberDogGlobals import receiveSwitchField, prepareSwitchField, InventoryType, isLocatable, GiftOrigin
from pirates.uberdog.DistributedInventoryBase import DistributedInventoryBase
from pirates.inventory.InventoryGlobals import *
from pirates.inventory import ItemGlobals
from pirates.economy import EconomyGlobals
import copy
import types
from direct.task.Task import Task
from pirates.reputation import ReputationGlobals
from pirates.piratesbase import Freebooter
TEST_TYPE_LIMITS = 1
TEST_TYPE_TRADES = 2

class InvItem(tuple):

    def verifyItem(self):
        if len(self) == 0:
            self.notify.warning('verifyItem: bad item structure, no fields!')
            return False

        if (self[TradableInventoryBase.ITEM_CAT_IDX] == InventoryType.ItemTypeMoney or self[TradableInventoryBase.ITEM_CAT_IDX] == InventoryType.ItemTypeMoneyWagered) and len(self) != 2:
            self.notify.warning('verifyItem: bad item structure, money requires 2 fields (%s)' % str(self))
            return False

        return True


    def viableForTrade(self):
        if not self.verifyItem():
            return False

        return True


    def getLocation(self):
        if self[TradableInventoryBase.ITEM_CAT_IDX] == InventoryType.ItemTypeMoney:
            return Locations.RANGE_GOLD[0]
        elif self[TradableInventoryBase.ITEM_CAT_IDX] == InventoryType.ItemTypeMoneyWagered:
            return Locations.RANGE_GOLD_WAGERED[0]
        elif itemStoresLocation(self[TradableInventoryBase.ITEM_CAT_IDX]):
            return self[TradableInventoryBase.ITEM_LOCATION_IDX]
        elif self[TradableInventoryBase.ITEM_CAT_IDX] == 0 and self[TradableInventoryBase.ITEM_ID_IDX] == 0:
            if len(self) > TradableInventoryBase.ITEM_LOCATION_IDX:
                return self[TradableInventoryBase.ITEM_LOCATION_IDX]

        else:
            return None


    def setLocation(self, location):
        oldLoc = self.getLocation()
        if oldLoc == None and oldLoc == location and location == Locations.INVALID_LOCATION or location == Locations.NON_LOCATION:
            return self

        idx = TradableInventoryBase.ITEM_LOCATION_IDX
        result = InvItem(self[:idx] + (location,) + self[idx + 1:])
        return result


    def getType(self):
        if itemStoresLocation(self[TradableInventoryBase.ITEM_CAT_IDX]):
            return self[TradableInventoryBase.ITEM_ID_IDX]
        else:
            return None


    def getCat(self):
        return self[TradableInventoryBase.ITEM_CAT_IDX]


    def getId(self):
        return self[TradableInventoryBase.ITEM_ID_IDX]


    def getCount(self, default = None):
        if itemStoresLocation(self[TradableInventoryBase.ITEM_CAT_IDX]):
            itemCat = self[TradableInventoryBase.ITEM_CAT_IDX]
            if itemCat == InventoryType.ItemTypeConsumable:
                return self[TradableInventoryBase.ITEM_COUNT_IDX]
            elif itemCat == InventoryType.ItemTypeMoney or itemCat == InventoryType.ItemTypeMoneyWagered:
                return self[1]
            else:
                return default
        else:
            return self[1]


    def adjustCount(self, delta):
        itemCat = self[TradableInventoryBase.ITEM_CAT_IDX]
        if itemCat == InventoryType.ItemTypeConsumable:
            idx = TradableInventoryBase.ITEM_COUNT_IDX
        elif not itemStoresLocation(self[TradableInventoryBase.ITEM_CAT_IDX]):
            idx = 1
        else:
            return None
        result = self[idx] + delta
        max = getItemLimit(itemCat, self.getType())
        if max == None:
            pass
        1
        if result < 0:
            return None
        elif result > max:
            delta = max - self[idx]

        return InvItem(self[:idx] + (self[idx] + delta,) + self[idx + 1:])


    def getUpgrades(self):
        if self[TradableInventoryBase.ITEM_CAT_IDX] == InventoryType.ItemTypeWeapon:
            return self[TradableInventoryBase.ITEM_UPGRADES_IDX]
        else:
            return None


    def getColor(self):
        if self[TradableInventoryBase.ITEM_CAT_IDX] == InventoryType.ItemTypeClothing:
            return self[TradableInventoryBase.ITEM_COLOR_IDX]
        else:
            return None


    def compare(self, other, excludeLoc = False):
        if self and other and self.getCat() == other.getCat() and isStackableType(self.getCat()) and self.getType() == other.getType():
            return True
        elif excludeLoc and self and other and self.setLocation(1) == other.setLocation(1):
            return True
        else:
            return self == other



class InvItemList(dict):

    def __setitem__(self, key, value):
        if self.has_key(key):
            print 'error, item %s already exists (%s)! clear the item first' % (key, value)
            return False

        dict.__setitem__(self, key, value)
        return True


    def swapItems(self, item1, item2):
        item1Loc = item1[TradableInventoryBase.ITEM_LOCATION_IDX]
        item2Loc = item2[TradableInventoryBase.ITEM_LOCATION_IDX]
        if self.has_key(item2Loc):
            del self[item2Loc]

        if item2[TradableInventoryBase.ITEM_CAT_IDX]:
            self[item2Loc] = item2

        if self.has_key(item1Loc):
            del self[item1Loc]

        if item1[TradableInventoryBase.ITEM_CAT_IDX]:
            self[item1Loc] = item1



    def addToItem(self, location, quantity):
        existingItem = self.get(location)
        if existingItem:
            del self[location]
            existingItem = existingItem.adjustCount(quantity)
            self[location] = existingItem

        return existingItem


    def removeFromItem(self, location, quantity):
        existingItem = self.get(location)
        if existingItem:
            if existingItem.getCount() > quantity:
                existingItem = existingItem.adjustCount(-quantity)
            else:
                existingItem = None
            del self[location]
            if existingItem:
                self[location] = existingItem


        return existingItem



class TradableInventoryBase(DistributedInventoryBase):
    ITEM_CAT_IDX = 0
    ITEM_ID_IDX = 1
    ITEM_LOCATION_IDX = 2
    ITEM_COUNT_IDX = 3
    ITEM_UPGRADES_IDX = 3
    ITEM_COLOR_IDX = 3
    STATUS_ITEM_ADDED = 1
    STATUS_ITEM_REMOVED = 2
    STATUS_ITEM_MODIFIED = 3
    STATUS_ITEM_MODIFIED_OVERFLOW = 4

    def __init__(self, repository):
        DistributedInventoryBase.__init__(self, repository)
        self._locatableItems = InvItemList()
        self.tempAdds = []
        self.tempRems = []
        self.selfTestsTask = None
        self.selfTestTrades = []
        self.testPending = False
        self.areLocatablesReady = 0


    def findAvailableLocation(self, itemCat, overflow = False, itemId = None, count = 1, equippable = True):
        if overflow:
            ranges = expandRanges((Locations.RANGE_OVERFLOW,))
        elif not equippable and itemCat == InventoryType.ItemTypeWeapon:
            pass
        equippable = itemCat == InventoryType.ItemTypeCharm
        ranges = self.getPossibleLocations(itemCat, itemId, equippable, expanded = True)
        if itemId and isStackableType(itemCat):
            existingStacks = self._findLocatablesWithValues([
                (self.ITEM_CAT_IDX, itemCat),
                (self.ITEM_ID_IDX, itemId)])
            if existingStacks:
                existingStack = existingStacks.values()[0]
                if existingStack.getCount() >= self.getItemLimit(existingStack.getCat(), itemId):
                    return Locations.INVALID_LOCATION

                return existingStack.getLocation()


        for currLocation in xranges:
            if self.locationAvailable(currLocation, itemType = itemId):
                return currLocation
                continue

        return Locations.INVALID_LOCATION


    def locationIsValid(self, location, itemCat = None, itemType = None, includeEquip = True):
        if itemCat:
            typePasses = False
            if location in xrange(Locations.RANGE_OVERFLOW[0], Locations.RANGE_OVERFLOW[1] + 1):
                return True

            ranges = self.getPossibleLocations(itemCat, itemType, includeEquip, expanded = True)
            if location in xranges:
                typePasses = True

        else:
            typePasses = True
        if location != Locations.NON_LOCATION and location != Locations.INVALID_LOCATION and location <= Locations.TOTAL_NUM_LOCATIONS:
            pass
        return typePasses


    def canRemoveLocatable(self, item, tempRemove = False):
        numValues = len(item)
        if numValues > self.ITEM_CAT_IDX and isLocatable(item.getCat()):
            currItem = self._locatableItems.get(item.getLocation())
            if currItem and currItem.compare(item):
                if tempRemove:
                    self.tempRems.append(item)

                return True


        return False


    def canAddLocatables(self, items, equippable = True, tempAdd = False):
        results = []
        if not tempAdd:
            prevTmpAdds = self.tempAdds
            self.tempAdds = []

        for currItem in items:
            location = Locations.NON_LOCATION
            itemType = None
            numValues = len(currItem)
            currLoc = currItem.getLocation()
            if isLocatable(currItem.getCat()):
                if currLoc == Locations.NON_LOCATION or currLoc == None:
                    location = self.findAvailableLocation(currItem.getCat(), itemId = currItem.getType(), count = currItem.getCount(), equippable = equippable)
                elif self.locationAvailable(currLoc, itemType = currItem.getType()) or currItem.getCount(default = 1) == 0:
                    location = currLoc

                itemType = currItem.getCat()

            if self.locationIsValid(location, itemType, itemType = currItem.getType(), includeEquip = equippable) and location not in results:
                results.append(location)
                self.tempAdds.append(location)
                continue
            results.append(Locations.NON_LOCATION)

        if not tempAdd:
            self.tempAdds = prevTmpAdds

        return results


    def locationAvailable(self, location, includeReserved = True, itemType = None):
        existingItem = self._locatableItems.get(location)
        if existingItem:
            existingCat = existingItem.getCat()

        if existingItem and isStackableType(existingCat):
            if existingItem.getCount() < self.getItemLimit(existingCat, existingItem.getType()):
                if itemType == None or itemType == existingItem.getType():
                    existingItem = None

            itemType == existingItem.getType()

        if existingItem and filter(lambda x: x.getLocation() == location, self.tempRems):
            existingItem = None

        if not existingItem == None and includeReserved == False:
            pass
        return location not in self.tempAdds


    def locatablesReady(self, ready):
        self.notify.info('recieved LocatablesReady value %s from inventory %s (previous value %s)' % (ready, self.doId, self.areLocatablesReady))
        self.areLocatablesReady = ready


    def getLocatablesReady(self):
        return self.areLocatablesReady


    def setLocatables(self, items):
        if not self.areLocatablesReady:
            return None

        self._locatableItems = InvItemList(map(lambda x: (x.getLocation(), x), receiveSwitchField(items, InvItem)))
        for currLoc in self._locatableItems:
            messenger.send(getLocationChangeMsg(self.doId), [
                currLoc])
            item = self._locatableItems[currLoc]
            messenger.send(getCategoryChangeMsg(self.doId, item.getCat()), [
                item.getType()])
            messenger.send(getCategoryQuantChangeMsg(self.doId, item.getCat()), [
                item.getCount()])

        messenger.send(getAnyChangeMsg(self.doId))


    def getQuantityAtLocation(self, location):
        item = self._locatableItems.get(location)
        if item:
            return 1

        return 0


    def getLocatable(self, location, default = None):
        return self._locatableItems.get(location, default)


    def getLocatables(self):
        return self._locatableItems


    def getStackQuantity(self, stackType):
        itemClass = None
        if isLocatable(stackType):
            itemClass = ItemGlobals.getClass(stackType)

        if itemClass:
            return self.getItemQuantity(itemClass, stackType)
        else:
            return self.getItemQuantity(stackType)


    def getItemQuantity(self, itemCat, itemId = None):
        if isLocatable(itemCat):
            findFields = [
                (self.ITEM_CAT_IDX, itemCat)]
            if itemId:
                findFields.append((self.ITEM_ID_IDX, itemId))

            itemCounts = self._findLocatablesWithValues(findFields, countsOnly = True)
            if itemId:
                return itemCounts.get(itemId, 0)
            else:
                return sum(itemCounts.values())
        else:
            return DistributedInventoryBase.getStackQuantity(self, itemCat)


    def getItemsInCategory(self, category):
        if isLocatable(category):
            return self._findLocatablesWithValues([
                (self.ITEM_CAT_IDX, category)])
        else:
            return DistributedInventoryBase.getStacksInCategory(self, category)


    def _findLocatablesWithValues(self, fieldValues, countsOnly = False):
        locatables = { }
        for currItem in self._locatableItems.itervalues():
            for (currField, currValue) in fieldValues:
                if len(currItem) <= currField:
                    break

                if currValue != currItem[currField]:
                    break
            if countsOnly:
                currItemType = currItem.getType()
                itemCount = currItem.getCount()
                if itemCount == None:
                    itemCount = 1

                if currItemType in locatables:
                    locatables[currItemType] += itemCount
                else:
                    locatables[currItemType] = itemCount
            locatables[currItem.getLocation()] = currItem

        return locatables


    def getAllWeapons(self):
        return self._findLocatablesWithValues([
            (self.ITEM_CAT_IDX, InventoryType.ItemTypeWeapon)])


    def getAllClothing(self):
        return self._findLocatablesWithValues([
            (self.ITEM_CAT_IDX, InventoryType.ItemTypeClothing)])


    def getAllJewelry(self):
        return self._findLocatablesWithValues([
            (self.ITEM_CAT_IDX, InventoryType.ItemTypeJewelry)])


    def getAllTattoos(self):
        return self._findLocatablesWithValues([
            (self.ITEM_CAT_IDX, InventoryType.ItemTypeTattoo)])


    def getAllOfType(self, itemCat, itemType):
        return self._findLocatablesWithValues([
            (self.ITEM_CAT_IDX, itemCat),
            (self.ITEM_ID_IDX, itemType)])


    def getAllOverflow(self):
        overflowItems = { }
        for currOverflowLoc in expandRanges((Locations.RANGE_OVERFLOW,)):
            currOverflowItem = self._locatableItems.get(currOverflowLoc)
            if currOverflowItem:
                overflowItems[currOverflowLoc] = currOverflowItem
                continue

        return overflowItems


    def trashItems(self, items = [], count = 1):
        verifiedItems = []
        for currItem in items:
            if currItem:
                currInvItem = InvItem(currItem)
                currLocation = currInvItem.getLocation()
                item = self._locatableItems.get(currLocation)
                if item.compare(currInvItem):
                    verifiedItems.append(currInvItem)

            item.compare(currInvItem)

        self.notify.debug('trashLocatables %s' % str(verifiedItems))
        self.sendUpdate('trashLocatables', [
            prepareSwitchField(verifiedItems)])


    def getOverflowItems(self):
        overflow = []
        for currLoc in xrange(Locations.RANGE_OVERFLOW[0], Locations.RANGE_OVERFLOW[1] + 1):
            currItem = self._locatableItems.get(currLoc)
            if currItem:
                overflow.append(currItem)
                continue

        return overflow


    def filterAdds(self, takingList):
        itemCats = { }
        nonLocatables = []
        for currItem in takingList:
            itemCat = currItem.getCat()
            if not isLocatable(itemCat):
                nonLocatables.append(currItem)
                continue

            if itemCats.has_key(itemCat):
                itemCats[itemCat][1].append(currItem)
                continue
            itemCats[itemCat] = [
                0,
                [
                    currItem]]
            possibleLocs = self.getPossibleLocations(itemCat, currItem.getType(), includeEqup = True, expanded = True)
            for currLoc in possibleLocs:
                if self.locationAvailable(currLoc, currItem.getType()):
                    itemCats[itemCat][0] += 1
                    continue



        def cmp(item1, item2):
            goldCost1 = ItemGlobals.getGoldCost(item1[1])
            if not goldCost1:
                goldCost1 = item1[1]

            goldCost2 = ItemGlobals.getGoldCost(item2[1])
            if not goldCost2:
                goldCost2 = item2[1]

            return int(goldCost2 - goldCost1)

        chosen = []
        for (currCat, currCatInfo) in itemCats.items():
            available = currCatInfo[0]
            items = currCatInfo[1]
            if available < len(items):
                items.sort(cmp)
                chosen.extend(items[:available])
                continue
            chosen.extend(items)

        chosen.extend(nonLocatables)
        return chosen


    def getStackLimit(self, stackType):
        return self.getItemLimit(stackType)


    def getItemLimit(self, category, type = None):
        limit = getItemLimit(category, type)
        if limit == None:
            limit = DistributedInventoryBase.getStackLimit(self, category)

        return limit


    def getPossibleLocations(self, category, type, equippable, expanded = False):
        return getLocationRanges(category, type, equippable, expanded)


    def getFreeLocations(self, category, type):
        freeLocations = []
        possibleLocations = self.getPossibleLocations(category, type, False, True)
        for locationId in possibleLocations:
            if not self._locatableItems.get(locationId):
                freeLocations.append(locationId)
                continue

        return freeLocations


    def getItemRequirements(self, itemType, otherAdds = []):
        if not itemType:
            return None

        results = { }
        if game.process == 'client':
            paidStatus = Freebooter.getPaidStatus(self.ownerId)
        else:
            paidStatus = Freebooter.getPaidStatusAI(self.ownerId)
        rarity = ItemGlobals.getRarity(itemType)
        if rarity != ItemConstants.CRUDE and not paidStatus:
            results['paidStatus'] = (rarity != ItemConstants.CRUDE, False)

        itemClass = ItemGlobals.getClass(itemType)
        if itemClass == InventoryType.ItemTypeWeapon or itemClass == InventoryType.ItemTypeCharm:
            itemRepId = ItemGlobals.getItemRepId(itemType)
            itemRep = self.getReputation(itemRepId)
            itemLevel = ReputationGlobals.getLevelFromTotalReputation(itemRepId, itemRep)[0]
            weaponReq = ItemGlobals.getWeaponRequirement(itemType)
            trainingToken = EconomyGlobals.getItemTrainingReq(itemType)
            trainingAmt = self.getItemQuantity(trainingToken)
            for currAdd in otherAdds:
                otherAdd = InvItem(currAdd)
                if otherAdd.getCat() == trainingToken and otherAdd.getCount() > 0:
                    trainingAmt += otherAdd.getCount()
                    continue

            if not weaponReq == None:
                pass
            weaponLevelPass = itemLevel >= weaponReq
            if not trainingToken == 0 and trainingToken == None:
                pass
            weaponTrainPass = trainingAmt > 0
            if weaponLevelPass:
                pass
            results['itemLevel'] = (weaponReq, weaponTrainPass)
        else:
            results['itemLevel'] = (0, True)
        return results


    def _TradableInventoryBase__runSelfTest_limits(self, itemCatFilter, verbose):
        itemIds = ItemGlobals.getAllItemIds()
        for currItemId in itemIds:
            if itemCatFilter != None and itemCatFilter != ItemGlobals.getClass(currItemId):
                continue

            itemIds = ItemGlobals.getAllConsumableIds()
            itemLimit = ItemGlobals.getStackLimit(currItemId)
            itemCat = ItemGlobals.getClass(currItemId)
            quantity = self.getItemQuantity(itemCat, currItemId)
            if isStackableType(itemCat):
                pass
            1
            if verbose:
                if not itemLimit:
                    pass
                print 'item limit for item %s:%s passed (quantity: %s limit:%s)' % (itemCat, currItemId, quantity, 1)
                continue



    def _TradableInventoryBase__runSelfTest_giving(self, itemCatFilter, itemTypeFilter = None, count = None, verbose = None):
        itemIds = ItemGlobals.getAllItemIds()
        for currItemId in itemIds:
            itemCat = ItemGlobals.getClass(currItemId)
            if itemCatFilter != None and itemCat != itemCatFilter:
                continue

            if not count and ItemGlobals.getStackLimit(currItemId):
                pass
            actualCount = None
            testItem = self.getTestItem(itemCat, currItemId, count = actualCount)
            if game.process == 'ai':

                def tradeSuccess(tradeObj):
                    if verbose:
                        print '  trade success'

                    self.testPending = False


                def tradeFail(tradeObj, reason):
                    reasonStr = reason
                    RejectCode = RejectCode
                    import otp.uberdog.RejectCode
                    for currCode in RejectCode.__dict__.keys():
                        if reason == RejectCode.__dict__[currCode]:
                            reasonStr = currCode
                            continue

                    if verbose:
                        print '  trade fail %s (%s)' % (reasonStr, tradeObj)

                    if reason == RejectCode.OVERFLOW:
                        for currGiving in tradeObj.giving:
                            checkItem = InvItem(currGiving)
                            itemCat = checkItem.getCat()
                            if not itemCat == InventoryType.ItemTypeWeapon:
                                pass
                            ranges = self.getPossibleLocations(itemCat, checkItem.getType(), itemCat == InventoryType.ItemTypeCharm)
                            for currRange in xranges:
                                minVal = currRange[0]
                                if len(currRange) > 1:
                                    maxVal = currRange[1]
                                else:
                                    maxVal = minVal
                                for currLocation in xrange(minVal, maxVal + 1):
                                    if not self._locatableItems.has_key(currLocation):
                                        print '    WARNING: trade %s failed with overflow when it should not have %s' % (tradeObj, currLocation)
                                        continue



                    elif reason == RejectCode.UNDERFLOW:
                        print '    WARNING: trade %s failed with underflow when it should not have' % tradeObj

                    self.testPending = False


                def tradeTimeout(tradeObj):
                    if verbose:
                        print '  trade timeout'

                    self.testPending = False

                AIMagicWordTrade = AIMagicWordTrade
                import pirates.uberdog.AIMagicWordTrade
                trade = AIMagicWordTrade(self, self.doId, self.ownerId)

                def removeSetup(tradeObj, removeCat, removeType):
                    ranges = self.getPossibleLocations(removeCat, removeType, False)
                    itemToRemove = self._locatableItems.get(ranges[0][0])
                    tradeObj.takeItem(itemToRemove)

                trade.setSuccessCallback(tradeSuccess)
                trade.setFailureCallback(tradeFail)
                trade.setTimeoutCallback(tradeTimeout)
                self.selfTestTrades.insert(0, (lambda param1 = trade, param2 = itemCat, param3 = testItem.getType(): removeSetup(param1, param2, param3), trade))
                AIGift = AIGift
                import pirates.uberdog.AIGift
                trade = AIGift(self, GiftOrigin.MAGIC_WORD, self.doId, self.ownerId)
                trade.giveItem(testItem)
                trade.setSuccessCallback(tradeSuccess)
                trade.setFailureCallback(tradeFail)
                trade.setTimeoutCallback(tradeTimeout)
                self.selfTestTrades.insert(1, (None, trade))
                continue



    def runSelfTests(self, itemCatFilter = None, testType = None, verbose = False):
        print 'starting tests...'

        def startTests(task = None):
            if testType == None or testType == TEST_TYPE_LIMITS:
                self._TradableInventoryBase__runSelfTest_limits(itemCatFilter, verbose)

            if testType == None or testType == TEST_TYPE_TRADES:
                self._TradableInventoryBase__runSelfTest_giving(itemCatFilter, verbose = verbose)


            def processAsyncTests(task = None):
                if not self.testPending:
                    if self.selfTestTrades:
                        testTradeInfo = self.selfTestTrades.pop()
                        if testTradeInfo[0]:
                            testTradeInfo[0]()

                        testTradeInfo[1].sendTrade()
                        if verbose:
                            print 'sending trade %s' % str(testTradeInfo[1])

                        self.testPending = True
                    else:
                        self.selfTestsTask = None
                        print 'finished tests.'
                        return Task.done

                return Task.cont

            self.selfTestsTask = taskMgr.add(processAsyncTests, 'runSelfTests')
            return Task.done

        taskMgr.doMethodLater(0, startTests, 'selfTestsStart')


    def getTestItem(self, category, type = None, location = None, count = None, color = None):
        type2gen = {
            STInt8: 'int()',
            STInt16: 'int()',
            STInt32: 'int()',
            STInt64: 'int()',
            STUint8: 'int()',
            STUint16: 'int()',
            STUint32: 'int()',
            STUint64: 'int()',
            STFloat64: 'int()',
            STString: 'str()',
            STBlob: 'str()',
            STBlob32: 'str()',
            STInt16array: '[]',
            STInt32array: '[]',
            STUint16array: '[]',
            STUint32array: '[]',
            STInt8array: '[]',
            STUint8array: '[]',
            STUint32uint8array: '[]',
            STChar: 'int()' }
        locatablesField = self.dclass.getFieldByName('setLocatables').asAtomicField()
        switchObj = None
        result = tuple()
        for currElement in xrange(locatablesField.getNumElements()):
            arrayParam = locatablesField.getElement(currElement).asArrayParameter()
            if arrayParam and arrayParam.getName() == 'items':
                itemStruct = arrayParam.getElementType().asClassParameter().getClass()
                for currItemField in xrange(itemStruct.getNumFields()):
                    switchObj = itemStruct.getField(currItemField).asSwitchParameter().getSwitch()


        if switchObj:
            numCases = switchObj.getNumCases()
            testPacker = DCPacker()
            testPacker.rawPackUint16(category)
            caseIdx = switchObj.getCaseByValue(testPacker.getString())
            numFields = switchObj.getNumFields(caseIdx)
            for currField in xrange(numFields):
                if currField == 0:
                    newVal = (category,)
                elif currField == 1 and type != None:
                    newVal = (type,)
                elif currField == 2 and location != None:
                    newVal = (location,)
                elif currField == 3 and count != None:
                    newVal = (count,)
                elif currField == 3 and color != None:
                    newVal = (color,)
                else:
                    fieldInfo = switchObj.getField(caseIdx, currField)
                    fieldType = fieldInfo.asParameter().asSimpleParameter()
                    if not fieldType:
                        fieldType = STUint8array
                    else:
                        fieldType = fieldType.getType()
                    exec 'newVal = (' + type2gen.get(fieldType) + ',)'
                result = result[:] + newVal


        return InvItem(result)


    def clearTemps(self):
        self.tempRems = []
        self.tempAdds = []


