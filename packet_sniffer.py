from scapy.all import sniff, IP

def packet_callback(packet):
    
    if packet.haslayer(IP):
        
        src = packet[IP].src
        dst = packet[IP].dst
        proto = packet[IP].proto
        
        print(f"Source: {src} → Destination: {dst} | Protocol: {proto}")

print("Starting packet sniffer...")

sniff(prn=packet_callback, count=20)