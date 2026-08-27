#####################################################################################################

from urllib.parse import urlparse
import sys
import time

print(f"{'='*50}\n")

url = input("Entrez l'URL à analyser : ")

url = urlparse(url).netloc
print("\nL'url devient après \"url parsing\" : " + url)

if url.startswith("www."):
  url = url.replace("www.", "", 1)
  print("L'url devient après \"replace\" : " + url)

url = url.split(".")[0]
print("L'url devient après \"split\" : " + url)

print(f"\n{"="*50}")
