# script for eval of potential and confidence scores
# run on a batch of pdbs
import sys
import os
import argparse
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.score import cgRNASP

def main():
    parser = argparse.ArgumentParser(description='Evaluate potential scores')
    parser.add_argument('--pdb_dir', help='directory of pdb files')
    parser.add_argument('--out_dir', help='output directory')
    parser.add_argument('--print', help='print output', action='store_true')
    args = parser.parse_args()

    res_cgrnasp = cgRNASP.cgRNASP(args.pdb_dir, args.out_dir)
    res_cgrnasp_p = cgRNASP.cgRNASP_C(args.pdb_dir, args.out_dir)
    res_cgrnasp_pc = cgRNASP.cgRNASP_PC(args.pdb_dir, args.out_dir)
    if args.print:
        print(res_cgrnasp)
        print(res_cgrnasp_p)
        print(res_cgrnasp_pc)
    return 


if __name__ == '__main__':
    main()
    

