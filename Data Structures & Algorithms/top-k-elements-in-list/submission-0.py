import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashtable = {}
        for i in nums:
            if i in hashtable:
                hashtable[i] += 1
            else:
                hashtable[i] = 1
        
        heap = [];
        heapSize = 0;
        for i in hashtable:
            heapq.heappush(heap, (hashtable[i], i))
            heapSize+=1
            if heapSize > k:
                heapq.heappop(heap)
                heapSize-=1
        res = []
        for i in heap:
            res.append(i[1])
        return res