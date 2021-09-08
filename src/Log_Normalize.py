import pandas as pd

from log_normalize_func import *
import argparse
import humanfriendly


parser = argparse.ArgumentParser()
# ~~~~Module Required Arguments~~~~~ #
parser.add_argument("-f", "--filename",
                    type=str,
                    help="Name of the file to be read")

parser.add_argument("-o", "--output_filename",
                    type=str,
                    help="The basename to use for output file",
                    default = "out")


args = parser.parse_args()


print("~~~~~~~~~~~~~~~~~~~~~~")
print("Using arguments:")
print(args)
print("Now getting work done.")
print("~~~~~~~~~~~~~~~~~~~~~~")

if args.filename != None:

    in_data = read_gct(args.filename)
    out_df = log_normalize(in_data)
    out_name = args.output_filename + ".gct"

    out_df.to_csv(out_name)

    print("Process completed. " + (out_name) + " is outputted. ")
else:
    print("Nothing is inputted!")
