print("CYBERSECURITY TOOLKIT")

print("1 Password Checker")
print("2 Caesar Cipher")
print("3 Port Scanner")
print("4 Hash Generator")

choice = input("Choose tool: ")

if choice == "1":
    import password_checker

elif choice == "2":
    import cipher

elif choice == "3":
    import port_scanner

elif choice == "4":
    import hash_generator