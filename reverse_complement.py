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


