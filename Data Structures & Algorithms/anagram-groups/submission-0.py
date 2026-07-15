class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = {}
        for s in strs:
            k = [0]*26
            for i in s:
                k[ord(i) - ord('a')] +=1
            
            if tuple(k) in hashtable:
                hashtable[tuple(k)].append(s)
            else:
                hashtable[tuple(k)] = [s]
        
        return list(dict.values(hashtable))
                