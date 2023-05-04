# Simple while loop for adding and removing names/ objects to and from a list using 'append' and 'remove'

cars = ["BMW", "Acura", "GMC"]
print(f"Here is a list of the cars: {cars}.")
valid_responses = ["add", "remove", "exit"]

decision = ""

while decision.lower() != "exit":
    
    decision = input("Would you like to add or remove to the list? Type 'add', 'remove', or 'exit'. ")

    if decision.lower() == "add":
        new_car = input("Add new car here: ")
        if new_car in cars:
            print("Car already in list.")
        else:
            cars.append(new_car)
            print(f"{new_car} was added to the list.")
            print(f"Here is the updated list: {cars}")

    elif decision.lower() == "remove":
        remove_car = input("Remove car here: ")
        if remove_car not in cars:
            print("Car not found in list.")
        else:
            cars.remove(remove_car)
            print(f"{remove_car} was removed from the list.")
            print(f"Here is the updated list: {cars}")

    elif decision.lower() not in valid_responses:
        print("Invalid option.")

print(f"Here is the final list of cars: {cars}")
