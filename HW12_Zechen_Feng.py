# -*- coding: utf-8 -*-
"""
Create on Friday Nov 17 2019

@author: Zechen Feng (10452166)

This is homework 12.
"""

import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/instructors")
def instructors():
    """ instructor function """
    data_path = 'stevens/SSW-810.db'
    # load database file
    database = sqlite3.connect(data_path)
    # query
    sql = """select I.CWID, I.Name, I.Dept, G.Course, count(*) as Students
                    FROM instructors I
                    join grades G
                    on I.CWID = G.InstructorCWID
                    group by I.CWID, I.Name, I.Dept, G.Course"""
    results = database.execute(sql)
    # change data type
    data = [{'CWID': cwid, 'Name': name, 'Dept': dept, 'Course': course, 'Students': Students}
            for cwid, name, dept, course, Students in results]
    # close the database
    database.close()
    return render_template('instructors.html',
                           title='Stevens Repository',
                           table_title='Courses and student counts',
                           instructors=data)


if __name__ == '__main__':
    app.run(debug=True)
