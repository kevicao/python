848. Shifting Letters


class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        chars = 'abcdefghijklmnopqrstuvwxyz'
        h = {}
        for i, c in enumerate(chars):
            h[c] = i
        
        for i in range(len(shifts)-2, -1, -1):
            shifts[i] = shifts[i] + shifts[i+1]
        
        ans = ''
        for i, c in enumerate(S):
            ans += chars[(h[c] + shifts[i])%26]
            
        return ans
        

 # facebook rotational cipher

 def rotationalCipher(string, rotation_factor):
  # Write your code here
    Upper = 'abcdefghijklmnopqrstuvwxyz'
    Lower = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    hu = {}
    hl = {}
    for i, c in enumerate(Upper):
        hu[c] = i
    for i, c in enumerate(Lower):
        hl[c] = i
        
    ans = ''
    for c in string:
        if c.isdigit():
            ans += str((int(c)+rotation_factor)%10)
        elif c in hu:
            ans += Upper[(hu[c]+rotation_factor)%26]
        elif c in hl:
            ans += Lower[(hl[c]+rotation_factor)%26]
        else:
            ans += c
    return ans
            
# rotationalCipher("All-convoYs-9-be:Alert1.", 4) == "Epp-gsrzsCw-3-fi:Epivx5."
rotationalCipher("abcdZXYzxy-999.@", 200) == "stuvRPQrpq-999.@"
# rotationalCipher("All-convoYs-9-be:Alert1.", 4)
