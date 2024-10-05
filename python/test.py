import allOne.all_one as all_one


obj = all_one.AllOne()
obj.inc("a")
obj.inc("a")
obj.inc("a")
obj.inc("a")
obj.inc("b")
obj.inc("b")
obj.inc("c")
obj.dec("c")
print(obj.getMaxKey())
print(obj.getMinKey())


