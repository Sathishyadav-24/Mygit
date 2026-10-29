import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
from brief_check import missing_decisions


class BriefCheckTests(unittest.TestCase):
    def test_detects_table_and_milestone_placeholders(self):
        text = '| Problem | To decide |\n| Platform | To decide (web or mobile) |\n- **Deliverable:** To decide\n- **Open questions:** None\n'
        self.assertEqual(missing_decisions(text), ['Problem', 'Platform', 'Deliverable'])

    def test_completed_brief_has_no_missing_decisions(self):
        self.assertEqual(missing_decisions('| Problem | Organize notes |\n- **Deliverable:** A prototype\n'), [])

    def test_cli_exit_codes_and_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            brief = Path(tmp) / 'brief.md'
            brief.write_text('| Problem | To decide |\n', encoding='utf-8')
            command = [sys.executable, str(ROOT / 'src' / 'brief_check.py'), str(brief)]
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn('Problem', result.stdout)
            brief.write_text('| Problem | Organize notes |\n', encoding='utf-8')
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0)
            self.assertIn('No', result.stdout)
            brief.unlink()
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertIn('Cannot read brief', result.stderr)


if __name__ == '__main__':
    unittest.main()
