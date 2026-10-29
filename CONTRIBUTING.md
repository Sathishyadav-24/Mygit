# Contributing to Mygit

Thanks for helping improve Mygit. Keep changes focused and explain the problem they solve.

## Suggest a change

For a substantial feature or change in direction, open an issue describing the goal and expected result before starting work. Small fixes can go straight to a pull request.

## Make a change

1. Clone the repository. If you do not have write access, fork it first and clone your fork.
2. Create a branch:

   ```sh
   git switch -c feature/short-description
   ```

3. Make a focused change. Update documentation and add or update tests where relevant.
4. Review the changes, stage them, and commit:

   ```sh
   git status
   git add -A
   git diff --cached
   git commit -m "Describe your change"
   git push -u origin feature/short-description
   ```

5. Open a pull request to Mygit's `main` branch. Describe what changed, why, and how you checked it; link a related issue if there is one.

## Before submitting

- Check that no passwords, keys, private information, generated dependencies, or local environment files are included.
- Run the applicable checks and mention their results in the pull request. Run `python3 -m unittest discover -s tests -v` (or `py -3 -m unittest discover -s tests -v` on Windows).
- Keep setup and usage instructions current when the behavior or required tools change.
