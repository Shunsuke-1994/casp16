import os
import subprocess
import argparse

# DSSRの実行コマンド
dssr_command = "x3dna-dssr -i={input_file} -o={output_file}"

# 再帰的にPDBファイルを探索し、DSSRを実行する関数
def run_dssr_recursive(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".pdb"):
                pdb_file = os.path.join(root, file)
                dssr_output = os.path.splitext(pdb_file)[0] + ".out"
                
                # DSSRコマンドを実行
                command = dssr_command.format(input_file=pdb_file, output_file=dssr_output)
                subprocess.run(command, shell=True)

# コマンドライン引数のパーサーを作成
parser = argparse.ArgumentParser(description="Run DSSR recursively on PDB files in a directory.")
parser.add_argument("directory", help="Directory containing PDB files")

# コマンドライン引数を解析
args = parser.parse_args()

# 指定されたディレクトリをルートとして、DSSRを再帰的に実行
run_dssr_recursive(args.directory)