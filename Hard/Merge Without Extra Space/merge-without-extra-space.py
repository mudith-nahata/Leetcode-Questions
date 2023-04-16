#User function Template for python3

class Solution:
    
    #Function to merge the arrays.
    def merge(self,arr1,arr2,n,m):
        a3=[]*(n+m)
        for num1 in arr1:
            a3.append(num1)
        for num2 in arr2:
            a3.append(num2)
        a3.sort()
        k=0
        for i in range(n):
            arr1[i]=a3[k]
            k+=1
        for i in range(m):
            arr2[i]=a3[k]
            k+=1
        return arr1,arr2
        



#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n,m = map(int, input().strip().split())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob=Solution()
        ob.merge(arr1, arr2, n, m)
        print(*arr1,end=" ")
        print(*arr2)
# } Driver Code Ends