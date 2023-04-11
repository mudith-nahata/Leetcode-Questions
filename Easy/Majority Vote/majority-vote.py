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
        c1,c2=0,0
        for nums in a:
            if el1==nums:
                c1+=1
            if el2==nums:
                c2+=1
        ans=[]
        if c1>len(a)//3:
            ans.append(el1)
        if c2>len(a)//3:
            ans.append(el2)
        if len(ans)==0:
            return [-1]
        return ans
                
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