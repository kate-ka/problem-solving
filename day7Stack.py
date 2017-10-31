from pprint import pprint
import re


def operation_and(a, b):
    return a & b


def operation_rshift(a, b):
    return a >> b


def operation_lshift(a, b):
    return a << b


def operation_or(a,b):
    return a | b


def operation_not(a):
    return (65535 + ~a) + 1


def parse_command(str_to_parse):
    var_one, command, var_two = re.search(
        '^([a-z0-9]+)?\s?(AND|OR|LSHIFT|RSHIFT|NOT)?\s?([a-z0-9]+)?$',str_to_parse).groups()
    return var_one, var_two, command



operations = {
    'AND': operation_and,
    'RSHIFT': operation_rshift,
    'NOT': operation_not,
    'OR': operation_or,
    'LSHIFT': operation_lshift
}

data = open('day7.txt', 'r')
gates = {}
cache = {}

for op in data.readlines():
    parts = op.split('->')
    gates[parts[1].strip()] = parts[0].strip()


def check_if_int(item):
    try:
        int(item)
        return True
    except:
        return False


def add_to_stack(item_to_calculate, stack):
    gate_to_calcuate = gates[item_to_calculate]
    #print '%s -> %s' % (gate_to_calcuate, item_to_calculate)
    var1, var2, command = parse_command(gate_to_calcuate)
    stack.append((item_to_calculate, var1, var2, command))

def calculate(item_to_calculate):
    results = {}

    stack_to_calculate = []
    add_to_stack(item_to_calculate, stack_to_calculate)

    while stack_to_calculate:
        # print stack_to_calculate

        item_to_calculate, var1, var2, command = stack_to_calculate[-1]

        value1 = None
        can_run_command = True

        if var1:
            if not check_if_int(var1) and var1 not in results:
                add_to_stack(var1, stack_to_calculate)
                can_run_command = False
            elif var1 in results:
                value1 = results[var1]
            else:
                value1 = int(var1)

        value2 = None
        if var2:
            if not check_if_int(var2) and var2 not in results:
                add_to_stack(var2, stack_to_calculate)
                can_run_command = False
            elif var2 in results:
                value2 = results[var2]
            else:
                value2 = int(var2)

        if can_run_command:
            command_args = []

            if value1 is not None:
                command_args.append(value1)
            if value2 is not None:
                command_args.append(value2)

            if command:
                results[item_to_calculate] = operations[command](*command_args)
            else:
                results[item_to_calculate] = command_args[0]

            stack_to_calculate.pop()

    return results[item_to_calculate]






# print calculate('a')







