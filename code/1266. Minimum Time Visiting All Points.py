class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        total_time = 0
        position = points[0]
        for nextpoint in points[1:]:
            while nextpoint != position:
                if position[0] != nextpoint[0] and position[1] != nextpoint[1]:
                    x = (1 if nextpoint[0] > position[0] else -1)
                    y = (1 if nextpoint[1] > position[1] else -1)
                    
                    position[0] += x
                    position[1] += y
                    total_time += 1
                elif  position[1] != nextpoint[1]:
                    y = (1 if nextpoint[1] > position[1] else -1)
                    position[1] += y
                    total_time += 1
                else:
                    x = (1 if nextpoint[0] > position[0] else -1)
                    position[0] += x
                    total_time += 1

        return total_time
