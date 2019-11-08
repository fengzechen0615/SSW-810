# -*- coding: utf-8 -*-
"""
Create on Friday Nov 1 2019

@author: Zechen Feng (10452166)

This is homework 9.
"""
import os
from collections import defaultdict
from prettytable import PrettyTable


class Repository:
    """
        initialize everything
        read files
        print pretty tables
    """
    def __init__(self, path):
        self._students = dict()
        self._instructors = dict()
        self._majors = defaultdict()

        self._get_instructors(os.path.join(path, 'instructors.txt'))
        self._get_majors(os.path.join(path, 'majors.txt'))
        self._get_students(os.path.join(path, 'students.txt'))
        self._get_grades(os.path.join(path, 'grades.txt'))

    def _get_students(self, path):
        """ read the students file and create an instance of students for each row """
        try:
            for cwid, name, major_name in file_reading_gen(path, 3, sep=';', header=True):
                self._students[cwid] = Student(cwid, name, major_name, self._majors[major_name])
        except FileExistsError as error:
            print(error)
        except ValueError as error:
            print(error)

    def _get_instructors(self, path):
        """ get instructor function """
        try:
            for cwid, name, dept in file_reading_gen(path, 3, sep='|', header=True):
                self._instructors[cwid] = Instructor(cwid, name, dept)
        except FileExistsError as error:
            print(error)
        except ValueError as error:
            print(error)

    def _get_majors(self, path):
        """ get major function """
        try:
            for dept, required_electives, course in \
                    file_reading_gen(path, 3, sep='\t', header=True):
                if dept not in self._majors:
                    self._majors[dept] = Major(dept)
                self._majors[dept].add_course(course, required_electives,)
        except FileExistsError as error:
            print(error)
        except ValueError as error:
            print(error)

    def _get_grades(self, path):
        """ get grades function """
        try:
            for student_cwid, course, grade, instructor_cwid in \
                    file_reading_gen(path, 4, sep='|', header=True):
                if student_cwid in self._students:
                    # tell the student about a course
                    self._students[student_cwid].add_course(course, grade)
                else:
                    print(f"Found grade for unknown student {student_cwid}")
                if instructor_cwid in self._instructors:
                    # tell the instructor about a course/student
                    self._instructors[instructor_cwid].add_students(course)
                else:
                    print(f"Found grade for unknown instructor {instructor_cwid}")
        except FileExistsError as error:
            print(error)
        except ValueError as error:
            print(error)

    def student_pretty_table(self):
        """ student pretty table function """
        pretty_table = PrettyTable()
        pretty_table.field_names = Student.PT_FIELD
        for student in self._students.values():
            pretty_table.add_row(student.pretty_table_row())
        return pretty_table

    def instructor_pretty_table(self):
        """ instructor pretty table function """
        pretty_table = PrettyTable()
        pretty_table.field_names = Instructor.PT_FIELDS
        for instructor in self._instructors.values():
            for items in instructor.pretty_table_row():
                pretty_table.add_row(items)
        return pretty_table

    def major_pretty_table(self):
        """ major pretty table function """
        pretty_table = PrettyTable()
        pretty_table.field_names = Major.PT_FIELDS
        for major in self._majors.values():
            pretty_table.add_row(major.pretty_table_row())
        return pretty_table


class Student:
    """
        initial everything
        add course
        pretty table row
    """
    PT_FIELD = ['CWID', 'Name', 'Major', 'Completed Courses',
                'Remaining Required', 'Remaining Electives']

    def __init__(self, cwid, name, major_name, major):
        self._cwid = cwid
        self._name = name
        self._major_name = major_name
        # instance of class Major corresponding to this student's major
        self._major = major
        #  _courses[course] = grade
        self._courses = dict()

    def add_course(self, courses, grade):
        """add course function"""
        self._courses[courses] = grade

    def pretty_table_row(self):
        """ pretty table row """
        passed = self._major.passed_course(self._courses)
        rem_required = self._major.remaining_required(self._courses)
        rem_electives = self._major.remaining_electives(self._courses)
        if rem_required is None:
            return [self._cwid, self._name, self._major_name,
                    sorted(passed), rem_required, sorted(rem_electives)]
        elif rem_electives is None:
            return [self._cwid, self._name, self._major_name,
                    sorted(passed), sorted(rem_required), rem_electives]
        return [self._cwid, self._name, self._major_name,
                sorted(passed), sorted(rem_required), sorted(rem_electives)]


class Major:
    """
        initialize everything
        add course
        pass course
        remain required
        remain elective
    """

    PT_FIELDS = ['Dept', 'Required', 'Electives']

    def __init__(self, dept):
        self._dept = dept
        # set of required courses
        self._required = set()
        # set of elective courses
        self._electives = set()
        self._passing_grades = {'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C'}

    def add_course(self, course, flag):
        """ add course to _required or electives based on flag """
        if flag.upper() == 'E':
            self._electives.add(course)
        elif flag.upper() == 'R':
            self._required.add(course)
        else:
            raise ValueError(f"Flag {flag} is invalid for course {course}")

    def passed_course(self, course_grades):
        """ get course_grades[course] = grade from the Student
            return a set of passed courses base on the course and grades """
        completed_courses = {course for course, grade in course_grades.items()
                             if grade in self._passing_grades}
        return completed_courses

    def remaining_required(self, passed):
        """ given a set of passed courses, return a set of remaining required courses """
        remaining_required = self._required - self.passed_course(passed)
        return remaining_required

    def remaining_electives(self, passed):
        """ given a set of passed courses, return a set of remaining elective courses"""
        if self._electives.intersection(self.passed_course(passed)):
            remaining_electives = None
        else:
            remaining_electives = self._electives
        return remaining_electives

    def pretty_table_row(self):
        """ pretty table row """
        return [self._dept, sorted(self._required), sorted(self._electives)]


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
        """ add students function """
        self._courses[course] += 1

    def pretty_table_row(self):
        """ pretty table row function """
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


if __name__ == '__main__':
    STEVENS = Repository('stevens')
    print("Majors Summary")
    print(STEVENS.major_pretty_table())
    print("Student Summary")
    print(STEVENS.student_pretty_table())
    print("Instructor Summary")
    print(STEVENS.instructor_pretty_table())
