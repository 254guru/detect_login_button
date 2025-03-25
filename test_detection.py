import unittest
from detect_login_button import find_login_button

class TestLoginButtonDetection(unittest.TestCase):
    def test_detect_login_button(self):
        """Test that the login button detection returns a valid coordinate."""
        test_image_path = "tublian_screenshot.png"  # Ensure this exists or generate it before testing
        coordinates = find_login_button(test_image_path)

        # Assert that coordinates are returned and are reasonable values
        self.assertIsNotNone(coordinates, "Login button was not detected.")
        self.assertTrue(isinstance(coordinates, tuple) and len(coordinates) == 2, "Invalid coordinates format.")
        self.assertTrue(coordinates[0] > 0 and coordinates[1] > 0, "Coordinates should be positive values.")

if __name__ == "__main__":
    unittest.main()
