#!/usr/bin/env python
"""Setup script to make Cheshire installable with pip."""

from pathlib import Path

from setuptools import find_packages, setup

readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text()


setup(
    # This should be the *installed* package name e.g. catalystcoop.pudl not pudl
    name="catalystcoop.handbook",
    description="A one line description of the package.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    # setuptools_scm lets us automagically get package version from GitHub tags
    setup_requires=["setuptools_scm"],
    use_scm_version=True,
    author="Catalyst Cooperative",
    author_email="pudl@catalyst.coop",
    maintainer="Chesire Cat",
    maintainer_email="pudl@catalyst.coop",
    url="",  # Can be repo or docs URL if no separate web page exists.
    project_urls={
        "Source": "https://github.com/catalyst-cooperative/handbook",
        "Documentation": "https://catalystcoop-handbook.readthedocs.io",
        "Issue Tracker": "https://github.com/catalyst-cooperative/handbook/issues",
    },
    license="MIT",
    # Fill in search keywords that users might use to find the package
    keywords=[],
    python_requires=">=3.8,<3.11",
    # In order for the dependabot to update versions, they must be listed here.
    # Use the format pkg_name>=x,<y", Included packages are just examples:
    install_requires=[
        "pandas>=1.4,<1.5.4",
        "sqlalchemy>=1.4,<1.4.47",
    ],
    extras_require={
        "dev": [
            "black>=22.0,<22.13",  # A deterministic code formatter
            "isort>=5.0,<5.12",  # Standardized import sorting
            "tox>=3.20,<4.4",  # Python test environment manager
            "twine>=3.3,<4.1",  # Used to make releases to PyPI
        ],
        "docs": [
            "doc8>=0.9,<1.2",  # Ensures clean documentation formatting
            "furo>=2022.4.7",
            "myst-parser~=0.18.0",
            "mdformat~=0.7.16",
            "sphinx>=4,!=5.1.0,<6.1.4",  # The default Python documentation engine
            "sphinx-autoapi>=1.8,<2.1",  # Generates documentation from docstrings
            "sphinx-issues>=1.2,<3.1",  # Allows references to GitHub issues
        ],
        "tests": [
            "bandit>=1.6,<1.8",  # Checks code for security issues
            "coverage>=5.3,<7.2",  # Lets us track what code is being tested
            "doc8>=0.9,<1.2",  # Ensures clean documentation formatting
            "flake8>=4.0,<6.1",  # A framework for linting & static analysis
            "flake8-builtins>=1.5,<2.2",  # Avoid shadowing Python built-in names
            "flake8-colors>=0.1,<0.2",  # Produce colorful error / warning output
            "flake8-docstrings>=1.5,<1.8",  # Ensure docstrings are formatted well
            "flake8-rst-docstrings>=0.2,<0.4",  # Allow use of ReST in docstrings
            "flake8-use-fstring>=1.0,<1.5",  # Highlight use of old-style string formatting
            "mccabe>=0.6,<0.8",  # Checks that code isn't overly complicated
            "mypy>=0.942,<0.992",  # Static type checking
            "pep8-naming>=0.12,<0.14",  # Require PEP8 compliant variable names
            "pre-commit>=2.9,<3.1",  # Allow us to run pre-commit hooks in testing
            "pydocstyle>=5.1,<6.4",  # Style guidelines for Python documentation
            "pytest>=6.2,<7.3",  # Our testing framework
            "pytest-console-scripts>=1.1,<1.4",  # Allow automatic testing of scripts
            "pytest-cov>=2.10,<4.1",  # Pytest plugin for working with coverage
            "rstcheck[sphinx]>=5.0,<6.2",  # ReStructuredText linter
            "tox>=3.20,<4.4",  # Python test environment manager
        ],
        "types": [
            "types-setuptools",
        ],
    },
    # A controlled vocabulary of tags used by the Python Package Index.
    # Make sure the license and python versions are consistent with other arguments.
    # The full list of recognized classifiers is here: https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    # Directory to search recursively for __init__.py files defining Python packages
    packages=find_packages("src"),
    # Location of the "root" package:
    package_dir={"": "src"},
    # package_data is data that is deployed within the python package on the
    # user's system. setuptools will get whatever is listed in MANIFEST.in
    include_package_data=True,
    # entry_points defines interfaces to command line scripts we distribute.
    # Can also be used for other resource deployments, like intake catalogs.
    entry_points={
        "console_scripts": [
            # "script_name = dotted.module.path.to:main_script_function",
            "winston = handbook.cli:main",
        ]
    },
)
