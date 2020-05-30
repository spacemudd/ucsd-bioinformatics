__author__ = 'Shafiq al-Shaar'
__email__ = 'shafiqalshaar@gmail.com'

""" This class computes the frequency of k-mer pattern.
"""
class ComputingFrequencies:

	""" Sets the k-mer length for the frequency to be found.
	"""
	def set_kmer_length(self, length):
		self.kmer_length = length

	""" Sets the genome.
	"""
	def set_genome(self, genome):
		self.genome = genome

	def pattern_to_number(self, pattern):
		if len(pattern) == 0:
			return 0

		symbol_to_number = {'A':0, 'C':1, 'G':2, 'T':3}

		length = len(pattern)

		prefix = pattern[:length-1]

		symbol = pattern[length-1]

		return 4 * self.pattern_to_number(prefix) + symbol_to_number[symbol]

	""" Compute the frequency of the k-mer.
	"""
	def compute_frequencies(self, ReturnArray=False):
		frequency_arr = []

		length_of_genome = len(self.genome)

		for pos in range(4 ** self.kmer_length):
			frequency_arr.append(0)

		for pos in range(length_of_genome - self.kmer_length + 1):
			pattern = self.genome[pos:pos+self.kmer_length]
			encode = self.pattern_to_number(pattern)
			frequency_arr[encode] = frequency_arr[encode] + 1

		if ReturnArray:
			return frequency_arr

		return ' '.join( str(e) for e in frequency_arr )

def main():
	lab = ComputingFrequencies()

	with open('C:/projects/ucsd-bioinformatics/FrequentWordsDataset.txt', 'r') as file:
		text = file.read()

	kmer_length = raw_input('Set the k-mer length [Default: 2]: ')
	length = int(kmer_length) or 2
	lab.set_kmer_length(length)

	lab.set_genome(text)

	frequencies = lab.compute_frequencies()

	print('')
	print('  ==========================')
	print('  LAB RESULT')
	print('  --------------------------')
	print('  '+frequencies)
	print('  --------------------------')

if __name__ == '__main__':
	main()