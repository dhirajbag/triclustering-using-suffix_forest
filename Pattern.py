import copy

class Pattern:
    def __init__(self, itemset: set, object: dict):
        self.itemset = set(itemset)
        self.object = copy.deepcopy(object)
    
    def __eq__(self, __o) -> bool:
        if len(__o.itemset) != len(self.itemset):
            return False
        if self.itemset != __o.itemset:
            return False
        return self.object == __o.object

    def add_item(self, item):
        self.itemset.add(item)
    
    def get_object(self) -> dict:
        return copy.deepcopy(self.object)
    
    def get_itemset(self) -> set:
        return self.itemset
    
    def get_copy(self):
        return Pattern(self.itemset, self.object)
    
    def size(self) -> int:
        return len(self.itemset)
    
    def is_closed(self, pattern_list) -> bool:
        """Checks whether the pattern is closed within pattern_list"""
        search_space = [pat for pat in pattern_list if pat.get_object()==self.get_object() and pat.size() > self.size()]
    
        for pat in search_space:
            if self.get_itemset().issubset(pat.get_itemset()):
                return False
                
        return True
    
    def intersection(self, other):
        """Returns the interesction with the given pattern"""
        itemset = self.get_itemset().intersection(other.get_itemset())
        new_object = self.get_object()
        other_object = other.get_object()
        for key in other_object:
            if key in new_object:
                for e in other_object[key]:
                    if e not in new_object[key]:
                        new_object[key].append(e)
            else:
                new_object[key] = other_object[key]

        return Pattern(itemset, new_object)


    def __str__(self): 
        return "Pattern(\n\titemset: "+str(self.itemset)+"\n\tobject: "+str(self.object)+"\n)"


if __name__ == "__main__":
    p1 = Pattern({}, {"AP" : []})
    p2 = copy.deepcopy(p1)

    p2.object["AP"] = [1]

    print(p1.get_itemset())