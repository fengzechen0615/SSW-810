"""
Create on Friday Nov 16 2019

@author: Zechen Feng (10452166)

This is homework 11.
"""
import unittest
from prettytable import PrettyTable
from HW11_Zechen_Feng import Repository, Student, Instructor, Major


class TestRepository(unittest.TestCase):
    """ Test Module Generator File Class """
    def test_repository_student(self):
        """ Test student data """
        pretty_table_student = PrettyTable()
        pretty_table_student.field_names = Student.PT_FIELD
        students = [['10103', 'Jobs, S', 'SFEN',
                     ['CS 501', 'SSW 810'], ['SSW 540', 'SSW 555'], None],
                    ['10115', 'Bezos, J', 'SFEN',
                     ['SSW 810'], ['SSW 540', 'SSW 555'], ['CS 501', 'CS 546']],
                    ['10183', 'Musk, E', 'SFEN',
                     ['SSW 555', 'SSW 810'], ['SSW 540'], ['CS 501', 'CS 546']],
                    ['11714', 'Gates, B', 'CS',
                     ['CS 546', 'CS 570', 'SSW 810'], [], None],
                    ['11717', 'Kernighan, B', 'CS',
                     [], ['CS 546', 'CS 570'], ['SSW 565', 'SSW 810']]]

        for student in students:
            pretty_table_student.add_row(student)
        self.assertTrue(Repository('stevens').student_pretty_table().get_string()
                        == pretty_table_student.get_string())

    def test_repository_instructor(self):
        """ Test instructor data """
        pretty_table_instructor = PrettyTable()
        pretty_table_instructor.field_names = Instructor.PT_FIELDS
        instructors = [['98764', 'Cohen, R', 'SFEN', 'CS 546', 1],
                       ['98763', 'Rowland, J', 'SFEN', 'SSW 810', 4],
                       ['98763', 'Rowland, J', 'SFEN', 'SSW 555', 1],
                       ['98762', 'Hawking, S', 'CS', 'CS 501', 1],
                       ['98762', 'Hawking, S', 'CS', 'CS 546', 1],
                       ['98762', 'Hawking, S', 'CS', 'CS 570', 1]]

        for instructor in instructors:
            pretty_table_instructor.add_row(instructor)
        self.assertTrue(Repository('stevens').instructor_pretty_table().get_string()
                        == pretty_table_instructor.get_string())

    def test_repository_major(self):
        """ Test major data """
        pretty_table_major = PrettyTable()
        pretty_table_major.field_names = Major.PT_FIELDS
        majors = [['SFEN', ['SSW 540', 'SSW 555', 'SSW 810'], ['CS 501', 'CS 546']],
                  ['CS', ['CS 546', 'CS 570'], ['SSW 565', 'SSW 810']]]

        for major in majors:
            pretty_table_major.add_row(major)
        self.assertTrue(Repository('stevens').major_pretty_table().get_string()
                        == pretty_table_major.get_string())

    def test_repository_instructor_database(self):
        """ Test instructor database """
        pretty_table_instructor_database = PrettyTable()
        pretty_table_instructor_database.field_names = Instructor.PT_FIELDS
        instructors = [('98762', 'Hawking, S', 'CS', 'CS 501', 1),
                       ('98762', 'Hawking, S', 'CS', 'CS 546', 1),
                       ('98762', 'Hawking, S', 'CS', 'CS 570', 1),
                       ('98763', 'Rowland, J', 'SFEN', 'SSW 555', 1),
                       ('98763', 'Rowland, J', 'SFEN', 'SSW 810', 4),
                       ('98764', 'Cohen, R', 'SFEN', 'CS 546', 1)]
        for instructor in instructors:
            pretty_table_instructor_database.add_row(instructor)
        self.assertTrue(Repository('stevens').instructor_database_pretty_table().get_string()
                        == pretty_table_instructor_database.get_string())


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
