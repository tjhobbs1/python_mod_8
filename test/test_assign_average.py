import unittest
import more_fun_with_collections.assign_average as grade


class GradeT_est(unittest.TestCase):
    def test_switch_statement(self):
        self.assertEqual(grade.switch_average("A"),90)
        self.assertEqual(grade.switch_average("B"),80)
        self.assertEqual(grade.switch_average("C"),70)
        self.assertEqual(grade.switch_average("D"),60)
        self.assertEqual(grade.switch_average("F"),50)
        self.assertEqual(grade.switch_average("T"),"Not a valid grade")
        self.assertEqual(grade.switch_average(80),"Not a valid grade")
        self.assertEqual(grade.switch_average("a"),"Not a valid grade")


if __name__ == '__main__':
    print(unittest.main())

