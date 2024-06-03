#include "pred/BRFoldingTree.h"
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>

using namespace NSPforcefield;
using namespace NSPpred;
using namespace std;

void printHelp(){
    cout << "Usage: BRiQ_Evaluate $INPUT" << endl;
}

int main(int argc, char** argv){

	if(argc != 2 || argv[1] == "-h")
	{
		printHelp();
		exit(0);
	}

    string inputFile = string(argv[1]);
    //string outputPDB = string(argv[2]);

    //checkInputFile(inputFile);

    cout << "init energy table:" << endl;
    EnergyTable* et = new EnergyTable();

    cout << "init folding tree" << endl;
    BRFoldingTree* ft = new BRFoldingTree(inputFile, et);

    double shift = 0.0;
    double breakCTWT = 1.0;
    double connectWT = 1.0;
    double clashWT = 1.0;
    bool verbose = false;

    double energy = ft->totalEnergy(breakCTWT, connectWT, clashWT, shift, verbose);

    cout << "Energy: " << energy << endl;

    // BRTreeInfo* treeInfo = ft->getTreeInfo();
    // treeInfo->printPDB(outputPDB);

    delete et;
    delete ft;
    // delete treeInfo;
}