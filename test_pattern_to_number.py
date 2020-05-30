import unittest
import pattern_to_number

class TestLaboratoryPatternToNumber(unittest.TestCase):


	def test_lab_finding_pattern_to_number(self):
		lab = pattern_to_number.PatternToNumber()

		number = lab.pattern_to_number('AGT')

		self.assertEqual(number, 11, 'Result should be 11", Actual: {}'.format(number))

if __name__ == '__main__':
    unittest.main()