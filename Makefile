.PHONY: doctor doctor-strict test audit-roles validate

doctor:
	python3 skills/vault/scripts/vault_doctor.py --vault-root scaffold/vault

doctor-strict:
	python3 skills/vault/scripts/vault_doctor.py --vault-root scaffold/vault --strict

test:
	python3 -m unittest discover -s tests -v

audit-roles:
	python3 scripts/audit_roles.py

validate: test doctor-strict audit-roles
