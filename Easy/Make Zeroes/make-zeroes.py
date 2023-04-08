#User function Template for python3


import copy
class Solution:
    def MakeZeros(self, matrix):
        mat=copy.deepcopy(matrix)
        s=0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j]==0:
                    if i>0 :
                        s+=mat[i-1][j]
                        matrix[i-1][j]=0
                    if i<len(mat)-1:
                        s+=mat[i+1][j]
                        matrix[i+1][j]=0
                    if j>0:
                        s+=mat[i][j-1]
                        matrix[i][j-1]=0
                    if j<len(mat[i])-1:
                        s+=mat[i][j+1]
                        matrix[i][j+1]=0
                    matrix[i][j]=s
                    s=0
       # print(matrix)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int,input().split())))
		ob = Solution()
		ob.MakeZeros(matrix)
		for i in range(n):
			for j in range(m):
				print(matrix[i][j], end = " ")
			print()
# } Driver Code Ends