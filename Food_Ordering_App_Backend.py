# ADMIN SECTION
import pandas as pd
d1=({'Name':['Tandoori Chicken','Vegan Burger','Truffle Cake'],                 # lists of food storing using pandas 
                       'Quantity':['4 pieces','1 Piece','500gm'],
                       "Price":[240,320,900],
                       'Discount':[10,0,20],
                       'Stock':[8,15,20]})
df1=pd.DataFrame(d1)


def add_food_items(df1):                                                  # function for add food items by admin
    print(df1)
    print("You are going to add\n")
    food=input("Food:")
    quantity=input("Quantity:")
    price=int(input("Price:"))
    discount=int(input("Discount in percentage:"))
    stock=int(input("Stock:"))
    
    d=pd.DataFrame({'Name':food,'Quantity':quantity,"Price":price,'Discount':discount,'Stock':stock},index=[0])
    
    df1=pd.concat([df1,d],ignore_index=True)                            # appending with previous list which is dataframe
    
    row,col=df1.shape
    for i in range(row):                                  
      df1['FoodID'][i]=i+1                                             # adding food_id automatically
   
    print(df1)                                                         # showing last list to the admin

def edit_food(df1):                                                    # function for edit food items
    
    foodid=int(input("Enter FooID : "))
    
    print(df1[df1.FoodID==foodid])
    change=input("What do you want to change(Name,Quantity,Price,Discount,Stock): ").lower()    #asking user which is to be edited(name,quanity....)
    if change=='name':
        name=input("Enter the new name of food: ")
        d=df1[df1.FoodID==foodid]['Name']
        df1.loc[foodid-1,'Name']=name
        print(df1)
    elif change=='quantity':
        name=input("Enter the new quantity of food(ex:1p,400ml...): ")
        d=df1[df1.FoodID==foodid]['Quantity']
        df1.loc[foodid-1,'Quantity']=name
        print(df1)
    elif change=='price':
        name=int(input("Enter the new price of food: "))
        d=df1[df1.FoodID==foodid]['Price']
        df1.loc[foodid-1,'Price']=name
        print(df1)
    elif change=='discount':
        name=int(input("Enter the new discount: "))
        d=df1[df1.FoodID==foodid]['Discount']
        df1.loc[foodid-1,'Discount']=name
        print(df1)
    else:
        name=int(input("Enter the new stock: "))
        d=df1[df1.FoodID==foodid]['Stock']
        df1.loc[foodid-1,'Stock']=name
        print(df1)                                                              #will show the last list to admin
def view_list_of_food(df1):                                             # function for view the list
  print(df1)
def remove_item(df1):                                                   #function for removing food item
  
  print("You have these food items :")
  print(df1['Name'])
  name=input("Enter the food item to remove(Enter the food item exactly how it shows in table) : ")
  i=df1[df1['Name']==name].index
  df=df1.drop(i)
  print(df)                                                             #showing last remaining list

# USER SECTION
import pandas as pd
d1=({'Name':['Tandoori Chicken','Vegan Burger','Truffle Cake'],
                       'Quantity':['4 pieces','1 Piece','500gm'],
                       "Price":[240,320,900],
                       'Discount':[10,0,20],
                       'Stock':[8,15,20]})
df1=pd.DataFrame(d1)
import datetime
dicti={"almas":['Almas','1234567890','almas@gmail.com','Ghandhi Nagar']}        # dictionary for storing password as key and other details as value in list
passwords=["almas","al1"]                                                       # list of passwords
lists=[]
def register():                                                                 #function for register by user
  print("Register here")
  name=input("Enter your Full Name : ")
  phone=input("Enter your phone number : ")
  if len(phone)!=10:
    print("Enter valid phone number")
    phone=int(input("Enter your phone number : "))
  email=input("Enter your email address : ")
  address=input("Enter your Address : ")
  password=input("Enter password : ")
    
  
  if password not in passwords:
    passwords.append(password)                                            # appending new password to list
  else:
    print("Sorry ... This password is already existed ")
    
  dicti[password]=[name,phone,email,address]                              # appending new details to dictionary
  
  print("Registered Successfully")
  return dicti,passwords
