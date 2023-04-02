#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        zero_count,one_count,two_count=0,0,0
        for i in range(n):
            if arr[i]==0:
                zero_count+=1
            elif arr[i]==1:
                one_count+=1
            else:
                two_count+=1
        for i in range(zero_count):
            arr[i]=0
        for i in range(zero_count,zero_count+one_count):
            arr[i]=1
        for i in range(zero_count+one_count,n):
            arr[i]=2
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends