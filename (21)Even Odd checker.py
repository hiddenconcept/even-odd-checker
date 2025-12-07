num = int(input("Enter a number: "))

mod = num % 2

if mod == 0:
    print(f"The number {num} is Even")
elif num % 7 == 0:
    print(f"The number {num} is Dividable by 7!")
else:
    print(f"The number {num} is Odd")
