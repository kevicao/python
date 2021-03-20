564. Find the Closest Palindrome


reflect left half to right
and change middle by 1 or -1 to find the right one
need handle many corner cases such as 100 - 1 is 99 (addCarry)
and 11, 101, 1000, 999, etc


class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        
        if int(n) < 10:
            return str(int(n)-1)
        
        if self.check9(n):
            return str(int(n) + 2)
        
        if self.check100(n):
            return str(int(n)-1)
        
        if self.check101(n):
            return str(int(n) - 2)
        
        fh = n[:len(n)/2]
        sh = fh[::-1]
        
        if len(n)%2:
            odd = n[len(n)/2]
        
        #reverse
        if len(n)%2:
            #odd
            pal1 = fh +odd + sh
            
            if odd == '0':
                temp = self.addCarry(fh, -1)
                pal2 = temp + '9' + temp[::-1]
            else:
                pal2 = fh + str(int(odd) - 1) + sh
                
            if odd == '9':
                temp = self.addCarry(fh, 1)
                pal3 = temp + '0' + temp[::-1]
            else:
                pal3 = fh + str(int(odd) + 1) + sh
        else:
            pal1 = fh + sh
            
            smallsize = len(fh)
            if fh[smallsize - 1] == '0':
                temp = self.addCarry(fh, -1)
            else:
                temp = fh[0:smallsize-1] + str(int(fh[smallsize-1] ) - 1)
                
            pal2 = temp + temp[::-1]
            
            if fh[smallsize - 1] == '9':
                temp = self.addCarry(fh, 1)
            else:
                temp = fh[0:smallsize-1] + str(int(fh[smallsize-1] ) + 1)
                
            pal3 = temp + temp[::-1]
        
        diff1 = abs(int(n) - int(pal1))
        diff2 = abs(int(n) - int(pal2))
        diff3 = abs(int(n) - int(pal3))
        print(pal1, pal2, pal3)
        print(diff1, diff2, diff3)
        
        if pal1 == n:
            return pal2 if diff2 <= diff3 else pal3
        else:
            values = [diff2, diff1,  diff3]
            res = [pal2, pal1, pal3]
            return res[values.index(min(values))]
        
        
    def check9(self,n):
        for x in n:
            if x != '9':
                return False
            
        return True
    
    def check101(self,n):
        if n[0] == '1' and n[-1] == '1':
            if len(n) == 2:
                return True
            else:     
                for x in n[1:-1]:
                    if x != '0':
                        return False
            return True
            
        return False
    
    def check100(self,n):
        if n[0] == '1':
            for x in n[1:]:
                if x != '0':
                    return False
            return True
        
        return False
    
    def addCarry(self,n,carry):
        n = n.split()
        if carry == -1:
            itr = len(n) - 1
            while itr >= 0 and n[itr] == '0':
                    n[itr] == '9'
                    itr -= 1
            if itr >=0:
                n[itr] = str(int(n[itr]) -1)
        else:
            for i in range(len(n)-1, -1, -1):
                temp = int(n[i])
                n[i] = str((temp + carry)%10)
                carry = (temp+carry)/10
                
        return ''.join(n)