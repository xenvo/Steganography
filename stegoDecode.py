import base64
import urllib.request
from stegano import lsb

#Meminta user input untuk link image Imgur
imgurLink = input("Insert IMGUR Image Link: ")

#Mengambil gambar dari link Imgur yang tadi diinput
urllib.request.urlretrieve(imgurLink, "lesterDecode.png")

#Mengambil message dari file PNG yang sudah ditarik dari Imgur
image_decode = lsb.reveal("lesterDecode.png")

print("\nENCRYPTED MESSAGE FOUNDED!!")
print("This is the encrypted message: " + image_decode)

#Melakukan decoding dari encrypted message
msg_encrypted = image_decode.encode("utf-8")
msg_decode = base64.b64decode(msg_encrypted)
print(f"\nDecode Message: " + msg_decode.decode("utf-8"))