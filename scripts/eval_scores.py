# script for eval of potential and confidence scores
# run on a batch of pdbs
import sys
import os
import argparse
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.score import DFIER_RNA, RNA_BRiQ, rsRNASP, cgRNASP

def main():
    parser = argparse.ArgumentParser(description='Evaluate potential scores')
    parser.add_argument('pdb_dir', help='directory of pdb files')
    parser.add_argument('out_dir', help='output directory')
    return 


if __name__ == '__main__':
    main()
    

