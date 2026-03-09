import hashlib

text = input("Enter text to hash: ")

hash_object = hashlib.sha256(text.encode())

print("SHA256 Hash:", hash_object.hexdigest())