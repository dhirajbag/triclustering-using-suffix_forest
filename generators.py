# Finds generators from the list of FCPs
# Input: List of FCPs
# Output: List of generators


# A Generator element g has two parts:
# g[0] is the generator pattern
# g[1] is the closure pattern

import itertools
from Pattern import Pattern

def get_generators(FCP: list):
    """Returns the list of generators from the FCP list"""

    FCP.sort(key = comparator)
    GEN = []
    
    for i in range(len(FCP)):
        pattern = FCP[i].get_copy()
        found_gen = False
        generator_size = 1

        while found_gen == False and generator_size < pattern.size():
            subsets = get_all_subsets(pattern.get_itemset(), generator_size)

            for subset in subsets:
                not_generator = False
                for generator in GEN:
                    if generator[0].get_itemset() == subset:
                        not_generator = True
                        break
                if not_generator == False:
                    #TODO: Is this what is meant by "for all C ∈ FCP preceding F ∈ FCP" ?
                    for j in range(i):
                        if subset.issubset(FCP[j].get_itemset()):
                            not_generator = True
                            break
                if not_generator == False:
                    #TODO: Is this the correct Object List for the generators ?
                    GEN.append([Pattern(subset, pattern.get_object()), pattern])
                    found_gen = True
            generator_size += 1

        if found_gen == False:
            GEN.append([pattern, pattern.get_copy()])
    
    return GEN



def comparator(pattern: Pattern) ->int:
    """Custom key funtion that will be used for used for soring FCPs
    based on the size of the pattern"""
    return pattern.size()

def get_all_subsets(subset: set, n: int) ->list:
    """Returns all possible subsets of size n from the given subset"""
    return [set(tpl) for tpl in itertools.combinations(subset, n)]


if __name__ == "__main__":
    print(get_all_subsets(set([1, 2, 3, 4, 5]), 3))
