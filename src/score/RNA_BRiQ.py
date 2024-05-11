import os
import subprocess
import pandas as pd

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
        # add 1 line at the top of the file
        with open(self.briq_input, "r") as f:
            lines = f.readlines()
        with open(self.briq_input, "w") as f:
            f.write(f"pdb {self.input_pdb}\n")
            f.writelines(lines)
        return
    
    def Refinement(self):
        return
    
    def Predict(self):
        return
    
    def Evaluate(self):
        """
        Evaluate the potential of the RNA structure
        """
        cmd_eval_energy = f"EnergyEvaluation {self.briq_input} {self.input_pdb} > {self.briq_output}"
        res = subprocess.run(cmd_eval_energy, shell = True, capture_output=True)
        with open(self.briq_output, "r") as f:
            lines = f.readlines()

        return float(lines[-1].strip().replace("Energy: ", ""))
    
    
def RNA_BRiQ_batch(pdb_dir, out_dir):
    """
    input_dir: str
        the directory where the pdb files are stored
    """
    pdb_files = [f for f in os.listdir(pdb_dir) if f.endswith(".pdb")]
    energies = []
    for pdb_file in pdb_files:
        briq = RNA_BRiQ(os.path.join(pdb_dir, pdb_file))
        briq.AssignSS()
        energies.append(briq.Evaluate())

    df = pd.DataFrame({"pdb": pdb_files, "energy": energies})
    df.to_csv(os.path.join(out_dir, "energies_RNABRiQ.txt"), index = False, sep=" ")
    return
if __name__ == "__main__":
    # pdb_file = "/Users/sumishunsuke/Desktop/RNA/casp16/third_party/RNA-BRiQ/test/S_000001.pdb"
    # briq = RNA_BRiQ(pdb_file)
    # briq.AssignSS()
    # print(briq.Evaluate())

    pdb_dir = "/Users/sumishunsuke/Desktop/RNA/casp16/third_party/RNA-BRiQ/test"
    out_dir = "/Users/sumishunsuke/Desktop/RNA/casp16/third_party/RNA-BRiQ/test"
    RNA_BRiQ_batch(pdb_dir, out_dir)

