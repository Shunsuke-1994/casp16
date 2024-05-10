import subprocess
import os

def cgRNASP(pdb_dir, out_dir):
    num_pdb_files = len([f for f in os.listdir(pdb_dir) if f.endswith(".pdb")])
    res = subprocess.run(f"./third_party/cgRNASP/cgRNASP/cgRNASP {pdb_dir} {num_pdb_files} {out_dir}/energies_cgRNASP.txt", shell = True, capture_output=True)
    return res

def cgRNASP_C(pdb_dir, out_dir):
    num_pdb_files = len([f for f in os.listdir(pdb_dir) if f.endswith(".pdb")])
    res = subprocess.run(f"./third_party/cgRNASP/cgRNASP-C/cgRNASP-C {pdb_dir} {num_pdb_files} {out_dir}/energies_cgRNASP-P.txt", shell = True, capture_output=True)
    return res


def cgRNASP_PC(pdb_dir, out_dir):
    num_pdb_files = len([f for f in os.listdir(pdb_dir) if f.endswith(".pdb")])
    res = subprocess.run(f"./third_party/cgRNASP/cgRNASP-PC/cgRNASP-PC {pdb_dir} {num_pdb_files} {out_dir}/energies_cgRNASP-PC.txt", shell = True, capture_output=True)
    return res


