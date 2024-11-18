import os
import baset  
import addres  
import getpass 

def main():
    services = [
        {"name": "Switch between bases", "action": baset.swith},  
        {"name": "IP Addressing", "action": addres.ip_add}
    ]
    
    print("We have the following services:")
    for i, service in enumerate(services, 1):
        print(f"{i}. {service['name']}")
    
    try:
        choice = int(input("Enter the number corresponding to your choice: "))
        if 1 <= choice <= len(services):
            services[choice - 1]["action"]() 
        else:
            print("Invalid choice. Please select a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


u = input("Enter username: \n")
p = getpass.getpass("Enter password: \n")  #hide the password 
namex = u + ".txt"

if os.path.exists(namex):
    with open(namex, "r") as file:
        lines = file.readlines()

    if u + "\n" in lines and p + "\n" in lines:
        print("Login successful!")
        if __name__ == "__main__":
            main()
    else:
        print("Invalid username or password.")
else:
    print("You are a new user:")
    print(f"Your username: {u}, Your password: {p}")
    with open(namex, "w") as file:
        file.write(u + "\n")
        file.write(p + "\n")
        file.write("0\n")
