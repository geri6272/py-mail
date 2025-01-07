import json
import os
from pprint import pprint as pp
from time import sleep as s
n_exit = True

with open('settings.json', 'r') as file: 
    setting = json.load(file)

with open('data.json', 'r') as file2:
    data = json.load(file2)

def get_user():
    global user
    user = input("Enter your username: ")

def settings():
    for key in setting:
        print(f"{key} = {setting[key]}")
    edit = input("Enter the editable setting (use enter to skip): ")
    if edit in setting:
        setting[edit] = input("Enter the new value: ")
        with open('settings.json', 'w') as file:
            json.dump(setting, file)
        c = input("change anything else(y/n): ")
        if c.lower() == 'y':
            settings()
        else:
            return
    elif edit != "":
        print("Setting not found try again.")
        settings()

def get_id():
    return data["id"][user]  

def get_id_by_addres():
    global reciver
    reciver = input("Enter the reciver's address: (example@pymail.com): ").lower()
    print(reciver)
    if reciver in data["mails"]:
        return data["mails"][reciver]
    else:
        print("User not found try again.")
        return "error"

def refresh():
    with open('data.json', 'r') as file2:
        data = json.load(file2)

def send_messange():
    rec_id = get_id_by_addres()
    if rec_id != "error":
        message = input("Enter your message: ")
        with open('data.json', 'w') as file3:
            data["users"][rec_id]["mails"].append(message)
            data["users"][rec_id]["sender"].append(data["users"][get_id()]["name"])
            json.dump(data, file3, indent=4)
    else:
        print("the receiver didn't exist")

def register():
    username = input("select your mail username: ")
    if " " in username:
        print("for the easyer use dont use space in your username")
        register()
    surname = input("Enter your surname: ")
    name = input("Enter your name: ")
    email = input("Enter your email addres without @pymail.com: ")
    email = email + "@pymail.com"
    if username != "" and surname != "" and name != "" and email != "":
        with open('data.json', 'w') as file5:
            data["users"][len(data["users"]) + 1]["user_name"] = username
            data["users"][len(data["users"]) + 1]["surname"] = surname
            data["users"][len(data["users"]) + 1]["name"] = name
            data["users"][len(data["users"]) + 1]["email"] = email
            data["users"][len(data["users"]) + 1]["mails"] = []
            data["users"][len(data["users"]) + 1]["sender"] = []
            data["id"][username] = len(data["users"])
            data["mails"][email] = len(data["users"])
            json.dump(data, file5, indent=4)



def read_mail():
    os.system('cls||clear')
    id = get_id()
    if len(data["users"][id]["sender"]) <= int(setting["max_mails"]):
        for i in range(len(data["users"][id]["sender"])):
            print(f'{data["users"][id]["sender"][i] + " - " + data["users"][id]["email"]}:')
            print()
            print({data["users"][id]["mails"][i]})
            print("\n")
        ch = input("Press enter to menu")
        if ch == "":
            return
        else:
            print("error wrong input")
            read_mail()    
    else:
        for i in range(int(setting["max_mails"])):
            print(f'{data["users"][id]["sender"][i] + " - " + data["users"][id]["email"]}:')
            print()
            print({data["users"][id]["mails"][i]})


def log_in():
    if user in data["id"]:
        id = get_id()
        print(f'üdv {data["users"][id]["name"] + " " + data["users"][id]["surname"]}')
        print(f'önnek {len(data["users"][id]["mails"])} levele van')
        choice = input("1. send message\n2. read messages\n3. refresh\n4. exit\n")
        if choice == "1":
            send_messange()
        elif choice == "2":
            read_mail()
        elif choice == "3":
            refresh()
        elif choice == "4":
            exit()  
        else:
            print("Invalid choice try again.")
    else:
        register = input("Not found user, do you want create new? (y/n):")  
        if register.lower() == "y":  
            register()
        else:
            print("return to menu")
            s(2)
            return

def del_user():
    user_p = input("Enter your password if you are an admin: ")
    if setting["admin_pass"] == user_p:
        print("Admin mode")
        print("coming soon...")
        s(3)
        return
    else:
        print("acces denied")
        print("exited better code later...")  
        print("coming soon...")
        s(3)
        return

while n_exit == True:
    os.system('cls||clear')
    print("1. login/register")
    print("2. settings")
    print("3. delete user")
    print("4. exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        get_user()
        log_in()
    elif choice == "2":
        settings()
    elif choice == "3":
        del_user()
    elif choice == "4":
        exit()
    else:
        print("Invalid choice. Please try again.")


