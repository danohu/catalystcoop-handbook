# Catalyst Cooperative Handbook

[The Catalyst Cooperative Handbook](https://catalystcoop-handbook.readthedocs.io/en/latest/) contains the cooperative's bylaws, policies and general information.

This repo allows us to version control and review changes to our policies.

<!-- readme-intro -->

## Setup Conda Environment

To edit these docs you need to clone the [`catalyst-handbook`](https://github.com/catalyst-cooperative/catalystcoop-handbook) repo and set up a conda environment:

```
git clone git@github.com:catalyst-cooperative/catalystcoop-handbook.git
```

We use the conda package manager to specify and update our development environment. We recommend using [miniconda](https://docs.conda.io/en/latest/miniconda.html) rather than the large pre-defined collection of scientific packages bundled together in the Anaconda Python distribution. You may also want to consider using [mamba](https://github.com/mamba-org/mamba) – a faster drop-in replacement for conda written in C++.

```
conda update conda
conda env create --name handbook --file environment.yml
conda activate handbook
```

## Git Pre-commit Hooks

Git hooks let you automatically run scripts at various points as you manage your source code. “Pre-commit” hook scripts are run when you try to make a new commit. These scripts can review your code and identify bugs, formatting errors, bad coding habits, and other issues before the code gets checked in. This gives you the opportunity to fix those issues before publishing them.

To make sure they are run before you commit any code, you need to enable the pre-commit hooks scripts with this command:

```
pre-commit install
```

The scripts that run are configured in the .pre-commit-config.yaml file.

## How to make changes

### CLI

To make changes to the handbook, edit the relevant markdown documents in the `docs/` directory. Once the changes are made
you can build the docs by running:

```
tox -e docs
```

This command will build the docs and write the html files to `docs/_build/`. You can view the docs locally by opening the `docs/_build/index.html` file.
Once the docs are built locally, you can push your changes and open a PR for review. There is a GitHub Action that will build and deploy the changes
to Read the Docs.

### UI

If you don't want to make edits with a CLI and code editor, you can use the GitHub UI:

1. Click the "Edit" button for the document you want to change:

<img width="1265" alt="image" src="https://user-images.githubusercontent.com/17532695/199124407-0f2036e8-c669-40f4-9083-d23e636b553d.png">

2. Make you're changes.
3. Select "Create a **new branch** for this comment and start a pull request", add a commit message and select "Commit changes":
   <img width="1216" alt="image" src="https://user-images.githubusercontent.com/17532695/199124752-e7c0eccd-1300-4c27-9821-82b6155b4c9e.png">

4. Tag someone to review your changes.

The changes must be reviewed and approved by someone else to be merged into the `main` branch.
