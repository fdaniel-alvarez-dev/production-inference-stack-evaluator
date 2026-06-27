PYTHON ?= python
PYTHONPATH := src

.PHONY: setup lint test security docs example clean

setup:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -e .

lint:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m compileall -q src tests

test:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m unittest discover -s tests/unit -p 'test_*.py'

security:
	bash scripts/basic_secret_scan.sh

docs:
	@test -f README.md
	@test -f docs/architecture.md
	@test -f docs/security/threat-model.md
	@grep -q "Start with workload characterization" README.md

example:
	mkdir -p reports
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m inference_stack_eval.cli evaluate --metrics examples/minimal/metrics.csv --weights examples/minimal/weights.json --out reports/minimal_report.md

clean:
	rm -rf reports .pytest_cache .mypy_cache .ruff_cache build dist *.egg-info
	find . -type d -name __pycache__ -prune -exec rm -rf {} +

validate-public:
	python scripts/validate_repo.py
