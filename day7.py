"""
--- Day 7: Some Assembly Required ---

This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates!
Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal
(a number from 0 to 65535). A signal is provided to each wire by a gate, another wire,
 or some specific value. Each wire can only get a signal from one source, but can provide
  its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together:
x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

123 -> x means that the signal 123 is provided to wire x.
x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason,
 you'd like to emulate the circuit instead, almost all programming languages (for example,
 C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456
In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

Your puzzle answer was 16076.

--- Part Two ---

Now, take the signal you got on wire a, override wire b to that signal, and reset the other
wires (including wire a). What new signal is ultimately provided to wire a?

Your puzzle answer was 2797.
"""

import re


def operation_and(a, b):
    return a & b


def operation_rshift(a, b):
    return a >> b


def operation_lshift(a, b):
    return a << b


def operation_or(a, b):
    return a | b


def operation_not(a):
    return (65535 + ~a) + 1


def parse_str(string_to_parse):
    var1, command, var2 = re.search('^([0-9a-z]+)?\s?(AND|OR|RSHIFT|LSHIFT|NOT)?\s?([0-9a-z]+)?$', string_to_parse).groups()
    return var1, var2, command

operations = {
    'AND': operation_and,
    'RSHIFT': operation_rshift,
    'LSHIFT': operation_lshift,
    'OR': operation_or,
    'NOT': operation_not,
}

data = open('day7.txt', 'r')
gates = {}
cache = {}

for op in data.readlines():
    parts = op.split('->')
    gates[parts[1].strip()] = parts[0].strip()


print(gates)

def calculate(item_to_calculate):
    if item_to_calculate in cache:
        return cache[item_to_calculate]

    try:
        # check if given item is digit
        # it this case we just return it
        value = int(item_to_calculate)
        return value
    except:
        pass

    gate_to_calculate = gates[item_to_calculate]
    var1, var2, command = parse_str(gate_to_calculate)

    if command:
        operation_func = operations[command]
        if var1 and var2:
            result = operation_func(calculate(var1), calculate(var2))
        else:
            result = operation_func(calculate(var2))
    elif var1 in gates:
        result = calculate(var1)
    else:
        result = int(var1)

    cache[item_to_calculate] = result

    return result

print(calculate('a')) # 2797
