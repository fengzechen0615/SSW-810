"""
Create on Friday Nov 1 2019

@author: Zechen Feng (10452166)

This is homework 10.
"""
import unittest
from prettytable import PrettyTable
from HW10_Zechen_Feng import Repository, Student, Instructor, Major


class TestRepository(unittest.TestCase):
    """ Test Module Generator File Class """
    def test_repository_student(self):
        """ Test student data """
        pretty_table_student = PrettyTable()
        pretty_table_student.field_names = Student.PT_FIELD
        students = [['10103', 'Baldwin, C', 'SFEN',
                     ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'],
                     sorted({'SSW 555', 'SSW 540'}), 'None'],
                    ['10115', 'Wyatt, X', 'SFEN',
                     ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'],
                     sorted({'SSW 555', 'SSW 540'}), 'None'],
                    ['10172', 'Forbes, I', 'SFEN',
                     ['SSW 555', 'SSW 567'],
                     sorted({'SSW 540', 'SSW 564'}), sorted({'CS 545', 'CS 513', 'CS 501'})],
                    ['10175', 'Erickson, D', 'SFEN',
                     ['SSW 564', 'SSW 567', 'SSW 687'],
                     sorted({'SSW 555', 'SSW 540'}), sorted({'CS 545', 'CS 513', 'CS 501'})],
                    ['10183', 'Chapman, O', 'SFEN',
                     ['SSW 689'],
                     sorted({'SSW 555', 'SSW 540', 'SSW 567', 'SSW 564'}),
                     sorted({'CS 545', 'CS 513', 'CS 501'})],
                    ['11399', 'Cordova, I', 'SYEN',
                     ['SSW 540'],
                     sorted({'SYS 800', 'SYS 612', 'SYS 671'}), 'None'],
                    ['11461', 'Wright, U', 'SYEN',
                     ['SYS 611', 'SYS 750', 'SYS 800'],
                     sorted({'SYS 612', 'SYS 671'}), sorted({'SSW 565', 'SSW 540', 'SSW 810'})],
                    ['11658', 'Kelly, P', 'SYEN',
                     [],
                     sorted({'SYS 800', 'SYS 612', 'SYS 671'}),
                     sorted({'SSW 565', 'SSW 540', 'SSW 810'})],
                    ['11714', 'Morton, A', 'SYEN',
                     ['SYS 611', 'SYS 645'],
                     sorted({'SYS 800', 'SYS 612', 'SYS 671'}),
                     sorted({'SSW 565', 'SSW 540', 'SSW 810'})],
                    ['11788', 'Fuller, E', 'SYEN',
                     ['SSW 540'],
                     sorted({'SYS 800', 'SYS 612', 'SYS 671'}), 'None']]

        for student in students:
            pretty_table_student.add_row(student)
        self.assertTrue(Repository('stevens').student_pretty_table().get_string()
                        == pretty_table_student.get_string())

    def test_repository_instructor(self):
        """ Test instructor data """
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
        self.assertTrue(Repository('stevens').instructor_pretty_table().get_string()
                        == pretty_table_instructor.get_string())

    def test_repository_major(self):
        """ Test major data """
        pretty_table_major = PrettyTable()
        pretty_table_major.field_names = Major.PT_FIELDS
        majors = [['SFEN', sorted({'SSW 564', 'SSW 555', 'SSW 567', 'SSW 540'}),
                   sorted({'CS 501', 'CS 513', 'CS 545'})],
                  ['SYEN', sorted({'SYS 612', 'SYS 671', 'SYS 800'}),
                   sorted({'SSW 540', 'SSW 565', 'SSW 810'})]]

        for major in majors:
            pretty_table_major.add_row(major)
        self.assertTrue(Repository('stevens').major_pretty_table().get_string()
                        == pretty_table_major.get_string())


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
