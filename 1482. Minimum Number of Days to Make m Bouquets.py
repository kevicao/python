1482. Minimum Number of Days to Make m Bouquets



class Solution:
    def minDays(self, bloomDay, m, k):
        res=m*k
        if res>len(bloomDay):
            return -1
         
        tmp=list(set(bloomDay))
        tmp.sort()
 
         
         
        l,r=0,len(tmp)-1
        while l<r:
            mid=(l+r)//2
            if self.isMinDay(bloomDay,tmp[mid],m,k):
                r=mid
            else:
                l=mid+1
        if r<l:
              return -1
        return tmp[r]
     
     
    def isMinDay(self,bloomDay,day,m,k):        
        cnt=0
         
        i=0
        while i<len(bloomDay):
            if bloomDay[i]>day:
                i+=1
                continue
            j=1
            while i+j<len(bloomDay) and bloomDay[i+j]<=day and j<k:
                j+=1
             
            if j==k:
                cnt+=1
                i+=j
                if cnt==m:
                    return True
            else:
                i+=j 
                
        return False










# too slow; the key is the search space, not how to organize

class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if m*k > len(bloomDay) or len(bloomDay) == 0:
            return -1
        
        dic = dict()
        for i, x in enumerate(bloomDay):
            if x in dic:
                dic[x] = dic[x] + [i]
            else:
                dic[x] = [i]
                
        days = sorted(dic.keys())
        
        tmp = [0]*len(bloomDay)
        d_count = 0
        for day in days:
            d_count += len(dic[day])
            for index in dic[day]:
                tmp[index] = 1
            if d_count >= m*k:
                b_count = 0
                f_count = 0
                flag = 0
                for y in tmp:
                    if y == 1:
                        if flag == 0:
                            f_count = 1
                            flag = 1
                        else:
                            f_count += 1
                        if f_count == k:
                            b_count += 1
                            if b_count == m:
                                return day
                            f_count = 0
                            flag = 0

                    else:
                        flag = 0
        return -1
