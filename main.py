import sys
import os

def parseargs():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)

    inputfile = sys.argv[1]
    outputfile = sys.argv[2]

    inputext = os.path.splitext(input_file)[1]
    output_ext = os.path.splitext(output_file)[1]

    if input_ext not in ['.xml', '.json', '.yml', '.yaml'] or output_ext not in ['.xml', '.json', '.yml', '.yaml']:
        print("Supported formats are: .xml, .json, .yml, .yaml")
        sys.exit(1)

    return input_file, output_file

if __name == "__main":
    input_file, output_file = parse_args()