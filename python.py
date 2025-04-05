def get_numbers():
    user_input = input("Enter numbers separated by commas: ")
    try:
        numbers = [float(num.strip()) for num in user_input.split(',')]
        return numbers
    except ValueError:
        print("Please enter valid numbers.")
        return []

def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def main():
    numbers = get_numbers()
    if numbers:
        average = calculate_average(numbers)
        print(f"The average is: {average}")
    else:
        print("No valid numbers entered.")

if __name__ == "__main__":
    main()
