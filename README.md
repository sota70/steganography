# Space Replacing Steganography
This is a script that allows you to hide secret message in other text file.<br />
The script breaks secret message down to binary level then replace the binary with 2 different spaces<br />
then put them in other text file which is called cover file.

# Usage
python3 text_steg.py [hide | seek] [options]

## Hide secret message:<br />
python3 text_steg.py -o [output path] -s [secret message file path] -c [cover file path]<br />
ex) python3 text_steg.py -o hidden_text.txt -s secret.txt -c cover.txt<br />

## Discover secret message:<br />
python3 text_steg.py -o [output path] -s [file path secret message is hidden]<br />
ex) python3 text_steg.py -o discovered_text.txt -s hidden_text.txt<br />
