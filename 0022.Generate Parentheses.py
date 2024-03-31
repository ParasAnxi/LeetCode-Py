class Solution:
    def solve(self,ans,n,z,output):
        if n == 0 and z == 0:
            ans.append(output)
            return
        if n > 0:
            self.solve(ans,n - 1, z + 1,output + '(')
        if z > 0:
            self.solve(ans,n, z - 1, output + ')')
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.slove(ans,n,0,"")
        return ans