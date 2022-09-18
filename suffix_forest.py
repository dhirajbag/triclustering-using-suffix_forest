
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




if __name__=='__main__':
    print("Hello world!")

    SFD_mdm = {
        "AP": [3, 14, 15, 16, 31],
        "GU": [1, 2, 3, 14, 15, 16, 31],
        "OD": [1, 2, 14, 15, 31],
        "ANI": [16, 31]
    }

    SFD_om = {
        "AP": [3, 4, 5,14,15, 16, 31],
        "MA": [3],
        "KE": [2,14, 15, 16, 31],
        "WB": [4, 5, 14, 15],
        "ANI": [2]
    }

    arr = get_all_suffix(SFD_mdm["AP"], {
        "AP": ["MDM"]
    })

    print(arr)

