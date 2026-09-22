import tempfile
import unittest
from pathlib import Path

from tools.password_checker import check_password
from tools.file_hash import sha256_file
from tools.url_analyzer import urlparse\n


class TestPasswordChecker(unittest.TestCase):
    def test_strong_password_scores_high(self):
        score, feedback = check_password("StrongPass123!")
        self.assertEqual(score, 6)
        self.assertEqual(feedback, [])

    def test_short_password_gets_feedback(self):
        score, feedback = check_password("abc")
        self.assertLess(score, 3)
        self.assertIn("Use at least 8 characters.", feedback)


class TestFileHash(unittest.TestCase):
    def test_sha256_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "sample.txt"
            path.write_text("hello", encoding="utf-8")
            self.assertEqual(
                sha256_file(str(path)),
                "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824",
            )


class TestURLAnalyzer(unittest.TestCase):
    def test_invalid_port_raises(self):\n        with self.assertRaises(ValueError):\n            urlparse("https://example.com:invalid")\n\n    def test_url_components(self):
        parsed = urlparse("https://example.com:8080/path?x=1#section")
        self.assertEqual(parsed.scheme, "https")
        self.assertEqual(parsed.hostname, "example.com")
        self.assertEqual(parsed.port, 8080)
        self.assertEqual(parsed.path, "/path")
        self.assertEqual(parsed.query, "x=1")
        self.assertEqual(parsed.fragment, "section")


if __name__ == "__main__":
    unittest.main()
