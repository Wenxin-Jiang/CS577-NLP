#!/bin/bash

# Change to the directory containing the zip files
cd /scratch/gilbreth/jiang784/PTMTorrent/huggingface

# Loop through all .tar.gz files and extract them
for file in *.tar.gz; do
  echo "Extracting $file"
  tar -xzf "$file"
done

echo "Extraction completed"
