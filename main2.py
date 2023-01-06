import qrcode
from tkinter import Tk, Frame, Label, Entry, Button, messagebox, Canvas
from PIL import ImageTk, Image

# Creating the window
wn = Tk()
wn.title('QR Code Generator')
wn.geometry('400x500')
wn.config(bg='slate blue')


# Function to generate the QR code and save it
def generateCode():
    # Creating a QRCode object of the size specified by the user
    qr = qrcode.QRCode(version=size.get(),
                       box_size=10,
                       border=5)
    qr.add_data(text.get())  # Adding the data to be encoded to the QRCode object
    qr.make(fit=True)  # Making the entire QR Code space utilized
    img = qr.make_image()  # Generating the QR Code
    fileDirec = loc.get() + '\\' + name.get()  # Getting the directory where the file has to be saved
    img.save(f'{fileDirec}.png')  # Saving the QR Code
    # Showing the pop-up message on saving the file
    rawimg = Image.open(f'{fileDirec}.png')
    rawimg = rawimg.resize((150, 150), Image.LANCZOS)
    qrimg = ImageTk.PhotoImage(rawimg)
    qrdisp = Label(Frame5, image=qrimg)
    qrdisp.place(relx=0.25, rely=0.15, relwidth=0.5, relheight=0.8)
    messagebox.showinfo("QR Code Generator", "QR Code is saved successfully!")

# Label for the window
headingFrame = Frame(wn, bg="grey", bd=5)
headingFrame.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.1)
headingLabel = Label(headingFrame, text="Generate QR Code", bg='ghost white', font=('Helvetica', 14, 'bold'))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

# Taking the input of the text or URL to get QR code
Frame1 = Frame(wn, bg="slate blue")
Frame1.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.15)
label1 = Label(Frame1, text="Enter the Text/URL", bg="slate blue", fg='azure', font=('Helvetica', 9, 'bold'))
label1.place(relx=0.05, rely=0.2, relheight=0.2)
text = Entry(Frame1, font='Helvetica 9')
text.place(relx=0.05, rely=0.4, relwidth=0.9, relheight=0.3)

# Getting input of the location to save QR Code
Frame2 = Frame(wn, bg="slate blue")
Frame2.place(relx=0.15, rely=0.25, relwidth=0.7, relheight=0.15)
label2 = Label(Frame2, text="Your Saving Location", bg="slate blue", fg='azure',font=('Helvetica', 9, 'bold'))
label2.place(relx=0.05, rely=0.2, relheight=0.2)
loc = Entry(Frame2, font='Helvetica 9')
loc.place(relx=0.05, rely=0.4, relwidth=0.9, relheight=0.3)

# Getting input of the QR Code image name
Frame3 = Frame(wn, bg="slate blue")
Frame3.place(relx=0.15, rely=0.35, relwidth=0.7, relheight=0.15)
label3 = Label(Frame3, text="Name your QR Code", bg="slate blue", fg='azure',font=('Helvetica', 9, 'bold'))
label3.place(relx=0.05, rely=0.2, relheight=0.2)
name = Entry(Frame3, font='Helvetica 9')
name.place(relx=0.05, rely=0.4, relwidth=0.9, relheight=0.3)

# Getting the input of the size of the QR Code
Frame4 = Frame(wn, bg="slate blue")
Frame4.place(relx=0.15, rely=0.45, relwidth=0.7, relheight=0.15)
label4 = Label(Frame4, text="Enter size: 1 to 40 (1 = 21x21)", bg="slate blue", fg='azure', font=('Helvetica', 9, 'bold'))
label4.place(relx=0.05, rely=0.2, relheight=0.2)
size = Entry(Frame4, font='Helvetica 9')
size.place(relx=0.25, rely=0.4, relwidth=0.5, relheight=0.3)

# Button to generate and save the QR Code
button = Button(wn, text='Generate Code', font='Helvetica 9 bold', command=generateCode)
button.place(relx=0.37, rely=0.6, relwidth=0.25, relheight=0.06)

# QR Code Display
Frame5 = Frame(wn, bg="slate blue")
Frame5.place(relx=0.15, rely=0.66, relwidth=0.7, relheight=0.35)
label5 = Label(Frame5, text="QR Display", bg="slate blue", fg='azure', font=('Helvetica', 9, 'bold'))
label5.place(relx=0.38, rely=0.0, relheight=0.2)
canvas = Canvas(Frame5, bg='white', height=75, width=75)
canvas.place(relx=0.25, rely=0.15, relwidth=0.5, relheight=0.8)

# Runs the window till it is closed manually
wn.mainloop()
