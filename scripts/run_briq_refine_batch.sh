#!/bin/bash

run_briq_refinement() {
    local pdb_file=$1
    local base_name="${pdb_file%.*}"
    local briq_in_file="${base_name}.briq.in"
    local briq_refine_pdb="${base_name}.briq.refine.pdb"
    local log_file="${base_name}_briq_refine.log"

    BRiQ_Refinement "${briq_in_file}" "${briq_refine_pdb}" 42 > "$log_file" 2>&1
}

export -f run_briq_refinement

if [ $# -ne 2 ]; then
    echo "Usage: $0 <directory> <nproc>"
    exit 1
fi

directory=$1
nproc=$2

find "$directory" -maxdepth 1 -type f -name "*.pdb" | xargs -I{} -P "$nproc" bash -c 'run_briq_refinement "$@"' _ {}