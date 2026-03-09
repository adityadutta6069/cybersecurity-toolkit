message = input("Enter message: ")
shift = int(input("Enter shift number: "))

encrypted = ""

for char in message:
    if char.isalpha():
        encrypted += chr((ord(char) + shift - 97) % 26 + 97)
    else:
        encrypted += char

print("Encrypted message:", encrypted)