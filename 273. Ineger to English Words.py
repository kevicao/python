
273. Integer to English Words

pay attention to edge cases, deal with extra space

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
            
        ans = ''
        n = num
        if n//10**9 > 0:
            ans = ans.strip(' ') + ' ' + self.hundred(n//10**9) + ' Billion'
            ans = ans.strip(' ')
            n = n%10**9

        if n//10**6 > 0:
            ans =  ans.strip(' ') + ' ' + self.hundred(n//10**6) + ' Million'
            ans = ans.strip(' ')
            n = n%10**6

        if n//10**3 > 0:
            ans = ans.strip(' ') + ' ' + self.hundred(n//10**3) + ' Thousand'
            ans = ans.strip(' ')
            n = n%10**3
            
        if n > 0:
            return (ans.strip(' ') + ' ' + self.hundred(n).strip(' ')).strip(' ')
        elif len(ans) > 0:
            return ans.strip(' ')
        else:
            return 'Zero'
        
                
    def hundred(self, n):
        single_dic = {1: 'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8: 'Eight', 9:'Nine'}
        double_dic = {2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninety'}
        teen_dic = {0:'Ten', 1:'Eleven', 2:'Twelve', 3:'Thirteen', 4:'Fourteen', 5:'Fifteen', 6:'Sixteen', 7:'Seventeen', 8:'Eighteen', 9:'Nineteen'}
        
        s = ''            
        if n//100 > 0:
            s = s.strip(' ') + ' ' + single_dic[n//100] + ' Hundred'
            s = s.strip(' ')
            n = n%100
            
        if n//10 >= 2:
            s = s.strip(' ') + ' ' + double_dic[n//10]
            s = s.strip(' ')
            n = n%10
            if n > 0:
                return (s + ' ' + single_dic[n]).strip(' ')
            else:
                return s
        elif n//10 == 1:
            s = s.strip(' ') + ' ' + teen_dic[n%10]
            return s.strip(' ')
        elif n > 0:
            return (s + ' ' + single_dic[n]).strip(' ')
        
        if len(s) > 0:
            return s.strip(' ')
        else:
            return 'Zero'

          

