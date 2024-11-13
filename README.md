# pyarmor-test

in order to win the 5 $TAO bounty, you must submit a PR to this repository with your code solution. Your code solution should have a single executable file that, when ran, will take the obfuscated_file.py as an input, reverse the obfuscation, and output the original file. Include your $TAO address in your PR description as well as any necessary info needed to run the script. 


## Challenge accepted!:

### clone repo
```bash
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
```

### this is the output which looks like Fernet encryption, so we can decrypt it using the following code
```
gAAAAABnNB-...
```

### research a bit and create the memdump.py

### clear the previous dump files
```bash
rm -rf *.dump
```

### run the obfuscated_file.py and the memdump.py at the same time while converting the binary to readable strings
```bash
python3 obfuscated_file.py & pgrep -f obfuscated_file.py | xargs -I {} python3 memdump.py {}
```

### convert the binary to readable strings
```bash
strings *.dump > process.dump
```

### analyze the dump with your eyeballs and think

### grepy grep
```bash
grep -i 'miner' process.dump
```

### ...look some more

### search Datura's github!

### Ding Ding Ding! We have a winner!
```bash
https://raw.githubusercontent.com/Datura-ai/compute-subnet/refs/heads/main/neurons/validators/src/miner_jobs/machine_scrape.py
```

 ok but we must satisfy the criteria...so create a python script that searches for strings from the process.dump file in all repos found belonging to the Fish himself https://github.com/Datura-ai

### go into a frenzie, build, test, execute such script
python3 find_match.py

### now make an executable bash file to do all of this in one go

So now you can just run:
```bash
./doit.sh
```
🫡

-siruok
