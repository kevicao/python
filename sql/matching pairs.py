def matching_pairs(s, t):
    # Write your code here
    count = 0
    mismatch = []
    h = {}
    for i in range(len(t)):
        if s[i] in h:
            h[s[i]] += 1
        else:
            h[s[i]] = 1
            
        if s[i] == t[i]:
            count += 1
        else:
            mismatch.append(i)
            
    if len(mismatch) == 0:
        for key in h:
            if h[key] >= 2:
                return count
        return count - 2
    
    if len(mismatch) == 1:
        for i in range(len(s)):
            if mismatch[0] != i and s[i] == s[mismatch[0]]:
                return count
        for i in range(len(t)):
            if mismatch[0] != i and t[i] == s[mismatch[0]]:
                return count
            
        return count - 1
    

    if len(mismatch) >= 2:
        print('herer')
        single = []
        double = []
        for i in range(len(mismatch)):
            for j in range(i+1, len(mismatch)):
                if s[mismatch[i]] == t[mismatch[j]]:
                    if s[mismatch[j]] == t[mismatch[i]]:
                        double.append([i,j])
                    else:
                        single.append([i,j])
        if double:
            return count + 2
        if single:
            return count + 1
        
        return count
                    
matching_pairs("ABC", "ADB")
                
            
            
        