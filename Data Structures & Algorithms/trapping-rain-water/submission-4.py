class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left, right = 0, 1
        carry = 0

        while right < len(height):
            if height[left] > height[right]:
                carry += height[right]
                right += 1                
                continue
            else:
                w = (right - left) -1
                h = min(height[left], height[right])
                water += (w * h) - carry
                left = right
                right += 1
                carry = 0
        

        peak = left
        r = len(height) - 1
        l = r - 1
        carry = 0
        while l >= peak:
            if height[r] > height[l]:
                carry += height[l]
                l -= 1
            else:
                w = (r - l) -1
                h = min(height[l], height[r])
                water += (w * h) - carry
                r = l
                l -= 1
                carry = 0



        return water