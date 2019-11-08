# -*- coding: utf-8 -*-
"""
Create on Friday Nov 1 2019

@author: Zechen Feng (10452166)

This is homework 9.
"""

import os
from collections import defaultdict
from prettytable import PrettyTable


class Student:
    """
        - CWID
        - name
        - department
        - course
    """
    PT_FIELDS = ['CWID', "Name", "Course"]

    def __init__(self, cwid, name, major):
        self._cwid = cwid
        self._name = name
        self._major = major
        self._courses = dict()

    def add_course(self, courses, grade):
        """add course function"""
        self._courses[courses] = self._cwid

    def pretty_table_row(self):
        """pretty table row function"""
        return [self._cwid, self._name, sorted(self._courses.keys())]


class Instructor:
    """
        - CWID
        - name
        - department
        - course/#students
    """
    PT_FIELDS = ['CWID', 'Name', 'Dept', 'Course', 'Students']

    def __init__(self, cwid, name, dept):
        self._cwid = cwid
        self._name = name
        self._dept = dept
        self._course = dict()
        self._courses = defaultdict(int)

    def add_students(self, course):
        """add students function"""
        self._courses[course] += 1

    def pretty_table_row(self):
        """pretty table row function"""
        for course, student in self._courses.items():
            yield [self._cwid, self._name, self._dept, course, student]


def file_reading_gen(path, fields, sep=',', header=False):
    """file reading generator"""
    try:
        # open the file
        file_open = open(path, 'r')
    except FileNotFoundError:
        # can't open the file
        raise FileNotFoundError(f"Can't open '{path}'")
    else:
        # use count and boolean to skip the header line.
        with file_open:
            count = 1
            while True:
                # create an empty list
                new_list = []
                try:
                    line = next(file_open)
                    # use the sep the split the line
                    items = line.split(sep)
                    if header is True:
                        # check the header's field, the empty is right.
                        # Only check the field of the header.
                        if len(items) != fields:
                            raise ValueError(f"ValueError: {path} has {fields} "
                                             f"fields on line {count} but excepted {len(items)}")
                        if count != 1 and header is True:
                            # check the field of other lines. The empty is right.
                            # Only check the field of the lines.
                            if len(items) != fields:
                                raise ValueError(f"ValueError: {path} has {fields} fields "
                                                 f"on line {count} but excepted {len(items)}")
                            for item in items:
                                # remove the '\n' from the end
                                new_list.append(item.replace("\n", ""))
                            # tuple
                            yield tuple(new_list)
                    else:
                        if len(items) != fields:
                            raise ValueError(f"ValueError: {path} has {fields} "
                                             f"fields on line {count} but excepted {len(items)}")
                        for item in items:
                            # remove the '\n' from the end
                            new_list.append(item.replace("\n", ""))
                        # tuple
                        yield tuple(new_list)
                    count += 1
                except StopIteration:
                    break


class Repository:
    """
        Need to know:
        - students
        - instructors
    """
    def __init__(self, path):
        # student[cwid] = Student
        self.students = dict()
        # instructors[cwid] = Instructor
        self.instructors = dict()

        self._get_students(os.path.join(path, "students.txt"))
        self._get_instructors(os.path.join(path, "instructors.txt"))
        self._get_grades(os.path.join(path, "grades.txt"))

        # if pretty_table:
        #     self.student_pretty_table()
        #     self.instructor_pretty_table()

    def _get_students(self, path):
        """get students function"""
        try:
            for cwid, name, major in file_reading_gen(path, 3, sep='\t', header=False):
                self.students[cwid] = Student(cwid, name, major)
        except FileExistsError as error:
            print(error)
        except ValueError as error:
            print(error)
        return self.students

    def _get_instructors(self, path):
        """get instructor function"""
        try:
            for cwid, name, dept in file_reading_gen(path, 3, sep='\t', header=False):
                self.instructors[cwid] = Instructor(cwid, name, dept)
        except FileExistsError as error:
            print(error)
        except ValueError as error:
            print(error)

    def _get_grades(self, path):
        """get grades function"""
        try:
            for student_cwid, course, grade, instructor_cwid in \
                    file_reading_gen(path, 4, sep='\t', header=False):
                if student_cwid in self.students:
                    # tell the student about a course
                    self.students[student_cwid].add_course(course, grade)
                else:
                    print(f"Found grade for unknown student {student_cwid}")
                if instructor_cwid in self.instructors:
                    # tell the instructor about a course/student
                    self.instructors[instructor_cwid].add_students(course)
                else:
                    print(f"Found grade for unknown instructor {instructor_cwid}")
        except FileExistsError as error:
            print(error)
        except ValueError as error:
            print(error)

    def student_pretty_table(self):
        """student pretty table function"""
        # print("Student Summary")
        pretty_table = PrettyTable()
        pretty_table.field_names = Student.PT_FIELDS
        for student in self.students.values():
            pretty_table.add_row(student.pretty_table_row())
        # print(pretty_table)
        return pretty_table.get_string()

    def instructor_pretty_table(self):
        """instructor pretty table function"""
        # print("Instructor Summary")
        pretty_table = PrettyTable()
        pretty_table.field_names = Instructor.PT_FIELDS
        for instructor in self.instructors.values():
            for items in instructor.pretty_table_row():
                pretty_table.add_row(items)
        # print(pretty_table)
        return pretty_table.get_string()


if __name__ == '__main__':
    STEVENS = Repository('stevens')
    print("Student Summary")
    print(STEVENS.student_pretty_table())
    print("Instructor Summary")
    print(STEVENS.instructor_pretty_table())
