# topological ordering
# https://en.wikipedia.org/wiki/Topological_sorting
# amazon interview https://www.careercup.com/question?id=5134681810927616

List = [[5,11], [7,11], [7,8], [3,8], [11,2], [11,9], [11,10], [8,9], [3,10] ]

def topo_ordering(List):
    
    incoming = dict()
    outgoing = dict()
    nodes = []
    
    sorted_nodes = []
    
    for e in List:
        if e[1] not in incoming.keys():
            incoming[e[1]] = [e[0]]
        else:
            incoming[e[1]].append(e[0])
            
        if e[0] not in outgoing.keys():
            outgoing[e[0]] = [e[1]]
        else:
            outgoing[e[0]].append(e[1])
        
        for n in e:
            if n not in nodes:
                nodes.append(n)
                
    s = []
    for n in nodes:
        if n not in incoming.keys():
            s.append(n)
            
    while len(s) > 0:
        n = s.pop(-1)
        sorted_nodes.append(n)
        
        if len(outgoing) > 0:
            for m in outgoing[n]:
                incoming[m].remove(n)
                
                if len(incoming[m]) == 0:
                    s.append(m)
                    incoming.pop(m)
            outgoing.pop(n)
    
    if len(incoming) > 0:
        return 'error'
    else:
        return sorted_nodes
        
        
print topo_ordering(List)
        
        
                
        
    
        