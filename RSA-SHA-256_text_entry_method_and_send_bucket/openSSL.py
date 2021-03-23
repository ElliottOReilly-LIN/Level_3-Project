import subprocess


def runOpenSSL(secret):
    print("File received by OPENSSL:\n\n\n!", secret)
    file = open('secretMSG.txt', 'w')
    file.write(secret)
    file.close()

    # ----- Generate private keys for user A and User B #-3 is used for optimum speed,

    # 1. ----- the exponent, 65557 being the default
    # openssl genrsa -out privkeyA.pem -3
    subprocess.run(["openssl", "genrsa", "-out", "privkeyA.pem", "-3"])

    # 2. ------ Produce the public key from the private key for USER A
    # openssl rsa -in privkeyA.pem -pubout -out pubkeyA.pem
    subprocess.run(["openssl", "rsa", "-in", "privkeyA.pem", "-pubout", "-out", "pubkeyUSER-A.pem"])

    # 2. ------ Produce the public key from the private key for USER B
    # openssl rsa -in privkeyA.pem -pubout -out pubkeyB.pem
    subprocess.run(["openssl", "rsa", "-in", "privkeyA.pem", "-pubout", "-out", "pubkeyUSER-B.pem"])

    # 3. ------ Create a signiture using a hash function #default sha256#
    # openssl dgst -sign privkeyA.pem -out signiture.bin msg
    subprocess.run(["openssl", "dgst", "-sign", "privkeyA.pem", "-out", 'signiture.bin', 'secretMSG.txt'])

    # 4. ------ Encrypt using RSA #by default# using the public key of user B
    # openssl pkeyutl -encrypt -in secretMSG.txt -pubin -inkey pubkeyB.pem -out -raw RSAciphertext-RAW.bin
    subprocess.run(["openssl", "pkeyutl", "-encrypt", "-in", "secretMSG.txt", "-pubin",
                    "-inkey", "pubkeyUSER-B.pem", "-out", "RSAciphertext.bin"])

    # openssl base64 -in RSAciphertext-RAW.bin -out RSA64
    subprocess.run(["openssl", "base64", "-in", "RSAciphertext.bin", "-out", "RSABase64Cipher"])

    # print("OpenSSL will encrypt your message..")
    # # Store des_key and run the HEX viewer
    # subprocess.run(["xxd", "-b", "privkeyA.pem"])

    # Pipe the ciphertext into a page code format that the the LSB algorithm can accept
    # subprocess.run(["xxd", "-p", "ciphertext.enc", "hexcodeCiph.enc"])

    print("\nEncrypted text: ")

    subprocess.run(["cat", "RSAciphertext.bin"])

    print("\nConverted ready for tranmission: ")

    subprocess.run(["cat", "RSABase64Cipher"])

    myfile = open('secretMSG.txt', 'r')
    pt = myfile.read()

    # print('\nYour secret message was: {}'.format(pt))
