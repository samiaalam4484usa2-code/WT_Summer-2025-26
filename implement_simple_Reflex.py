def simple_reflex_agent(percept):
    print('Perception Received: '+ str(percept))
    location = percept[0]
    status = percept[1]
    if location =='Front' and status == "Person":
        action = "Back_Open"
    elif location == "Back" and status == "Person":
        action = "Front_Open"
    else:
        action = "No_Action"
    return action

import random
Location = random.choice(['Front','Back'])
Condition = random.choice(['Person','No_Person'])

while True:
    action= simple_reflex_agent((Location,Condition))
    print('Action Performed: '+ action)
    cmd = input('Get Perception (yes/no): ')
    if(cmd == 'no' or cmd != 'yes'): break
    if action == 'Back_Open':
        Location = 'Front'
        Condition = random.choice(['Person','No_Person'])
    elif action== 'Front_Open':
        Location = 'Back'
        Condition = random.choice(['Person','No_Person'])
    else:
        Condition = 'No_Action'   