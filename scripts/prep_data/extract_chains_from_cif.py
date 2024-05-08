import argparse
import os
from Bio import PDB

def extract_and_save_chain(cif_path, chain_id, output_path):
    parser = PDB.MMCIFParser()
    structure = parser.get_structure('PDB_structure', cif_path)
    for model in structure:
        for chain in model:
            if chain.id == chain_id:
                if len(chain_id) >1:
                    chain.id = chain_id[0] # if chain id is more than one character, only take the first character
                io = PDB.PDBIO()
                io.set_structure(chain)
                io.save(output_path)
                print(f'Successfully extracted chain {chain_id} from {cif_path} and saved to {output_path}')

def process_pdb_list(list_path, cif_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(list_path, 'r') as file:
        for line in file:
            pdb_id, chain_id = line.strip().split('_')
            cif_file_path = os.path.join(cif_dir, f'{pdb_id}.cif')
            output_file_path = os.path.join(output_dir, f'{pdb_id}_chain{chain_id}.pdb')
            if os.path.exists(cif_file_path):
                extract_and_save_chain(cif_file_path, chain_id, output_file_path)
            else:
                print(f'File {cif_file_path} does not exist')

def main():
    parser = argparse.ArgumentParser(description='Extract specified chains from CIF files and save as PDB files.')
    parser.add_argument('--filename', type=str, required=True, help='Path to the text file containing PDB IDs and chain IDs.')
    parser.add_argument('--cif-dir', type=str, required=True, help='Directory containing CIF files.')
    parser.add_argument('--output-dir', type=str, required=True, help='Directory to save the extracted PDB files.')
    args = parser.parse_args()

    process_pdb_list(args.filename, args.cif_dir, args.output_dir)

if __name__ == '__main__':
    main()

