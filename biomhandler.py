import os
import sys
import argparse
import numpy
import h5py
import biom

def tojson(input_data):
    table = biom.parse.parse_biom_table(input_data)
    table.type = "Table"
    result = table.to_json(biom.parse.generatedby())
    return result

parser = argparse.ArgumentParser(description='handle input')
parser.add_argument('input', metavar='I', type=str, help='input')
args = parser.parse_args()

if h5py.is_hdf5(args.input):
    with h5py.File(args.input, 'r') as h5_file:
        json_data = tojson(h5_file)
else:
    with open(args.input, 'r') as file:
        json_data = file.read()

print(json_data)
sys.exit()
