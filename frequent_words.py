__author__ = 'Shafiq al-Shaar'
__email__ = 'shafiqalshaar@gmail.com'

import genome_pattern
from collections import Counter

""" This class finds frequent k-mers.
"""
class FrequentWords:
	def __init__(self, dataset='', kmer=3, debug=False):
		self.dataset = dataset
		self.kmer = kmer
		self.debug = debug

	""" Reads the dataset file to memory.
	"""
	def set_dataset_from_file(self, filePath):
		with open(filePath, 'r') as genomeFile:
			self.dataset = genomeFile.read()
			print('Loaded '+filePath+' successfully.')

	""" Sets the length of k-mer to be found.
	"""
	def set_kmer(self, kmer):
		self.kmer = kmer

	""" Builds the frequent k-mer found.
	"""
	def build_frequent_words(self, showResult=True):
		patternFinder = genome_pattern.GenomePattern()
		patternFinder.set_genome(self.dataset)

		frequent_words = {}

		for pos in range(len(self.dataset) - self.kmer):
			chunk = self.dataset[pos:pos+self.kmer]

			patternFinder.set_pattern_text(chunk)
			hits = patternFinder.count_pattern(showResults=False)

			frequent_words.update({chunk: hits})

			if self.debug:
				print('Chunk: '+chunk+' - Current position: {}:{}'.format(pos, pos+self.kmer))
				print('Found hits: ', hits)

		counter = Counter(frequent_words)
		most_common = counter.most_common()

		
		topHits = most_common[0][1]

		# Clean up
		result = []
		for chunk in most_common:
			if (chunk[1] == topHits):
				result.append(chunk)

		if showResult:
			print('')
			print('  ==========================')
			print('  LAB RESULT')
			print('  Top frequent words for k-mer: {}'.format(self.kmer))
			print('  --------------------------')
			for chunk in result:
				print('  {}'.format(chunk[0]))
			print('  ==========================')
			print('')

		return result


def main():
	laboratory = FrequentWords(debug=False)
	laboratory.set_dataset_from_file('C:/projects/ucsd-bioinformatics/FrequentWordsDataset.txt') # Edit this path for your environment.
	laboratory.set_kmer(9)
	laboratory.build_frequent_words()

if __name__ == '__main__':
	main()
