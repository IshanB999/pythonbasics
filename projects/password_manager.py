
def add():
   account_name=input("Account name: ")
   password=input("password: ")

   with open("passfile.txt",'a') as f:
      f.write(account_name+","+password+"\n")

def view():
   with open("passfile.txt",'r')as f:
      for line in f.readlines():
         account_name,password=line.split(",")
         print("Acc_name: ",account_name,"  ","password: ",password)
      

while True:
 mode=input("Would you like to view or add passwords (add/view): ? and if you wanna quit input q   ").lower()
 if mode=="q":
    break
 if mode=="add":
    add()
 elif mode=="view":
    view()
 else:
    print("Invalid input")
    continue