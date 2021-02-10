import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--age", type=int)
args = parser.parse_args()

print(f"Happy birthday, you are already {args.age} years old!")