import os, sys, argparse, numpy, h5py, biom

def tojson(input_data):
    table = biom.parse.parse_biom_table(input_data)
    table.type = "Table"
    result = table.to_json(biom.parse.generatedby())
    return result

parser = argparse.ArgumentParser(description='handle input')
parser.add_argument('input', metavar='I', type=str, help='input')
args = parser.parse_args()

if h5py.is_hdf5(args.input):
  with h5py.File(args.input) as h5_file:
    json = tojson(h5_file)
    h5_file.close()
else:
  with open(args.input, 'r') as file:
    json = file.read()
    file.close()

print json

sys.exit()
