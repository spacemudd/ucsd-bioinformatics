import unittest
import reverse_complement

class TestLaboratoryReverseComplement(unittest.TestCase):

	def test_lab_finding_reverse_complement(self):
		lab = reverse_complement.ReverseComplement()

		reverse_complement_string =  lab.get_reverse_complement_from_nucleotide('AAAACCCGGT')

		self.assertEqual(reverse_complement_string, 'ACCGGGTTTT', 'Reverse nucleotide should be "ACCGGGTTTT", Actual: '+reverse_complement_string)

if __name__ == '__main__':
    unittest.main()