__author__ = 'Shafiq al-Shaar'
__email__ = 'shafiqalshaar@gmail.com'

""" This class finds the reverse complement of a nucleotide.
"""
class ReverseComplement:

	""" Get the reverse complement from a nucleotide string text.
	"""
	def get_reverse_complement_from_nucleotide(self, nucleotides):
		complement = ''

		switcher = {
			'A': 'T',
			'T': 'A',
			'G': 'C',
			'C': 'G',
			'U': 'A',
		}

		for nucleotide in nucleotides:
			complement += switcher.get(nucleotide, 'Invalid nucleotide')

		return self.reverse_string(complement)

	def reverse_string(self, text):
		string = ''
		for i in text:
			string = i + string
		return string

def main():
	lab = ReverseComplement()

	with open('C:/projects/ucsd-bioinformatics/FrequentWordsDataset.txt', 'r') as file:
			text = file.read()

	reverse = lab.get_reverse_complement_from_nucleotide(text)

	print('')
	print('  ==========================')
	print('  LAB RESULT')
	print('  --------------------------')
	print('  Nucleotide: '+text)
	print('  Reverse complement: '+reverse)
	print('  --------------------------')

if __name__ == '__main__':
	main()
