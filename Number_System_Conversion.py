
'''
Four types of number system.
--Binary ==>Base 2 (0,1)
--Decimal ==> Base 10 (0-9)
--Octal ==> Base 8 (0-7)
--Hexadecimal ==> 16 (0-9,A,B,C,D,E,F)
'''

#Converting Decimal to Binary:


print(bin(25))      #We use "bin()" function for making "Binary" and the reuslt is "0b11001"
                    #0b==> Binary and 11001==>25

#Converting Binary to Decimal:

print(0b11001)      #We write 0b11001 for making Binary to Decimal and the result is "25"

#Converting Decimal to Octal:

print(oct(25))      #We use "oct()" function for making "Octal" and the result is "0o31"
                    #0o==> Octal and 31==>25

#Converting Octal to Decimal:

print(0o31)         #We write 0o31 for making Octal to Decimal and the result is "25"

#Converting Decimal ot Hexadecimal:

print(hex(25))      #We use "hex()" function for making "Hexadecimal" and the result is "0x19"
                    #0x==> Hexadecimal and 19==>25

#Converting Hexadecimal to Decimal:

print(0x19)         #We write 0x19 for making Hexadecimal to Decimal and the result is "25"

#Converting Binary to Hexadecimal:

print(hex(0b101101))    #We write hex(0b101101) for making Binary to Hexadecimal and the result is "0x2d"


'''
So by using these functions we can convert one number system to another number system.
The functions are:
--bin()
--oct()
--hex()
'''
