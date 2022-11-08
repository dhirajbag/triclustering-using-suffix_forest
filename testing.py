from suffix_forest import build_sufix_forest
from frequent_patterns import get_FCPs
from demodata import SFD_mdm, SFD_om
from association_rules import Rule

forest = build_sufix_forest({"MDM": SFD_mdm, "OM": SFD_om})
FCPs = get_FCPs(forest)
print("Total "+str(len(FCPs))+" FCP geerated.")
# for pat in FCPs:
#     print(pat)

from generators import get_generators

GEN = get_generators(FCPs)

# for gen in GEN:
#     print("generator: " + str(gen[0]))
#     print("closure: " + str(gen[1]))

rules = Rule.generate_rules(GEN, FCPs)

from json import dumps

with open("forest.json", "w") as outputfile:
    outputfile.write(dumps(forest, indent=2))

for key in list(rules.keys()):
    print("Total "+str(len(rules[key]))+" "+str(key)+" rules generated.")
    with open("rule_"+str(key)+".json", "w") as outputfile:
        outputfile.write(dumps([rule.toJSON() for rule in rules[key]], indent=2))

from printing_util import generate_forest_image
generate_forest_image(forest, "forest.png")
