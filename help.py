import mscvrt

print("""malformed_packet - sends a lot of malformed packets to server
null_ping - sends handshake packet with wrong next state field
big_handshake - sends large handshake packet
login_spam - sends ton of login packet with normal nickname
double_login - login spam with doubled login start packet

Press any key to quit""")

msvcrt.getch()