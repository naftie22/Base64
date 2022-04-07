import argparse
import base64


def encode(text)-> str:
	
	enc_text = base64.b64encode(bytes(u'{}'.format(text), "utf-8"))
	return enc_text

def decode(coded_string)-> str:
	decoded_text = base64.b64decode(coded_string)
	return decoded_text



def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--text", type=str, required=True, help="text to be encoded and decoded")
	parser.add_argument("--decode", help="text to be decoded", action="store_true")
	parser.add_argument("--encode", help="choose whether to encode given text", action="store_true")
	args = parser.parse_args()

	if args.encode:
		etext = encode(args.text)
		print(etext.decode('UTF-8'))

	elif args.decode:
		decoded_text = decode(args.text)
		print(decoded_text.decode('UTF-8'))

	else:
		print("No encode/decode option specified. Exiting...")

if __name__ == '__main__':
	main()