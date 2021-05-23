
# 84. Largest Rectangle in Histogram
# Finds the maximum area under the histogram represented 
# by histogram. See below article for details. 
# https:#www.geeksforgeeks.org/largest-rectangle-under-histogram/ 
class Solution(object):
    def largestRectangleArea(self, histogram):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = list()

        max_area = 0 # Initialize max area

        # Run through all bars of
        # given histogram
        index = 0
        while index < len(histogram):

            # If this bar is higher 
            # than the bar on top
            # stack, push it to stack

            if (not stack) or (histogram[stack[-1]] <= histogram[index]):
                stack.append(index)
                index += 1

            # If this bar is lower than top of stack,
            # then calculate area of rectangle with 
            # stack top as the smallest (or minimum
            # height) bar.'i' is 'right index' for 
            # the top and element before top in stack
            # is 'left index'
            else:
                # pop the top
                top_of_stack = stack.pop()

                # Calculate the area with 
                # histogram[top_of_stack] stack
                # as smallest bar
                area = (histogram[top_of_stack] * 
                       ((index - stack[-1] - 1) 
                       if stack else index))

                # update max area, if needed
                max_area = max(max_area, area)

        # Now pop the remaining bars from 
        # stack and calculate area with 
        # every popped bar as the smallest bar
        while stack:

            # pop the top
            top_of_stack = stack.pop()

            # Calculate the area with 
            # histogram[top_of_stack] 
            # stack as smallest bar
            area = (histogram[top_of_stack] * 
                  ((index - stack[-1] - 1) 
                    if stack else index))

            # update max area, if needed
            max_area = max(max_area, area)

        # Return maximum area under 
        # the given histogram
        return max_area


# my code
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        s = []
        max_area = 0
        
        for i in range(len(heights)):
            if (not s) or heights[i] >= heights[s[-1]]:
                s.append(i)
            else:
                while s and heights[i] < heights[s[-1]]:
                    top = s.pop(-1)
                    max_area = max(max_area, (i-s[-1]-1 if s else i)*heights[top])
                s.append(i)
        
        i += 1
        while s:
            top = s.pop(-1)
            max_area = max(max_area, (i-s[-1]-1 if s else i)*heights[top])
                    
        return max_area


# 85. Maximal Rectangle with all 1s in a 1/0 matrix

#https://www.geeksforgeeks.org/maximum-size-rectangle-binary-sub-matrix-1s/
# Python3 program to find largest rectangle 
# with all 1s in a binary matrix 

#take each row as heights; for next row, stack up with previous row results

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        
        row = len(matrix)
        col = len(matrix[0])
        h = [0]*col
        max_rectangle = 0
        print(h)
        
        for r in matrix:
            h = [int(r[i]) + h[i] if r[i] == "1" else 0 for i in range(col)]
            max_rectangle = max(max_rectangle, self.largestRectangleArea(h))
            print(h)
            
        return max_rectangle
	



# dynamic programming to find max suqare with all 1s

def printMaxSubSquare(M):
    R = len(M) # no. of rows in M[][]
    C = len(M[0]) # no. of columns in M[][]
 
    S = [[0 for k in range(C)] for l in range(R)]
    # here we have set the first row and column of S[][]
    for j in range(C):
        S[0][j] = M[0][j]
    for i in range(R):
        S[i][0] = M[i][0]
 
    # Construct other entries
    for i in range(1, R):
        for j in range(1, C):
            if (M[i][j] == 1):
                S[i][j] = min(S[i][j-1], S[i-1][j],
                            S[i-1][j-1]) + 1
            else:
                S[i][j] = 0
     
    # Find the maximum entry and
    # indices of maximum entry in S[][]
    max_of_s = S[0][0]
    max_i = 0
    max_j = 0
    for i in range(R):
        for j in range(C):
            if (max_of_s < S[i][j]):
                max_of_s = S[i][j]
                max_i = i
                max_j = j
 
    print("Maximum size sub-matrix is: ")
    for i in range(max_i, max_i - max_of_s, -1):
        for j in range(max_j, max_j - max_of_s, -1):
            print (M[i][j], end = " ")
        print()

        
 # Driver Program
M = [[0, 1, 1, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]]
 
printMaxSubSquare(M)


