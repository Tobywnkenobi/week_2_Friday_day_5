"""

list
amount of people and time
 


4 people

person_1= 1 minute
person_2 = 2 minutes
person_3 = 5 minutes
person_4 = 10 minutes

Can only travel at the slowest person's pace. 
Can only cross 2 at a time
only 1 flashlight, so every trip has a return trip if there is a person remaining.
17


person                                                  person

1,2                  person_1 will take the person_2                total = 2 min
                   return trip for person_1                1        total = 3 min
 3,4,2               person_3 and person_4                          total = 13 min
 3,4               person_2 goes back                      2        total = 15 min
 1,2               the last two person_1 and person_2               total = 17 min


return                                                              total = 17

"""

people = [10, 2, 5, 1]
def cross_bridge(people):
    time = 0
    people.sort()
    time += people[1] + people[0]
    time += people[3] + people[1]
    time += people[1]
    print(f"All of the people crossed the bridge in {time} minutes")
    return time
    
cross_bridge(people)
