## A class that implements subject
## 0 = knight squares
## 1-8 = straight or diagonal squares going clockwise


from observer import Observer

class Subject:

    def __init__(self):
        self._allItem = []
        knights = []
        self._allItem.append(knights)
    def attatch(self, index, newItem):
        if index == 0:
            self._allItem[index].append(newItem)
        else:
            self._allItem.append(newItem)
    def detatch(self, index, newItem):
        if index == 0:
            self._allItem[index].remove(newItem)
        else:
            self._allItem.remove(newItem)
    def notify(self, info):
        for i in self._allItem:
            if i.update() == None:
                print("Error :)")