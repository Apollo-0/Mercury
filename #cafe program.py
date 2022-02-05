#cafe program
import time
print("**************************************************")
print("Welcome to Cloudy Cafe!")
print()
time.sleep(1)

while True:
    print("""
    Please pick an option:
    a) Food Options
    b) Snack Options
    c) Desert Options
    d) Drink options
    Q) QUIT """)

    time.sleep(1)
    opt = input("Your option is: ")

    if opt == 'a':
        print("=========================================")
        print("You hav chosen: Food Options")
        print("=========================================")

    time.sleep(1)

    print("""
    1) Fried rice with egg
    2) Spaghetti Bolognese
    3) Beef Steak
    4)Chcken Salad
    """)

    time.sleep(1)
    fopt = input("Your Food Option is: ")

    time.sleep(1)
    if fopt == '1':
        print("+++++++++++++++++++++++++++++++++++++++++")
        print("You have chosen: Fried rice and egg")
        time.sleep(1)
        print("This will cost: £4.99")
        print("+++++++++++++++++++++++++++++++++++++++++")
        print()
        print("**************************************************")


    if fopt == '2':
        print("+++++++++++++++++++++++++++++++++++++++++")
        print("You have chosen: Spaghetti Bolognese")
        time.sleep(1)
        print("This will cost: £5.45")
        print("+++++++++++++++++++++++++++++++++++++++++")
        print()
        print("**************************************************")


    if fopt == '3':
        print("+++++++++++++++++++++++++++++++++++++++++")
        print("You have chosen: Beef Steak")
        time.sleep(1)
        print("This will cost: £5.00")
        print("+++++++++++++++++++++++++++++++++++++++++")
        print()
        print("**************************************************")


    if fopt == '4':
        print("+++++++++++++++++++++++++++++++++++++++++")
        print("You have chosen: Chicken Salad")
        time.sleep(1)
        print("This will cost: £4.90")
        print("+++++++++++++++++++++++++++++++++++++++++")
        print()
        print("**************************************************")

    breakpoint()


    if opt == 'b':
        print("=========================================")
        print("You hav chosen: Snack Options")
        print("=========================================")

    print("""
    1) Turkey Sandwiches
    2) French Fries
    3) Crossaint
    4) Fruit Salad""")

    sopt = input("Your Snack Option is: ")

    time.sleep(1)
    if sopt == '1':
        print("+++++++++++++++++++++++++++++++++++++++++")
        print("You have chosen: Turey Sandwiches")
        time.sleep(1)
        print("This will cost: £2.50")
        print("+++++++++++++++++++++++++++++++++++++++++")
        print()
        print("**************************************************")

    
    if sopt == '2':
        print("+++++++++++++++++++++++++++++++++++++++++")
        print("You have chosen: French Fries")
        time.sleep(1)
        print("This will cost: £2.10")
        print("+++++++++++++++++++++++++++++++++++++++++")
        print()
        print("**************************************************")


    if sopt == '3':
        print("+++++++++++++++++++++++++++++++++++++++++")
        print("You have chosen: Crossaint")
        time.sleep(1)
        print("This will cost: £1.50")
        print("+++++++++++++++++++++++++++++++++++++++++")
        print()
        print("**************************************************")

    
    if sopt == '4':
        print("+++++++++++++++++++++++++++++++++++++++++")
        print("You have chosen: French Fries")
        time.sleep(1)
        print("This will cost: £2.00")
        print("+++++++++++++++++++++++++++++++++++++++++")
        print()
        print("**************************************************")

    breakpoint()


    if opt == 'c':
        print("=========================================")
        print("You hav chosen: Desert Options")
        print("=========================================")

    print("""
    1) Ice Cream
    2) Caramel Cake
    3) Chocolate Brownie
    4) Strawberry Donut""")

    dopt = input("Your Desert Option is: ")

    time.sleep(1)
    if dopt == '1':
        print("+++++++++++++++++++++++++++++++++++++++++")
        print("You have chosen: Ice Cream")
        time.sleep(1)
        print("This will cost: £1.90")
        print("+++++++++++++++++++++++++++++++++++++++++")
        print()
        print("**************************************************")

    
    if dopt == '2':
        print("+++++++++++++++++++++++++++++++++++++++++")
        print("You have chosen: Caramel Cake")
        time.sleep(1)
        print("This will cost: £2.00")
        print("+++++++++++++++++++++++++++++++++++++++++")
        print()
        print("**************************************************")


    if dopt == '3':
        print("+++++++++++++++++++++++++++++++++++++++++")
        print("You have chosen: Chocolate Brownie")
        time.sleep(1)
        print("This will cost: £1.50")
        print("+++++++++++++++++++++++++++++++++++++++++")
        print()
        print("**************************************************")

    
    if dopt == '4':
        print("+++++++++++++++++++++++++++++++++++++++++")
        print("You have chosen: Strawberry Donut")
        time.sleep(1)
        print("This will cost: £1.90")
        print("+++++++++++++++++++++++++++++++++++++++++")
        print()
        print("**************************************************")

    breakpoint()



    if opt == 'd':
        print("=========================================")
        print("You hav chosen: Drink Options")
        print("=========================================")

    print("""
    1) Milkshake
    2) Smoothie
    3) Hot Chocolate
    4) Ice Tea
    5) Soda""")

    sopt = input("Your Drink Option is: ")
    
    #Putting bopt instead of dopt because then we'd have two and it would get mixed up with drink and desert
    #The b in bopt just stands for beverage instead

    time.sleep(1)
    if bopt == '1':
        print("+++++++++++++++++++++++++++++++++++++++++")
        print("You have chosen: Milkshake")
        time.sleep(1)
        print("This will cost: £2.50")
        print("+++++++++++++++++++++++++++++++++++++++++")
        print()
        print("**************************************************")

    
    if bopt == '2':
        print("+++++++++++++++++++++++++++++++++++++++++")
        print("You have chosen: Smoothie")
        time.sleep(1)
        print("This will cost: £2.45")
        print("+++++++++++++++++++++++++++++++++++++++++")
        print()
        print("**************************************************")


    if bopt == '3':
        print("+++++++++++++++++++++++++++++++++++++++++")
        print("You have chosen: Hot Chocolate")
        time.sleep(1)
        print("This will cost: £2.50")
        print("+++++++++++++++++++++++++++++++++++++++++")
        print()
        print("**************************************************")

    
    if bopt == '4':
        print("+++++++++++++++++++++++++++++++++++++++++")
        print("You have chosen: Ice Tea")
        time.sleep(1)
        print("This will cost: £2.00")
        print("+++++++++++++++++++++++++++++++++++++++++")
        print()
        print("**************************************************")

    
    if bopt == '5':
        print("+++++++++++++++++++++++++++++++++++++++++")
        print("You have chosen: Soda")
        time.sleep(1)
        print("This will cost: £1.10")
        print("+++++++++++++++++++++++++++++++++++++++++")
        print()
        print("**************************************************")

    breakpoint()