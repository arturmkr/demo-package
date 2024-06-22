# Python Packaging Example

This repository demonstrates effective practices for packaging Python code, using a simple system metrics collection library as an example. The actual code used for demonstration is hosted in a separate repository, which you can access [here](https://github.com/arturmkr/metrics).

## Installation

To install this package directly from GitHub using pipenv, add the following to your `Pipfile`:

```toml
[packages]
metrics = { git = "https://github.com/arturmkr/metrics-package.git", ref = "main", egg = "metrics" }