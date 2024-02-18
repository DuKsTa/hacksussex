# HackSussex Setup Guide

This guide will walk you through the setup process for your HackSussex project. Please follow the steps below to ensure that your environment is correctly configured.

### Prerequisites

Ensure you have Homebrew installed on your system to use the `brew` command. Homebrew is a package manager for macOS (and Linux) that simplifies the installation of software. Visit the [Homebrew website](https://brew.sh/) for installation instructions if you do not have it installed.

### Step 1: Install Poetry

[Poetry](https://python-poetry.org/) is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

To install Poetry, use the following command in your terminal:

```bash
brew install poetry
```

### Step 2: Install Dependencies
With Poetry installed, you can now install the project dependencies. Dependencies are external libraries or packages that your project relies on.

Navigate to your project directory and run:

```bash
poetry install
```

This command reads the pyproject.toml file in your project directory (if present) and installs the dependencies specified there.

### Step 3: Run the Project
Before running the project, activate the Poetry shell. This will spawn a new shell subprocess, which is configured to use the virtual environment created by Poetry for your project.

```bash
poetry shell
python3 main.py
```
