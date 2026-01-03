class Solution(object):
    def maxArea(self, height):
        Best = 0
        i_left = 0
        i_right = len(height) - 1
        while i_left < i_right:
            length = i_right - i_left
            height_left = height[i_left]
            height_right = height[i_right]
            if height_left < height_right:
                area = length * height_left
                Best = max(area,Best)
                i_left += 1
            else:
                area = length * height_right
                Best = max(area,Best)
                i_right -= 1
        return Best
