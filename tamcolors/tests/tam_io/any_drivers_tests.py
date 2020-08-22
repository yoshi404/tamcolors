# built in libraries
import unittest.mock

# tamcolors libraries
from tamcolors import tam_io


def get_any_io():
    return tam_io.tam_identifier.TAMIdentifier("any_driver_tests",
                                               tam_io.any_drivers.ANYColorDriver,
                                               tam_io.any_drivers.ANYColorChangerDriver,
                                               tam_io.any_drivers.ANYKeyDriver,
                                               tam_io.any_drivers.ANYUtilitiesDriver).get_io()


class AnyIOTests(unittest.TestCase):
    def test_get_io(self):
        io = get_any_io()
        self.assertTrue(io.able_to_execute())

    def test_set_slash_get_mode(self):
        io = get_any_io()
        io.set_mode(2)
        self.assertEqual(io.get_mode(), 2)

    def test_get_modes(self):
        io = get_any_io()
        self.assertEqual(io.get_modes(), (2,))

    def test_get_key(self):
        io = get_any_io()
        self.assertEqual(io.get_key(), False)

    def test_get_dimensions(self):
        io = get_any_io()
        self.assertEqual(io.get_dimensions(), (85, 25))

    def test_get_color(self):
        io = get_any_io()
        for spot in range(16):
            color = io.get_color(spot)
            self.assertIsInstance(color, tam_io.tam_colors.RGBA)

    def test_set_color(self):
        io = get_any_io()
        io.set_color(5, (55, 66, 77))
        color = io.get_color(5)

        self.assertEqual(color, (55, 66, 77))
        io.set_tam_color_defaults()

    def test_set_color_2(self):
        io = get_any_io()

        io.set_color(1, (155, 166, 177))
        color = io.get_color(1)

        self.assertEqual(color, (155, 166, 177))
        io.set_tam_color_defaults()

    @staticmethod
    def test_reset_colors_to_console_defaults():
        io = get_any_io()
        io.reset_colors_to_console_defaults()

    @staticmethod
    def test_set_tam_color_defaults():
        io = get_any_io()
        io.set_tam_color_defaults()
