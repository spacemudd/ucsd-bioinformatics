import unittest
import computing_frequencies

class TestLaboratoryComputingFrequencies(unittest.TestCase):

	def test_lab_finding_freqent_kmers(self):
		lab = computing_frequencies.ComputingFrequencies()
		lab.set_genome('ACGCGGCTCTGAAA')
		lab.set_kmer_length(2)
		string = lab.compute_frequencies()

		self.assertEqual(string, '2 1 0 0 0 0 2 2 1 2 1 0 0 1 1 0', 'Actual: '+string)

if __name__ == '__main__':
    unittest.main()