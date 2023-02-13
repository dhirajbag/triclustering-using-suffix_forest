
import pandas as pd

def get_clusters(FCP: list, min_support_count = 1, min_size = 2) ->list:
    """Returns a list of tri-clusters from the given list of FCPs"""
    
    return [fcp.toJSON(include_object=True)
     for fcp in FCP if fcp.support_count() >= min_support_count and fcp.size() >= min_size]


def write_triclusters_to_csv(path_to_output_dir: str, FCP: list, item_name_map: dict,  dataset_size: int, min_support_count = 1, min_size = 2):

    data = list()
    for fcp in FCP:
        if fcp.support_count() >= min_support_count and fcp.size() >= min_size:
            itemset = str([item_name_map[number] for number in fcp.get_itemset()])
            support_count = fcp.support_count()
            support_percentage = 100*support_count/dataset_size
            support_obj = fcp.get_object_as_line()
            data.append([itemset, support_count, support_percentage, support_obj])
            
    df = pd.DataFrame(data, columns=["Itemset", "Support(count)", "Support(%)", "Support Object"])
    filepath = f"{path_to_output_dir}/triclusters.csv"
    df.to_csv(filepath)
    print(f"Created file {filepath}")
