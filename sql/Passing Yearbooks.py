Passing Yearbooks

# arr is fixed. each person only transfer to the same person

#to make sure each book go back to onwer, there has to be connected cycle...there may be different cycle though

def findSignatureCounts(arr):
    L = len(arr)
    res = [0] * L
    # set of visited students
    visited = set()
    for i in range(len(arr)):
        if i not in visited:
            j = i
            # the students of the same group as student i
            group = set([i])
            # keep passing the yearbook until it goes back to i
            while arr[j]-1 != i:
                j = arr[j]-1
                group.add(j)
            # update the visited set
            visited.update(group)
            for k in group:
                res[k] = len(group)
    return res

findSignatureCounts([2, 1])