# week 0 problem 1
# create a function that returns a list of (vitamins,injections) tuples for each attribute that they need.
# Complete problem statement in README.mds


# your input type should be a list,
# output should also be a list containing tuples
# Example:
# input: [250, 0, 250, 0, 0, 0]
# expected output: [(25,0),(0,0),(25,0),(0,0),(0,0),(0,0)]
# input: [500, 1, 2, 3, 4, 5]
#expected output: "No medicine given"
# HINT: using % operator to find remainder may be helpful
import math


def dose(needs):
    #YOUR SOLUTION STARTS HERE
    condition = sum(needs)
    if condition >=500:
        return 'No medicine given'
    
    vitamins = []
    injections =[]

    for need in needs:
        if need >250: 
            return 'No medicine given'
        else:
            vitamins_need = math.ceil(need/10)
            injection_need = vitamins_need*10-need

            vitamins.append(vitamins_need)
            injections.append(injection_need)

    return list(zip(vitamins,injections))
    #YOUR SOLUTION ENDS HERE
