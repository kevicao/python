Slow Sums

def getTotalTime(arr):
  # Write your code here
    arr = sorted(arr, reverse = True)
    ans = 0
    for i in range(1, len(arr)):
        arr[i] = arr[i] + arr[i-1]
        ans += arr[i]
        
    return ans  