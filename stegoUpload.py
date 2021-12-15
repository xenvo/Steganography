import pyimgur
import base64
import requests
import json
from stegano import lsb

msg = input("Message to encode with UTF-8: ")
msg_utf8 = msg.encode("utf-8")
msg_b64encoded = base64.b64encode(msg_utf8)
print(f"Encoded string to Base64: " + msg_b64encoded.decode("utf-8"))
msg_b64decoded = msg_b64encoded.decode("utf-8")
image = lsb.hide("lester.png", msg_b64decoded)
image.save("lesterStego.png")
image_decode = lsb.reveal("lesterStego.png")
print(image_decode) 
print("\nMessage succesfully injected")
CLIENT_ID = "82163dae73db44e"
PATH = "lesterStego.png"
imageUpload = pyimgur.Imgur(CLIENT_ID)
uploaded_image = imageUpload.upload_image(PATH, title="Stegano")
print(uploaded_image.link)

#Source:
#https://pythonrepo.com/repo/Damgaard-PyImgur-python-third-party-apis-wrappers
#https://www.geeksforgeeks.org/encoding-and-decoding-base64-strings-in-python/
#https://www.youtube.com/watch?v=lvky-tmoTvg
#https://www.geeksforgeeks.org/image-based-steganography-using-python/
