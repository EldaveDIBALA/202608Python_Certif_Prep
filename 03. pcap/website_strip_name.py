#####################################################################################################

from urllib.parse import urlparse
import sys
import time

url = input("Entrez le texte ou l'Url à encoder dans le QR code : ")

qr_code = urlparse(url).netloc
print(qr_code)

if qr_code.startswith("www."):
  qr_code = qr_code.replace("www.", "", 1)
  print(qr_code)
  
  sys.exit()

# url2 = url1.split(".")[0]
# print(url2)
