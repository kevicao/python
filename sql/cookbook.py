
s.isdigit()
5//2 #2
5%2 #1
bin(5) #0b101
bin(5<<1) #0b1010


[x if x is not None else '' for x in List]
List.index(5) #return the index of 5
List.remove('a')
List.pop(-1)


slots1 = sorted(slots1, reverse = True, key=lambda x: x[0])


myset = {"apple", "banana", "cherry"}
myset = set([1,2,3])
set1 | set2 #union, set1.union(set2); intersection: &; difference: -;


from collections import defaultdict
d = defaultdict(list) #list: [], int: 0
d = defaultdict(lambda: "Not Present")
d["a"] = 1
d["b"]
########binary search###############
import bisect
a = [1,3,5]
bisect.bisect_left(a, 2) #1.  log(n) 
a.insert(1,2) #a = [1,2,3,5]
bisect.insort_left(a, 2) # for insert, 


####priority queue with heapq
import heapq
lo = []
hi = []
heapq.heapify(lo) #n*log(n), in place change, lo[0] is the smallest one, lo.pop(0)
heapq._heapify_max(hi)
heapq._heapreplace_max(a, 7)
heapq._heappop_max(a)
def _heappush_max(heap, item):
    heap.append(item)
    heapq._siftdown_max(heap, 0, len(heap)-1)

heapq.heappush(lo, value) #log(n) for push and pop
value = heapq.heappop(lo)
heapsort(iterable):
	h = []
	for value in iterable:
		heappush(h, value)
		return [heappop(h) for i in range(len(h))]

########deal with file ####################

with open('dog_breeds.txt', 'wr') as f:
	line = f.readline()
	f.write(line)

banana =  {'a':'b'}
import pickle
with open("Fruits.obj","wb") as f:
	pickle.dump(banana,f)
	pickle.load(file)

########deal with class ########################

# Definition of class
class TreeNode(object):
	self.xy = 6. #can be used in any fucntion
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def test1(self, y): 
        def extract_D():
            j = 0
            return j
   
        self.i = 0
        num = extract_num()
        num = self.test2(2)

    def test2(self, z)
    	return 0
obj = TreeNode(5)
obj.test1(3)

#########dfs and bfs################
#dfs of a tree:pre-order
def serialize(node, stream):
    if node == None:
        stream.dump(MARKER);
        return
    stream.dump(node.data);
    serialize(node.left, stream)
    serialize(node.right, stream)


