List = [2, 7, 11, 15]
target = 9

def two_sum(List, target):
    Dict = dict()
    for index, x in enumerate(List):
        if x not in Dict.keys():
            Dict[target-x] = index
        else:
            print 'found the two number:', index, Dict[x]
            print List[index], List[Dict[x]]
            
            
two_sum(List, target)

two_sum(List, 26)

