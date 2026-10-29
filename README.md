# Mygit

Mygit is a starting place for planning, building, testing, and preparing a software project for release. Its purpose, audience, and technology are still to be decided. This structure can be adapted to a web app, API, Android app, or another kind of project.

## Current status

The repository includes a small project-brief readiness checker and automated tests. The product, platform, and deployment setup remain undecided.

## Get started

1. Clone the repository and enter its folder:

   ```sh
   git clone https://github.com/Sathishyadav-24/Mygit.git
   cd Mygit
   ```

2. Install Python 3.9 or newer. No third-party packages are required.
3. Run the brief checker from the repository root:

   ```sh
   python3 src/brief_check.py
   ```

   On Windows, use `py -3 src/brief_check.py`. Edit [the project brief](docs/project-brief.md) to replace the `To decide` placeholders. The checker lists placeholders in the brief's two-column table and milestone fields; it does not judge whether answers are meaningful. Exit codes: `0` means no matching placeholders, `1` means decisions remain, and `2` means the file could not be read. To check a different brief, pass its path as an argument.

4. Run the tests from the repository root:

   ```sh
   python3 -m unittest discover -s tests -v
   ```

   On Windows, use `py -3 -m unittest discover -s tests -v`. Choose the next milestone from the [roadmap](ROADMAP.md).

## Repository guide

| Path | Purpose |
| --- | --- |
| [src/](src/) | Project source code, including the brief checker. |
| [tests/](tests/) | Automated tests and test resources. |
| [docs/](docs/) | Project notes, beginning with the project brief. |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to propose, check, and submit changes. |
| [ROADMAP.md](ROADMAP.md) | Suggested steps from idea to first release. |

The folders are a starting point: rename or reorganize them if the chosen tools need a different layout.

## Configuration

Do not commit passwords, API keys, private data, or real environment files to this public repository. The starter [.gitignore](.gitignore) excludes common local environment files; extend it for the tools you choose. Add a safe example configuration and document its use when configuration is needed.
