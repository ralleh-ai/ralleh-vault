from __future__ import annotations

import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


class RoleAuditTests(unittest.TestCase):
    def run_audit(self, repo_root: Path) -> subprocess.CompletedProcess[str]:
        audit = repo_root / "scripts" / "audit_roles.py"
        return subprocess.run(["python3", str(audit)], cwd=repo_root, text=True, capture_output=True)

    def test_current_roles_are_golden(self) -> None:
        result = self.run_audit(ROOT)
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
        self.assertIn("ROLE vault", result.stdout)
        self.assertIn("ROLE vault-fast", result.stdout)
        self.assertIn("Verdict: golden", result.stdout)

    def test_missing_required_section_fails(self) -> None:
        tmp = Path(tempfile.mkdtemp(prefix="vault-role-audit-"))
        self.addCleanup(lambda: shutil.rmtree(tmp, ignore_errors=True))

        # Copy only the paths required by the audit script.
        shutil.copytree(ROOT / "agents", tmp / "agents")
        shutil.copytree(ROOT / "scripts", tmp / "scripts")

        target = tmp / "agents" / "roles" / "vault" / "AGENTS.md"
        text = target.read_text(encoding="utf-8")
        text = text.replace("## Verification Protocol", "## Verification")
        target.write_text(text, encoding="utf-8")

        result = self.run_audit(tmp)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing required section", result.stdout)


if __name__ == "__main__":
    unittest.main()
