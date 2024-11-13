# pyarmor-test

in order to win the 5 $TAO bounty, you must submit a PR to this repository with your code solution. Your code solution should have a single executable file that, when ran, will take the obfuscated_file.py as an input, reverse the obfuscation, and output the original file. Include your $TAO address in your PR description as well as any necessary info needed to run the script. 

### STEPS TO REPRODUCE

# clone repo
cd $HOME
git clone https://github.com/Datura-ai/pyarmor-test
cd ./pyarmor-test

# set up venv with python 3.11
deactivate
python3.11 -m venv .venv

# activate venv
source .venv/bin/activate

# install dependencies
pip install psutil
pip install cryptography

# run the file
python3 obfuscated_file.py


# this is the output which looks like Fernet encryption, so we can decrypt it using the following code
```
gAAAAABnNB91QjN013O-it-gSZcU4g4D7V7hP-EukxHaAgZ7I7pepQ6ML_tfGP-QREQQlq_eqQkH9ofQq64RLWL2UmCcnENzM5n4ETW9UcArSvU15YiyCmb9sD_hd2SBQm5TY8L5A8bODweW8HxWFS47LkyEYjMwnRgFwPnq6CmWgaBRJ_ktaHg7JAG_EWR1TeiPSK8nrwFvYP9Z5CGPMmeYcJZV4FyAyy1N6wK9ND6JSjcWn40JZ6lFaEAjH32L9XQlRjLw-_HC7EmFwNEPT6omcygMvrkL9oP5Lh50wVTlPF3DUft1RAWIrB8Fbnktv6WbCbmd064Zs2yFbKOWhDdHepGYYAsYtVhKaJ7nAgjaZqyZSBBKzJYWaz4YAKZXFK3MLgK4aXePOw9Bmsbj6UfcvXSwcVemvXwDnvUdPBsjj3igCGOg1VUdQrWUlLHMCrFAKLJaICnEVSnxR9yTYtUih4fVyoZIDSho-CUzHLYU79AckC29980d4UPvtA84g49U7BehtO5o0EnmvB46R53bYa_K9Fvj7aVUVGFk_X_nmlACE-0taDKLWrHe70J96mq8CJKn3RYi6aq8xD6jRaRdRJg4CgyEKsdOARGCKxvrdDTwgV-6NCA4X7awn5rvXITbdCOJMuUaXMrRWrS1srEJg4iJ0niCi0a6TBu8Fv6sjWHFCGO6n0IgIAt_huSdBQQgGcvoGjPIFtMX-pzKPT5DerbnVmhXazaVdJYpUrSudb_xZ-kNMHPDxsaXijXHv-keBJrPZH6HcbyvQV3q_C_tTnToVi27N0VcfeQVNFB_0aqKVyI6LmCZAVROtVfVwY13bJepRObzTDs_4Sp1y4CQvgjEJm9cxLYyoEckaR32RhFXz-ulf5j4J8207uhi80bQcFyUTLz9cucJeYZPVw1eGlqX21H7_zlHEOuai21hSfEYSonQSlcXNiQEe53eD1ZO2RXSXd3jmaCqFrmaHE0FtkpK-IchPZv0f_Az7s28gV0-HtmkQgV7ThBTHehi5KIIt3rYOIRY4NV493Xl7uVKviRwm_-KU5dpDSWQC9ymocgOJAKh7WDI3OAWT6SN51oA4gig4DLlMA7XN0bVWc0FLCTHtC4_TqYDC9gq4pbnhtt_EgGta8bMh-BH725bllhi_PAnEqHsvD587fIQmRObRRZIIs3Ex7ofjfZba4bH4o-gm-Nn_CP1ccpZQp_L4Md-CTUrj6mrgKZhkuu__er1tbwVEA8AMHUhrocatne2eU9hh-5FfUA=
```

# now create the memdump.py file with the following code


# clear the previous dump files
rm -rf *.dump;

# run the obfuscated_file.py and the memdump.py at the same time while converting the binary to readable strings
python3 obfuscated_file.py & pgrep -f obfuscated_file.py | xargs -I {} python3 memdump.py {}

# convert the binary to readable strings
strings *.dump > process.dump

# analyze with your eyeballs
echo "Yo! Look at this..."

# grepy grep
grep -i 'miner' process.dump

# look some more

# search Datura's github

# Ding Ding Ding!
https://raw.githubusercontent.com/Datura-ai/compute-subnet/refs/heads/main/neurons/validators/src/miner_jobs/machine_scrape.py

# satisfy the criteria...so create a python script that searches for strings from the process.dump file in all repos found belonging to the Fish himself https://github.com/Datura-ai

# execute such script
python3 find_match.py

# now make an executable bash file to do all of this in one go

```bash
#!/bin/bash

sudo apt install -y python3.11 python3-venv git
cd $HOME
git clone https://github.com/Datura-ai/pyarmor-test
cd ./pyarmor-test

deactivate
python3.11 -m venv .venv
source .venv/bin/activate

pip install psutil
pip install cryptography

# for kicks
echo "Looking for this?..."
python3 obfuscated_file.py

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
```