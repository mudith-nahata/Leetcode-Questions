#User function Template for python3


class Solution:
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self,matrix, n):
              #reverse rows
        p1=0
        p2=n-1
        while p1<p2:
            for i in range(n):
                matrix[i][p1],matrix[i][p2]=matrix[i][p2],matrix[i][p1]
            p1+=1
            p2-=1
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        #reverse rows
        #p1=0
        #p2=n-1
        #while p1<p2:
            #for i in range(n):
                #matrix[i][p1],matrix[i][p2]=matrix[i][p2],matrix[i][p1]
            #p1+=1
            #p2-=1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        matrix = [[0 for j in range(n)] for i in range(n)]
        line1 = [int(x) for x in input().strip().split()]
        k=0
        for i in range(n):
            for j in range (n):
                matrix[i][j]=line1[k]
                k+=1
        obj = Solution()
        obj.rotateby90(matrix,n)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j],end=" ")
        print()

# } Driver Code Ends