print("==== CYBERSECURITY TOOLKIT ====")

print("1. Password Strength Checker")
print("2. Hash Generator")
print("3. Dictionary Password Cracker")
print("4. Port Scanner")
print("5. Packet Sniffer")
print("6. Brute Force Tool")
print("7. Web Vulnerability Scanner")

choice = input("\nSelect a tool (1-7): ")

if choice == "1":
    import password_checker

elif choice == "2":
    import hash_generator

elif choice == "3":
    import password_cracker

elif choice == "4":
    import port_scanner

elif choice == "5":
    import packet_sniffer

elif choice == "6":
    import bruteforce

elif choice == "7":
    import web_scanner

else:
    print("Invalid option")