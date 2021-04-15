528. Random Pick with Weight



class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        

    def pickIndex(self):
        """
        :rtype: int
        """
        
        if len(self.w) ==1:
            return 0
        
        acc = [self.w[0]]
        for i in range(1,len(self.w)):
            acc.append(acc[i-1] + self.w[i])
        
        import random
        import bisect

        return bisect.bisect(acc, random.uniform(0,acc[-1]) )
        
       



# build long array; pass time limit

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        

    def pickIndex(self):
        """
        :rtype: int
        """
        
        if len(self.w) ==1:
            return 0
        
        acc = []
        for i in range(len(self.w)):
            acc = acc + [i]*self.w[i]
        
        import random
        
        ind = int(random.uniform(0,len(acc)))

        return acc[ind]


# Microsoft interview questions
# Suppose a discrete probability distribution P is defined as a list P = [p0, p1, p2, …., pN].
# The i_th index is the probability of value i. For example, p2 is the probability of value 2 and p10 is the probability of value 10.
# You can assume for i < 0 and i > N the probability is 0. Also assume that probabilities add up to 1.
# Write a function that takes P and an integer K and outputs K values that match the probability distribution P. Do not use numpy.

###
###
def cal_accumulated_p(P):
    ## calculate the accumulated P
    tmp = 0
    List = [0]
    for i in range(len(P)):
        tmp += P[i]
        List.append(tmp)
    return List
 
def find_num(P, num):
    for i in range(len(P)-1):
        if num >= P[i] and num < P[i+1]:
            return i

def find_num_binarySearch(P, num):
    #binary search should be faster
    left = 0
    right = len(P) -1
    
    while left < right:
        mid = (left + right)//2
        if P[mid] <= num and P[mid + 1] > num:
            return mid
        elif P[mid] > num:
            right = mid
        elif P[mid] < num:
            left = mid

def generate_K(P, K):
    import random
    acc_arr = cal_accumulated_p(P)
    print(acc_arr)
    
    for i in range(K):        
        num = random.uniform(0,1) #random number between 0 and 1 uniformly
        index = find_num_binarySearch(acc_arr, num)
        
        print(num, index)
    
P = [0.1, 0.2, 0.4, 0.3]

generate_K(P, 2)

#acc_arr = [0.1, 0.3, 0.7, 1]
#num = 0.15
# index = 0 output
# num = 0.08

 
 
        