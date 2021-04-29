Encrypted Words

# You've devised a simple encryption method for alphabetic strings that shuffles the characters in such a way that the resulting string is hard to quickly read, but is easy to convert back into the original string.
# When you encrypt a string S, you start with an initially-empty resulting string R and append characters to it as follows:
# Append the middle character of S (if S has even length, then we define the middle character as the left-most of the two central characters)
# Append the encrypted version of the substring of S that's to the left of the middle character (if non-empty)
# Append the encrypted version of the substring of S that's to the right of the middle character (if non-empty)
# For example, to encrypt the string "abc", we first take "b", and then append the encrypted version of "a" (which is just "a") and the encrypted version of "c" (which is just "c") to get "bac".
# If we encrypt "abcxcba" we'll get "xbacbca". That is, we take "x" and then append the encrypted version "abc" and then append the encrypted version of "cba".



import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def findEncryptedWord(s):
  # Write your code here
    if len(s) == 0:
        return ''
    if len(s) == 1:
        return s
    
    if len(s)%2 == 0:
        mid = len(s)//2 - 1
    else:
        mid = len(s)//2
        
    
    l = findEncryptedWord(s[:mid])
    r = findEncryptedWord(s[mid+1:])
    
    return s[mid] + l + r  
	











# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  s1 = "abc"
  expected_1 = "bac"
  output_1 = findEncryptedWord(s1)
  check(expected_1, output_1)

  s2 = "abcd"
  expected_2 = "bacd"
  output_2 = findEncryptedWord(s2)
  check(expected_2, output_2)

  # Add your own test cases here
  