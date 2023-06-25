from unittest import TestCase, main
from MainProblem.project import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student_no_courses = Student('Guy 1')              # студента няма курсове
        self.student_with_courses = Student(                    # студента има курсове

            'Guy 2', {'math': ['some note']}

        )

    def test_initialization(self):
        self.assertEqual('Guy 1', self.student_no_courses.name)
        self.assertEqual({}, self.student_no_courses.courses)   # проверка дали студента без курсове има някакви курсове, сравнява се с празен речник
        self.assertEqual({'math': ['some note']},               # проверка дали студента с курсове има такива, сравнява се с данни в речника
                         self.student_with_courses.courses
                         )

    def test_enroll_add_notes_to_existing_course(self):
        result = self.student_with_courses.enroll(
            "math", ["one more note"]                           # добавя се нова бележка (стойност на ключа на речника)
        )

        self.assertEqual(
            "one more note",                                    # проверява се дали втората бележка е в речника
            self.student_with_courses.courses["math"][1]
        )

        self.assertEqual(                                       # проверява се дали връща правилният резултат
            "Course already added. Notes have been updated.",
            result
        )

    def test_enroll_add_notes_to_non_existing_course_without_third_param(self):
        result = self.student_no_courses.enroll(                        # опитваме се да добавим курс при студента без курсове
            'math', ['math notes']                                      # с празен стринг
        )

        self.assertEqual(                                               # проверява се дали в речника на студента без курсове
            'math notes', self.student_no_courses.courses['math'][0]    # е добавен курса, дали го е направило на списък и
        )                                                               # дали е на индекс 0

        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_add_notes_to_non_existing_course_with_third_param(self):
        result = self.student_no_courses.enroll(                        # опитваме се да добавим курс при студента без курсове
            'math', ['math notes'], 'Y'                                 # разликата с предходния тест е че се добавя Y
        )                                                               # т.е. добавяме бележки с 'Y'

        self.assertEqual(                                               # проверява се дали в речника на студента без курсове
            'math notes', self.student_no_courses.courses['math'][0]    # е добавен курса, дали го е направило на списък и
        )                                                               # дали е на индекс 0

        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_without_adding_notes(self):
        result = self.student_no_courses.enroll(                        # не добавяме курс при студента без курсове
            'math', ['math notes'], 'N'                                 # защото сме казали 'N'
        )

        self.assertEqual(                                               #
            0, len(self.student_no_courses.courses['math'])             # проверява се дали дължината на речника е 0
        )                                                               #

        self.assertEqual("Course has been added.", result)              # проверява се дали връща това което трябва

    def test_add_notes_on_existing_course(self):
        result = self.student_with_courses.add_notes(                   # проверява се дали курса съществува при студента с курсовете
            'math', 'new note'
        )

        self.assertEqual(
            'new note', self.student_with_courses.courses['math'][-1]
        )

        self.assertEqual("Notes have been updated", result)

    def test_add_notes_raises_exception(self):
        with self.assertRaises(Exception) as error:
            self.student_no_courses.add_notes('math', 'some note')

        self.assertEqual("Cannot add notes. Course not found.", str(error.exception))

    def test_leave_course_successful(self):
        result = self.student_with_courses.leave_course('math')
        self.assertEqual({}, self.student_with_courses.courses)

        self.assertEqual("Course has been removed", result)

    def test_leave_course_raises_exception(self):
        with self.assertRaises(Exception) as error:
            self.student_no_courses.leave_course('math')

        self.assertEqual("Cannot remove course. Course not found.", str(error.exception))


if __name__ == '__main__':
    main()