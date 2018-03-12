
def two_sum(List, target):
    Dict = dict()
    for index, x in enumerate(List):
        if x not in Dict.keys():
            Dict[target-x] = index
        else:
            print 'found the two number:', index, Dict[x]
            print List[index], List[Dict[x]]
            
            
def three_sum(List):
    solution = []
    for i in range(len(List)):
        
           