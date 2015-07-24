#! /usr/bin/python
#################################################
#                 barebackURL                   #
#################################################
# teekayzed                                     #
# teekayzed@users.noreply.github.com            #
#                                               #
# Features:                                     #
#   - Takes Proofpoint protected URLs from      #
#      submitted Potential Phish report         #
#      and saves them in run directory          #
#################################################
#################################################
'''
barebackURL 
.Input full paste of submitted Potential Phish
  report and parses it to extract links
.Parses extracted links
.Outputs to screen each decoded/deobfuscated
  link

	

#######################
#  TO DO LIST
#  --Item To Do
#  
#  --Figure out input methods
#    --ARGS for input from textfile
#    --If no textfile then input from
#       echo command
#  --Function for regex extraction
#  --Function to make it hex encoded
#  --Function for hex conversion
#    --ARG for convert to and convert
#       from
#
#######################
'''

#########
# IMPORTS
#########
import sys #Needed for getArgs
import re #Needed for regexExtract
import urllib #Needed for hexConvert
#########
# VARS
#########
programName="barebackURL.py"
programDescription="Accept input of Proofpoint protected links and output normal links"
programVersion="1.0"

verbose=False


##################################################
# FUNCTIONS
##################################################

#############
# GET ARGS
#############1
# Requirements:
## import sys
def getArgs():
	parser = argparse.ArgumentParser(prog=programName, description=programDescription)
	parser.add_argument("-a","--arg",help="ARG HELP",required=False)
	parser.add_argument("-v","--verbose",help="Increase verbosity",action="store_true",required=False)

	return parser.parse_args()

	###############################################
	# OTHER NOTES 
	# 
	# For groups of args [in this case one of the two is required]:
	# group = parser.add_mutually_exclusive_group(required=True)
	# group.add_argument("-a1", "--arg1", help="ARG HELP")
	# group.add_argument("-a2", "--arg2", help="ARG HELP")
	#
	# To make a bool thats true:
	# parser.add_argument("-a","--arg",help="ARG HELP", action="store_true")
	#
	###############################################

#############
# END OF ARGS
#############

#############
# REGEX EXTRACTION
#############
# Requirements:
## import re
def regexExtract(regex,strInput):
	#print strInput
	output = re.findall(regex,strInput)
	return output

#############
# END OF REGEX EXTRACTION
#############


#############
# characterReplace
#############
#Character replacement
# EX: characterReplace(string,"-","%")
def characterReplace(strInput,origChar,replacementChar):
	strOutput = strInput.replace(origChar,replacementChar)
	return strOutput

#############
# END OF PERCENT ENCODING
#############


#############
# HEX CONVERSION
#############
# Requirements:
## import urllib
def hexConvert(strInput):
	strInput = urllib.unquote(strInput)
	return strInput

#############
# END HEX CONVERSION
#############


#############
# MAIN
#############
# Calls other functions from above
def main():
	strInput = """
https://urldefense[.]proofpoint[.]com/v2/url?u=http-3A__www[.]google[.]com_&d=hdfskhafdslhkafdslhafdsflhfdsalhfadslhkfdsahjlfdsalhfdsalhfdsalhdfsalhfadslh"""

	urls = regexExtract('u=(http-3A.*)&d=',strInput)
	#print urls
	output = []
	for url in urls:
		url = characterReplace(url,"-","%")
		url = characterReplace(url,"_","/")
		url = characterReplace(url,"[.]",".")
		url = hexConvert(url)
		output.append(url)
	print "Output time!!!!!"
	print output
	for element in output:
		print element

#############
# END OF MAIN
#############



##################################################
# END OF FUNCTIONS
##################################################


###########################
# PROG DECLARE
###########################
if __name__ == '__main__':
	#args = getArgs()
	main()
	
