from util import get_support_count

class Rule:
    def __init__(self, antecedent_set = set(), consequent_set = set(), support_object = dict(), confidence = 0.0):
        self._antecedent = antecedent_set
        self._consequent = (consequent_set - antecedent_set)
        self._support_object = support_object
        self._support = get_support_count(support_object)
        self._confidence = confidence
    
    def support(self) ->int:
        return self._support
    
    def confidence(self) ->float:
        return self._confidence
    
    def antecedent(self) ->set:
        return self._antecedent
    
    def consequent(self) ->set:
        return self._consequent
    
    def is_valid(self, min_confidence: float) ->bool:
        return self._confidence >= min_confidence
    
    def is_exact(self) ->bool:
        return self._confidence == 1.0
    
    def generate_rules(GEN, FCP) ->list:
        """Generates and returns a list of Association Rules from the
         given generator list GEN and frequent closed pattern list FCP"""

        AR_E = list()
        AR_SB = list()
        AR_PB = list()

        for g in GEN:
            for pattern in FCP:
                if g[1].get_itemset() == pattern.get_itemset():
                    if(g[0].get_itemset() != pattern.get_itemset()):
                        rule = Rule(g[0].get_itemset(), pattern.get_itemset(), pattern.get_object(), 1.0)
                        AR_E.append(rule)
                else:
                    if g[1].get_itemset().issubset(pattern.get_itemset()):
                        confidence = float(get_support_count(pattern.get_object()))/float(get_support_count(g[1].get_object()))
                        rule = Rule(g[0].get_itemset(), pattern.get_itemset(), pattern.get_object(), confidence)
                        AR_SB.append(rule)
        
        for Fi in FCP:
            for Fj in FCP:
                if(Fi.size() < Fj.size() and Fi.get_itemset().issubset(Fj.get_itemset())):
                    confidence = float(get_support_count(Fj.get_object()))/float(get_support_count(Fi.get_object()))
                    rule = Rule(Fi.get_itemset(), Fj.get_itemset(), Fj.get_object(), confidence)
                    AR_PB.append(rule)
        
        return {
            "AR_E": AR_E,
            "AR_SB": AR_SB,
            "AR_PB": AR_PB
        }
    
    def __str__(self):
        return "Rule(\n\t"+str(self._antecedent)+" => "+str(self._consequent)+"\n\tSupport: "+str(self.support())+"\n\tConfidence: "+str(self.confidence())+"\n)\n"
    
    def toJSON(self, include_object = False) ->dict:
        JSON = {
            "antecedent": list(self.antecedent()),
            "consequent": list(self.consequent()),
            "support": self.support(),
            "confidence": self.confidence()
        }

        if(include_object):
            JSON["object"] = self._support_object
        
        return JSON





