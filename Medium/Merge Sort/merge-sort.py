#User function Template for python3
#User function Template for python3
class Solution:
    def merge(self,arr, l, mid, r):
        n1=mid-l+1
        n2=r-mid
        l1=[0]*n1
        r1=[0]*n2
        for i in range(n1):
            l1[i]=arr[l+i]
        for j in range(n2):
            r1[j]=arr[mid+1+j]
        i=0
        j=0
        k=l
        while i<n1 and j<n2:
            if l1[i]<=r1[j]:
                arr[k]=l1[i]
                i+=1
            else:
                arr[k]=r1[j]
                j+=1
            k+=1
        while i<n1:
            arr[k]=l1[i]
            i+=1
            k+=1
        while j<n2:
            arr[k]=r1[j]
            j+=1
            k+=1
        return

    def mergeSort(self,arr, l, r):

        if l>=r:
            return 

        mid=l+(r-l)//2

        self.mergeSort(arr,l,mid)

        self.mergeSort(arr,mid+1,r)

        self.merge(arr,l,mid,r)




#{ 
 # Driver Code Starts
#Initial Template for Python 3


import sys
input = sys.stdin.readline
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends