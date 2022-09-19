from pathlib import Path
from re import sub
from Crypto.Cipher import DES, ARC2, ARC4
from Crypto.Util.Padding import pad


patientFile = Path(__file__).parent.joinpath("PATIENT0")

class File():
    def __init__(self):
        self.mystery_1 = Path(__file__).parent.joinpath("File Conversion", "Mystery File(s)", "above clue 4.txt")
        self.mystery_2 = Path(__file__).parent.joinpath("File Conversion", "Mystery File(s)", "pseudo-random bytes.txt")
        self.pdf_1 = Path(__file__).parent.joinpath("File Conversion", "PDF Streams", "Part_1.txt")
        self.pdf_2 = Path(__file__).parent.joinpath("File Conversion", "PDF Streams", "Part_2.txt")
        self.pdf_5 = Path(__file__).parent.joinpath("File Conversion", "PDF Streams", "Part_5.txt")

outputFile = Path(__file__).parent.joinpath("output.txt")

# key = bytearray.fromhex("F7 66 35 AB") # 4 bytes
key = bytearray("f76635ab", encoding = "utf-8") # 8 bytes <-- DES, RC2, RC4 Compliant
print(f"Length: {len(key)}")

class Cipher():
    def __init__(self):
        
        # self.DES_CFB = DES.new(key, DES.MODE_CFB)
        # self.DES_OFB = DES.new(key, DES.MODE_OFB)
        
        # self.RC2_ECB = ARC2.new(key, ARC2.MODE_ECB) # <-- Does not work on mystery_2, pdf_1, pdf_5
        # self.RC2_CBC = ARC2.new(key, ARC2.MODE_CBC) # <-- Padding needed
        # self.RC2_CFB = ARC2.new(key, ARC2.MODE_CFB)
        # self.RC2_OFB = ARC2.new(key, ARC2.MODE_OFB)
        # self.RC2_CTR = ARC2.new(key, ARC2.MODE_CTR) <-- Impossible to create a nonce for short block sizes
        # self.RC2_OPENPGP = ARC2.new(key, ARC2.MODE_OPENPGP)
        # self.RC2_EAX = ARC2.new(key, ARC2.MODE_EAX)
        
        self.RC4 = ARC4.new(key)

# CFB, OFB, 
# DES, RC2, RC4
# cipher = Cipher().RC2_ECB
# file = File().mystery_2

if __name__ == "__main__":
    cipher = Cipher().RC4
    file = File().pdf_5
    with open(file, "r") as mystery, open(outputFile, "wb") as output:
        data = bytes.fromhex(mystery.read())
        # data = pad(data, block_size = 8) # <-- For CBC Mode
        value = cipher.decrypt(data)
        output.write(value)
