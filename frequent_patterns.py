import copy
from Pattern import Pattern


def get_FCPs(h_tree):
    """Returns all the Frequent Closed Patterns from the suffix forest h_tree"""

    all_patterns = get_all_Patterns(h_tree)
    FCP = [ pattern for pattern in all_patterns if pattern.is_closed(all_patterns)]

    # Handled the case when the intersection itemset is already present in FCP
    new_may_exist = True
    while new_may_exist:
        NFCP = []
        modify_patterns = [] 
        for pat1 in FCP:
            for pat2 in FCP:
                if pat1.get_itemset() != pat2.get_itemset():
                    pat = pat1.intersection(pat2)

                    if(pat.size()==0):
                        continue
                    # Finding pat in FCP
                    found_in_fcp = False
                    for i in range(len(FCP)):
                        if(FCP[i].get_itemset()==pat.get_itemset()):
                            found_in_fcp = True
                            # If the leaf object of pat is not already included,
                            # then, noting that down in modifY_patterns
                            if(not pat.is_object_subset(pat.get_object(), FCP[i].get_object())):
                                modify_patterns.append({"idx": i, "leaf": pat.get_object()})
                            break
                    
                    if not found_in_fcp:
                        # Finding in NFCP
                        found_in_nfcp = False
                        for i in range(len(NFCP)):
                            if(NFCP[i].get_itemset()==pat.get_itemset()):
                                NFCP[i].merge_leaf(pat.get_object())
                                found_in_nfcp = True
                                break
                        if not found_in_nfcp:
                            NFCP.append(pat)
                 
        if len(NFCP) + len(modify_patterns) == 0:
            new_may_exist = False
        else:
            # Patching the previously noted leaves to corresponding FCP
            for patch in modify_patterns:
                FCP[patch["idx"]].merge_leaf(patch["leaf"])
            for pat in NFCP:
                FCP.append(pat)
    
    return FCP



def get_all_Patterns(h_tree) -> list:
    """ Returns all possible item sets along with their object lists """
    all_patterns = []
    for key in list(h_tree.keys()):
        some_patterns = form_patterns(h_tree[key])
        for pattern in some_patterns:
            if pattern.size() > 0:
                # Case when same itemset already exists but with a different leaf
                # Merging both the leaves in that case
                already_present = False
                for i in range(len(all_patterns)):
                    if(all_patterns[i].get_itemset()==pattern.get_itemset()):
                        already_present = True
                        all_patterns[i].merge_leaf(pattern.get_object())
                        break

                if not already_present:
                    all_patterns.append(pattern)           
    return all_patterns

def form_patterns(h_node):
    """Returns all possible item sets along with their object lists
     by traversing the input h_node """
    
    # CANNOT directly return if we encounter a leaf
    # The the current node may have both a leaf and children
    result = []

    for child in h_node["children"]:
        partial_patterns = form_patterns(child)
        for pattern in partial_patterns:
            new_pattern = copy.deepcopy(pattern)
            new_pattern.add_item(h_node["item"])
            result.append(pattern)
            result.append(new_pattern)
    
    if h_node["leaf"] != None:
        result.append(Pattern(set(), h_node["leaf"]))
        result.append(Pattern(set([h_node["item"]]), h_node["leaf"]))

    return result
    

if __name__ == "__main__":
    h_tree = {
        1 : {
            "item" : 1,
            "leaf" : None,
            "children" : [
                {
                    "item" : 2,
                    "leaf" : {"AP" : ["MDM", "OM"]},
                    "children" : []
                },
                {
                    "item" : 3,
                    "leaf" : {"AP" : ["OM", "MDM"]},
                    "children" : []
                }
            ]
        }
    }

    patterns = get_all_Patterns(h_tree)
    for pattern in patterns:
        print (pattern)
    # from json import dumps
    # with open("patterns.json", "w") as outputfile:
    #     outputfile.write(dumps(patterns, indent=2))

    if h_tree[1]["children"][0]["leaf"] == h_tree[1]["children"][1]["leaf"]:
        print ("Same")
    else:
        print("Different")

