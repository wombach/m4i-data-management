# How to contribute

This repository is managed by the Van Oord Data Management Platform team.

## Preamble
If you have found a bug, please [file an issue](https://github.com/VanOord/nxtgen-ldv-python-cdc/issues/new). The team will evaluate the problem and incorporate a planned fix onto the backlog if appropriate.

Please find the Data Management Plaform roadmap and backlog [here](https://vanoord.visualstudio.com/Data%20Management).

## Coding conventions
Please observe the following coding conventions:

### Editorconfig
Code style conventions for this repo are enforced through the `.editorconfig`.

#### Install EditorConfig
To enable `.editorconfig` for your editor, please follow these steps:

##### Visual Studio
Editorconfig is enabled in Visual Studio by default.

##### Visual Studio Code
Please install the plugin [EditorConfig for VS Code](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)

##### Vim
```bash
mkdir -p ~/.vim/pack/local/start
cd ~/.vim/pack/local/start
git clone https://github.com/editorconfig/editorconfig-vim.git
```

## Testing
This project uses `pytest` as its unit testing framework.
To run the unit tests, please install `pytest` and then execute the `pytest` command from the project root folder.

```bash
pytest
```

Unit tests are grouped per module.
Unit test modules are located in the same folder as their respective covered modules.
They can be recognized by the `test__` module name prefix, followed by the name of the covered module.

## Submitting changes
When working on a change, please observe the following guidelines:

### Starting off
When you want to start making changes, please check out the `main` branch into a separate `feature-branch`. Feature branches follow the following naming conventions:

- It must be descriptive of the feature or user story you're working on
- It includes a user story number where applicable
- Words are separated using `kebab-case`

The following example checks out the `main` branch into the  `1234-my-feature-branch`, and creates the feature branch if it doesn't yet exist:

```bash
git checkout -b 1234-my-feature-branch main
```

### Commiting work in progress
Please use your `feature-branch` to commit your work while it is in progress.

Always write a clear log message for your commits. One-line messages are fine for small changes, but bigger changes should look like this:

```bash
git commit -m "A brief summary of the commit

A paragraph describing what changed and its impact."
```

#### Pre-commit
For this repository, `pre-commit` has been enabled. Before every commit, the following checks are performed:

- Does the code conform with coding style conventions?
- Do the unit tests pass?

Please follow these instructions to enable `pre-commit` for your editor or repository:

##### Visual Studio (+Code)
Please install the [pre-commit](https://marketplace.visualstudio.com/items?itemName=MarkLarah.pre-commit-vscode) plugin

##### Linux
```bash
pip3 install -u pre-commit
cd /path/to/repo
pre-commit install
```

##### Windows
```bash
pip install pre-commit
cd /path/to/repo
python -m pre_commit install
```

### Submitting changes
To submit the changes in your `feature-branch` to the `main` branch, please send a [pull request](https://github.com/VanOord/nxtgen-ldv-python-cdc/pull/new/main).

#### Pull request conventions
A pull request should consist of the following:

- A reference to the feature or user story on the DMP backlog
- References to any applicable design documents.
- A short description of your proposed solution.

#### Review criteria
Pull requests are subject to peer review and need at least `1` approval before being allowed to merge. The following criteria generally apply:

- The pull request includes all the necessary information as described above
- New code must be covered by unit tests
- All existing unit tests must be updated to reflect the changes
- New code must be covered by documentation in accordance with the guidelines
- All existing documentation must be updated to reflect the changes
- All unit tests must pass
- All `pre-commit` checks must pass

#### Merge policies
Furthermore, the following policies apply for pull requests to the `main` branch:

- Pull requests to main need at least `1` approval before being allowed to merge.
- Stale approvals are automatically dismissed.
- The only merge strategy allowed is squash merge.
- Merged branches will be automatically deleted.



