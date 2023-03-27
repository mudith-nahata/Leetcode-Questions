#Sort the array using insertion sort

#Sort the array using insertion sort

class Solution:
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        for i in range(0,n-1):
            for j in range(i+1,n):
                if arr[j]<arr[i]:
                    temp=arr[i]
                    arr[i]=arr[j]
                    arr[j]=temp
                    
                    
                    
#{ 
 # Driver Code Starts
if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
    
        Solution().insertionSort(arr,n)
    
        for i in range(n):
            print(arr[i],end=" ")
    
        print()
# } Driver Code Ends