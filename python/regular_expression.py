import re

# search the word in a line
if re.search('pramod1','i am pramod'):
    print("pramod is found")
else:
    print("pramod is not found")


# find all matches using findall() method
li=re.findall("ape","ape what was the apex and apexing,inape")
for i in li:
    print(i)


#finditer return iter of matching objects
#you can use span to get the location

thestr = "the ape was at the apex"
for i in re.finditer("ape",thestr):
    #span return the tuple
    loctuple=i.span()
    print(loctuple)

    #slice the match out using tuple values

    print(thestr[loctuple[0]:loctuple[1]])


#---------------match 1 of several letters-------------
#squre brackets will match any one of the   charater between
#the brackets not including upper and lowercase verties

lo="cat rat mat fat"
allanimals=re.findall("[crmfp]at",lo)#onother expression is [c-m ,C-M].at
# ^ denoted any character match but whatewer inside the brackets [^cr].at
for i in allanimals:
    print(i)
print()

#

#replace matching item using compile and sum methods
owlfood="cat rat pat mat"
print(owlfood)
regex=re.compile("[cr]at")
owlfood=regex.sub("owl",owlfood)
print(owlfood)

# match any charcter with dot
#findall([.\.]) . -> is any charcter
#                \. ->is dot

long = '''this 
is  a long 
string that
goes to on for many
lines'''
print(long)

regex=re.compile("\n")
long=regex.sub(" ",long)
print(long)

#serarch multiple numbers

number='123,1234,12345,123456'
print("matches : ",re.findall("\d{5,6}",number))

#match any single character aor any number
#\w is the same as [a-zA-Z0-9_]

phone="123-456-7890"
if re.search("\w{3}-\w{3}-\w{4}",phone):
    print("the phone number is",phone)


#white space
# \s is same as the  [\f\n\n\t\t\v]

if re.search("\w{2,10}\s\w{2,20}","toshiba maramastu2"):
    print("it is valid name")


# + matches one are more times
email="prmodhs418@gamil.com"
print("the gmail is ",re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[a-zA-Z]{2,3}",email))