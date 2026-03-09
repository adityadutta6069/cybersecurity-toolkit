import time

correct_username = "admin"
correct_password = "cyber123"

username = input("Enter username to attack: ")

attempt = 0

with open("wordlist.txt","r") as file:

    for password in file:

        password = password.strip()
        attempt += 1

        print(f"Attempt {attempt}: Trying password -> {password}")

        time.sleep(1)   # delay between attempts

        if username == correct_username and password == correct_password:
            print("\n✅ PASSWORD FOUND:", password)
            print("Total attempts:", attempt)
            break

    else:
        print("\n❌ Password not found in wordlist")