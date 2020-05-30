__author__ = 'Shafiq al-Shaar'
__email__ = 'shafiqalshaar@gmail.com'

""" This class finds each k-mer substring of Text matches a Pattern.
"""
class GenomePattern:

	""" Reads the genome file to memory.
	"""
	def read_file(self, filePath):
		with open(filePath, 'r') as genomeFile:
			self.genome = genomeFile.read()
			print('Loaded '+filePath+' successfully.')
			
	""" Set the genome text.
	"""
	def set_genome(self, dataset=None):
		if dataset is None:
			print('')
			genome = raw_input(' Set the genome data [Default: GACCATACTG]: ')
			genome = genome or 'GACCATACTG'
			self.genome = genome
		else:
			self.genome = dataset
	
	""" Set the specific pattern text required to search for.
	"""
	def set_pattern_text(self, text=None):
		if text is None:
			print('')
			pattern = raw_input(' Set the pattern [Default: ATA]: ')
			pattern = pattern or 'ATA'
			self.patternText = pattern
		else:
			self.patternText = text

	""" Count how many times it's present.
	"""
	def count_pattern(self, showResults=True):
		count = 0

		if len(self.genome) == 0:
			raise Exception('There is no dataset loaded')

		for position in range(0, len(self.genome) - len(self.patternText) + 1): # + 1 because we're starting from 1.
			kmer = self.get_substring(position)
			if kmer == self.patternText:
				count += 1

		if showResults:
			print('')
			print('  ==========================')
			print('  LAB RESULT')
			print('  --------------------------')
			print('    Occurence of '+self.patternText+': {}'.format(count))
			print('  ==========================')
			print('')

		return count
				
	""" Get the substring.
	"""
	def get_substring(self, position):
		return self.genome[position:position+len(self.patternText)]
		
def main():
	laboratory = GenomePattern()
	# laboratory.read_file('C:/projects/ucsd-bioinformatics/Vibrio_cholerae.txt') # To load the file, uncomment this line and comment laboratory.set_genome()
	# laboratory.read_file('C:/projects/ucsd-bioinformatics/SampleDataset.txt') # To load the file, uncomment this line and comment laboratory.set_genome()
	laboratory.set_genome()
	laboratory.set_pattern_text()
	laboratory.count_pattern()
	

if __name__ == '__main__':
	main()
