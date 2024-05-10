import subprocess
import os

def rsRNASP(pdb_dir, out_dir):
    num_pdb_files = len([f for f in os.listdir(pdb_dir) if f.endswith(".pdb")])
    res = subprocess.run(f"./third_party/rsRNASP/rsRNASP-batch {pdb_dir} {num_pdb_files} {out_dir}/energies_rsRNASP.txt", shell = True, capture_output=True)
    return res
