Contact=[]
while True:
    a={}
    name=input("Enter your name: ")
    email=input("Enter your email: ")
    phone=input("Enter your phone number: ")
    a["name"]=name
    a["email"]=email
    a["phone"]=phone
    Contact.append(a)
    ch=input("Do you want to add more contacts? (yes/no): ")
    if ch.lower()=="yes":
        continue
    else:
        break
print("The contact list is: ",Contact)
a = input("Enter the email of the contact you want to search: ")
for i in Contact:
    for key in i.items():
        if key == a:
            print("The contact details are: ", i)
        