def log_in():                                                             # function for login
  print("Login here")
  p=input("Enter password : ")
  if p in passwords:
    print("You have logged in successfully")
    print("You have three options :\n1.Place New Order\n2.Order History\n3.Update Profile\n")
    num=int(input("You just need to enter corresponding numbers for choosing any one of options : "))
    if num==1:
      place_new_order()
    elif num==2:
      order_history()
    elif num==3:
      update_profile()
    else:
      print("You have entered invalid number")

def place_new_order(total=0,lists=[]):                          #function for place order
  global now
  
  # df1.insert(0, 'FoodID', range(1, 1 + len(df1)))
  
  now = datetime.datetime.now()
  print("The food we providing are : ")
  length=df1['FoodID'].max()
  for i in range(length):
    print(df1['Name'][i],"(",df1['Quantity'][i],")","[INR",df1['Price'][i],"]")
  order=input("Order food by their corresponding number(like 1,2) : ").split(",")
  
  orders=[int(i)-1 for i in order]
  print(orders)
  print("You have ordered : ")
  for i in orders:
    lists.append([df1['Name'][i],df1['Quantity'][i],df1['Price'][i]])
    print(df1['Name'][i],"of",df1['Quantity'][i],"and the price is",df1['Price'][i])

  for i in range(len(orders)):
    total=total+df1['Price'][i+1]
  print("Your total bill is :",total)
  yesno=input("Do you want to order more(y/n) : ").lower()
  if yesno=='y':
    place_new_order(total,lists)
  else:
    print("Thanks")
    order_history(lists)
    exit()
  return now
  
def order_history(lists=[]):                                        # function for printing order history
  if not lists:
    print("You have not oredered anything yet")
  else:
    print("You have ordered\n\n")
    print(now,"\n\n",lists)
def update_profile():                                               # function for updating
  passw=input("Enter your password : ")
  if passw in passwords:
    print("Your details are :\nName :",dicti[passw][0],"\nPhone Number :",dicti[passw][1],"\nEmail Address :",dicti[passw][2],"\nAddress :",dicti[passw][3])
    update=input("What do you need to update [N] --> Name, [P] --> Phone Number, [E] --> Email Address, [A] --> Address, [NO] --> None :").lower()
    if update == 'n':
      name=input("Enter your updated name : ")
      dicti[passw][0]=name
    elif update == 'p':
      name=input("Enter your updated phone number : ")
      dicti[passw][1]=name      
    elif update == 'e':
      name=input("Enter your updated email address : ")
      dicti[passw][2]=name  
    elif update == 'a':
      name=input("Enter your updated phone number : ")
      dicti[passw][3]=name
    elif update == 'no':
      yn=input("Then do you need to change password(y/n) :").lower()
      if yn=='y':
        password()
      else:
        exit()
    else:
      print("You have entered wrong option")
def password():
  passw=input("Enter your password again : ")
  
  if passw in passwords:
    new=input("Enter your new password : ")
    index=passwords.index(passw)
    passwords[index]=new
    dicti[new]=dicti[passw]
    del dicti[passw]
    print("Your new password and details are :",dicti) 
  else:
    print("This password is not existing")


# MAIN SECTION

import pandas as pd
d1=({'Name':['Tandoori Chicken','Vegan Burger','Truffle Cake'],
                       'Quantity':['4 pieces','1 Piece','500gm'],
                       "Price":[240,320,900],
                       'Discount':[10,0,20],
                       'Stock':[8,15,20]})
df1=pd.DataFrame(d1)
df1.insert(0, 'FoodID', range(1, 1 + len(df1)))
print("\t\t\t\t*****************************WELCOME TO VIATA FOOD ORDERING APP*****************************\t\t\t\t")
au=input("\nCan you tell us whether you are Admin or User : ").lower()
if au=='admin':
  print("The food items are :\n")
  print(df1)
  df1.drop(['FoodID'],axis=1)
  select=int(input("Do you need to \n1. Add Food Item\n2. Edit Food Item\n3. View whole list of Food\n4. Remove a Food Item(Only enter corresponding number) : "))
  if select==1:
    add_food_items(df1)
  elif select==2:
    edit_food(df1)
  elif select==3:
    view_list_of_food(df1)
  elif select==4:
    remove_item(df1)
  else:
    print("You have entered wrong number")
elif au=='user':
  reg=input("Are you new here (y/n) :").lower()
  if reg=='y':
    register()
    log_in()
  else:
    log_in()
