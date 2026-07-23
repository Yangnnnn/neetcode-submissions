class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for i in strs:
            res+=str(len(i)) + "#" + i
        return res
    def decode(self, s: str) -> List[str]:
        # 5#Hello5#World
        res = []
        i = 0
        while i < len(s) :
            num = ''
            j = i
            while s[j] != '#':
                num += s[j]
                j+=1
            res.append(s[j+1:j+1+int(num)])
            i = j + 1 + int(num) 
        return res
