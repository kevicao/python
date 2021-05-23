


# this link gives compicated solutions which I do not know whehter we need
# https://www.geeksforgeeks.org/minimum-number-appends-needed-make-string-palindrome/

def appendToPalindrome(string):
    l = 0
    r = len(string) - 1
    count = 0
    while l <= r:
        if string[l] != string[r]:
            count += 1
            l += 1
        else:
            if isPalindrome(string[l:r+1]):
                return count
            else:
                l += 1
                count += 1
    return count

def isPalindrome(string):
    l = 0
    r = len(string) - 1
    while l < r:
        if string[l] == string[r]:
            l += 1
            r -= 1
        else:
            return False
        
    return True

print(appendToPalindrome('abede')) #2
print(appendToPalindrome('aabb')) #2
print(appendToPalindrome('')) #2
print(isPalindrome(''))
print(isPalindrome('ab'))