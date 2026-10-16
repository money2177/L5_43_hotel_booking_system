# Lab 5: Static Code Analysis

## Issue Documentation

| Issue | Type | Original Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Unsafe eval() | Security | 42 | Evaluates a string as Python code, potentially executing unsafe expressions. | Replaced with a validated numeric multiplier. |
| Hard-coded secret | Security | 65, 78 | A secret-like value is stored in the source code and printed. | Removed the embedded secret and its output. |
| Shell command execution | Security | 59 | os.system() executes a shell command containing a filename. | Removed shell execution and used a normal print statement. |
| Weak MD5 hashing | Security | 49 | MD5 is unsuitable when collision resistance is required. | Replaced MD5 with SHA-256. |
| Mutable default argument | Bug | 18 | A default list may be shared between function calls. | Changed the default to None and initialized a list when needed. |
| Bare exception | Reliability | 26-28 | A bare except silently suppresses errors. | Added explicit checks for valid room numbers and booking status. |
| Unused variables | Code Quality | 31, 41 | Unused variables and imports reduce readability. | Removed unused variables and imports. |
| Unsafe file handling | Reliability | 55-57 | Manual file handling lacks explicit encoding and safe resource management. | Used pathlib with explicit UTF-8 encoding. |
| Naming conventions | Style | 18 | bookRoom does not follow snake_case naming conventions. | Renamed the function to book_room. |
| Missing docstrings | Code Quality | Throughout | Functions lack documentation. | Added docstrings to the functions. |

## Verification

The updated code must be analyzed again using Pylint,
Bandit, and Flake8.

The final Pylint score must exceed 9.5/10.
All Bandit findings and Flake8 formatting issues
must be reviewed and addressed.