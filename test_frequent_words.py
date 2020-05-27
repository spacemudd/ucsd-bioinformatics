import unittest
import frequent_words

class TestLaboratoryFrequentKmers(unittest.TestCase):

	def test_lab_finding_freqent_kmers(self):
		lab = frequent_words.FrequentWords(dataset='ACTGACTCCCACCCC', debug=False)
		lab.set_kmer(3)
		self.assertEqual(lab.build_frequent_words()[0][0], 'CCC', 'Should be CCC')

if __name__ == '__main__':
    unittest.main()