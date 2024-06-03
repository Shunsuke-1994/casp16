# caps16 
## setup
`setup_third_parties.sh` の以下の部分を書き換えて動かす. 
```
    export BRiQ_DATAPATH=$FILEPATH/RNA-BRiQ/BRiQ_data
    export PATH=$PATH:$FILEPATH/BRiQ/build/bin  ## Change "FILEPATH" to the real path containing the compiled codes
```
RNA-BRiQ以外は使わないのでコメントアウトしてある.  
動かす際には、
```
bash setup_third_parties.sh
```

## notebooks
targetごとにnotebookを作成して解析している.  

## datasests
`datasets/casp16/R12**/pdb` の下にpdbファイルがあるようにしてある.  
notebookを参照のこと.  