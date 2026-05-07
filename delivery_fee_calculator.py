import math


chicken_price = 20000 * 2
hamburger_price = 5000 * 3
pizza_price = 21000 * 1

food_total = chicken_price + hamburger_price + pizza_price

total_delivery_cost = 0
base_fee = 0
extra_tip = 0
surcharge_rate = 1.0


print(f"[Author: Minwoo]")

while True:
    print("\n1. Apply Delivery Surcharge")
    print("2. Check Total Payment Amount")
    print("3. Exit")
    
    choice = input("Select an option: ")

    if choice == '1':
        while True:
            is_raining = input("Is it raining? (Y/N): ").upper()
            if is_raining in ['Y', 'N']:
                break
            print("Please enter 'Y' or 'N'.")
        
        dist = float(input("*** Enter delivery distance (km): ***: "))
        base_fee = 3000
        
        
        if dist > 2:
            extra_tip = math.ceil(dist - 2) * 1000
        else:
            extra_tip = 0
            
        
        if is_raining == 'Y':
            surcharge_rate = 1.17
        else:
            surcharge_rate = 1.00
            
        total_delivery_cost = int((base_fee + extra_tip) * surcharge_rate)
        
        print("\n[Delivery Cost Details]")
        print(f"Base Fee: {base_fee} KRW")
        print(f"Extra Distance Fee: {extra_tip} KRW")
        print(f"Surcharge Rate: {surcharge_rate:.2f}")
        print(f"Total Delivery Cost: {total_delivery_cost} KRW")

    elif choice == '2':
        total_payment = food_total + total_delivery_cost
        print(f"\n[Total Payment - {total_payment} KRW]")
        print(f"< Food Total - {food_total} KRW >")
        print(f" - Chicken: 20,000 * 2 = 40,000")
        print(f" - Pizza: 21,000 * 1 = 21,000")
        print(f" - Burger: 5,000 * 3 = 15,000")
        print(f"< Delivery Cost - {total_delivery_cost} KRW >")
        print(f" - Base Fee: {base_fee}")
        print(f" - Extra Distance Fee: {extra_tip}")
        print(f" - Surcharge Rate: {surcharge_rate:.2f}")

    elif choice == '3':
        print("Closing the program. Goodbye!")
        break

    else:
        print("\n**** Invalid input. Please select a number from the menu. ****\n")
