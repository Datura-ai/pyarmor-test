#!/bin/bash
# Credit to: https://medium.com/@liad_levy/reverse-pyarmor-obfuscated-python-script-using-memory-dump-technique-9823b856be7a

sudo apt install -y python3.11 python3.11-venv git
deactivate
python3.11 -m venv .venv
source .venv/bin/activate

pip install psutil
pip install cryptography
pip install pyarmor
pip install requests

# for kicks
echo "Looking for this?..."
python3 obfuscated_file.py

# gloat hehe
sleep 3

# clear the previous dump files
rm -rf *.dump;

# run the obfuscated_file.py and the memdump.py at the same time while converting the binary to readable strings
python3 obfuscated_file.py & pgrep -f obfuscated_file.py | xargs -I {} python3 memdump.py {}

# wait a moment
sleep 3

# convert the binary to readable strings
strings *.dump > process.dump

# analyze with your eyeballs
echo "Yo! Look at this..."

# grepy grep
grep -i 'miner' process.dump

# process the dump
python3 find_match.py
