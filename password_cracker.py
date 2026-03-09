import hashlib

target_hash = input("Enter hash: ")
hash_type = input("Enter hash type (md5/sha1/sha256): ")

with open("wordlist.txt","r") as file:

    for word in file:
        word = word.strip()

        if hash_type == "md5":
            hashed = hashlib.md5(word.encode()).hexdigest()

        elif hash_type == "sha1":
            hashed = hashlib.sha1(word.encode()).hexdigest()

        elif hash_type == "sha256":
            hashed = hashlib.sha256(word.encode()).hexdigest()

        if hashed == target_hash:
            print("Password found:", word)
            break

    else:
        print("Password not found")