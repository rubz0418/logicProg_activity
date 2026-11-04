
# IT405L - Logic Programming
# Activity 1: Logical Operators and an Expression Evaluator

#Logical Operators

def my_and(a, b):
    if a == True:
        return b == True
    return False


def my_or(a, b):
    if a == True:
        return True
    return b == True


def my_not(a):
    return a == False




#Implication Operator

def my_implies(a, b):
    if a == True:
        return b == True
    return True




#Test All Logical Operators

print("=== MY_AND ===")
print(True, True, my_and(True, True))
print(True, False, my_and(True, False))
print(False, True, my_and(False, True))
print(False, False, my_and(False, False))

print()

print("=== MY_OR ===")
print(True, True, my_or(True, True))
print(True, False, my_or(True, False))
print(False, True, my_or(False, True))
print(False, False, my_or(False, False))

print()

print("=== MY_NOT ===")
print(True, my_not(True))
print(False, my_not(False))

print()

print("=== MY_IMPLIES ===")
print(True, True, my_implies(True, True))
print(True, False, my_implies(True, False))
print(False, True, my_implies(False, True))
print(False, False, my_implies(False, False))



#Expression Evaluator

def evaluate(expr):
    # Base case
    if expr is True:
        return True

    if expr is False:
        return False

    # Get the operator
    op = expr[0]

    # Unary operator
    if op == "not":
        return my_not(evaluate(expr[1]))

    # Evaluate both operands
    left = evaluate(expr[1])
    right = evaluate(expr[2])

    # Binary operators
    if op == "and":
        return my_and(left, right)

    if op == "or":
        return my_or(left, right)

    if op == "implies":
        return my_implies(left, right)

    # Unknown operator
    raise ValueError("unknown operator: %r" % op)



#Test the Expression Evaluator

print()
print("=== EVALUATOR TESTS ===")

expr1 = ("and", True, False)
expr2 = ("or", True, False)
expr3 = ("not", False)
expr4 = ("implies", True, False)
expr5 = ("and", True, ("not", False))
expr6 = ("implies", ("or", False, True), False)

print("Test 1:", expr1, "=", evaluate(expr1))
print("Test 2:", expr2, "=", evaluate(expr2))
print("Test 3:", expr3, "=", evaluate(expr3))
print("Test 4:", expr4, "=", evaluate(expr4))
print("Test 5:", expr5, "=", evaluate(expr5))
print("Test 6:", expr6, "=", evaluate(expr6))




#Expected Failure

print()
print("=== EXPECTED FAILURE ===")

#print(evaluate(("or", True, ("and", 1/0, False))))





#Compare With and Without Brackets

print()
print("=== WITH BRACKETS ===")

with_brackets = (
    "and",
    (
        "or",
        ("implies", ("not", True), True),
        False
    ),
    ("not", True)
)

print("Expression: (((not True implies True) or False) and not True)")
print("Value:", evaluate(with_brackets))


print()
print("=== WITHOUT BRACKETS ===")

without_brackets = (
    "implies",
    ("not", True),
    (
        "or",
        True,
        ("and", False, ("not", True))
    )
)

print("Expression: not True implies True or False and not True")
print("Value:", evaluate(without_brackets))






#One Pair of Brackets

print()
print("=== ONE PAIR OF BRACKETS ===")

step9 = (
    "or",
    ("not", ("implies", True, True)),
    ("and", False, ("not", True))
)

print("Expression: not (True implies True) or False and not True")
print("Value:", evaluate(step9))

print("Was one pair enough to change the answer? Yes")





