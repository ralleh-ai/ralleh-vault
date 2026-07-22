.PHONY: doctor doctor-strict test validate

doctor:
	python3 skills/vault/scripts/vault_doctor.py --vault-root scaffold/vault

doctor-strict:
	python3 skills/vault/scripts/vault_doctor.py --vault-root scaffold/vault --strict

test:
	python3 -m unittest discover -s tests -v

validate: test doctor-strict
