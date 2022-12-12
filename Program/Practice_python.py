import argparse
parser = argparse.ArgumentParser(prog='Practice.py',description='Please enter the path to specify the context of file')
parser.add_argument('ls')
args = parser.parse_args()
print(args.ls)