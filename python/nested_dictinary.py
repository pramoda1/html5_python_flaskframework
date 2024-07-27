# declaring ad defining nested dictinary 
# 
people={1:{"name":"john","age":20,"sex":"male"},
       2:{"name":"marie","age":21,"sex":"female"}}
print(people) 

# acccesing the element  to a dictionary

print(people[1]["name"])
print(people[2]["name"])
print(people[1]["age"])


#addingg nested dictionary

people[3]={"name":"pramod","age":21,"sex":"male"}
print(people[3])
print(people)

#deleting distinary elements

print(people[3])
del people[3]["sex"]
print(people[3])

#Itering through a nested distinary

print(people.items())

for p_id, p_info in people.items():
    print("\n person id :",p_id)

    for key in p_info:
        print(key + ':',p_info[key])