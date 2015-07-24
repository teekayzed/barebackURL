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
#      deobfuscates/decodes them,               #
#      and outputs them to screen.              #
#################################################
#################################################
'''
barebackURL 
.Input full paste of submitted Potential Phish
  report and parses it to extract links
.Parses extracted links
.Outputs to screen each decoded/deobfuscated
  link
 '''

#########
# IMPORTS
#########
import sys #Needed for sys.argv for Input
import re #Needed for regex
import urllib #Needed for hex conversion
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
# MAIN
#############
# Calls other functions from above
def main(strInput):
	#print strInput
	urls = re.findall('u=(http-3A.*)&d=',strInput)
	#print urls
	output = []
	for url in urls:
		url = url.replace("-","%")
		url = url.replace("_","/")
		url = url.replace("[.]",".")
		url = urllib.unquote(url)
		output.append(url)
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
	#strInput = str(sys.stdin.readlines())
	#strInput = raw_input()
	strInput = str(sys.argv[1])
	
	#print strInput
	main(strInput)
