cars = {
    '1': {"name": "Hyundai Creta", "availability_status": "yes", "per_day_rent": 3000},
    '2': {"name": "Tata Nexon", "availability_status": "yes", "per_day_rent": 2000},
    '3': {"name": "Toyota Fortuner", "availability_status": "yes", "per_day_rent": 5000},
    '4': {"name": "Hyundai Aura", "availability_status": "yes", "per_day_rent": 3000},
    '5': {"name": "Toyota Innova", "availability_status": "yes", "per_day_rent": 5000}
}
def book_a_car():
    user_name = input("enter your name: ")
    for car_id, car_info in cars.items():
        print(f"car number: {car_id}, name: {car_info['name']}, rent: ₹{car_info['per_day_rent']}, availability status: {car_info['availability_status']}")
        print()
    car_no = input("enter car number (1-5): ")
    if car_no not in cars:
        print("invalid car number.")
        return
    if cars[car_no]["availability_status"] == "no":
        print("sorry, this car is already booked.")
        return
    try:
        days = int(input("enter how many days you want the car: "))
    except ValueError:
        print("invalid input. please enter days as a number.")
        return
    if days <= 0:
        print("days must be at least 1.")
        return
    amount = days * cars[car_no]["per_day_rent"]
    print("total amount to be paid is ₹", amount)
    booking = input("press 1 to confirm booking or 2 to cancel: ")
    if booking == "1":
        cars[car_no]["availability_status"] = "no"
        print("booking confirmed!")
    elif booking == "2":
        print("booking cancelled.")
    else:
        print("invalid input.")
def return_a_car():
    car_no = input("enter the car number to return: ")
    if car_no in cars and cars[car_no]["availability_status"] == "no":
        cars[car_no]["availability_status"] = "yes"
        print("car returned successfully and 20000 credited to your account.")
    else:
        print("invalid car number.")
def display_cars():
    print("available cars:")
    for car_id, car_info in cars.items():
        print(f"car number: {car_id}, name: {car_info['name']}, rent: ₹{car_info['per_day_rent']}, availability status: {car_info['availability_status']}")
    print()
while True:
    print("CAR RENTAL SYSTEM")
    print("1. Rent a car")
    print("2. Return a car")
    print("3. Display available cars")
    print("4. Exit")
    ch = input("enter your choice (1-4): ")
    if ch == "1":
        book_a_car()
    elif ch == "2":
        return_a_car()
    elif ch == "3":
        display_cars()
    elif ch == "4":
        print("Thank you")
        break
    else:
        print("invalid option")
