import unittest
from user import *

class TestCap(unittest.TestCase):

	def test_email_validity(self):
		email = 'test_case'
		test = User('IN', 'Test Case', email, 9876512345, 'GJ', 12345)
		result = test.test_email()
		self.assertEqual(result, "Please provide a valid email.")

	def test_document(self):
		test = User('IN', 'Test Case', 'temp@gmail.com', 9876512345, 'GJ', 12345)
		result = test.upload_document({'document_name' : 'medical_report.gif', 'document_content' : 'Hospital', 'Result' : 'Negative'})
		self.assertEqual(result, "Please select a valid file format.")

	def test_family_add(self):
		test_1 = User('IN', 'Test Case 1', 'temp1@gmail.com', 9876512345, 'GJ', 12345)
		test_2 = User('IN', 'Test Case 1', 'temp2@gmail.com', 9876512346, 'GJ', 41344)
		result = test_1.add_family(test_2)  
		self.assertEqual(result, "Added Family")


if __name__ == '__main__':
	unittest.main()