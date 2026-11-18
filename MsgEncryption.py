def Menu():
    while True:
        print("==========MENU==========")
        print("(1) Encryption")
        print("(2) Decryption")
        print("(3) Quit")
        print("========================")
        user_input = input("Your option: (1/2/3)  ")
        print("========================")
        if user_input == "1":
            print("")
            print("--------Encryption-------")
            Encrypt()
        elif user_input == "2":
            Decrypt()
        elif user_input == "3":
            break
        else: 
            print("Invalid option.")
            print("")

def Encrypt():
    while True:
        print("")
        encrypt_input = input("Enter your message and shift: ")
        print("")
        try: 
            message, shift = [x.strip() for x in encrypt_input.split(",")]
            shift = int(shift)
            break
        except ValueError:
            print("Invalid input. Try again.")
            continue
    print("")
    new_message = []
    for i in message:
        new_index = ord(i) + shift
        new_message.append(chr(new_index))
    print(f"Encrypted message: {"".join(new_message)}")
    print("")

def Decrypt():
    while True:
        print("")
        decrypt_input = input("Enter your message and shift: ")
        print("")
        try: 
            message, shift = [x.strip() for x in decrypt_input.split(",")]
            shift = int(shift)
            break
        except ValueError:
            print("Invalid input. Try again.")
            continue
    print("")
    new_message = []
    for i in message:
        new_index = ord(i) - shift
        new_message.append(chr(new_index))
    print(f"Encrypted message: {"".join(new_message)}")
    print("")

Menu()
