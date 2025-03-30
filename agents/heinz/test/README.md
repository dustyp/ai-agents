# Agent Testing Framework

This directory contains the testing framework for verifying agent behavior, procedure execution, and rule compliance.

## Structure

- `bootstrap/`: Tests for agent bootstrap process
- `procedures/`: Tests for procedure execution and validation
- `rules/`: Tests for rule compliance and flattened rule system integrity

## Test Philosophy

The agent testing framework follows these principles:

1. **Reproducibility**: Tests should produce consistent results
2. **Isolation**: Each test should focus on a specific feature or behavior
3. **Clarity**: Test failure messages should clearly indicate what went wrong
4. **Coverage**: Tests should cover core functionality and edge cases
5. **Performance**: Tests should execute efficiently

## Rule Testing

The rule tests verify the integrity of the flattened rule system in CLAUDE.md and the reference examples. The tests ensure:
- All required rule categories exist
- Critical rules are properly defined
- Rule index properly maps to the flattened rule system

## Running Tests

To run all tests:
```bash
./run_tests.sh
```

To run a specific test category:
```bash
./run_tests.sh bootstrap
./run_tests.sh procedures
./run_tests.sh rules
```