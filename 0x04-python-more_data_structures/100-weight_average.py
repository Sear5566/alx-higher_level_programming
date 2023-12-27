#!/usr/bin/python3
def weight_average(my_list=[]):
    weight = 0
    score_weight = 0
    if my_list:
        for tuples in my_list:
            weight += (tuples[0] * tuples[1])
            score_weight += tuples[1]
        return (weight / score_weight)
    return (0)
