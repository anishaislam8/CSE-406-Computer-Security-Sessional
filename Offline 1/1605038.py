from BitVector import *
import copy
import numpy as np
import time
from collections import deque
import tkinter as tk
from tkinter import filedialog
import base64 
import os

# SBox and InvSBox

Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

# Mixer and InvMixer

Mixer = [
    [BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03")],
    [BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02")]
]

InvMixer = [
    [BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09")],
    [BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D")],
    [BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B")],
    [BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E")]
]

# calculate round constants for all 10 rounds

round_constants = []
round_constants.append(["01", "00", "00", "00"])
rc = []
rc.append("01")

AES_modulus = BitVector(bitstring='100011011')

for i in range(1,10) :
    bv1 = BitVector(hexstring=rc[i-1])
    bv2 = BitVector(hexstring="02")
    a = bv1.gf_multiply_modular(bv2, AES_modulus, 8)

        
    if a.int_val() <= 0x80 :
        val = a.get_bitvector_in_hex()

    elif a.int_val() > 0x80 :
        xor = BitVector(hexstring="11B")
        result = a ^ xor
        val = result.get_bitvector_in_hex()

    rc.append(val)
    round_constants.append([val, "00", "00", "00"])




# take key as input

key = input("Enter key : ")

if (len(key) < 16) :
    key = key.ljust(16, '0')
elif (len(key) > 16) :
    key = key[0:16]

# convert the ascii key into hex value

keyInHex = key.encode("utf-8").hex()
twoBitHex = []
for i in range(0,len(keyInHex),2) :
    twoBitHex.append(keyInHex[i:i+2])

# create the first four words

words = []
for i in range(0, len(twoBitHex),4):
    words.append(twoBitHex[i:i+4])

# function g

def nextWord (word_index) :
    # next word
    temp = []
    for i in range(4):
        a = int(words[word_index][i], 16)
        b = int(g[g_index][i], 16)
        xor = a^b
        xor = BitVector(intVal=xor, size=8) 
        xor = xor.get_bitvector_in_hex()
        temp.append(xor)

    words.append(temp)

def gSteps (word, g_index, round_index) :
    
    wordNew = copy.deepcopy(word)
    
    # circular byte left shift
    element = wordNew.pop(0)
    wordNew.append(element)
    
    # byte substitution s-box (g is defined before)
    g_word = []
    for element in wordNew:
        b = BitVector(hexstring=element)
        int_val = b.intValue()
        s = Sbox[int_val]
        s = BitVector(intVal=s, size=8)
        g_word.append(s.get_bitvector_in_hex())

    g.append(g_word)
    
    # adding round constant
    int_g = int(g[g_index][0], 16)
    int_rc = int(round_constants[round_index][0], 16)
    summation = int_g ^ int_rc
    g[g_index][0] = BitVector(intVal=summation, size=8) 
    g[g_index][0] = g[g_index][0].get_bitvector_in_hex()


# Key scheduling

time0 = time.time()

g = []
g_index = 0
round_index = 0
word_index = 0

gSteps(words[3], g_index, round_index)
nextWord(word_index)

for i in range(5,44,4) :

    for j in range (i, i+3): # w5, w6, w7
      
        word_index+=1
        temp = []
        for k in range(4):
            a = int(words[word_index][k], 16)
            b = int(words[j-1][k], 16)
            xor = a^b
            xor = BitVector(intVal=xor, size=8) 
            xor = xor.get_bitvector_in_hex()
            temp.append(xor)
        words.append(temp)
        
    # *******generate w8 as g(w7) xor words[word_index]********
    
    # before entering the function increase word_index, g_index, round_index
    word_index += 1
    g_index += 1
    round_index += 1
    
    if word_index == 40 :
        break
    
    
    # call function
    gSteps(words[j], g_index, round_index)
    nextWord(word_index)

roundKeys = []
for i in range(0,len(words),4) :
    roundKeys.append(words[i:i+4])
time1 = time.time()

key_scheduling_time = time1-time0


# input text or image
inputType = input("Enter type 1) Image 2) Text : ")

if inputType == "2":
    text = input("Enter text : ")
elif inputType == "1" :
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    filename, file_extension = os.path.splitext(file_path)

    # open our image file in read binary mode
    with open(file_path, "rb") as image2string:
        # reads the image and encodes it
        byte_data = base64.b64encode(image2string.read())
    
    text = byte_data.decode('utf-8') 



paddingLength = 0

blocks = []
if (len(text) < 16) :
    paddingLength = 16 - len(text)
    text = text.ljust(16,'0')
    blocks.append(text)
elif (len(text) > 16) :
    for i in range(0,len(text),16) :
        blocks.append(text[i:i+16])
    if(len(blocks[len(blocks) - 1]) < 16) : 
        paddingLength = 16 - len(blocks[len(blocks) - 1])
        blocks[len(blocks) - 1] = blocks[len(blocks) - 1].ljust(16,'0')
else :
    blocks.append(text)


# Encryption

time0 = time.time()

cipherText = []

for n in range(len(blocks)) :
    
    textInHex = blocks[n].encode("utf-8").hex()
    
    twoBitHexText = []
    for j in range(0,len(textInHex),2) :
        twoBitHexText.append(textInHex[j:j+2])

        
    # round 0
    twoBitHexTextMatrix = np.array(twoBitHexText, dtype = str).reshape((4,4)).T
    keyMatrix = np.array(roundKeys[0], dtype = str).reshape((4,4)).T
    
    state = []
    
    for i in range(4) :
        for j in range(4) :
            a = BitVector(hexstring=twoBitHexTextMatrix[i][j])
            b = BitVector(hexstring=keyMatrix[i][j])
            result = a ^ b
            result = result.get_bitvector_in_hex()
            state.append(result)
    
    stateMatrix = np.array(state, dtype = str).reshape((4,4))
    
    
    # round 1 to 10
    
    for m in range(1,11) :

        # substitution bytes

        for i in range(4):
            for j in range(4) :
                b = BitVector(hexstring=stateMatrix[i][j])
                int_val = b.intValue()
                s = Sbox[int_val]
                s = BitVector(intVal=s, size=8)
                stateMatrix[i][j] = s.get_bitvector_in_hex()



        #shift row
        for i in range(1,4) :
            d = deque(stateMatrix[i])
            d.rotate(-i)
            stateMatrix[i] = d

        

        # mix column
        if m != 10 :
            another_temp = []

            for i in range(16) :
                another_temp.append("00")
            another_temp = np.array(another_temp, dtype=str).reshape((4,4))

            for i in range(4) :
                for j in range(4) :
                    for k in range(4) :
                        bv1 = Mixer[i][k]
                        bv2 = BitVector(hexstring=stateMatrix[k][j])
                        a = bv1.gf_multiply_modular(bv2, AES_modulus, 8)
                        bv3 = BitVector(hexstring=another_temp[i][j])
                        xor = bv3 ^ a
                        another_temp[i][j] = xor.get_bitvector_in_hex()

            stateMatrix = another_temp


        # add round key
        keyMatrixNewRound = np.array(roundKeys[m], dtype = str).reshape((4,4)).T

        for i in range(4) :
            for j in range(4) :
                a = BitVector(hexstring=stateMatrix[i][j])
                b = BitVector(hexstring=keyMatrixNewRound[i][j])
                result = a ^ b
                result = result.get_bitvector_in_hex()
                stateMatrix[i][j] = result


    for j in range(4) :
        for i in range(4) :
            cipherText.append(stateMatrix[i][j])

time1 = time.time()
encryption_time = time1-time0


# Decryption

originalText = []

cipherTextBlock = []

for i in range(0,len(cipherText),16):
    cipherTextBlock.append(cipherText[i:i+16])

time0 = time.time()

for m in range(len(cipherTextBlock)) :
    cipherMatrix = np.array(cipherTextBlock[m], dtype=str).reshape((4,4)).T
    keyMatrixDecryption = np.array(roundKeys[10-0], dtype = str).reshape((4,4)).T
    
    # round 0
    
    state = []
    
    for i in range(4) :
        for j in range(4) :
            a = BitVector(hexstring=cipherMatrix[i][j])
            b = BitVector(hexstring=keyMatrixDecryption[i][j])
            result = a ^ b
            result = result.get_bitvector_in_hex()
            state.append(result)
    
    stateMatrix = np.array(state, dtype = str).reshape((4,4))
    
    # round 1 to 10
    
    for m in range(1,11) :
        
        # inverse shift row
        for i in range(1,4) :
            d = deque(stateMatrix[i])
            d.rotate(i)
            stateMatrix[i] = d
            

        # inverse substitution bytes

        for i in range(4):
            for j in range(4) :
                b = BitVector(hexstring=stateMatrix[i][j])
                int_val = b.intValue()
                s = InvSbox[int_val]
                s = BitVector(intVal=s, size=8)
                stateMatrix[i][j] = s.get_bitvector_in_hex()


        # add round key
        keyMatrixNewRound = np.array(roundKeys[10-m], dtype = str).reshape((4,4)).T

        for i in range(4) :
            for j in range(4) :
                a = BitVector(hexstring=stateMatrix[i][j])
                b = BitVector(hexstring=keyMatrixNewRound[i][j])
                result = a ^ b
                result = result.get_bitvector_in_hex()
                stateMatrix[i][j] = result
        

        

        # inverse mix column
        if m != 10 :
            another_temp = []

            for i in range(16) :
                another_temp.append("00")
            another_temp = np.array(another_temp, dtype=str).reshape((4,4))

            for i in range(4) :
                for j in range(4) :
                    for k in range(4) :
                        bv1 = InvMixer[i][k]
                        bv2 = BitVector(hexstring=stateMatrix[k][j])
                        a = bv1.gf_multiply_modular(bv2, AES_modulus, 8)
                        bv3 = BitVector(hexstring=another_temp[i][j])
                        xor = bv3 ^ a
                        another_temp[i][j] = xor.get_bitvector_in_hex()

            stateMatrix = another_temp


        


    for j in range(4) :
        for i in range(4) :
            originalText.append(stateMatrix[i][j])
    
time1 = time.time()
decryption_time = time1-time0


# deciphered text

s = ''
s = s.join(originalText)
finalText = bytearray.fromhex(s).decode()
finalLength = len(finalText) - paddingLength
decipheredText = finalText[:finalLength]

if inputType == "1" :

    b = decipheredText.encode('utf-8')

    with open('encode.bin', "wb") as file: 
        file.write(b)
    file = open('encode.bin', 'rb') 
    byte = file.read() 
    file.close() 
  
    decodeit = open("deciphered" + file_extension, 'wb') 
    decodeit.write(base64.b64decode((byte))) 
    decodeit.close() 

    print("Key scheduling time : ", key_scheduling_time)
    print("Encryption Time : ", encryption_time)
    print("Decryption time : ", decryption_time)
elif inputType == "2" :
    print("Original text : ", text)
    print("Deciphered text : ", decipheredText )
    print("Key scheduling time : ", key_scheduling_time)
    print("Encryption Time : ", encryption_time)
    print("Decryption time : ", decryption_time)


