# hex-to-b64.py
# Crypto challenges 1.1
# Kevin Graff

import sys
#import array

expected = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

# Check to make sure input is at least one character
if len(sys.argv) < 1:
	print("\tError: Requires a hex number as argument")
	sys.exit()

# Take the input and interpret it as hex, then encode to base64
input = sys.argv[1]
output = input.decode('hex').encode('base64')

# For future use if I want to encode the bits manually i'll need these
#bits = (input & 63)
#output = (input >> 4)

print("\n  Input hex string:")
print(input)

print("\n  Output and expected base64 strings:")
print(output)
print(expected)

# Decode the output to a string
print("\n  Output decoded to string:")
print(output.decode('base64'))

if(output.decode('base64') == expected.decode('base64')):
	print("\nMatch!\n")
else:
	print("\nNo match..\n")

sys.exit()
