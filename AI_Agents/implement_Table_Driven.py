# Implement diffierent types of agent implementation to do a certain task of your choice. 
# 1. Table Driven Agent
# 2. Simple Reflex Agent

# Before implementation describe the following:

# 1. Agent Description: The aim of the agent .....
# 2. List the sensors:
# 3. Sensors' values: 
# 3. List the actions:
# 4. Agent function: perception --> action

# padestrian cross (zebra crossing)

table={('Traffic_Light_Green','Person_Present'):'No_Crossing',
       ('Traffic_Light_Green','Person_Absent'):'No_Crossing',
       ('Traffic_Light_Red','Person_Present'):'Cross',
       ('Traffic_Light_Red','Person_Absent'):'Cross',
       ('Traffic_Light_Yellow','Person_Present'):'No_Crossing',
       ('Traffic_Light_Yellow','Person_Absent'):'No_Crossing'}

percepts=[]  # to store percept sequence  
def table_driven_agent(percept):
    print('Perception Received: '+ str(percept))
    percepts.append(percept) # updating percept history
    action = lookup(percept,table) # searching for action
    return action

def lookup(p,t):
    return t[p]

# lets simulate the agent
import random

Location = random.choice(['Traffic_Light_Green', 'Traffic_Light_Yellow', 'Traffic_Light_Red'])
Condition = random.choice(['Person_Present','Person_Absent'])

while True: # to perceieve environment repeatedly
    action = table_driven_agent((Location, Condition))
    print('Action Performed: '+ action)
    cmd = input('Get Perception (yes/no): ')
    if(cmd != 'yes'): break
    if action == 'Cross':
        Location = random.choice(['Traffic_Light_Green', 'Traffic_Light_Yellow'])
        Condition = random.choice(['Person_Present','Person_Absent'])
    elif action == 'No_Crossing':
        Location = 'Traffic_Light_Red'
        Condition = random.choice(['Person_Present','Person_Absent'])
    # elif action == 'No_Crossing':
    #     Location = 'Traffic_Light_Yellow'
    #     Condition = random.choice(['Person_Present','Person_Absent'])
    else:
        Condition = 'Person_Absent'   
