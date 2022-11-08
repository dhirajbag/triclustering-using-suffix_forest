# Extracts Frequent Closed Patterns (FCPs)
# Input: h_tree
# Output: FCP

import copy
from Pattern import Pattern


def get_FCPs(h_tree):
    """Returns all the Frequent Closed Patterns from the suffix forest h_tree"""

    all_patterns = get_all_Patterns(h_tree)
    FCP = [ pattern for pattern in all_patterns if pattern.is_closed(all_patterns)]
    
    new_may_exist = True
    while new_may_exist:
        NFCP = []
        for pat1 in FCP:
            for pat2 in FCP:
                if pat1 != pat2:
                    pat = pat1.intersection(pat2)
                    if pat.size() > 0 and pat not in FCP and pat not in NFCP:
                        NFCP.append(pat)
        
        if len(NFCP) == 0:
            new_may_exist = False
        else:
            for pat in NFCP:
                FCP.append(pat)
    
    return FCP

# def are_same(pattern1, pattern2):
#     """Checks whether two patterns are same along with their objects"""
#     if len(pattern1["itemset"]) != len(pattern2["itemset"]):
#         return False
#     pass


# def get_insersection(pattern1, pattern2):
#     """Returns the interesction of two patterns """


def get_all_Patterns(h_tree) -> list:
    """ Returns all possible item sets along with their object lists """
    all_patterns = []
    for key in list(h_tree.keys()):
        some_patterns = form_patterns(h_tree[key])
        for pattern in some_patterns:
            if pattern.size() > 0:
                all_patterns.append(pattern)

    return all_patterns

def form_patterns(h_node):
    """Returns all possible item sets along with their object lists
     by traversing the input h_node """
    
    if h_node["leaf"] != None:
        return [
            Pattern(set(), h_node["leaf"]),
            Pattern(set([h_node["item"]]), h_node["leaf"])
        ]

    result = []

    for child in h_node["children"]:
        partial_patterns = form_patterns(child)
        for pattern in partial_patterns:
            new_pattern = copy.deepcopy(pattern)
            new_pattern.add_item(h_node["item"])
            result.append(pattern)
            result.append(new_pattern)

    return result

# def is_closed(pattern, all_patterns):
#     search_space = [pat for pat in all_patterns if pat["object"]==pattern["object"] and len(pat["itemset"]) > len(pattern)]
    
#     for pat in search_space:
#         if is_subset(pattern["itemset"], pat["itemset"]):
#             return False
            
#     return True

# def is_subset(A, B):
#     """Checks whether A is a subset of B"""
#     return all(x in B for x in A)
    


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

