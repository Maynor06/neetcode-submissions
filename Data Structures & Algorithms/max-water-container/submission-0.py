class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        left, right = 0, len(heights)-1

        while right > left:
            width = right - left
            height = min(heights[left], heights[right])
            areaCalc = width * height
            area = max(area, areaCalc)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1


        return area