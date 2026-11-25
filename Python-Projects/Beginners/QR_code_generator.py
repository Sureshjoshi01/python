# Write a program to generate a QR code based on user input, such as text or a
# URL. The QR code should be saved as an image file that can be scanned with a
# smartphone.


# Optional Enhancements
# • Add options for the user to choose the color of the QR code. This will allow
# users to generate QR codes that match their style or branding.
# • Implement a feature that lets the user generate multiple QR codes at once by
# providing a list of URLs or texts. Each QR code should be saved with a unique
# filename.


import qrcode
import random

def qr_generator(url,color):
    count = random.randint(1,100000)
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=color)
    img.save(f"qr_code_{count}.png")

print("**********QR Code Genrator**********")
print("1.Generate single QR code for an URL")
print("2.Generate multiple QR code for multiple URLs")
while True:
    ans = int(input("Select your Option : "))
    if ans not in (1,2):
        print("Only option 1 and 2 are availaible")
    else:
        break
      
if ans == 1:
    print("Enter URLs or text : ",end="")
    url = input().strip()
    print("Choose color of QR Code : ",end="")
    color = input().strip()
    qr_generator(url,color)
    print("QR code is successfully generated")
elif ans == 2:
    qr_code = []
    print("Enter comma separated list of urls : ")
    url = input().split()
    qr_code = url.split(",")
    print(qr_code)
    color = "black"
    for i in qr_code:
        qr_generator(url,color)


