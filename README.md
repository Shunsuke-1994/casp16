# caps16 
## setup
`setup_third_parties.sh` の以下の部分を書き換えて動かす. 
```
    export BRiQ_DATAPATH=$FILEPATH/RNA-BRiQ/BRiQ_data
    export PATH=$PATH:$FILEPATH/BRiQ/build/bin  ## Change "FILEPATH" to the real path containing the compiled codes
```
RNA-BRiQ以外は使わないのでコメントアウトしてある.  
RNA-BRiQに、 `BRiQ_Evaluate` というコマンドを使えるようにするために, tmpからRNA-BRiQ/execにcpするようになっている.  
動かす際には、
```
bash setup_third_parties.sh
```
で諸々入るはず(ほとんどRNA-BRiQのreadmeと同じ).  

## scripts
```
scripts
├── calc_rmsd.py
├── check_and_rerun.py
├── eval_scores.py
├── prep_data
│   ├── download_cif_from_file.py
│   ├── extract_chains_from_cif.py
│   └── run_dssr_recursive.py
└── run_briq_refine_batch.sh
```
`eval_scores.py` は、`src/RNA_BRiQ.py` を動かしている.  
他のfileは無視してください.  

## notebooks
targetごとにnotebookを作成して解析している.  
各targetに対して, `eval_scores.py`と`calc_rmsd.py` を動かす.  

## datasests
`datasets/casp16/R12**/pdb` の下にpdbファイルがあるようにしてある.  
notebookを参照のこと.  