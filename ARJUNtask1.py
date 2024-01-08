def getCPUuse():
    #return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip(\
)))

print(getCPUuse())
acc_no = int(input("enter account account no"))
Balance= float(input("enter current balance"))
#transaction_amount = input("enter amount of transaction")
for i in "loop":
 option =int(input("enter 1 for deposit: enter 2 for withdrawl:"))


 if option == 1:
  Deposit=int(input("enter amount to deposit"))
  print("deposited amount:",Deposit)
  Balance= Balance+ Deposit
  print("Total balance:", Balance)
 elif option == 2:
  withdraw=int(input("enter amount to withdraw"))
  if(Balance< withdraw):
   print("withdraw amount exceeded balance")
  else:
   Balance= Balance- withdraw
   print("Total balance:", Balance)
 else:
  print("choose correct option")
  if i=="p":
    break


 

 
