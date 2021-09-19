#QR code encoder / decoder

#ENCODER
########
import qrcode
data = 'Data for teh QR Code'

qr = qrcode.QRCode(version = 1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color = 'green', back_color = 'white')
img.save('path where the qrcode has to be stored (replace \ with / in the folder path)')

#DECODER
########
from pyzbar.pyzbar import decode
from PIL import Image
img = Image.open('path of the image file (replace \ with / in the folder path)')
result = decode(img)
print(result)
