'''
https://neetcode.io/problems/car-fleet/question?list=neetcode150
'''
def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    # first lets create a tuple list of the position and speed of the cars
    car_list = [(position[i],speed[i]) for i in range(len(position))]

    # sort the car_list based on position, in descending order
    car_list = sorted(car_list,key=lambda x: x[0],reverse=True)

    # define the stack
    stack = []

    # check for each pair
    for p,s in car_list:
        stack.append((target - p) / s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]: # if the new car is reaching before the last car's time, they will join into a fleet
            stack.pop()

    return len(stack)

target = 10
position = [8,3,7,4,6,5]
speed = [4,4,4,4,4,4]

print(carFleet(target,position, speed))


