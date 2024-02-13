import qrcode
import os

# Text or data to be included in the QR code
data = input("Enter a link:")

# Generate QR code
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

# Save QR code as image
image = qr.make_image(fill_color="black", back_color="white")

# Get Desktop Location
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file_path = os.path.join(desktop, 'QR Code.png')

# Save QR code to desktop
image.save(file_path)

input("The link has been converted into a QR code and saved to your desktop.")