#User function Template for python3

class Solution:
    def search(self, a: list, low : int, high : int, target : int):
        # l: The starting index
        # h: The ending index, you have to search the key in this range
        # Complete this function
        n=len(a)
        l,h=0,n-1
        while(l<=h):
            mid=(l+h)//2
            if(a[mid]==target):
                return mid
            if(a[mid]>=a[l]):
                if(target>=a[l]) and (target<a[mid]):
                    h=mid-1
                else:
                    l=mid+1
            else:
                if(target>a[mid]) and (target<=a[h]):
                    l=mid+1
                else:
                    h=mid-1
        return -1
                
                
                
        
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        A = [int(x) for x in input().split()]
        k = int(input())
        ob=Solution()
        print(ob.search(A, 0, n - 1, k))
# } Driver Code Ends