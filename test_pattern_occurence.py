import unittest
import pattern_occurence

class TestLaboratoryPatternOccurence(unittest.TestCase):


	def test_lab_finding_pattern_occurence(self):
		lab = pattern_occurence.PatternOccurence()
		lab.set_pattern('ATAT')
		lab.set_genome('GATATATGCATATACTT')

		pattern_occurence_positions =  lab.get_starting_positions()

		self.assertEqual(pattern_occurence_positions, '1 3 9', 'Result should be 1 3 9", Actual: '+pattern_occurence_positions)

if __name__ == '__main__':
    unittest.main()