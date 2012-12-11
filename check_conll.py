#!/usr/bin/python
#
# Copyright 2012 Michele Filannino
#  
# gnTEAM, School of Computer Science, University of Manchester.
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the GNU General Public License.
#	
# authors: Michele Filannino
# email:  filannim@cs.man.ac.uk
#		
# For details, see http://www.cs.man.ac.uk/~filannim/

import re
import sys

class CoNLL_sentence:

	def __init__(self, sentence, line_number):
		self.sentence = []
		self.corrupted = False
		self.length = 0
		self.start_line = line_number

		conll = sentence.strip().split('\n')
		self.length = len(conll)
		line_counter = 1
		for conll_line in conll:
			line = conll_line.strip().split('\t')
			if not(len(line)==8 or len(line)==10):
				self.corrupted = True
				if len(line)>1:
					print str(self.start_line+line_counter-1), '** wrong line dimension **', line
				break
			
			#ID
			if (not(re.match('[0-9]+',line[0].strip())) or line[0]!=str(line_counter).strip()):
				self.corrupted = True
				print str(self.start_line+line_counter-1), '** wrong ID format **', line
				break
			
			#FORM
			if (not(re.match('.+',line[1]))):
				self.corrupted = True
				print str(self.start_line+line_counter-1), '** wrong FORM content **', line
				break
					
			#LEMMA
			if (not(re.match('.+',line[2]))):
				self.corrupted = True
				print str(self.start_line+line_counter-1), '** wrong LEMMA content **', line
				break

			#CPOSTAG
			if (not(re.match('[A-Za-z-+]|_',line[3]))):
				self.corrupted = True
				print str(self.start_line+line_counter-1), '** wrong CPOSTAG content **', line
				break

			#POSTAG
			if (not(re.match('[A-Za-z-+]|_',line[4]))):
				self.corrupted = True
				print str(self.start_line+line_counter-1), '** wrong POSTAG content **', line
				break

			#FEATS
			if (not(re.match('[.\|]*|_',line[5]))):
				self.corrupted = True
				print str(self.start_line+line_counter-1), '** wrong FEATS content **', line
				break

			#HEAD
			if (not(re.match('[0-9]+',line[6])) or int(line[6])>self.length):
				self.corrupted = True
				print str(self.start_line+line_counter-1), '** wrong HEAD content **', line
				break

			#DEPREL
			if (not(re.match('.+|_',line[7]))):
				self.corrupted = True
				print str(self.start_line+line_counter-1), '** wrong DEPREL content **', line
				break

			if len(line)==10:
				#PHEAD
				if (not(re.match('[0-9]+|_',line[8]))):
					self.corrupted = True
					print str(self.start_line+line_counter-1), '** wrong PHEAD content **', line
					break
				else:
					if re.match('[0-9]+',line[8]):
						if int(line[8])>self.length:
							self.corrupted = True
							print str(self.start_line+line_counter-1), '** wrong PHEAD number **', line
							break

				#PDEPREL
				if (not(re.match('.+|_',line[9]))):
					self.corrupted = True
					print str(self.start_line+line_counter-1), '** wrong PDEPREL content **', line
					break

			line_counter += 1


def main():
	line_number = 1
	start_line = 1
	conll = ''
	output = open(sys.argv[1]+'.filtered','w')
	for line in open(sys.argv[1],'rU'):
		if len(line.strip())>0:
			conll += line
		else:
			sentence = CoNLL_sentence(conll.strip(),start_line)
			if not(sentence.corrupted): 
				# save in a file
				output.write(conll)
				output.write('\n')
			start_line = line_number+1
			conll = ''
		line_number += 1

if __name__ == '__main__':
	main()