import bike_rental as br

bike_system = br.BikeRental(100)
customer = br.Customer()

# TODO 10 - Main program logic: print options to the console
while True:
    print("""
    ====== Bike Rental App ======
    1. Display available Bikes
    2. Request a bike on hourly basis - $5
    3. Request a bike on daily basis  - $20
    4. Request a bike on weekly basis - $60
    5. Return a bike(s)
    6. Exit
    """)

    # TODO 11 - Ask from user to get option (check if it is int)
    choice = input("Enter choice: ")
    try:
        choice = int(choice)
    except ValueError:
        print('The choice has to be from the available choices.')
        continue

    # TODO 12 - Based on selected choice call methods from Bike Rental and Customer classes
    if choice == 1:
        bike_system.display_stock()
    elif choice == 2:
        requested_bikes = customer.request_bike()
        rental_time = bike_system.rent_bike_on_hourly_basis(requested_bikes)
        customer.rental_time = rental_time
        # customer.rental_time = bike_system.rent_bike_on_hourly_basis(customer.request_bike())
        customer.rental_basis = 1
    elif choice == 3:
        customer.rental_time = bike_system.rent_bike_on_daily_basis(customer.request_bike())
        customer.rental_basis = 2
    elif choice == 4:
        customer.rental_time = bike_system.rent_bike_on_weekly_basis(customer.request_bike())
        customer.rental_basis = 3
    elif choice == 5:
        request_tuple = customer.return_bike()
        bill = bike_system.return_bike(request_tuple)
        customer.bill = bill
        customer.rental_time, customer.rental_basis, customer.bikes = 0, 0, 0
    elif choice == 6:
        break
    else:
        print('Invalid input: Please enter a number between 1-6')
print('Thankyou for using our bike rental system.')
