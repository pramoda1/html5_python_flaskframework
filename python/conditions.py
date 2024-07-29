#if...else....elif

age=int(input("enter the age of the person"))
if age < 5:
    print("too young")
elif age == 5:
    print("kindrgreten")
elif age > 5 and age <= 17:
    grade = age - 5
    print("go to {}".format(grade))
else:
    print("goto college")


#nested if
# this program is check the positive 
# negetive or zero

n=int(input("enter the any number"))
if n >= 0:
    if n == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("negetive number")