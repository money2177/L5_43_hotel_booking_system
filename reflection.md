# Lab 5: Static Code Analysis Reflection

## 1. What is static code analysis?

Static code analysis examines source code without executing
the program. It helps identify potential bugs, security
vulnerabilities, and coding-style problems early in development.

## 2. What did Pylint, Bandit, and Flake8 contribute?

Pylint identifies code-quality issues, naming problems,
unused variables, and potential programming mistakes.

Bandit identifies potentially insecure Python coding patterns.

Flake8 checks Python formatting and style conventions.

Using these tools together provides a more comprehensive
review of the source code.

## 3. Which issues were most important?

The most important security issues included unsafe eval()
usage, a hard-coded secret, and shell command execution.

These were addressed by replacing dynamic evaluation with
validated numeric input, removing the embedded secret,
and removing unnecessary shell execution.

Other improvements included correcting mutable default
arguments, replacing MD5 hashing, and improving file handling.

## 4. What are the limitations of static analysis?

Static analysis can identify suspicious code patterns,
but it cannot guarantee that a program is completely correct
or secure.

The program must also be tested, and the analysis tools
must be rerun after changes to verify the results.