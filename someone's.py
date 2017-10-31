import numpy as np
import re

ins_pat = re.compile("([a-z ]+)?([0-9]+),([0-9]+)[a-z ]+?([0-9]+),([0-9]+)")

TURN_ON = "turn on"
TURN_OFF = "turn off"
TOGGLE = "toggle"

class Instruction():
    def __init__(self,what,x1,y1,x2,y2):
        self.what = what
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

def parse_ins(ins):
    what,x1,y1,x2,y2 = ins_pat.findall(ins)[0]
    x1,y1,x2,y2 = map(int, [x1,y1,x2,y2])
    x1,x2 = sorted([x1,x2])
    y1,y2 = sorted([y1,y2])
    what = what.strip()
    return Instruction(what,x1,y1,x2,y2)

def apply_instructions(instructions):
    instructions = map(parse_ins, instructions)
    lights = np.zeros((1000,1000),dtype=np.int)
    lights.fill(-1)
    for ins in instructions:
        if ins.what == TURN_ON:
            lights[ins.x1:(ins.x2+1),ins.y1:(ins.y2+1)] = 1
        elif ins.what == TURN_OFF:
            lights[ins.x1:(ins.x2+1),ins.y1:(ins.y2+1)] = -1
        elif ins.what == TOGGLE:
            lights[ins.x1:(ins.x2+1),ins.y1:(ins.y2+1)] *= -1
        print (lights==1).sum()
    return lights

def apply_instructions2(instructions):
    instructions = map(parse_ins, instructions)
    lights = np.zeros((1000,1000),dtype=np.int)
    lights.fill(0)
    for ins in instructions:
        if ins.what == TURN_ON:
            lights[ins.x1:(ins.x2+1),ins.y1:(ins.y2+1)] += 1
        elif ins.what == TURN_OFF:
            lights[ins.x1:(ins.x2+1),ins.y1:(ins.y2+1)] -= 1
            lights[lights < 0] = 0
        elif ins.what == TOGGLE:
            lights[ins.x1:(ins.x2+1),ins.y1:(ins.y2+1)] += 2
        print (lights).sum()
    return lights


instructions = open("day6.txt").readlines()
lights = apply_instructions(instructions)
# lights = apply_instructions2(instructions)

b = np.array([[0, 1, 2, 3],
            [10, 11, 12, 13],
              [20, 21, 22, 23],
              [30, 31, 32, 33],
              [40, 41, 42, 43]])

b[2:4, 1:3] = 0
print(b[:,2])  # The third column

print(b)