# Code Review Guidelines

## 1. Code Quality Checks
Before merging, ensure that:
- Code passes **Flake8** checks (`flake8 app.py`).
- All **pytest** tests pass (`pytest`).

## 2. Best Practices
- Follow **PEP 8** coding style.
- Keep functions small and modular.

## 3. Reviewing API Code
- Ensure API endpoints return the expected responses.
- Validate error handling.
- Log critical actions for debugging.

## 4. Security Checks
- No sensitive credentials in code.
- Validate all input data.
