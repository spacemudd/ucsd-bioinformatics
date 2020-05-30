import unittest
import clump_finding

class TestLaboratoryClumpFinding(unittest.TestCase):

	def test_lab_clump_finding(self):
		lab = clump_finding.ClumpFinding()
		lab.set_genome('CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA')
		lab.set_kmer_length(5)
		lab.set_window_length(50)
		lab.set_t_occurences(4)

		string = lab.get_clumps()

		self.assertEqual(string, 'CGACA GAAGA', 'Actual: '+string)

if __name__ == '__main__':
    unittest.main()