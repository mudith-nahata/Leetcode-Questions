#User function Template for python3

class Solution:
    def Solve(self, n, a):
        el1=-1
        el2=-1
        c1=0
        c2=0
        for i in a:
            if i==el1:
                c1+=1
            elif i==el2:
                c2+=1
            elif c1==0:
                el1=i
                c1=1
            elif c2==0:
                el2=i
                c2=1
            else:
                c1-=1
                c2-=1
                    
        # print(el1,el2)
        l=[]
        if a.count(el1)>(n//3):
            l.append(el1)
        if a.count(el2)>(n//3):
            l.append(el2)
        if len(l)==0:
            return [-1]
        return l
                
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        ob = Solution()
        res = ob.Solve(n, a)
        for val in res:
            print(val, end = ' ')
        print()
# } Driver Code Ends