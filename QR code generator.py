# converts a text/link into a QR code

import qrcode


def generate_qrcode(link):
    qr = qrcode.QRCode(
        version=1,    # controls the size of the QR Code (the smallest, version 1, is a 21×21 matrix)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # About 7% or fewer errors can be corrected.
        box_size=10,  # controls how many pixels each “box” is
        border=4,     # controls how many boxes thick the border should be
    )

    qr.add_data(link)  # add data to the QRCode object
    qr.make(fit=True)  # with (fit=True) ensures that the entire dimension of the QR Code is utilized
    img = qr.make_image(fill_color='black', back_color='white')  # convert the QRCode object into an image file
    img.save("QRimg.png")


url = input("Enter your url: ")
generate_qrcode(url)

