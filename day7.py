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
