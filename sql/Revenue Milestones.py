Revenue Milestones


def getMilestoneDays(revenues, milestones):
  # Write your code here
    tmp = []
    for i, x in enumerate(milestones):
        tmp.append([x,i])
    milestones = sorted(tmp, key = lambda x: x[0])
    
    milestone = milestones[0][0]
    index = 0
    s = 0
    ans = []
    
    for i, rev in enumerate(revenues):
        s += rev
        if s >= milestone:
            while s >= milestone: 
                ans.append([i+1, milestones[index][1]])
                index += 1
                if index == len(milestones):
                    break
                milestone = milestones[index][0]
            if index == len(milestones):
                break
    ans = sorted(ans, key = lambda x: x[1])        
    return [x[0] for x in ans]