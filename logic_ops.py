# IT 405L - Logic Programming
# Activity 1: Logical Operators and an Expression Evaluator


# STEP 2 - Logical Operators


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



# STEP 3 - Implication


def my_implies(a, b):
    if a == True:
        return b == True
    return True



# STEP 5 - Expression Evaluator


def evaluate(expr):
    # Base cases
    if expr == True:
        return True

    if expr == False:
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



# STEP 4 - Test all logical operators


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

print()



# STEP 6 - Test the evaluator


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



# STEP 7 - Expected failure


print()
print("=== STEP 7 - EXPECTED FAILURE ===")


#print(evaluate(("or", True, ("and", 1/0, False)))) 


# STEP 8 - Unbracketed Expression

print()
print("=== STEP 8 - UNBRACKETED EXPRESSION ===")

step8 = ("implies",
         ("not", True),
         ("or",
          True,
          ("and", False, ("not", True))))

print("Expression: not True implies True or False and not True")
print("Tuple:", step8)
print("Value:", evaluate(step8))


# STEP 9 - One Pair of Brackets

print()
print("=== STEP 9 - ONE PAIR OF BRACKETS ===")

step9 = ("or",
         ("not", ("implies", True, True)),
         ("and", False, ("not", True)))

print("Expression: not (True implies True) or False and not True")
print("Tuple:", step9)
print("Value:", evaluate(step9))


