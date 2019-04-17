string = 'abcabcbb'

def longest_sub_string(string):
    Length = dict()
    
    if len(string) == 0 or len(string) == 1:
        result = string
    
    else:
        max_length = 0
        max_index = 0
        for i in range(len(string) - 1):
            tmp = dict()
            tmp[string[i]] = i
            for j in range(i+1, len(string)):
                if string[j] in tmp.keys():
                    break
                else:
                    tmp[string[j]] = j
                
            Length[i] = j - i
            
            if j - i > max_length:
                max_length = j - i
                max_index = i
                
        result = string[max_index:max_index+max_length]
    
#    print max_length
#    print max_index
    
    return result
    
    
print longest_sub_string(string)
    
print longest_sub_string('bbbbb')
    
print longest_sub_string('pwwkew')
                
            