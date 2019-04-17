# https://www.geeksforgeeks.org/word-ladder-length-of-shortest-chain-to-reach-a-target-word/
# To check if strings differ by 
# exactly one character
 
def isadjacent(a, b):
    count = 0
    n = len(a)
 
    # Iterate through all characters and return false
    # if there are more than one mismatching characters
    for i in range(n):
        if a[i] != b[i]:
            count += 1
        if count > 1:
            break
 
    return True if count == 1 else False
 
# A queue item to store word and minimum chain length
# to reach the word.
class QItem():
 
    def __init__(self, word, len):
        self.word = word
        self.len = len
        
def shortestChainLen(start, target, D):
 
    # Create a queue for BFS and insert 
    # 'start' as source vertex
    Q = []
    item = QItem(start, 1)
    Q.append(item)
 
    while( len(Q) > 0):
 
        curr = Q.pop()
 
        # Go through all words of dictionary
        for it in D:
 
            # Process a dictionary word if it is 
            # adjacent to current word (or vertex) of BFS
            temp = it
            if isadjacent(curr.word, temp) == True:
 
                # Add the dictionary word to Q
                item.word = temp
                item.len  = curr.len + 1
                Q.append(item)
 
                # Remove from dictionary so that this 
                # word is not processed again.  This is 
                # like marking visited
                D.remove(temp)
 
                # If we reached target
                if temp == target:
                    return item.len
                    
                    
D = []
D.append("poon")
D.append("plee")
D.append("same")
D.append("poie")
D.append("plie")
D.append("poin")
D.append("plea")
start = "toon"
target = "plea"
print "Length of shortest chain is: %d" \
        % shortestChainLen(start, target, D)
         
# This code is contributed by Divyanshu Mehta    