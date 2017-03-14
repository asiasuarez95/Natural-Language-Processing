# Find all dollar amounts and phone numbers in a document and place brackets [] around them


#This command places brackets,[], around matches of the regular expressions.
#It then writes the new bracketed text into a file, that must be previously created
#called output_dollar.txt. 
import nltk
import re

regex = '(\$)(\d+)(((\.)(\d+)))?(((,)(\d+)))?(((,)(\d+)(\.)(\d+)))?( )?(((hundred)?(thousand)?(million)?(billion)? ?(dollars)?))?(((dollar)?(dollars))?)?( )?((and)?)?( )?((\d+))?( )?((cents)?)?'
pattern = re.compile(regex)
with open('test_dollar_phone_corpus.txt', 'r+', newline='', encoding='utf-8') as inputFile:
	with open('output_dollar.txt','r+', newline='', encoding='utf-8') as outputFile:
		lines = inputFile.read()
		for match in re.finditer(pattern, lines):
			lines = lines.replace(match.group(), "[" + str(match.group()) + "]")
		outputFile.write(lines)

#This part of the program takes and writes all of the matches on individual lines 
#of the regex  into a file, that must already exist, called dollar.txt

with open('test_dollar_phone_corpus.txt', 'r+') as inputFile:
	with open('dollar.txt','r+', newline='', encoding='utf-8') as outputDollarFile:
		line = inputFile.readlines()
		line = str(lines)
		for match in re.finditer(pattern, line):
			outputDollarFile.write(match.group() + "\n")
#This program places brackets,[], around matches of the regular expressions.
#It then writes the new bracketed text into a file, that must be previously created
#called output_phone.txt. 

regex = '((\()?[0-9][0-9][0-9]\)?)? ?-?\.?[0-9][0-9][0-9] ?\.?-?[0-9][0-9][0-9][0-9]?'
pattern = re.compile(regex)

with open('test_dollar_phone_corpus.txt', 'r+', newline='', encoding='utf-8') as inputFile:
	with open('output_phone.txt','r+', newline='', encoding='utf-8') as outputFile:
		lines = inputFile.read()
		for match in re.finditer(pattern, lines):
			lines = lines.replace(match.group(), "[" + str(match.group()) + "]")
		outputFile.write(lines)

with open('test_dollar_phone_corpus.txt', 'r+', newline='', encoding='utf-8') as inputFile:	
	with open('phone.txt','r+', newline='', encoding='utf-8') as outputPhoneFile:
		line = inputFile.readlines()
		line = str(lines)
		for match in re.finditer(pattern, line):
			outputPhoneFile.write(match.group() + "\n")