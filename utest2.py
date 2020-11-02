import unittest
from reverse import reverse

class TestDemo(unittest.TestCase):
	def test_reverse(self):
		self.assertEqual(reverse( {'hired': {'be': {'to': {'deserve': 'I'} } } }),{'I': {'deserve': {'to': {'be': 'hired'}}}} )


if __name__ == "__main__":
	unittest.main()
