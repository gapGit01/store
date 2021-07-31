Itoms = {"apple":20, "milk":30, "banana":20, "pepar":10, "coffe":20, "speaker":100,
        "mouse_pad":40, "book":20, "cake":30, "keybord":90, "a":10, "s":20, "d":50}


customer_inputs = ""
another_itom =""
count = 0
n = 0
stop = "ok"
stop2 = "that's it"
stop3 = "That's it"


while True:

    if customer_inputs != stop:
        customer_inputs = str(input("Enetr your food itom: ")).lower()

        if customer_inputs != stop and stop2 and stop3:
            pass
            quantity = int(input(f"How many {customer_inputs} you wont: "))

        if customer_inputs == (stop2 or stop3):
            print(f"\n you'er total Payment is R.S {count}\n Thank you come again!!!!\n")
            break



    if customer_inputs in Itoms:
        count = count + (quantity * (Itoms[customer_inputs])) 
        n = n + 1

    elif customer_inputs == stop:
        print(f"Total Payments R.S {count}\nThank you come again!!!!")
        print("-----------------------------------------------------------")
        break

    else:
        print(f"{customer_inputs} is out of stocke")
        print(f"Total Payments R.S {count}")

