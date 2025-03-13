from unittest import TestCase
import common
import os

def create_test_file(filename):
    with open(filename, "w") as file:
        file.write("Hello, World!\n")
        file.write("1234567890\n")
        file.write("! ~\n")

class TestReadFile(TestCase):

    def test_alphanumeric_file(self):
        """Test reading a file with alphanumeric characters"""
        # Create file with alphanumeric characters
        filename = "test_input.txt"
        create_test_file(filename)
        input_list = common.read_file(filename)
        self.assertEqual(len(input_list), 3)
        self.assertEqual(input_list[0], "Hello, World!")
        for line in input_list:
            self.assertTrue(line[-1] != "\n")
        os.remove(filename)
        
    def test_empty_file(self):
        """Test reading an empty file"""
        # Create empty file
        filename = "test_empty.txt"
        with open(filename, "w") as file:
            pass
        input_list = common.read_file(filename)
        self.assertEqual(len(input_list), 0)
        os.remove(filename)

class TestReshapeList(TestCase):

    def test_reshape_list(self):
        """Test reshaping a list"""
        lst = [1, 2, 3, 4, 5, 6]
        reshaped = common.reshape_list(lst, 2, 3)
        self.assertEqual(reshaped, [[1, 2, 3], [4, 5, 6]])

    def test_invalid_reshape_list(self):
        """Test reshaping a list with an invalid shape"""
        lst = [1, 2, 3, 4, 5, 6]
        with self.assertRaises(ValueError):
            common.reshape_list(lst, 2, 4)