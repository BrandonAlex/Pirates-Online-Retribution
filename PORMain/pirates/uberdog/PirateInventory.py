from pirates.uberdog.DistributedInventory import DistributedInventory
from direct.directnotify.DirectNotifyGlobal import directNotify


class PirateInventory(DistributedInventory):
    notify = directNotify.newCategory('Inventory')
