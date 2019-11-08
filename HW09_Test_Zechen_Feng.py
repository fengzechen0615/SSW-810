"""
Create on Friday Nov 1 2019

@author: Zechen Feng (10452166)

This is homework 9.
"""
import unittest
from HW09_Zechen_Feng import Repository, Student, Instructor
from prettytable import PrettyTable


class TestRepository(unittest.TestCase):
    """Test Module Generator File Class"""
    def test_repository_student(self):
        """Test student data"""
        pretty_table_student = PrettyTable()
        pretty_table_student.field_names = Student.PT_FIELDS
        students = [['10103', 'Baldwin, C', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']],
                    ['10115', 'Wyatt, X', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']],
                    ['10172', 'Forbes, I', ['SSW 555', 'SSW 567']],
                    ['10175', 'Erickson, D', ['SSW 564', 'SSW 567', 'SSW 687']],
                    ['10183', 'Chapman, O', ['SSW 689']],
                    ['11399', 'Cordova, I', ['SSW 540']],
                    ['11461', 'Wright, U', ['SYS 611', 'SYS 750', 'SYS 800']],
                    ['11658', 'Kelly, P', ['SSW 540']],
                    ['11714', 'Morton, A', ['SYS 611', 'SYS 645']],
                    ['11788', 'Fuller, E', ['SSW 540']]]

        for student in students:
            pretty_table_student.add_row(student)
        self.assertEqual(Repository('stevens').student_pretty_table(), pretty_table_student.get_string())

    def test_repository_instructor(self):
        """test instructor data"""
        pretty_table_instructor = PrettyTable()
        pretty_table_instructor.field_names = Instructor.PT_FIELDS
        instructors = [['98765', 'Einstein, A', 'SFEN', 'SSW 567', 4],
                       ['98765', 'Einstein, A', 'SFEN', 'SSW 540', 3],
                       ['98764', 'Feynman, R', 'SFEN', 'SSW 564', 3],
                       ['98764', 'Feynman, R', 'SFEN', 'SSW 687', 3],
                       ['98764', 'Feynman, R', 'SFEN', 'CS 501', 1],
                       ['98764', 'Feynman, R', 'SFEN', 'CS 545', 1],
                       ['98763', 'Newton, I', 'SFEN', 'SSW 555', 1],
                       ['98763', 'Newton, I', 'SFEN', 'SSW 689', 1],
                       ['98760', 'Darwin, C', 'SYEN', 'SYS 800', 1],
                       ['98760', 'Darwin, C', 'SYEN', 'SYS 750', 1],
                       ['98760', 'Darwin, C', 'SYEN', 'SYS 611', 2],
                       ['98760', 'Darwin, C', 'SYEN', 'SYS 645', 1]]

        for instructor in instructors:
            pretty_table_instructor.add_row(instructor)
        self.assertTrue(Repository('stevens').instructor_pretty_table() == pretty_table_instructor.get_string())


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
