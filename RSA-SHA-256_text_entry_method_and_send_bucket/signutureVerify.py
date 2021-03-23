import subprocess


def veryfyImage():

    print('\nThis file was definitely sent from USER-A: BOB')
    subprocess.run(["openssl", "dgst", "-verify", "pubkeyUSER-A.pem",
                    "-signature", "signiture.bin", "RSAhiddenOutVerify.txt"])

# openssl dgst -verify pubkeyA.pem -signature signiture.bin RSAhiddenOutVerify.txt
