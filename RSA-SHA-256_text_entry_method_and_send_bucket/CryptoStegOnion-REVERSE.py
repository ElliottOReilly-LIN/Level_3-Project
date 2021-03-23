from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from reverseOpenSSL import reverseDecrypt
from signutureVerify import veryfyImage
from googleCloudRetreive import retrieveImage


class EncryptWindow:
    def __init__(self, master):

        self.frame_header = ttk.Frame(master)  # Top level master frame
        master.resizable(False, False)
        master.geometry("460x220")
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
        ttk.Label(self.frame_header, text="Good afternoon Alice!",
                  style='Header.TLabel').grid(row=0, column=1, )
        ttk.Label(self.frame_header, text="     Go and grab your image from the cloud!").grid(
            row=1, column=1, sticky='w')

        # Build up the main content in an a second main frame, separate from the header
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        def goCloud():
            # call the encode function from stegapy
            retrieveImage()

        def goReverseOpenSSL():

            reverseDecrypt()

        def goVerify():

            veryfyImage()

        # Set of encryption options, with a command button to fire open the second window
        ttk.Button(self.frame_content, text='Fetch file', command=goCloud).grid(
            row=5, column=0, padx=8, pady=20, sticky='e')
        ttk.Button(self.frame_content, text='Decrypt', command=goReverseOpenSSL).grid(
            row=5, column=1, padx=8, pady=20, sticky='e')
        ttk.Button(self.frame_content, text='Verify HASH', command=goVerify).grid(
            row=5, column=2, padx=8, pady=20, sticky='e')
        ttk.Button(self.frame_content, text='Quit', command=master.destroy).grid(
            row=5, column=3, padx=8, pady=20, sticky='e')


def main():

    root = Tk()
    program = EncryptWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
