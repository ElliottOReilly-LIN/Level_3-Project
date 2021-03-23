import subprocess


# print("Andy's class from here:", random.__doc__)
# import subprocess

# # command = "/usr/bin/openssl genrsa -out privateKey.pem  -3"
# # subprocess.Popen(command)

# command = "/usr/bin/top"

# subprocess.run(["openssl", "genrsa", "-out", "pKey.pem", ])
# print("     noiw running the output..!\n\n\n\n\n")
# privKeyA = subprocess.run(["cat", "pKey.pem"])

# print(privKeyA)

def runOpenSSL(secret):
    print("File received by OPENSSL:\n\n\n!", secret)
    file = open('secretMSG.txt', 'w')
    file.write(secret)
    file.close()
    # generate a random 64 bit key for des to use
    subprocess.run(["openssl", "rand", "-out", "des_key8b", "8", ])

    print("OpenSSL will encrypt your message..")
    # Store des_key and run the HEX viewer
    subprocess.run(["xxd", "-b", "des_key8b"])
    print("\nDes Key :")
    subprocess.run(["cat", "des_key8b"])

    # generate a random 64 bit key for des to use
    subprocess.run(["openssl", "enc", "-des", "-a", "-in", "secretMSG.txt", "-out", "ciphertext.enc",
                    "-nosalt", "-iv", "0000000000000000", "-k", "des_key8b"])

    # Pipe the ciphertext into a page code format that the the LSB algorithm can accept
    # subprocess.run(["xxd", "-p", "ciphertext.enc", "hexcodeCiph.enc"])

    print("\nEncrypted text: ")

    subprocess.run(["cat", "ciphertext.enc"])

    myfile = open('secretMSG.txt', 'r')
    pt = myfile.read()

    # print('\nYour secret message was: {}'.format(pt))
