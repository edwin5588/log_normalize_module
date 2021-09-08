import pandas as pd

from log_normalize_func.py import *
import argparse
import humanfriendly


parser = argparse.ArgumentParser()
# ~~~~Module Required Arguments~~~~~ #
parser.add_argument("-f", "--filename",
                    type=str,
                    help="Name of the file to be read")

parser.add_argument("-o", "--output_filename",
                    type=str,
                    help="The basename to use for output file")



print("~~~~~~~~~~~~~~~~~~~~~~")
print("Using arguments:")
print(args)
print("Now getting work done.")
print("~~~~~~~~~~~~~~~~~~~~~~")

args = parser.parse_args()

out_filename = args.output_filename
if not out_filename.endswith('.txt'):
    out_filename = out_filename + '.txt'



in_data = pd.read_csv(args.filename)
out_df = log_normalize(in_data)
out_name = args.output_filename + ".gct"

out_df.to_csv(out_name)

print("Process completed. " + (out_name) + " is outputted. ")
