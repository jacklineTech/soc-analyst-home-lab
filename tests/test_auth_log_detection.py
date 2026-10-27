import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "detection-rules" / "analyze_auth_logs.py"
LOGS = ROOT / "evidence" / "sample-logs"


def analyze(filename):
    result = subprocess.run(
        [sys.executable, str(SCRIPT), str(LOGS / filename)],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout


class TestAuthenticationDetection(unittest.TestCase):

    def test_four_failures_trigger_alert(self):
        output = analyze("sample-auth.log")
        self.assertIn("Failed logins: 4", output)
        self.assertIn("ALERT: Repeated failed logins", output)

    def test_two_failures_do_not_trigger_alert(self):
        output = analyze("sample-auth-low-volume.log")
        self.assertIn("Failed logins: 2", output)
        self.assertIn("No alert: Count is below the configured threshold.", output)
        self.assertNotIn("ALERT: Repeated failed logins", output)

    def test_successful_login_is_counted(self):
        output = analyze("sample-auth.log")
        self.assertIn("Successful login events in sample: 1", output)


    def test_failures_followed_by_success_trigger_alert(self):
        output = analyze("sample-auth-suspicious-sequence.log")
        self.assertIn("Failed logins: 3", output)
        self.assertIn(
            "ALERT: Failed logins followed by a successful login from 192.0.2.75",
            output,
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
