
"""
Problem Description

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

Example 1:

Input:

gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

Output:

3
Explanation:
Start at station 3 (index 3). Your tank = 0.
Travel to station 4. Get 4 gas, spend 1 cost. Tank = 3.
Travel to station 0. Get 5 gas, spend 2 cost. Tank = 6.
Travel to station 1. Get 1 gas, spend 3 cost. Tank = 4.
Travel to station 2. Get 2 gas, spend 4 cost. Tank = 2.
Travel to station 3. Get 3 gas, spend 5 cost. Tank = 0.
You can return to station 3. Therefore, return 3.
"""
def solution(gas, cost):
    if sum(gas) < sum(cost):
        return -1

    total_tank = 0
    start_index = 0

    for i in range(len(gas)):
        total_tank = total_tank + gas[i] - cost[i]

        if total_tank < 0:
            start_index = i + 1
            total_tank = 0

    return start_index


print(solution([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))