from suffix_forest import build_sufix_forest
from frequent_patterns import get_FCPs
from demodata import SFD_mdm, SFD_om, SFD_1
from association_rules import Rule
from tricluster import get_clusters

# forest = build_sufix_forest({"D1": SFD_1})
forest = build_sufix_forest({"MDM": SFD_mdm, "OM": SFD_om})
FCPs = get_FCPs(forest, min_support_count=3)
triclusters = get_clusters(FCPs, min_support_count=3, min_size=2)

print("Total: "+str(len(FCPs))+" FCP generated.")

from generators import get_generators
GEN = get_generators(FCPs)

rules = Rule.generate_rules(GEN, FCPs)

from json import dumps

with open("forest.json", "w") as outputfile:
    outputfile.write(dumps(forest, indent=2))

with open("triclusters.json", "w") as outputfile:
    outputfile.write(dumps(triclusters, indent=2))

for key in list(rules.keys()):
    print("Total "+str(len(rules[key]))+" "+str(key)+" rules generated.")
    with open("rule_"+str(key)+".json", "w") as outputfile:
        outputfile.write(dumps([rule.toJSON(True) for rule in rules[key]], indent=2))

from printing_util import generate_forest_image
generate_forest_image(forest, "forest.png")
