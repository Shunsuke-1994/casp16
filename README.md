# caps16 
## setup
ほとんどRNA-BRiQのreadmeの記述と同一.  
`setup_third_parties.sh` の以下の部分, FILEPATH=$(pwd)となるようにしてある.  
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
### `scripts/eval_scores.py`
```
python scripts/eval_scores.py \
    --pdb_dir ./test \
    --out_dir ./test \
    --print \
    --cpu 2
```
`pdb_dir`にある全てのpdbファイルに対して, RNA-BRiQを実行する.  
`out_dir` にbriq入力ファイルとその出力が出てくる(.briq.in, .briq.out).  
.briq.outの最後の行にエネルギーの記載があるのでそれを読み込んでtxt,csvに書き出す.  

### `scripts/calc_rmsd.py`
```
python scripts/calc_rmsd.py \
    --pdb_dir ./test \
    --cpu 2 \
    --print_every 10
```
`pdb_dir` の全てのpdbファイルに対して, (N,N)の距離行列を計算する. print_enery毎にprintする.  
pdb_dirに, pdb idでソートされた距離行列がnpy, dfで出力される.  


## notebooks
targetごとにnotebookを作成して解析している.  
各targetに対して, `eval_scores.py`と`calc_rmsd.py` を動かす.  

## datasests
`datasets/casp16/R12**/pdb` の下にpdbファイルがあるようにしてある.  
notebookを参照のこと.  