#import
import os,sys
import time
import socket

os.system("clear") #รันคําสั่งเคลียหน้าTermux
os.system("cat Banner.txt ") #เเสดงข้อมูลในไฟล์ Banner.txt
print("\nEnter your web URL")
print("example URL : pornhub.com")
print("\nตัวอย่าง URL : pornhub.com (ภาษาไทย)")
URL = input("\nURL : ") #เป้าหมายของเราที่จะสแกนportเเละip
ip = socket.gethostbyname(str(URL)) #มีไว้หา ip ของเป้าหมาย

print("\nPlease wait..... (รอนานหน่อยนะครับ^_^)")

try: #สเเกน port
     for P in range(1, 9999): #ให้สเเกนจากport 1 - 9999
         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         Success = sock.connect_ex((ip, P))
         if Success == 0:
            print("\n======================================")
            print("\nip web : " + (str(ip))) #ให้แสดง ip ที่แสกนได้
            print("\nport open :  " + str(P)) #ให้แสดง port ที่แสกนได้
            print("\nฝากกดถูกใจให้เพจเราด้วยนะครับ^_^ : NAP SEC")
            print("\n======================================")
         sock.close()

except Exception:
    print("Error!")
    sys.exit()

#ฝากกดถูกใจให้เพจเราด้วยนะครับ^_^ : NAP SEC
