import qrcode
from PIL import Image
import qrcode.constants

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=20,border=2)
qr.add_data("https://www.linkedin.com/in/parth-datar-44875a24a/")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="yellow")
img.save("LINKEDIn.png")
