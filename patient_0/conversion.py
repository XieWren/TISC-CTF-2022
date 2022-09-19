from pathlib import Path

# Lines 7 - 3100: NTFS Start
# Lines 3101 - 50438: NULL
# Linus 50439 - 51275: NTFS Metadata --> https://en.wikipedia.org/wiki/NTFS#Partition_Boot_Sector_(PBS)
# Lines 51276 - 67590: NULL
# Lines 67591 - 67659: HX4(?)
# Lines 67660 - 67850: NULL
# Lines 67848 - 76039: 00 to FF Matrix
# Lines 76040 - 76042: 3. Are these True random bytes for Cryptology?
# Lines 76039 - 196358: Pseudo-Random Bytes(?)
# Lines 196359 - 197638: NTFS Metadata
# Lines 197639 - 201222: NULL but FF
# Lines 201223 - 202246: NTFS Metadata Record (RCRD) LogFile
# Lines 202247 - 205318: NULL but FF
# Lines 205319 - 207110: NTFS Metadata Record (RCRD) LogFile
# Lines 207111 - 327686: NULL but FF
# Lines 327687 - 332038: NULL
# Lines 332039 - 332417: 2. PNG File
# Lines 332418 - 332550: NULL
# Lines 332551 - 343306: ??? File
# Lines 343307 - 343318: 4. If you need a password, the original reading of the BPB was actually Checked and ReChecked 32 times!
# Lines 343319 - 343558: NULL
# Lines 343559 - 375489: 1. PDF
# Lines 375490 - 393190: NULL
# Lines 393191 - 393222: NTFS Metadata End


"""
Image.png: GIXFI2DJOJZXI6JAMZXXEIDUNBSSAZTMMFTT6ICHN4QGM2LOMQQHI2DFEBZXI4TFMFWS4CQ=
           GIXCAVDINFZHG5DZEBTG64RAORUGKIDGNRQWOPZAI5XSAZTJNZSCA5DIMUQHG5DSMVQW2LQK
Lines 332039 - 332417
"""
# with open(Path(__file__).parent.joinpath("image.png"), "wb") as image:
#     image.write(bytes.fromhex())

"""
Barometer.pdf
Lines 343559 - 375489
""" 
# with open(Path(__file__).parent.joinpath("document.pdf"), "wb") as document:
#     document.write(bytes.fromhex())

"""
Barometer Image Part 1
Lines 366881 - 372904
"""
# with open(Path(__file__).parent.joinpath("barometer_1.jfif"), "wb") as document:
#     document.write(bytes.fromhex(""))

"""
Barometer Image Part 2
Lines 372914 - 375277
"""
# with open(Path(__file__).parent.joinpath("barometer_2.jfif"), "wb") as document:
#     document.write(bytes.fromhex())


"""
Part 1
Lines 343569 - 355656

Part 2
Lines 355695 - 366840

Part 5
Lines 375281 - 375316
"""
