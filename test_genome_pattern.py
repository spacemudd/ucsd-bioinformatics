import unittest
import genome_pattern

class TestLaboratoryPatternOccurence(unittest.TestCase):

	def test_lab_finding_pattern_occurance(self):
		lab = genome_pattern.GenomePattern()
		lab.genome = 'GACCATACTG'
		lab.patternText = 'ATA'
		self.assertEqual(lab.count_pattern(), 1, 'Should be 1')
		lab.genome = 'ACAACTATGCATACTATCGGGAACTATCCT'
		lab.patternText = 'ACTAT'
		self.assertEqual(lab.count_pattern(), 3, 'Should be 3')

if __name__ == '__main__':
    unittest.main()