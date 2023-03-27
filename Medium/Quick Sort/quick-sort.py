#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        if low>=high:
            return
        i=low
        j=high
        pme=i+(j-i)//2
        while(i<=j):
            if(arr[i]<=arr[pme]):
                i+=1
            elif(arr[j]>=arr[pme]):
                j-=1
            else:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j-=1
        if pme<j:
            arr[pme],arr[j]=arr[j],arr[pme]
            pme=j
        elif i<pme:
            arr[pme],arr[i]=arr[i],arr[pme]
            pme=i
        self.quickSort(arr,low,pme-1)
        self.quickSort(arr,pme+1,high)
                
        #while i<j
    #def partition(self,arr,low,high):
        # code here
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends