def print_formatted(number):
    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]
        print(f"{decimal} {octal} {hexadecimal} {binary}")

number = int(input())
print_formatted(number)