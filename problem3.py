import argparse

parser = argparse.ArgumentParser()
parser.add_argument("text", type=str)
args = parser.parse_args()

print("The given text:", args.text)
print("All lowercase:", args.text.lower())
print("All uppercase:", args.text.upper())