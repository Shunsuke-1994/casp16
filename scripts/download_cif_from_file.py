import argparse
import requests
import time
import os

def download_cif(pdb_id, save_dir):
    url = f'https://files.rcsb.org/download/{pdb_id}.cif'
    response = requests.get(url)
    if response.status_code == 200:
        filepath = os.path.join(save_dir, f'{pdb_id}.cif')
        with open(filepath, 'wb') as file:
            file.write(response.content)
        print(f'{pdb_id} downloaded successfully to {filepath}.')
    else:
        print(f'Failed to download {pdb_id}.')

def read_pdb_list(filename):
    with open(filename, 'r') as file:
        pdb_ids = [line.strip().split('_')[0] for line in file.readlines()]
    return pdb_ids

def main():
    parser = argparse.ArgumentParser(description='Download PDB files from a list of PDB IDs in a text file.')
    parser.add_argument('--filename', type=str, help='The filename of the text file containing the list of PDB IDs.')
    parser.add_argument('--save_dir', type=str, help='The directory to save the downloaded PDB files.')
    args = parser.parse_args()

    if not os.path.exists(args.save_dir):
        os.makedirs(args.save_dir)

    pdb_ids = read_pdb_list(args.filename)
    for pdb_id in pdb_ids:
        download_cif(pdb_id, args.save_dir)
        time.sleep(1)  # Wait for 1 second before the next download

if __name__ == '__main__':
    main()

