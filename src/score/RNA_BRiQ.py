import subprocess, os

def RNA_BRiQ(pdb_dir, out_dir):
    pdb_files = " ".join([os.path.join(pdb_dir, f) for f in os.listdir(pdb_dir) if f.endswith(".pdb")])
    res = subprocess.run(f"./third_party/RNA-BRiQ/RNA-BRiQ {pdb_files} > {out_dir}/energies_RNABRiQ.txt", shell = True, capture_output=True)
    return res