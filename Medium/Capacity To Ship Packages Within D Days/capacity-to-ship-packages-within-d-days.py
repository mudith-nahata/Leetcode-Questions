#User function Template for python3

class Solution:
    def leastWeightCapacity(self, arr, N, D):
        # code here 
        def cap(capacity):
            days_req=1
            curr_load=0
            for weights in arr:
                curr_load+=weights
                if curr_load>capacity:
                    days_req+=1
                    curr_load=weights
                else:
                    continue
            return days_req<=D
        low=max(arr)
        high=sum(arr)
        while low<high:
            mid=low+(high-low)//2
            if cap(mid):
                high=mid
            else:
                low=mid+1
        return low

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        D=int(input())
        
        ob = Solution()
        print(ob.leastWeightCapacity(arr,N,D))
# } Driver Code Ends