def line(customers):
    if not customers:
        print("The line is currently empty.")
    else:
        parts = [f"{i + 1}. {name}" for i, name in enumerate(customers)]
        print("The line is currently: " + " ".join(parts))

def take_a_number(customers, name):
    customers.append(name)
    print(f"Welcome, {name}. You are number {len(customers)} in line.")

def now_serving(customers):
    if not customers:
        print("There is nobody waiting to be served!")
    else:
        current = customers.pop(0)
        print(f"Currently serving {current}.")  
