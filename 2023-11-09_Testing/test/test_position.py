from unittest import TestCase
from game.position import Position, Point


class PointTest(TestCase):
    def setUp(self) -> None:
        self.point = Point(1, 2)

    def test_init_positional(self):
        point = Point(1, 2)
        self.assertEqual(point.x, 1)
        self.assertEqual(point.y, 2)

    def test_init_keyword(self):
        point = Point(x=1, y=2)
        self.assertEqual(point.x, 1)
        self.assertEqual(point.y, 2)

    def test_str(self):
        self.assertEqual(str(self.point), '(1, 2)')


class PositionTest(TestCase):
    def setUp(self) -> None:
        self.point = Position(x=10, y=20)

    def test_position_set_keyword(self):
        self.point.position_set(x=1, y=2)
        self.assertEqual(self.point._position.x, 1)
        self.assertEqual(self.point._position.y, 2)

    def test_position_set_positional(self):
        with self.assertRaises(TypeError):
            self.point.position_set(1, 2)  # noqa

    def test_position_change_left(self):
        self.point.position_change(left=1)
        self.assertEqual(self.point._position.x, 9)
        self.assertEqual(self.point._position.y, 20)

    def test_position_change_right(self):
        self.point.position_change(right=1)
        self.assertEqual(self.point._position.x, 11)
        self.assertEqual(self.point._position.y, 20)

    def test_position_change_up(self):
        self.point.position_change(up=1)
        self.assertEqual(self.point._position.x, 10)
        self.assertEqual(self.point._position.y, 19)

    def test_position_change_down(self):
        self.point.position_change(down=1)
        self.assertEqual(self.point._position.x, 10)
        self.assertEqual(self.point._position.y, 21)

    def test_position_change_vertical(self):
        self.point.position_change(left=1, right=2)
        self.assertEqual(self.point._position.x, 11)
        self.assertEqual(self.point._position.y, 20)

    def test_position_change_horizontal(self):
        self.point.position_change(up=1, down=2)
        self.assertEqual(self.point._position.x, 10)
        self.assertEqual(self.point._position.y, 21)

    def test_position_change_omnidirectional(self):
        self.point.position_change(left=1, right=2, up=3, down=4)
        self.assertEqual(self.point._position.x, 11)
        self.assertEqual(self.point._position.y, 21)

    def test_position_change_positional(self):
        with self.assertRaises(TypeError):
            self.point.position_change(1)  # noqa
        with self.assertRaises(TypeError):
            self.point.position_change(1, 2)  # noqa
        with self.assertRaises(TypeError):
            self.point.position_change(1, 2, 3)  # noqa
        with self.assertRaises(TypeError):
            self.point.position_change(1, 2, 3, 4)  # noqa

    def test_position_get(self):
        current_x, current_y = self.point.position_get()
        self.assertEqual(current_x, 10)
        self.assertEqual(current_y, 20)
