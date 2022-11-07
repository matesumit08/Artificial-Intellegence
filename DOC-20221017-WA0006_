# function for logical AND
def logical_AND(a, b):
    return a and b

# function for logical OR
def logical_OR(a, b):
    return a or b

# function for implies case
def logical_Implies(a, b):
    return logical_OR(not a, b)

# defining a dictionary for logical symbols
OPERATION = {"^": logical_AND, "v": logical_OR, "=>": logical_Implies}

# Function of solve any form of expression of two variables with ~ ^ v =>
def solve(exp, values):

    length_exp = len(exp)

    left = ""
    right = ""
    operation = ""

    # Edge Cases
    if length_exp == 1:
        return values[exp[0]]
    elif length_exp == 2:
        return str((int(values[exp[1]]) + 1) % 2)

    # Extract left part of expression and the operation to perform
    idx = 0
    while idx < length_exp:
        if exp[idx] == "^" or exp[idx] == "v" or exp[idx] == "=":
            operation = exp[idx]
            break
        left += exp[idx]
        idx += 1
    idx += 1

    if exp[idx] == ">":
        operation += exp[idx]
        idx += 1

    # Extract right part of expression
    while idx < length_exp:
        right += exp[idx]
        idx += 1

    # Check for negation
    if left[0] == "~":
        left_value = str((int(values[left[1]]) + 1) % 2)
    else:
        left_value = str((int(values[left[0]])) % 2)

    if right[0] == "~":
        right_value = str((int(values[right[1]]) + 1) % 2)
    else:
        right_value = str((int(values[right[0]])) % 2)

    res = OPERATION[operation](int(left_value), int(right_value))
    return str(int(res))


def simplify(expressions, values):

    # Convert expressions to expressions of two variables and solve them one by one for current values
    stack = []
    for i, c in enumerate(expressions):
        if c == ")":
            exp = []
            while stack[-1] != "(":
                exp.append(stack.pop())
            stack.append(solve(exp[::-1], values))
        else:
            stack.append(c)

    # Check for result
    if stack[-1] == "1":
        return True
    return False

# function for splitting clauses
def split_clauses(expressions, values):
    stack = []
    index = 0

    # Split right and left part using stack
    for i, c in enumerate(expressions):
        if c == ")":
            stack.pop()
            if len(stack) == 0:
                index = i
                break
        elif c == "(":
            stack.append(c)

    if "=>" in expressions:

        left = expressions[: index + 1]
        right = expressions[index + 3 :]

        # Check for implication (p->q is not a theorem if p is true and q is false)
        if simplify(left, values):
            if not simplify(right, values):
                return "Not Theorem"


# Main function starts from here
if __name__ == "__main__":
    flag = 0
    expressions = str(input("Enter an expression: "))

    # Extract all variables present (Only alphabets from A to Z allowed in input)
    variable = set([x for x in expressions if x not in ["=", ">", "~", ")", "(", "^", "v"]])

    # All possible combinations of 0's and 1's
    for i in range(2 ** len(variable)):
        values = {}

        values["0"] = "0"
        values["1"] = "1"

        # generate binary of i of fixed length equal to len(variable)
        temp = format(i, "0" + str(len(variable)) + "b")

        for idx, c in enumerate(variable):
            values[c] = temp[idx]
        if split_clauses(expressions, values) == "Not Theorem":
            flag = 1

    if flag:
        print("Result: Its not a Theorem")
    else:
        print("Result : Its a Theorem")
