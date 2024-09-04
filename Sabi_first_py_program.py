
print("Come on in!")

name = input("what's your name?\n")

if name == "Ben" or name== "Patricia":
    evil_status = input ("are u evil?")
    if evil_status == "yes":
     print("get out of here")
     exit()
    else:
       print ("come on in!")

menu = ("espresso, latte, cappucino")

print("hello " + name + ", this is what were having today in the menu. What would you like to drink?:\n"  + menu ) 

order = input ()


print (name + " we ll have that " + order + " ready for u in a second")

price = 2

if order == "latte": 
    price = 4
    extra = input("Do you want extra whipped cream?\n")
    if extra.lower() == "yes":
        price = 10 
    else: 
        price = 4

    print(f"The total price is ${price}.")

elif order == "espresso":
    price = 3
elif order == "cappucino":
    price = 5
else:
   print ("sorry, we don't have that here")
   price = 0

#print(price)

quantity = input("how many coffes would you like?\n")


total = price * int(quantity) 



print("Sound good," + "we'll have your " + " " + quantity + " " + order +  " in a moment")

print("here is your " + order + "." + " that will be $" + str (total)) 

#if name == "Ben":
    #print("get out of here")
    #exit()









