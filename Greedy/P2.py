"""
Problem Description
Given an array of meeting time intervals where intervals[i] = [start_i, end_i], determine if a person could attend all meetings.
A person can attend all meetings if and only if no two meetings overlap. If one meeting ends at time t and another begins at the same time t, they are not considered to be overlapping.
Example 1
Input:
intervals = [[0,30],[5,10],[15,20]]
Output:
false
Explanation:
The first meeting [0,30] overlaps with the second meeting [5,10] and the third meeting [15,20].
"""

def solution(intervals):
    intervals.sort(key = lambda x:x[0])

    for i in range(1,len(intervals)):
        prev_meet_end = intervals[i-1][1]
        curr_meet_start = intervals[i][0]
        if curr_meet_start < prev_meet_end:
            return False

    return True
interval = [[7,10],[2,4]]
#interval = [[1, 3], [2, 4], [5, 7], [9, 10]]
print(solution(interval))


