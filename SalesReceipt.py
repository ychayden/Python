
Record = {}

def Input():
    print("==================================================")
    print("INPUT: ITEM, PRICE, QUANTITY. (enter DONE to quit)")
    print("==================================================")
    while True:
        print("")
        user_input = input("INPUT:")
        if user_input.upper() == "DONE":
            break
        try:
            item, price, quantity = [i.strip() for i in user_input.split(",")]
            price = float(price)
            quantity = int(quantity)
        except ValueError:
            print("")
            print(f"SKIPPED: {user_input}")
            continue
        key = item.upper()
        if key in Record:
            Record[key][0] += price
            Record[key][1] += quantity
        else:
            Record[item.upper()] = [price, quantity]

def Discount():
    for key, values in Record.items():
        if values[1] >= 20:
            values[0] = round((values[0] * 0.95),2)
        elif values[1] >= 50:
            values[0] = round((values[0] * 0.9),2)

def Print():
    print("")
    print("====================SALES RECEIPT====================") 
    for key, values in sorted(Record.items()):
        price_2 = f"${values[0]:.2f}"
        print(f"{key:<12}                         {price_2:>10} {values[1]:>4}")

Input()
Discount()
if not Record == {}:
    Print()


    

        
            

