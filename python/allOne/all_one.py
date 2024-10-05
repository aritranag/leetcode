class AllOne:

    def __init__(self):
        self.keyStore = {}
        self.maxCount = 0
        self.minCount = 0
        self.countKeyStore = {} # of the form count : {key : count}

    def inc(self, key: str) -> None:
        if key in self.keyStore:
            self.keyStore[key] += 1 #increment the count of the key by 1
        else:
            self.keyStore[key] = 1
        new_count = self.keyStore[key]
        
        # update the countKeyStore
        if new_count > 1:
            # delete it from the previous countkeyStore
            del self.countKeyStore[new_count-1][key]

            # if the count value for that countKeyStore is empty, delete it
            if not self.countKeyStore[new_count-1]:
                del self.countKeyStore[new_count-1]

        if new_count not in self.countKeyStore:
            self.countKeyStore[new_count] = {}
        self.countKeyStore[new_count][key] = new_count


    def dec(self, key: str) -> None:
        # decrease the count for the key
        self.keyStore[key] -= 1

        new_count = self.keyStore[key]

        # delete from the previous countKey
        del self.countKeyStore[new_count+1][key]
        if new_count == 0:
            del self.keyStore[key]
        else:
            # add to the new countKey
            if new_count not in self.countKeyStore:
                self.countKeyStore[new_count] = {}
            self.countKeyStore[new_count][key] = new_count

        if not self.countKeyStore[new_count+1]:
            del self.countKeyStore[new_count+1]
        

    def getMaxKey(self) -> str:
        # base case : if only a single entry is there, that is the 
        if len(self.keyStore.keys()) == 0:
            # there are no keys
            return ""
        elif len(self.keyStore.keys()) == 1:
            return list(self.keyStore.keys())[0]
        else:
            _maxVal = max(list(self.countKeyStore.keys()))
            return list(self.countKeyStore[_maxVal].keys())[0]

    def getMinKey(self) -> str:
        # base case : if only a single entry is there, that is the 
        if len(self.keyStore.keys()) == 0:
            # there are no keys
            return ""
        elif len(self.keyStore.keys()) == 1:
            return list(self.keyStore.keys())[0]
        else:
            _minVal = min(list(self.countKeyStore.keys()))
            return list(self.countKeyStore[_minVal].keys())[0]
        