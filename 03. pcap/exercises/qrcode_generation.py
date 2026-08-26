###############################################################################################################

""" Génération d'un QR code à partir d'une chaîne de caractères """

import os
import qrcode
from urllib.parse import urlparse
import sys
import time

text = input("Entrez le texte ou l'Url à encoder dans le QR code : ")

if text.startswith("http://") or text.startswith("https://"):
  qr_code = urlparse(text).netloc
  print(qr_code)

  if qr_code.startswith("www."):
    qr_code = qr_code.replace("www.", "", 1)
    print(qr_code)
else:
  qr_code = text

qr = qrcode.QRCode(
  box_size = 20,
  border = 10
)

qr.add_data(qr_code)  # Ajoute les données à encoder dans le QR code
qr.make(fit = True)

qr_code_image = qr.make_image(fill_color = "black", back_color = "white")
qr_code_image.save(os.path.join("/Users/eldavedibala/Documents/Engineer/SDET/202608Python_Certif_Prep/03. pcap/exercises", f"{qr_code}_qrcode.png"))

qr.print_ascii(invert = True)  # Affiche le QR code dans la console en utilisant des caractères ASCII

print("QR code généré avec succès !\n")
