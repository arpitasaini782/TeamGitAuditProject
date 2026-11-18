a=int(input("enter no."))
b=int(input("enter no."))
sign=input(" sum, multi,sub,divi")
if sign=="sum":
    print(a+b)
elif sign =="multi":
    print(a*b)
elif sign == "divi":
    print(a/b)
elif sign=="sub":
    print(a-b)
else:
    print("error ")