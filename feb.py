from datetime import datetime

print("We are learning git and github")

print("Hello Python world")

def display_month():
    now = datetime.now()

    current_month = now.strftime("%B")

    print(f"It's {current_month}")

display_month()