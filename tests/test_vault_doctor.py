from __future__ import annotations

import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DOCTOR = ROOT / "skills" / "vault" / "scripts" / "vault_doctor.py"
FIXTURES = ROOT / "tests" / "fixtures"


class VaultDoctorTests(unittest.TestCase):
    def run_doctor(self, vault_root: Path, *args: str) -> subprocess.CompletedProcess[str]:
        cmd = ["python3", str(DOCTOR), "--vault-root", str(vault_root), *args]
        return subprocess.run(cmd, text=True, capture_output=True)

    def copy_fixture(self, name: str) -> Path:
        tmp = Path(tempfile.mkdtemp(prefix="vault-fixture-"))
        self.addCleanup(lambda: shutil.rmtree(tmp, ignore_errors=True))
        shutil.copytree(FIXTURES / name, tmp / "vault")
        return tmp / "vault"

    def test_ok_fixture_passes_strict(self) -> None:
        root = self.copy_fixture("vault_ok")
        result = self.run_doctor(root, "--strict")
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)

    def test_missing_frontmatter_fails(self) -> None:
        root = self.copy_fixture("vault_missing_frontmatter")
        result = self.run_doctor(root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing frontmatter", result.stdout)

    def test_broken_wikilink_fails(self) -> None:
        root = self.copy_fixture("vault_broken_link")
        result = self.run_doctor(root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("broken wikilink", result.stdout)

    def test_approval_gate_enforced(self) -> None:
        root = self.copy_fixture("vault_approval_missing")
        result = self.run_doctor(root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("approval gate unmet", result.stdout)

    def test_stale_inbox_enforced(self) -> None:
        root = self.copy_fixture("vault_ok")
        stale = root / "Inbox" / "stale.md"
        stale.write_text("# stale item\n", encoding="utf-8")

        # Force stale check to trigger: threshold=0h means any existing file should fail.
        result = self.run_doctor(root, "--inbox-max-age-hours", "0")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("stale Inbox", result.stdout)


if __name__ == "__main__":
    unittest.main()
