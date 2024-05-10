import subprocess, os 

def DFIRE_RNA(pdb_dir, out_dir):
    pdb_files = " ".join([os.path.join(pdb_dir, f) for f in os.listdir(pdb_dir) if f.endswith(".pdb")])
    res = subprocess.run(f"./third_party/DFIRE_RNA/bin/DFIRE_RNA {pdb_files} > {out_dir}/energies_DFIRERNA.txt", shell = True, capture_output=True)
    return res