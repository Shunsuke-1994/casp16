import os
import numpy as np
from Bio.PDB import PDBParser, Superimposer
from multiprocessing import Pool


def calculate_rmsd(args):
    import warnings
    warnings.filterwarnings('ignore')

    parser = PDBParser()
    sup = Superimposer()

    pdb_dir, pdb_files, i, j = args
    if (j == i+1) and (i%10 == 0):
        print(f"Calculating RMSD for {i}th pdb file")
    structure1 = parser.get_structure('X', os.path.join(pdb_dir, pdb_files[i]))
    atoms1 = list(structure1.get_atoms()) #[atom for atom in structure1.get_atoms()]
    structure2 = parser.get_structure('Y', os.path.join(pdb_dir, pdb_files[j]))
    atoms2 = list(structure2.get_atoms())
    sup.set_atoms(atoms1, atoms2)
    sup.apply(atoms2)
    return i, j, sup.rms

if __name__ == '__main__':
    import argparse
    import os
    import numpy as np 
    import warnings
    warnings.filterwarnings('ignore')

    parser = argparse.ArgumentParser(description='Calculate RMSD')
    parser.add_argument('--pdb_dir', help='directory of pdb files')
    parser.add_argument('--cpu', help='number of cpus', default=7, type=int)
    args = parser.parse_args()

    pdb_files = [f for f in os.listdir(args.pdb_dir) if f.endswith(".pdb")]
    pdb_files.sort()
    print(pdb_files[:5])
    n = len(pdb_files)
    # n = 60
    print(f"Number of pdb files: {n}")
    rmsd_matrix = np.zeros((n, n))
    print(f"Calculating RMSD matrix {n}x{n} using {args.cpu} cpus")

    with Pool(args.cpu) as pool:
        results = pool.map(calculate_rmsd, [(args.pdb_dir, pdb_files, i, j) for i in range(n) for j in range(i+1, n)])

    for i, j, rmsd in results:
        rmsd_matrix[i, j] = rmsd
        rmsd_matrix[j, i] = rmsd

    np.save(os.path.join(args.pdb_dir, "rmsd_matrix_sorted_id.npy"), rmsd_matrix)
    print("RMSD matrix saved")


