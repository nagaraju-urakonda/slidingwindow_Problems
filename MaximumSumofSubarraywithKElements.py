def s_w(arr,k):
    n = len(arr)
    cur_sum = sum(arr[:k])
    max_sum = cur_sum
    
    for i in range(k,n):
        cur_sum = cur_sum + arr[i] - arr[i-k]
        max_sum = max(max_sum,cur_sum)
        
    return max_sum
arr = [100,200,300,400,500]
k = 2
print(s_w(arr,k)) # here the output is 900
        
    
