# Space Replacing Steganography
This is a script that allows you to hide secret message in other text file.
The script breaks secret message down to binary level then replace the binary with 2 different spaces
then put them in other text file which is called cover file.

# Usage
python3 text_steg.py [hide | seek] [options]

Hide secret message:
python3 text_steg.py -o [output path] -s [secret message file path] -c [cover file path]
ex) python3 text_steg.py -o hidden_text.txt -s secret.txt -c cover.txt

Discover secret message:
python3 text_steg.py -o [output path] -s [file path secret message is hidden]
ex) python3 text_steg.py -o discovered_text.txt -s hidden_text.txt
