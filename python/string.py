ab='pramod'
print(ab)
ac="pramod"
print(ac)
# tripple qouts  string can extend multiple line
ad='''hi every one my 
self pramod'''
print(ad)

#acess the characters in the string using slicing method
string="pramoda"
print(string)
print(string[1:])
print(string[:5])
print(string[-1])
print(string[-1:-3])
print(string[0])


#string are immutable but diffrent string can be assigned
str1="pramod"
print(str1)
str1="uday"
print(str1)
# str1[1]="x"

#concatination in string
#using +
print("string+str1-->",string+str1)
#using *
print("string*3 -->",string*3)

#iterating through the proble is count the l in "hello world"
str2="HELLO WORLD"
letter_coount=0
for letters in str2:
    if letters=="L":
        letter_coount+=1
print("the numberof in helo world -->",letter_coount)

#membership
print("L" in str2)
print("l" not in str2)

#built-in function
en=list(enumerate(str2))
print("enumarat of str2 is ",en)
print(len(str2))

#escape sequence
print(''' hi every one''')
print('''what "is\' u"''')
print(" what is 'your\'s name '")
print("c:\\user")
print("my name is \npramod")
print('my name is \t pramod')
print("the 10  hex  represention is \x41")


#format method()

# 1.default method 
default_method="{} and {}".format('pramod','uday')
print(default_method)
#2 positional order method
positional_order="{1} and {0}".format('pramod','uday')
print(positional_order)
#3.order using keyword arguments
keyword_order="{i} and {j}".format(i='pramod',j='uday') 
print(keyword_order)


#string methods
print("hell good morning".lower())
print("hell good morning".upper())
print("hell good morning".find("he"))
print("hello good morning".replace("hello","hi"))
