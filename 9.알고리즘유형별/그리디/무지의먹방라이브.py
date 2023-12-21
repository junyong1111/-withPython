import sys
def solution(food_times, k):
    answer = 0
    size = len(food_times)
    
    curr_food = 0
    while k:
        k-=1
        if sum(food_times) == 0:
            return -1
        
        if food_times[curr_food]==0:
            curr_food = (curr_food+1)%size
            k+=1
            continue
        food_times[curr_food] =food_times[curr_food]-1
        curr_food = (curr_food+1)%size
    
    answer = (curr_food+1)%size
    return answer