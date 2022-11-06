
def logical_AND(a, b):                            # function for logical AND
    return a and b

def logical_OR(a, b):                             # function for logical OR
    return a or b

def logical_Implies(a, b):                        # function for implies case
    return logical_OR(not a, b)

def notcheck(ch,stack):                           # Function to check and handle not(~) operator
        try:
            s = stack[-1]
            return True if s == '~'else False
        except IndexError:
            return False
def intopost(exp):                                 # Function to Infix expression to Postfix expression
    op = []
    st = []
    for o in exp:
        if o not in ['v','^','>','~','(',')']:
            op.append(o)  
        elif o == ')':
            while st[-1] != '(':
                a = st.pop()
                op.append(a) 
            st.pop()
        else:
            while notcheck(o,st):
                op.append(st.pop())
            st.append(o)      
    while len(st) != 0:
        op.append(st.pop())
    return op

def solve(exp,values):
    OPERATION = {"^": logical_AND, "v": logical_OR, ">": logical_Implies}  #dictionary for operations for symbols
    st = []
    for ch in exp[:-1]:
        if ch == '~':                                       #condition perform not operation
            a = st.pop()
            result = not(a)
            st.append(result)
        elif ch in ['v','^','>','(',')']:                   #condition to perform  operation and store result
            b = st.pop()                                    # into stack
            a = st.pop()
            result = OPERATION[ch](a,b)
            st.append(result)
        else:
            st.append(values[ch])
    return st

def main():
    # expression = input('Enter Expression: ')
    expression = '(P>Q)>((~Q>P)>Q)'
    # expression = 'P>(PvQ)'
    # expression = '(P^Q)>(PvR)'
    exp = intopost(expression)                          #convert expression into postfix form
    operators = set([x for x in expression if x not in [">", "~", ")", "(", "^", "v"]]) 
    flag = 0                                            # identifying all operators
    for i in range(2 ** len(operators)):                # generating all possible combinations of models  
        temp = format(i, "0" + str(len(operators)) + "b")         #Converting Integer into binary format
        values = {}
        values[0] = 0
        values[1] = 1
        for idx, c in enumerate(operators):
                values[c] = int(temp[idx])
        if solve(exp, values) == [1, 0]:               #False condition check for implication
                flag = 1
    print('Given expression is Not Therom ') if flag ==1 else print('Given expression is Therom')
main()
