#!/usr/bin/env bash

if [ "$EUID" -ne 0 ]
  then echo "Please run with sudo!"
  exit
fi


echo "Destroying existing mininet topology..."
mn -c

echo "Generating network traces..."

# Run the kernel server against various attackers.

python runner.py --server=kernel --client=opt-ack




echo "Creating graphs..."
python create_graphs.py
