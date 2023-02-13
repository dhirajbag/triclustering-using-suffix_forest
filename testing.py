from suffix_forest import build_sufix_forest
from frequent_patterns import get_FCPs
from generators import get_generators
from association_rules import Rule
from tricluster import write_triclusters_to_csv
from preprocessing import get_number_table_sfd_list_min_sup_count_datatset_size
from json import dumps
import pandas as pd
from demodata import SFD_mdm, SFD_om, SFD_1

# TODO: [Done] incorporate metrics such as lift in the association rules
# TODO: [Done] store SFDs in csv and then read
# TODO: [Done] use actual datasets (nominal/binary/ordinal)
# TODO: [Done] Preprocessing & SFD creation (item mapping)
# TODO: [Done] Decode the item numbers and use original values in the generated outputs
# TODO: [Done] association rules in csv
# TODO: [Done partially] store tri-clusters in csv
# TODO: create python notebook file and execute on google colab

# forest = build_sufix_forest({"D1": SFD_1})
(number_table, sfd_list, min_sup_count, dataset_size) = get_number_table_sfd_list_min_sup_count_datatset_size("./input/groceries_dataset.csv", min_sup_percentage=6)
# forest = build_sufix_forest({"MDM": SFD_mdm, "OM": SFD_om})
print(f"Dataset has {dataset_size} rows")
print(f"Minimum support count used for single items: {min_sup_count}")

forest = build_sufix_forest(sfd_list)

min_sup_count_itemsets = 1
print(f"Using minimum support count = {min_sup_count_itemsets} for finding FCPs")

FCPs = get_FCPs(forest, min_support_count = min_sup_count_itemsets)
GEN = get_generators(FCPs)

output_file_dir = "./output/"

item_name = dict()
for (name, number) in number_table.items():
    item_name[number] = name

write_triclusters_to_csv(output_file_dir, FCPs, item_name, dataset_size, min_support_count=min_sup_count_itemsets, min_size=2)

Rule.generate_csv(GEN, FCPs, item_name, dataset_size, output_file_dir, min_confidence=0.0)
