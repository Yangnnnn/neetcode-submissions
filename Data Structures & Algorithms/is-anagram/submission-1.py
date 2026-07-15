class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashtable1 = {}
        hashtable2 = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] in hashtable1:
                hashtable1[s[i]] += 1
            else:
                hashtable1[s[i]] = 1
            
            if t[i] in hashtable2:
                hashtable2[t[i]] += 1
            else:
                hashtable2[t[i]] = 1
        return hashtable1 == hashtable2
        