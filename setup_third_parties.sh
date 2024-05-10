# install third parties to "third_party" directory
PARENT_DIR=$(pwd)
if [ ! -d "third_party" ];then
    mkdir -p third_party
fi
cd  third_party

##### install BRiQ #####
# https://github.com/Jian-Zhan/RNA-BRiQ?tab=readme-ov-file
if [ ! -d "RNA-BRiQ" ];then
    git clone https://github.com/Jian-Zhan/RNA-BRiQ RNA-BRiQ
    mkdir RNA-BRiQ/build/
    cd RNA-BRiQ/build/
    cmake ../
    make
    cd ../
    FILEPATH = $(pwd)
    export BRiQ_DATAPATH=$FILEPATH/RNA-BRiQ/BRiQ_data
    export PATH=$PATH:$FILEPATH/BRiQ/build/bin  ## Change "FILEPATH" to the real path containing the compiled codes

    # somtimes fail???
    wget https://apisz.sparks-lab.org:8443/downloads/Resource/RNA/2_RNA_structure_prediction/RNA-BRiQ-data.tar.gz
    tar -xvz RNA-BRiQ-data.tar.gz --one-top-level=$BRiQ_DATAPATH
fi

cd $PARENT_DIR/third_party



##### install rsRNASP #####
# https://github.com/Tan-group/rsRNASP
if [ ! -d "rsRNASP" ];then
    git clone https://github.com/Tan-group/rsRNASP.git
    cd rsRNASP
    gcc rsRNASP.c -lm -o rsRNASP
    gcc rsRNASP-batch.c -lm -o rsRNASP-batch
    cd $PARENT_DIR/third_party
fi


##### install cgRNASP #####
# https://github.com/Tan-group/cgRNASP
if [ ! -d "cgRNASP" ];then
    git clone https://github.com/Tan-group/cgRNASP.git
    cd cgRNASP
    cd cgRNASP && gcc cgRNASP.c -lm -o cgRNASP
    cd ../
    cd cgRNASP-C && gcc cgRNASP-C.c -lm -o cgRNASP-C
    cd ../
    cd cgRNASP-PC && gcc cgRNASP-PC.c -lm -o cgRNASP-PC
    cd $PARENT_DIR/third_party
fi

##### install DFIRE-RNA #####
# https://github.com/tcgriffith/dfire_rna
if [ ! -d "RASP" ];then
    git clone https://github.com/tcgriffith/dfire_rna.git
    cd dfire_rna && make 
    ./install.sh
    cd $PARENT_DIR/third_party
fi

cd $PARENT_DIR