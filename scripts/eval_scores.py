# script for eval of potential and confidence scores
# run on a batch of pdbs
import sys
import os
import argparse
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.score import cgRNASP, rsRNASP, DFIRE_RNA, RNA_BRiQ

def summarize_scores(out_dir):
    """
    convert the output of the scores to a csv file
    """
    score_files = [f for f in os.listdir(out_dir) if f.endswith(".txt")]
    dict_name = {
        "energies_cgRNASP.txt": "cgRNASP[kBT]",
        "energies_cgRNASP-P.txt": "cgRNASP-P[kBT]",
        "energies_cgRNASP-PC.txt": "cgRNASP-PC[kBT]",
        "energies_rsRNASP.txt": "rsRNASP[kBT]",
        "energies_DFIRERNA.txt": "DFIRE_RNA",
        "energies_RNABRiQ.txt": "RNA_BRiQ"
    }
    
    for score_file in score_files:

        if "RNASP" in score_file:
            df = pd.read_table(os.path.join(out_dir, score_file), sep="     ", header=None)
            df.columns = ["pdb", dict_name[score_file]]
            df[dict_name[score_file]] = [float(f.split(" ")[0]) for f in df[dict_name[score_file]]] # remove the unit
        elif score_file == "energies_DFIRERNA.txt":
             # ignore last "  "
            df = pd.read_table(os.path.join(out_dir, score_file), sep=" ", header=None)
            df.columns = ["pdb", dict_name[score_file], "0", "1"]
            df.drop(columns=["0", "1"], inplace=True)
            df["pdb"] = [f.split("/")[-1] for f in df["pdb"]]
        # elif score_file == "energies_RNABRiQ.txt":
        #     break

        if score_file == score_files[0]:
            df_all = df
        else:
            df_all = pd.merge(df_all, df, on="pdb", how="outer")
    df_all.to_csv(os.path.join(out_dir, "energies_summary.csv"), index=False)
    return 

def main():
    parser = argparse.ArgumentParser(description='Evaluate potential scores')
    parser.add_argument('--pdb_dir', help='directory of pdb files')
    parser.add_argument('--out_dir', help='output directory')
    parser.add_argument('--print', help='print output', action='store_true')
    args = parser.parse_args()

    # cgRNASP
    res_cgrnasp = cgRNASP.cgRNASP(args.pdb_dir, args.out_dir)
    res_cgrnasp_c = cgRNASP.cgRNASP_C(args.pdb_dir, args.out_dir)
    res_cgrnasp_pc = cgRNASP.cgRNASP_PC(args.pdb_dir, args.out_dir)
    # rsRNASP
    res_rsrnasp = rsRNASP.rsRNASP(args.pdb_dir, args.out_dir)
    # dfire_rna
    res_dfire = DFIRE_RNA.DFIRE_RNA(args.pdb_dir, args.out_dir)
    # RNA_BRiQ
    # res_rnabriq = RNA_BRiQ.RNA_BRiQ(args.pdb_dir, args.out_dir)

    if args.print:
        print("cgRNSP\t:",res_cgrnasp.stdout.decode('utf-8'))
        # print("cgRNASP\t:",res_cgrnasp.stderr.decode('utf-8'))
        print("cgRNASP-C\t:",res_cgrnasp_c.stdout.decode('utf-8'))
        # print("cgRNASP-C\t:",res_cgrnasp_c.stderr.decode('utf-8'))
        print("cgRNASP-PC\t:",res_cgrnasp_pc.stdout.decode('utf-8'))
        # print("cgRNASP-PC\t:",res_cgrnasp_pc.stderr.decode('utf-8'))
        print("rsRNASP\t:",res_rsrnasp.stdout.decode('utf-8'))
        # print("rsRNASP\t:",res_rsrnasp.stderr.decode('utf-8'))
        # print("DFIRE_RNA\t:",res_dfire.stdout.decode('utf-8'))

    summarize_scores(args.out_dir)
    return 

if __name__ == '__main__':
    main()
    

