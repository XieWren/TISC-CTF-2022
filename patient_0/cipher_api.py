from requests import post
from json import dumps
from re import search
from pathlib import Path

class File():
    def __init__(self):
        self.mystery_1 = Path(__file__).parent.joinpath("File Conversion", "Mystery File(s)", "above clue 4.txt")
        self.mystery_2 = Path(__file__).parent.joinpath("File Conversion", "Mystery File(s)", "pseudo-random bytes.txt")
        self.pdf_1 = Path(__file__).parent.joinpath("File Conversion", "PDF Streams", "Part_1.txt")
        self.pdf_2 = Path(__file__).parent.joinpath("File Conversion", "PDF Streams", "Part_2.txt")
        self.pdf_5 = Path(__file__).parent.joinpath("File Conversion", "PDF Streams", "Part_5.txt")


key = bytearray.fromhex("F7 66 35 AB") # 4 bytes
outputFile = Path(__file__).parent.joinpath("output.txt")
file = File().mystery_1


with open(file, "r") as mystery, open(outputFile, "wb") as output:
    value = mystery.read()

value = "a1 3e 43"

response = post(
    url = "https://www.dcode.fr/api",
    headers = {
    },

    data = "tool=rc4-cipher&ascii=%7B%22text%22%3A%22a1+2e+ab%22%2C%22ascii%22%3A%22a12eab%22%7D&key=SECRET&ascii_format=char"
).json

print(response)

"""
import requests





data = 'tool=rc4-cipher&ascii=%7B%22text%22%3A%22a1+2e+ab%22%2C%22ascii%22%3A%22a12eab%22%7D&key=SECRET&ascii_format=char'

response = requests.post('https://www.dcode.fr/api/', cookies=cookies, headers=headers, data=data, verify=False)
"""