import random
import math

PI = math.pi

for i in range(1,10+1):
    test_case = i
    target_x = random.uniform(-20,20)
    target_y = random.uniform(-20,20)
    target_heading = random.uniform(0,2*PI) - PI #Range of -pi,pi 
    target_period = random.randint(10,50)
    target_period *= 1 - 2*random.randint(0,1)
    target_speed = random.uniform(1,5)
    hunter_x = random.uniform(-20,20)
    hunter_y = random.uniform(-20,20)
    hunter_heading = random.uniform(0,2*PI) - PI # Range of -pi,pi

    output = """'test_case': {},
     'target_x': {},
     'target_y': {},
     'target_heading': {},
     'target_period': {},
     'target_speed': {},
     'hunter_x': {},
     'hunter_y': {},
     'hunter_heading': {}
""".format(i, target_x, target_y, target_heading, target_period, target_speed, hunter_x, hunter_y, hunter_heading)

    print "    {" + output + "    },"
