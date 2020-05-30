import unittest
import number_to_pattern

class TestLaboratoryNumberToPattern(unittest.TestCase):

	def test_lab_finding_number_to_pattern(self):
		lab = number_to_pattern.NumberToPattern()

		nucleotides = lab.number_to_pattern(45, 4)

		self.assertEqual(nucleotides, 'AGTC', 'Result should be AGTC", Actual: '+nucleotides)

if __name__ == '__main__':
    unittest.main()