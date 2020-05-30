__author__ = 'Shafiq al-Shaar'
__email__ = 'shafiqalshaar@gmail.com'

""" This class converts a pattern to number.
"""
class PatternToNumber:
	""" Converts pattern to number using the last last char.
		pattern required string
	"""
	def pattern_to_number(self, pattern):
		if not pattern:
			return 0

		symbol_to_number = {'A':0, 'C':1, 'G':2, 'T':3}

		symbol = pattern[-1] # last symbol.
		size_of_pattern = len(pattern)
		prefix = pattern[0:size_of_pattern-1] # without the last symbol.

		return 4 * self.pattern_to_number(prefix) + symbol_to_number[symbol]

def main():
	lab = PatternToNumber()

	with open('C:/projects/ucsd-bioinformatics/FrequentWordsDataset.txt', 'r') as file:
		text = file.read()

	result = lab.pattern_to_number(text)

	print('')
	print('  ==========================')
	print('  LAB RESULT')
	print('  --------------------------')
	print('  '+text)
	print('  --------------------------')

if __name__ == '__main__':
	main()


