def balance(expr):
    stack=[]
    for c in expr:
        if c in["(","[","{"]:
            stack.append(c)
        else:
            if not stack:
                return False
            cc=stack.pop()
            if cc=="(":
                if c!=")":
                    return False
            if cc=="[":
                if c!="]":
                    return False
            if cc=="{":
                if c!="}":
                    return False
    if stack:
        return False
    return True

expr=input("enter the expression")

if balance(expr)==True:
    print("balanced")
else:
    print(" not balanced")
