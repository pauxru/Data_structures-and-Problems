"""
Question from Leetcode 435: https://leetcode.com/problems/non-overlapping-intervals/

Given an array of intervals intervals where intervals[i] = [starti, endi],
return the minimum number of intervals you need to remove to make the rest
of the intervals non-overlapping.

"""

intervals1 = [[1, 2], [2, 3], [3, 4], [1, 3]]  # Output: 1
intervals2 = [[1, 2], [1, 2], [1, 2]]  # Output: 2


def no_overlapping_intervals(intervals):
    intervals.sort()  # Sort to make the intervals follow each other incrementally
    count = 0  # Count variable

    current_end = intervals[0][1]  # take the first interval end
    for start, end in intervals[1:]:  # For start and end of other intervals from index 1 (2nd one)
        if start >= current_end:  # If start is large than previous interval's end
            current_end = end  # No overlapping and thus make end current end
        else:
            '''
            If start is less than previous end, there is overlapping there 
            We increase the count by one and not remove the value as it is not necessary
            '''
            count += 1
            current_end = min(current_end, end)  # Pick the minimum value of end to reduce chances of overlap
    return count


print(no_overlapping_intervals(intervals1))
