import argparse
import sys

def main(args):
    print(args.opts)
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Add a mandatory argument --input that takes a glob pattern of files or it is repeated for many files
    parser.add_argument("--input", help="input files globs", nargs="+", default=["file1", "file2"])
    # Add a mandatory argument --output that takes a single directory
    parser.add_argument("--output", help="output directory for pdf files", default="output")
    # Add an optional argument than can be repeated names --strings that takes a case sensitive token as input
    parser.add_argument("--names", help="Takes one or more case sensitive tokens as input", nargs="+", default=["Bill", "Clinton"])
    # Add an optional argument called --entities/no-entities that retreives a asks the program to get all entities
    parser.add_argument("--entities", help="Get all entities", action="store_true")
    # Add an optional flag --coref/no-coref that asks the program to redact all coreferences
    parser.add_argument("--coref", help="Redact all coreferences", action="store_true")
    # Add an optional flag --stats that specifies the location of the stats file containing the information about redacted tokens. By default, it should write to the standard error file.
    parser.add_argument("--stats", help="Specify the location of the stats file", default=sys.stderr)
    

    args = parser.parse_args()
    print(args)
