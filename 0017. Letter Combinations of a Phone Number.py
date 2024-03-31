class Solution:
    def solve(self,digits,ans,map,index,output):
        if index >= len(digits):
            ans.append(output)
            return
        dig = int(digits[index])
        val = map[dig]
        for ch in val:
            output += ch
            self.solve(digits,ans,map,index + 1,output)
            output = output[:-1]


    def letterCombination(self,digits: str)->List[str]:
        ans = []
        if not digits:
            return ans
        map = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        solve(digits,ans,map,0,"")
        return ans