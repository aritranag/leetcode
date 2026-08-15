'''
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

    TimeMap() Initializes the object of the data structure.
    void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
    String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

'''
class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key:str, value: str, timestamp:int) -> None:
        if key in self.timemap:
            _val = self.timemap[key]
            _val[timestamp] = value
        else:
            self.timemap[key] = {}
            self.timemap[key][timestamp] = value


    def get(self, key: str, timestamp: int) -> str:
        # if key not in timemap, return err
        if key not in self.timemap:
            return ""
        else:
            _val = self.timemap[key]
            # if timestamp exists use that
            if timestamp in _val:
                return _val[timestamp]
            else:
                # find the closest value lower than timestamp using binary search
                _ts = [i for i in _val.keys()]

                # 2 edge cases exist, 
                # timestamp is less than the lowest val in _ts, or timestamp is greater than the largest value
                if timestamp < _ts[0]:
                    return ""
                elif timestamp > _ts[-1]:
                    return _val[_ts[-1]]

                # timestamp lies somewhere in between, we need to find its position
                # can use bisec.bisect_right() to find the index where it can be inserted, so we have to pick the idx-1 for our answer
                l,r = 0,len(_ts)-1
                while l < r:
                    mid = l + (r-l)//2
                    if _ts[mid] > timestamp:
                        r = mid - 1
                    elif mid + 1 <= r and _ts[mid+1] > timestamp:
                        return _val[_ts[mid]]
                    else:
                        l = mid + 1
                return _val[_ts[l]]



timeMap = TimeMap()
print(timeMap.set("alice", "happy", 1))   # store the key "alice" and value "happy" along with timestamp = 1.
print(timeMap.set("alice", "happyness", 4)) 
print(timeMap.get("alice", 1))            # return "happy"
print(timeMap.get("alice", 2))            # return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
print(timeMap.set("alice", "sad", 3))     # store the key "alice" and value "sad" along with timestamp = 3.
print(timeMap.get("alice", 3))            # return "sad"
