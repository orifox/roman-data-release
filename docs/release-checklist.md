# Contributor Setup and Release Checklist

This page explains how to work on the documentation from your own computer,
and how to cut a versioned release. Placeholders in angle brackets
(`<like-this>`) must be replaced with your own values.

```{admonition} Prototype status
:class: warning
These steps describe the prototype setup (a public GitHub repository, the free
Read the Docs service, and the Zenodo Sandbox). Update this page when the
project moves to STScI-hosted Git or to the real Zenodo service.
```

## Part 1: One-time setup on your computer

### 1.1 Install the tools

You need Git, Python 3.10 or newer, and an editor. VS Code is what the
prototype uses.

- **Git:** <https://git-scm.com>. On a Mac, running `git --version` the first
  time may ask you to install the developer tools and accept Apple's license
  (`sudo xcodebuild -license`).
- **Python 3.10+:** <https://www.python.org>.
- **VS Code:** <https://code.visualstudio.com>. Useful extensions: MyST-Markdown,
  Python, and GitHub Pull Requests.
- Set your identity for commits (once per computer):
  ```
  git config --global user.name "Your Name"
  git config --global user.email "you@example.com"
  ```
  The email appears on commits in a public repository. GitHub offers a private
  `noreply` address under Settings > Emails.

### 1.2 Get access to the repository

Pick one of these:

- **Collaborator (direct push).** The repository owner adds you under the
  repository's **Settings > Collaborators** and you accept the invitation by
  email. You push branches to the main repository.
- **Fork (no invitation needed).** Click **Fork** on the repository page to
  copy it to your own GitHub account. You push to your fork and open a pull
  request back to the main repository.

### 1.3 Sign in to GitHub from your computer

GitHub does not accept account passwords for pushes. Use one of these:

- **GitHub CLI.** Install it from <https://cli.github.com>, then run
  `gh auth login` and choose GitHub.com, HTTPS, and "Login with a web browser".
- **VS Code.** The GitHub Pull Requests extension can sign you in through the
  browser the first time you push from VS Code's own terminal or Source
  Control panel.
- **Personal access token.** In GitHub, go to Settings > Developer settings >
  Personal access tokens. Create a fine-grained token limited to this
  repository, with Contents set to read and write. When `git push` asks for a
  password, paste the token. Tokens expire, so note the date. Never paste a
  token into a chat, a file, or a commit. If one leaks, revoke it.

### 1.4 Clone and build

```
git clone https://github.com/<owner>/<repo>.git
cd <repo>
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r docs/requirements.txt
sphinx-build -b html docs docs/_build/html
open docs/_build/html/index.html   # Linux: xdg-open
```

If you forked, clone your fork's address instead, then add the main repository
as a second remote so you can pull updates:

```
git remote add upstream https://github.com/<owner>/<repo>.git
```

If the build opens in your browser, your setup works.

## Part 2: Everyday editing workflow

1. **Update first.** Before you edit anything, run `git pull`. Do this every
   time, especially if anyone has edited files on the GitHub website.
2. **Make a branch** for your change: in VS Code, click the branch name in the
   bottom-left corner and choose "Create new branch...", or run
   `git checkout -b <short-description>`.
3. **Edit** the Markdown files in `docs/`. Cmd+Shift+V opens VS Code's preview
   (it shows ordinary Markdown only; MyST directives look plain).
4. **Build locally** and check for warnings:
   ```
   sphinx-build -b html docs docs/_build/html
   ```
5. **Commit.** In the Source Control panel, stage your files, type a short
   message, and click Commit. Or: `git add <files>` and `git commit -m "..."`.
6. **Push.** Click Publish Branch or Sync Changes, or run
   `git push -u origin <your-branch>`.
7. **Open a pull request** on GitHub. Fill in the template, ask for review
   from a subject-matter expert, and merge into `main` after approval.

Changes merged into `main` rebuild the `latest` version on Read the Docs.

## Part 3: Release checklist

Run this when a data release or calibration breakpoint is ready. Replace
`<tag>` with the label, for example `bp-27a`.

### Before tagging

- [ ] All pull requests for this release are merged into `main`.
- [ ] Reviewer sign-off is recorded for each section.
- [ ] No links to living pages (RDocs, Confluence) remain in archival text.
      Content that was linked has been copied in as static text or tables.
- [ ] Links to other documentation projects point to a **tagged** version,
      never `latest`, `stable`, or `main`.
- [ ] `CITATION.cff` is correct: title, authors, version, and license.
- [ ] The release manifest records which calibration and pipeline version this
      release used.
- [ ] A clean local build finishes without warnings.
- [ ] `git status` is clean and your branch is up to date with `origin/main`.

### Cut the release

- [ ] **Tag.** In VS Code: Command Palette, "Git: Create Tag...", enter
      `<tag>`, then "Git: Push Tags". Or in a terminal:
      ```
      git checkout main
      git pull
      git tag <tag>
      git push origin <tag>
      ```
- [ ] **GitHub Release.** On the repository page, choose Releases > Draft a new
      release, select the tag, add a title and short release notes (what is
      new since the previous release), and click Publish release.
      Zenodo archives releases, not bare tags.

### Verify

- [ ] **Read the Docs.** In the project dashboard, open the Versions tab and
      check that `<tag>` is listed and active, and that its build passed.
      Open `https://<project>.readthedocs.io/en/<tag>/` and confirm it shows
      the content you expect.
- [ ] **Zenodo.** Open the record (Uploads page, or the repository's entry in
      Zenodo's GitHub settings) and check that:
  - a version DOI exists for this release;
  - the Files section holds the source archive for this tag;
  - the title, authors, version, and license match `CITATION.cff`;
  - the concept DOI lists this version under Versions.
- [ ] **Record the result.** Add the tag, Read the Docs URL, and version DOI
      to the release manifest and the release notes.

### Later: the real Zenodo

The prototype uses the Zenodo Sandbox, whose records are throwaway. A record on
the real Zenodo is permanent and cannot be deleted. Before the first real
release, settle the metadata and the license, and link the repository at
<https://zenodo.org> instead of the sandbox.

## Part 4: Common problems

| Symptom | Likely cause and fix |
| --- | --- |
| `git push` says branches have diverged, or rejects the push | The remote has commits you lack (often files created on the GitHub website). Run `git pull --rebase origin main`, then `git push`. Don't force-push. |
| `git status` says "not origin/main" or Sync does nothing | The branch has no upstream. Run `git push -u origin <branch>`. |
| Push asks for a password | Use a token or sign in with the GitHub CLI or VS Code (Part 1.3). |
| Read the Docs build fails with "Could not import extension" | A typo in the extension name in `docs/conf.py`, or a package missing from `docs/requirements.txt`. The build log shows which. |
| A new tag does not appear under Versions | Check the project's version automation rules for tags. New tags may need a rule to be created and activated. Then check the GitHub App's access to the repository. |
| GitHub webhook returns an error saying the project uses the GitHub App | Remove the manual webhook. The Read the Docs GitHub App handles notifications. |
| Sphinx says the source parser for markdown is not registered | `myst_parser` is missing from `extensions` in `docs/conf.py`, or not installed in your active environment. |
| A MyST directive shows as a plain code block | The opening fence must be exactly three backticks followed by `{directive-name}`, with no space between. |
| Zenodo shows no record after a release | Confirm the repository's switch is on in Zenodo's GitHub settings, and that you published a GitHub *release* (not only a tag). |

> *Tag in haste, cite in perpetuity: a DOI is forever, so run the checklist first.*
