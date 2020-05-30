__author__ = 'Shafiq al-Shaar'
__email__ = 'shafiqalshaar@gmail.com'

""" This class finds the pattern of a number.
"""
class NumberToPattern:

	def number_to_pattern(self, index, k):
		number_to_symbol = {0:'A', 1:'C', 2:'G', 3:'T'}

		if k == 1:
			return number_to_symbol[index]

		pattern_collect = ''

		prefix_index = index // 4
		remainder = index % 4
		symbol = number_to_symbol[remainder]

		prefix_pattern = self.number_to_pattern(prefix_index, k - 1)

		return prefix_pattern+symbol

def main():
	lab = NumberToPattern()

	index = raw_input('index: ')
	k = raw_input('k: ')

	result = lab.number_to_pattern(int(index), int(k))

	print('')
	print('  ==========================')
	print('  LAB RESULT')
	print('  --------------------------')
	print('  '+result)
	print('  --------------------------')

if __name__ == '__main__':
	main()