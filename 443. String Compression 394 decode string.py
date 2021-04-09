443. String Compression

# work on each group

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        cnt = 1
        index = 0

        for i in range(len(chars) -1):
            if chars[i+1] == chars[i]:
                cnt += 1
            else:
                if cnt == 1:
                    chars[index] = chars[i]
                    index += 1
                else:
                    chars[index] = chars[i]
                    temp = [x for x in str(cnt)]
                    chars[index+1:(index+1 + len(temp))] = temp[:]
                    index += len(temp) + 1
                    cnt = 1
        
        i = len(chars) - 1
        if cnt == 1:
            chars[index] = chars[i]
            index += 1
        else:
            chars[index] = chars[i]
            temp = [x for x in str(cnt)]
            chars[index+1:(index+1 + len(temp))] = temp[:]
            index += len(temp) + 1
            cnt = 1 
            
        return index


# 394. Decode String
# s = "3[a]2[bc]"
# s = "2[abc]3[cd]ef"

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        q = []
        
        for x in s:
            if x != ']':
                q.append(x)
            else:
                tmp = []
                while len(q) > 0 and q[-1] != '[':
                    tmp.insert(0,q.pop(-1))
                q.pop(-1)
                number = []
                while len(q) > 0 and q[-1].isdigit():
                    number.insert(0,q.pop(-1))
                    
                k = int(''.join(number))
                q = q + tmp*k

                
        return ''.join(q)



# Implement a method to perform basic string compression using the counts of repeated characters. 
# For example, the string aabcccccddd would become a2b1c5d3. If the "compressed" string would not become smaller 
# than the original string, your method should return the original string.

# You can assume the string has only lowercase letters. (a-z)

def string_compress(s):
    result = ""
    cnt = 1
     
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            cnt += 1
        else:
            result += s[i] + str(cnt)
            cnt = 1
             
    result += s[i] + str(cnt)
     
    if len(result) >= len(s):
        return s
    return result
 
if __name__ == "__main__":
    print(string_compress("aabcccccddd"))# == "a2b1c5d3"
    assert string_compress("abcde") == "abcde"

