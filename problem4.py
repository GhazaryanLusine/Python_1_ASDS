import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--num_y", type=int)
parser.add_argument("--num_d", type=int)
args = parser.parse_args()

import datetime 
today= datetime.date.today()
if args.num_d and args.num_y:
    print(today + datetime.timedelta(days= args.num_y)*365 + datetime.timedelta(days= args.num_d))
elif args.num_d:
    print(today + datetime.timedelta(days= args.num_d))
elif args.num_y:
    print(today + datetime.timedelta(days= args.num_y)*365)

    