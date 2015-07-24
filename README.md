# barebackURL
Proofpoint URL de-obfuscation. Removes the Proofpoint URL re-write provided by URLDefense.


# Usage
python barebackURL.py "https://urldefense[.]proofpoint[.]com/v2/url?u=http-3A__www[.]google[.]com_&d=hdfskhafdslhkafdslhafdsflhfdsalhfadslhkfdsahjlfdsalhfdsalhfdsalhdfsalhfadslh"

# Sample Output:
"http://www.google.com/"
