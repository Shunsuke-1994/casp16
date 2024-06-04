import os
import subprocess
import pandas as pd
from multiprocessing import Pool
import time 

class RNA_BRiQ:
    def __init__(self, input_pdb, random_seed = 42):
        self.input_pdb = input_pdb
        self.random_seed = random_seed
        self.briq_input = input_pdb.replace(".pdb", ".briq.in")
        self.briq_output= input_pdb.replace(".pdb", ".briq.out")

    def AssignSS(self):
        """BRiQ_AssignSS $INPUTPDB $OUTFILE"""
        cmd = f"BRiQ_AssignSS {self.input_pdb} {self.briq_input}"
        res = subprocess.run(cmd, shell = True, capture_output=True)
        # print(res)
        # add 1 line at the top of the file
        with open(self.briq_input, "r") as f:
            lines = f.readlines()
        with open(self.briq_input, "w") as f:
            f.write(f"pdb {self.input_pdb}\n")
            f.writelines(lines)
        return
    
    def Refinement(self):
        briq_refinement_pdb = self.briq_input.replace(".briq.in", ".briq.refined.pdb")
        cmd = f"BRiQ_Refinement {self.briq_input} {briq_refinement_pdb} {self.random_seed}"
        res = subprocess.run(cmd, shell = True, capture_output=True)
        return res
    
    def Predict(self):
        return
    
    def Evaluate(self):
        """
        Evaluate the potential of the RNA structure
        """
        cmd_eval_energy = f"BRiQ_Evaluate {self.briq_input} > {self.briq_output}"
        res = subprocess.run(cmd_eval_energy, shell = True, capture_output=True)
        # with open(self.briq_output, "r") as f:
        #     lines = f.readlines()

        # return float(lines[-1].strip().replace("Energy: ", ""))
    
    
def process_pdb_file_eval(pdb_file):
    briq = RNA_BRiQ(pdb_file)
    briq.AssignSS()
    energy = briq.Evaluate()
    return os.path.basename(pdb_file), energy

def RNA_BRiQ_eval_batch(pdb_dir, out_dir, cpu=7):
    """ input_dir: str the directory where the pdb files are stored """
    pdb_files = [os.path.join(pdb_dir, f) for f in os.listdir(pdb_dir) if f.endswith(".pdb")]
    print(os.listdir(pdb_dir)[:4])
    with Pool(cpu) as pool:
        _ = pool.map(process_pdb_file_eval, pdb_files)


    out_files = [f for f in os.listdir(pdb_dir) if f.endswith(".briq.out")]
    pdbs_energies = []
    for out_file in out_files:
        with open(os.path.join(out_file, f), "r") as f:
            lines = f.readlines()
        energy = float(lines[-1].strip().replace("Energy: ", ""))
        pdbs_energies.append(
            (out_file.replace(".briq.out", ""), energy)
            )

    
    pdb_names, energies = zip(*pdbs_energies)
    df = pd.DataFrame({"pdb": pdb_names, "energy": energies})
    df.to_csv(os.path.join(out_dir, "energies_RNABRiQ.txt"), index=False, sep=" ")
    return


def RNA_BRiQ_refinement_batch(pdb_dir, out_dir):
    """
    input_dir: str
        the directory where the pdb files are stored
    """
    pdb_files = [f for f in os.listdir(pdb_dir) if f.endswith(".pdb")]
    energies = []
    for pdb_file in pdb_files:
        briq = RNA_BRiQ(os.path.join(pdb_dir, pdb_file))
        briq.AssignSS()
        briq.Refinement()
        # energies.append(briq.Evaluate())

    return

if __name__ == "__main__":
    # pdb_file = "/Users/sumishunsuke/Desktop/RNA/casp16/third_party/RNA-BRiQ/test/S_000001.pdb"
    # briq = RNA_BRiQ(pdb_file)
    # briq.AssignSS()
    # print(briq.Evaluate())

    pdb_dir = "/Users/sumishunsuke/Desktop/RNA/casp16/datasets/casp16/R1203_newMXfold2_pdb/AF3_FF2_HybridStructures"
    out_dir = "/Users/sumishunsuke/Desktop/RNA/casp16/datasets/casp16/R1203_newMXfold2_pdb/AF3_FF2_HybridStructures/scores"
    # RNA_BRiQ_eval_batch(pdb_dir, out_dir)
    RNA_BRiQ_eval_batch(pdb_dir, out_dir)
