from suffix_forest import build_sufix_forest
from frequent_patterns import get_FCPs
from demodata import SFD_mdm, SFD_om


forest = build_sufix_forest({"MDM": SFD_mdm})
FCPs = get_FCPs(forest)
print(len(FCPs))
for pat in FCPs:
    print(pat)

from printing_util import generate_forest_image
generate_forest_image(forest, "forest.png")


