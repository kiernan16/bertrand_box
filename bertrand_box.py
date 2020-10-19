#!/usr/bin/env python3
import random

box_A = ["G","G"] #not needed, only for demostration
box_B = ["G","S"]
box_C = ["S","S"] #not needed, only for demostration

x = 0
gold_picked = 0

while x < 10000:
    pick_box = random.randrange(0,3)
    
    if pick_box == 0:
        gold_picked += 1
        x += 1
        
    elif pick_box == 1:
        pick = random.randrange(0,2)
        
        if box_B[pick] == "G":
            x += 1
            
    elif pick_box == 2:
        continue
    
    if x % 1000 == 0 and not x == 0:
        percent = (gold_picked/x) * 100
        formatted_percent = round(percent, 2)
        print("{x} - Gold picked: {percent}%".format(x=x,percent=formatted_percent))