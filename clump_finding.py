__author__ = 'Shafiq al-Shaar'
__email__ = 'shafiqalshaar@gmail.com'

from computing_frequencies import ComputingFrequencies
from pattern_to_number import PatternToNumber
from number_to_pattern import NumberToPattern
import datetime
#from tqdm import tqdm

""" This class finds frequent k-mers.
"""
class ClumpFinding:
	def set_genome(self, genome):
		self.genome = genome

	def set_kmer_length(self, length):
		self.kmer_length = int(length)

	def set_window_length(self, length):
		self.window_length = int(length)

	def set_t_occurences(self, t):
		self.t_occurences = int(t)

	def get_clumps(self):
		frequent_patterns = []
		clumps = {}

		for pos in range(4**self.kmer_length - 1):
			clumps.update({pos: 0})

		text = self.genome[0:self.window_length]

		computing_frequencies = ComputingFrequencies()
		computing_frequencies.set_genome(self.genome)
		computing_frequencies.set_kmer_length(self.kmer_length)

		frequency_arr = computing_frequencies.compute_frequencies(ReturnArray=True)

		for pos in range(4**self.kmer_length - 1):
			if frequency_arr[pos] >= self.t_occurences:
				clumps.update({pos: 1})

		for pos in range(1, len(self.genome) - self.window_length):
			first_pattern = self.genome[pos-1:self.kmer_length]
			index = PatternToNumber().pattern_to_number(first_pattern)
			#frequency_arr.update({pos:  frequency_arr.get(pos)-1 })
			frequency_arr[pos] = frequency_arr[pos]-1

			last_pattern = self.genome[pos+self.window_length-self.kmer_length:self.kmer_length]
			index = PatternToNumber().pattern_to_number(last_pattern)
			#frequency_arr.update({pos: frequency_arr.get(pos)+1})
			frequency_arr[pos] = frequency_arr[pos]+1

			#if frequency_arr.get(pos) >= self.t_occurences:
			if frequency_arr[pos] >= self.t_occurences:
				clumps.update({pos: 1})

		for pos in range(4**self.kmer_length - 1):
			if clumps.get(pos) == 1:
				pattern = NumberToPattern().number_to_pattern(pos, self.kmer_length)
				frequent_patterns.append(pattern)

		print(frequent_patterns)

		return ' '.join(frequent_patterns)

	def print_to_file_clumps(self):
		basename = "clump_finding"
		suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
		filename = "_".join([basename, suffix])

		#print(self.get_clumps(), file=open(filename+".txt", "a") )
		f = open(filename+'.txt', 'w')
		f.write(self.get_clumps())
		f.close()

		return 'File printed to: '+filename+'.txt'

def main():
	lab = ClumpFinding()

	with open('C:/projects/ucsd-bioinformatics/E_coli.txt', 'r') as file:
		text = file.read()

	lab.set_genome(text)

	kmer_length = raw_input('Set kmer length (k): ')
	window_length = raw_input('Set window length (L): ')
	t_occurences = raw_input('Set occurences (t): ')

	lab.set_kmer_length(int(kmer_length))
	lab.set_window_length(int(window_length))
	lab.set_t_occurences(int(t_occurences))

	result = lab.print_to_file_clumps()
	
	print('')
	print('  ==========================')
	print('  LAB RESULT')
	print('  --------------------------')
	print('  '+result)
	print('  --------------------------')

if __name__ == '__main__':
	main()
