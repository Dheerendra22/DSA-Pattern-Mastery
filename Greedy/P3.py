def solution(intervals):
    intervals.sort(key = lambda x:x[0])
    result = []

    for i in range(1,len(intervals)):
        prev_meet_end = intervals[i-1]
        curr_meet_start = intervals[i]
        if curr_meet_start[0] < prev_meet_end[1]:
            result.append([prev_meet_end[0],curr_meet_start[1]])
        else:
            if i==1:
                result.append(prev_meet_end)
            result.append(curr_meet_start)
            

    return result
#interval = [[7,10],[2,4]]
interval = [[1, 3], [3, 4], [5, 7], [9, 10]]
print(solution(interval))