import qrcode

website_link = input('Enter the link to be qrified: ')
qr_name = input('Name for this thing: ')
color_decision = input('Want this in color-inverse[(y)es/(n)o]: ')
qr = qrcode.QRCode(version=1, box_size=5, border=5)
qr.add_data(website_link)
qr.make()

if color_decision == 'y':
    img = qr.make_image(fill_color='white', back_color='black')
else:
    img = qr.make_image(fill_color='black', back_color='white')
img_save = img.save(f'{qr_name}.png')
print(f'success!! :-  {qr_name}.png has been created..:)')
