import socket
import os
import datetime
import sys, traceback, types

def capture():
	if os.name == "nt":  # windows
	#Konfigurasi socket
		HOST = socket.gethostbyname(socket.gethostname())
		sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
		sock.bind((HOST, 2441))
		sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
		sock.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
		TimeStamp = datetime.datetime.now()

	else:
		print("Linux machine on build")
		

	while True:
		try:
			raw = sock.recvfrom(65535) #buffer size
			conv = raw[0].decode("utf-8", "replace").split("\r\n\r\n") #decode datagram to string
			if "HTTP" in conv[0][40:]:
				capt = conv[0][40:]
				with open("capturedheader.log", "a") as f:
					print("[", "="*25, "HEADER CAPTURED", "="*25, "]","\n\n", "At :", TimeStamp, "\n", capt, file=f)

			else:
				pass
		
			#subprocess.check_call(["attrib", "+H", "capturedheader.log"])
		except Exception as e:
			with open("eror.log", "a") as erLog:
				print("\n",TimeStamp,"\n", e, file=erLog)
			continue


if __name__ == "__main__":
	capture()
