
# cars = ["Red car","Blue Car","Yellow car"]

#  #           0        1             2 

# print(cars)

# print (cars[0])  # Red Car 

# print (cars[1]) # Blue Car 

# print (cars[2]) # Yellow Car 


# cars.append("neeli car")

# print(cars)

# print(cars[3] )

# #-------------------------------------------------# 

# # Create a List of Grocery Items.

# shopping_list1 = ["Milk" , "Eggs" , "Bread" , "Butter"] 

# #Print the list

# print("Shoopping List:" , shopping_list1)

# # add items to list 

# shopping_list1.append("cheese")

# print(shopping_list1)


# # remove item from list 

# shopping_list1.remove("Milk") 

# print(shopping_list1)

# #------------------------------------------------------#
# #                       DICTIONARY                     #
# #-------------------------------------------------------#

# # Key and Value pair 

# Bande =    {   
            
# "Prateek" : 22,

# "Arjun" : 23,

# "Ram"  : 24, 

# "Name" : 'Prateek' ,

# "Umar" : 22 ,

# "Kam" : 'developer' 

# }

# print(Bande) 


# print ("Arjun ki age hai  : ", Bande["Arjun"] )

# print("Prateek ki age hai :  ", Bande["Prateek"])

# print(Bande["Name"])

# # adding key value to dictionary 

# Bande["sham"] = 34 


# print(Bande)

# print(Bande["sham"])  

# # remove a key and pair 

# del Bande["Arjun"] 

# print(Bande)

# Bande["Arjun"] = 34 


# print(Bande)

# Dictonary of Contacts withlist in it 

Contacts = {                                  
              "Arjun" : ["555-666-777" , "arjun@hotmail.com"] ,
 
             "Prateek" : [ "222-333-444" , "p@hotmail.com"]
             
             
}

print(" Arjun ka Phone number hai :   ", Contacts["Arjun"][0]   )


print(" Prateek ka email hai :   ", Contacts["Prateek"][1]     )


# add entry to the dict 

Contacts["Ram"] = ["333-222-111" , "ram@hotmail.com"] 

print(Contacts) 

# delete entry from Dictionary or one value for the key 

del Contacts["Arjun"][0] 

print(Contacts) 

Contacts["sham"] = 22

print (Contacts)



