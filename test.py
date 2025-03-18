words = {"Love's", "gonna", "get", "me", "killed"}

odd_number_words = [number for number in words if len(number) % 2 != 0]

print(f"Filtered list = {odd_number_words}")