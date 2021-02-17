from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from openSSL import runOpenSSL
from encodeSimple import msgEncode
from googleCloudSend import sendImage


class EncryptWindow:
    def __init__(self, master):

        self.frame_header = ttk.Frame(master)  # Top level master frame
        master.resizable(False, False)
        master.geometry("560x280")
        master.configure(background='#e1d8b9')

        self.style = ttk.Style()
        self.style.configure('TFrame', background='#e1d8b9')
        self.style.configure('TButton', background='#e1d8b9')
        self.style.configure('TLabel', background='#e1d8b9', font=('Arial', 11))
        self.style.configure('Header.TLabel', font=('Arial', 20, 'bold'))

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        self.logo = PhotoImage(file='enc1.png')

        ttk.Label(self.frame_header, image=self.logo).grid(row=0, column=0, padx=5, pady=5, rowspan=2)
        ttk.Label(self.frame_header, text="  Welcome to CryptoStegOnion ",
                  style='Header.TLabel').grid(row=0, column=1, )
        ttk.Label(self.frame_header, text="       Choose your preferred Encyrption method: ").grid(
            row=1, column=1, sticky='w')

        # Build up the main content in an a second main frame, separate from the header
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        optWin = OptionWindow()
        # Set of encryption options, with a command button to fire open the second window
        desBut = ttk.Button(self.frame_content, text='DES', command=optWin.win2).grid(
            row=5, column=0, padx=8, pady=20, sticky='e')
        des3But = ttk.Button(self.frame_content, text='DES3', command=optWin.win2).grid(
            row=5, column=1, padx=8, pady=20, sticky='e')
        aesBut = ttk.Button(self.frame_content, text='AES', command=optWin.win2).grid(
            row=5, column=2, padx=8, pady=20, sticky='e')
        blowBut = ttk.Button(self.frame_content, text='Blowfish', command=optWin.win2).grid(
            row=5, column=3, padx=8, pady=20, sticky='e')
        camBut = ttk.Button(self.frame_content, text='Camilia', command=optWin.win2).grid(
            row=6, column=0, padx=8, pady=2, sticky='w')
        castBut = ttk.Button(self.frame_content, text='CAST', command=optWin.win2).grid(
            row=6, column=1, padx=8, pady=2, sticky='w')
        rc2But = ttk.Button(self.frame_content, text='RC2', command=optWin.win2).grid(
            row=6, column=2, padx=8, pady=2, sticky='w')
        rc4But = ttk.Button(self.frame_content, text='RC4', command=optWin.win2).grid(
            row=6, column=3, padx=8, pady=2, sticky='w')


class OptionWindow:
    def __init__(self):
        pass

    def win2(self):
        child = Toplevel(bg='#e1d8b9')
        child.title("Crpto/Stego Hybrid Customiser")
        child.geometry("430x280")

        self.child = ttk.Frame()  # Child of Top level master frame

        self.style = ttk.Style()
        self.style.configure('Header.TLabel', font=('Arial', 16, 'bold'))
        self.style.configure('TCheckbutton', background='#e1d8b9', font=('Arial', 11))

        ttk.Label(child, text="  Add optional asymmetric key:",
                  style='Header.TLabel').grid(row=0, column=0, columnspan=4)

        self.child.pack()

        withRSA = ttk.Checkbutton(child, text='RSA Key').grid(row=2, column=0, padx=25, pady=5, sticky='e')
        rsaKey = StringVar()
        rsaKey.set("RSA Key")

        withSHA128 = ttk.Checkbutton(child, text='SHA 128').grid(row=2, column=1, padx=25, pady=5, sticky='e')
        sha128 = StringVar()
        sha128.set("SHA 128"),

        withSHA256 = ttk.Checkbutton(child, text='SHA 256').grid(row=2, column=2, padx=25, pady=5, sticky='e')
        sha128 = StringVar()
        sha128.set("SHA 256")

        ttk.Label(child, text=" Select Cover image:", style='Header.TLabel').grid(
            row=3, column=0, sticky='w', columnspan=4)

        def openFile():

            global fileOpen
            fileOpen = StringVar()
            fileOpen = askopenfilename(initialdir="ellStegPi",
                                       title="Select File", filetypes=(("Image files files", "*.png"), ("all files", "*.*")))
            label3 = ttk.Label(text=fileOpen)
            label3.place(relx=0.3, rely=0.3)

        buttonSelect = ttk.Button(child, text="Select File", command=openFile).grid(
            row=5, column=0, padx=10, pady=5, sticky='w')

        # ---- grab secret message
        mystring = StringVar()

        # define the function that the signup button will do
        def getvalue():
            secretMSG = mystring.get()

            runOpenSSL(secretMSG)
            sslWindow = openSSLWindow()
            sslWindow.window3()

            return secretMSG
            # Label(root, text="Text to get").grid(row=0, sticky=W)  #label
        Label(child, text="Enter Secret Message: ").grid(row=6, column=0,
                                                         sticky='w', padx=10, pady=2, columnspan=4)

        Entry(child, textvariable=mystring).grid(row=7, column=0,
                                                 sticky='w', padx=10, pady=2, columnspan=4)  # entry textbox

        grabSecret = Button(child, text="CLick to Encrypt..!!", command=getvalue).grid(
            row=8, column=0, padx=8, pady=20, sticky='e')  # button


class openSSLWindow:
    def __init__(self):
        pass

    def window3(self):
        child = Toplevel(bg='#000000')
        child.title("OpenSLL subsystem for Encryption")
        child.geometry("600x180")

        self.child = ttk.Frame()  # Child of Top level master frame

        self.style = ttk.Style()
        # self.style.configure('TButton', background='#00FF00', font=('Arial', 20, 'bold'))
        # self.style.configure(background='#00FF00', font=('Arial', 20))

        # Call the encode function from encodeSimple.py
        def callStegapy():
            msgEncode()
            # call the encode function from stegapy
        sendImage()

        ttk.Label(child, text="\n  OpenSSL subsystem\n  Running in the background....",
                  style='Header.TLabel', font=('Courier', 20), foreground='#00FF00',
                  background='#000000').grid(row=0, column=0, columnspan=4)

        ttk.Button(child, text="Click to Send message to stegapy..!!", style='Header.TLabel', command=callStegapy).grid(
            row=5, column=0, padx=25, pady=25, sticky='w')

        self.child.pack()


def main():

    root = Tk()
    program = EncryptWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
