import base64
import urllib.request
from stegano import lsb

imgurLink = input("Insert IMGUR image link: ")
urllib.request.urlretrieve(imgurLink, "lesterDecode.png")
image_decode = lsb.reveal("lesterDecode.png")
print("\n[!]ENCRYPTED MESSAGE FOUND!!")
print("The encrypted message is " + image_decode)
msg_encrypted = image_decode.encode("utf-8")
msg_decode = base64.b64decode(msg_encrypted)
print(f"\nDecode message: " + msg_decode.decode("utf-8"))

#Source:
#https://stackoverflow.com/questions/8286352/how-to-save-an-image-locally-using-python-whose-url-address-i-already-know
#https://pythonrepo.com/repo/Damgaard-PyImgur-python-third-party-apis-wrappers
#https://www.geeksforgeeks.org/encoding-and-decoding-base64-strings-in-python/
