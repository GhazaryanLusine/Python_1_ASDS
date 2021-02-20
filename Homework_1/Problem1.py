import argparse

parser = argparse.ArgumentParser()
parser.add_argument("text",type=str)
parser.add_argument("first_word", type=str)
parser.add_argument("second_word", type=str)
args = parser.parse_args()

print(f"The given text: {args.text}")
print(f"First word:{args.first_word}")
print(f"Second word:{args.second_word}")
print(f"Output string: {args.text.replace(args.first_word,args.second_word)}")