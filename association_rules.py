


class Rule:
    def __init__(self):
        self._antecedent = set()
        self._consequent = set()
        self._antecedent_object = dict()
        self._consequent_object = dict()
        self._support = 0.0
        self._confidence = 0.0
    
    def support(self) ->float:
        return self._support
    
    def confidence(self) ->float:
        return self._confidence
    
    def antecedent(self) ->set:
        return self._antecedent
    
    def consequent(self) ->set:
        return self._consequent
    
    def is_valid(self, min_confidence: float) ->bool:
        return self._confidence >= min_confidence

