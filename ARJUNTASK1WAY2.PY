'''
import psutil

# Function to get CPU and memory utilization
def get_cpu_memory_usage():
    cpu_percent = psutil.cpu_percent()
    virtual_memory = psutil.virtual_memory()
    memory_percent = virtual_memory.percent
    return cpu_percent, memory_percent

if __name__ == "__main__":
    # Start monitoring CPU and memory before running your code
    initial_cpu, initial_memory = get_cpu_memory_usage()

    # Your existing Python code goes here
         
    # End monitoring CPU and memory after running your code
    final_cpu, final_memory = get_cpu_memory_usage()

    # Calculate the difference to get the actual CPU and memory usage during the execution of your code
    cpu_usage = final_cpu - initial_cpu
    memory_usage = final_memory - initial_memory

    # Print the results
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")
'''

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
  if i=="l":
    break
