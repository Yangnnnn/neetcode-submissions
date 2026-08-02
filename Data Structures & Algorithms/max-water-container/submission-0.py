class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0 
        end = len(heights) - 1
        area = 0
        while start < end:
            heightStart = heights[start]
            heightEnd = heights[end]
            area = max(area, (end-start) * min(heightStart, heightEnd))
            if heightStart>heightEnd:
                end -= 1
            else:
                start+=1
        return area