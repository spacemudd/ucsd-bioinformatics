__author__ = 'Shafiq al-Shaar'
__email__ = 'shafiqalshaar@gmail.com'

""" This class finds the pattern occurence in a genome.
"""
class PatternOccurence:
	""" Sets the pattern to find.
	"""
	def set_pattern(self, pattern):
		self.pattern = pattern

	""" Sets the genome to search in.
	"""
	def set_genome(self, genome):
		self.genome = genome

	""" Gets the starting positions of the pattern.
	"""
	def get_starting_positions(self):
		seperator = ' '

		positions = []

		for pos in range(len(self.genome) - len(self.pattern) + 1):
			
			""" To debug.
			"""
			# print('doing {}'.format(pos))
			# print('{}:{}'.format(pos, pos+len(self.pattern)))
			# print('checking if: '+self.genome[pos:pos+len(self.pattern)]+' equals '+self.pattern )

			if self.genome[pos:pos+len(self.pattern)] == self.pattern:
				positions.append(str(pos))

		return seperator.join(positions)

def main():
	lab = PatternOccurence()

	with open('C:/projects/ucsd-bioinformatics/FrequentWordsDataset.txt', 'r') as file:
			text = file.read()

	""" Set the genome from the text file.
	"""
	lab.set_genome(text)

	""" Get the pattern as a user input.
	"""
	pattern = raw_input(' Set the pattern to look for [Default: AAA]: ')
	pattern = pattern or 'AAA'
	lab.set_pattern(pattern)

	""" Get the positions.
	"""
	positions = lab.get_starting_positions()

	print('')
	print('  ==========================')
	print('  LAB RESULT')
	print('  --------------------------')
	print('  Positions: '+positions)
	print('  --------------------------')

if __name__ == '__main__':
	main()
