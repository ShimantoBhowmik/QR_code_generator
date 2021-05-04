import qrcode
import image

qr = qrcode.QRCode( 
    version = 15, #15 is used to represent the version of qr code, higher version means sophisticated picture and bigger code image
    box_size = 10,#10 is used to represent the size of the box where qr code will be displayed
    border = 5 #border of the qr code
)

data = "https://github.com/ShimantoBhowmik" #creating the qr code of my github account

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = 'black' , back_color = 'white')
img.save('sample.png')