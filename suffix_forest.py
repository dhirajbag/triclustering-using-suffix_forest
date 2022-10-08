from lib2to3.pgen2.token import NEWLINE


def get_all_suffix(arr, leaf_obj):
    all_suffix = []

    for i in range(len(arr)):
        all_suffix.append(get_suffix(arr, i, leaf_obj))

    return all_suffix


def get_suffix(arr, idx, leaf_obj):
    suffix = []

    while idx < len(arr):
        suffix.append(arr[idx])
        idx += 1

    suffix.append(leaf_obj)
    return suffix


def build_sufix_forest(sfd_list):
    # HTree
    h_tree = {}

    for type in sfd_list.keys():
        SFD = sfd_list[type]
        for state in SFD.keys():
            suffixes = get_all_suffix(SFD[state], {
                state: [type]
            })

            for suffix in suffixes:
                assert len(suffix) > 1

                if suffix[0] in h_tree.keys():
                    match(h_tree[suffix[0]], suffix)
                else:
                    h_tree[suffix[0]] = build(suffix)

    return h_tree


def match(h_node, suffix):
    assert h_node["item"] == suffix[0]

    if (len(suffix) == 2):  # suffix[1] is a leaf node
        if h_node["leaf"] == None:
            h_node["leaf"] = suffix[1].copy()
        else:
            # merge the new leaf with the existing leaf
            tree_leaf = h_node["leaf"]
            state = list(suffix[1].keys())[0]
            type = suffix[1][state][0]

            if (state in tree_leaf.keys()):
                if (type in tree_leaf[state]):
                    print("Warning: Same row already exists in forest for ("+state+", "+type+").")
                else:
                    tree_leaf[state].append(type)
            else:
                tree_leaf[state] = [type]
    else:
        # suffix[1] will not be a leaf

        # matching suffix[1]
        for child in h_node["children"]:
            if child["item"] == suffix[1]:
                match(child, suffix[1:])
                return
        # if no match is found, building h_node
        h_node["children"].append(build(suffix[1:]))


def build(suffix):
    assert len(suffix) >= 2
    h_node = {
        "item": suffix[0],
        "children": [],
        "leaf": None
    }

    if len(suffix) == 2:
        h_node["leaf"] = suffix[1].copy()
    else:
        h_node["children"].append(build(suffix[1:]))
    return h_node


if __name__ =='__main__':

    SFD_mdm = {
        "AP": [3, 14, 15, 16, 31],
        "GU": [1, 2, 3, 14, 15, 16, 31],
        "OD": [1, 2, 14, 15, 31],
        "ANI": [16, 31]
    }

    SFD_om = {
        "AP": [3, 4, 5, 14,15, 16, 31],
        "MA": [3],
        "KE": [2, 14, 15, 16, 31],
        "WB": [4, 5, 14, 15],
        "ANI": [2]
    }

    forest = build_sufix_forest({"MDM": SFD_mdm})

    from printing_util import generate_forest_image
    generate_forest_image(forest, "forest.png")

    from json import dumps
    with open("forest.json", "w") as outputfile:
        outputfile.write(dumps(forest, indent=2))
