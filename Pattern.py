import copy
class Pattern:
    def __init__(self, itemset: set, object: dict):
        self.itemset = itemset
        self.object = copy.deepcopy(object)
    
    def __eq__(self, __o) -> bool:
        if len(__o.itemset) != len(self.itemset):
            return False
        if self.itemset != __o.itemset:
            return False
        return self.object == __o.object

    def add_item(self, item):
        self.itemset.add(item)

    def __str__(self): 
        return "Pattern(\n\titemset: "+str(self.itemset)+"\n\tobject: "+str(self.object)+"\n)"


if __name__ == "__main__":
    p1 = Pattern({}, {"AP" : []})
    p2 = copy.deepcopy(p1)

    p2.object["AP"] = [1]

    print(p1)