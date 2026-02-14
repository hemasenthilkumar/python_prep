"""
🧠 Exercise 5: File Processor (Mocking open + Fixtures + CLI)

Now we combine everything.

🧩 Build This
# file_processor.py
class FileProcessor:
    def count_words(self, filepath):
        ...

🧪 Test Requirements

You MUST:

Mock open

Use patch("builtins.open")

Use mock_open

Test file not found

Test empty file

Test normal file

🚀 Add CLI Runner

Add:

if __name__ == "__main__":
    unittest.main(verbosity=2)


Run:

python -m unittest discover
"""


import unittest
from unittest.mock import mock_open, patch 
from fileutils import FileProcessor

class TestFileProcessor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.words_in_file= """
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
        
        Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
        when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
        It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
        
        It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages.
        """
        cls.processor = FileProcessor()
    
    @classmethod
    def tearDownClass(cls):
        del cls.processor 


    @patch("fileutils.os.path.exists", return_value=True)
    @patch("fileutils.open", new_callable=mock_open)
    def test_word_count_nonzero(self, mock_file, mock_exists):
        mock_file.return_value.readlines.return_value = self.words_in_file.splitlines()
        self.assertEqual(self.processor.count_words("dummy.txt"), 76)


    @patch("fileutils.os.path.exists", return_value=True)
    @patch("fileutils.open", new_callable=mock_open)
    def test_word_count_zero(self, mock_file, mock_exists):
        mock_file.return_value.readlines.return_value = ""
        self.assertEqual(self.processor.count_words("dummy.txt"), 0)

    @patch("fileutils.os.path.exists", return_value=False)
    @patch("fileutils.open", new_callable=mock_open)
    def test_file_not_found(self, mock_file, mock_exists):
        with self.assertRaises(FileNotFoundError):
            self.processor.count_words("dummy.txt")


if __name__ == "__main__":
    #f = FileProcessor()
    #print(f.count_words("/Users/vasanthhema/python_prep/test.txt"))
    unittest.main(verbosity=2)
