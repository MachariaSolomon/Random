import unittest
from main import reverse_or_uppercase

class TestFunctions(unittest.TestCase):

    # def test_check_password(self):
    #     actual = check_password('ABd1234@1', 'a F1#', '2w3E*', '2We3345', 'ABd1@', '#dhhGs4@1')
    #     expected = ','.join(['ABd1234@1', '#dhhGs4@1'])
    #     self.assertEqual(actual, expected)

    # def test_input_output_string(self):
    #     self.assertEqual(input_output_string('Solomon', 'Macharia'), 'Macharia')
    #     self.assertEqual(input_output_string('Solomon', 'Solomon'), 'Solomon', 'Solomon')

    def test_reverse_or_uppercase(self):
        self.assertEqual(reverse_or_uppercase([1, 2, 3]), ([3, 2, 1]))
        self.assertEqual(reverse_or_uppercase(['a', 'b', 'c']), (['A', 'B', 'C']))
        self.assertEqual(reverse_or_uppercase(['a', 'b', 3]), (['a', 'b', 3]))

    # def test_pig_latin(self):
    #     wordlist = ['will', 'dog', 'category', 'andela', 'electrician']
    #     actual_list = []
        
    #     for word in wordlist:
    #         actual_list.append(pig_latin(word))   
    #     expected_list = ['illway', 'ogday', 'ategorycay', 'andelaway', 'electricianway'] 
    #     self.assertEqual(actual_list, expected_list)

    # def test_find_question_marks(self):
    #     actual = (["arrb6???4xxbl5???eee5", "acc?7??sss?3rr1??????5", "5??aaaaaaaaaaaaaaaaaaa?5?5", "9???1???9???1???9"])
    #     expected = ("arrb6???4xxbl5???eee5", "acc?7??sss?3rr1??????5", "9???1???9???1???9")
    #     self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
