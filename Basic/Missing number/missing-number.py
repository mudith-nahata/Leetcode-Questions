#User function Template for python3

def missingNumber(A, N):
    #this for lopp is the numbers from 1 to n in the array 
    #for i in range(1,N+1):
        #count=0
        #for j in range(N-1):#the numbers from to elements in the array from o indexed
            #if A[j]==i:
                #count=1
        #if count==0:
            #return i
    #better Solution
    #hash=[0]*N+1
    #for i in range(N):
        #if hash[arr[i]]+=1
    #for i in range(1,N):
        #if hash[arr[i]]==0:
            #return i
    #better solution
    k=N*(N+1)//2
    s=sum(A)
    m=k-s
    return m

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        print(missingNumber(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends