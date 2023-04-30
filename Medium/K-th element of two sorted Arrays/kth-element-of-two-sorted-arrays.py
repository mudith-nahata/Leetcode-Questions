#User function Template for python3

class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        ans=[]
        for ele1 in arr1:
            ans.append(ele1)
        for ele2 in arr2:
            ans.append(ele2)
        ans=sorted(ans)
        return ans[k-1]
            
            
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m, k = sz[0], sz[1], sz[2]
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement( a, b, n, m, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends