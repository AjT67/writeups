# Setup — publishing this repo to GitHub

GitHub account: **AjT67** · target repo name: **writeups**

## One-time: tell git who you are

If you've never used git on this machine, open a terminal (in VS Code: `` Ctrl+` ``)
and run these once:

```powershell
git config --global user.name "AjT67"
git config --global user.email "ajnataylor@gmail.com"
```

---

## Option A — VS Code (easiest, no tokens)

1. **File → Open Folder** and pick this `writeups-repo` folder.
2. Open the **Source Control** panel (branch icon in the left sidebar, or `Ctrl+Shift+G`).
3. Click **Initialize Repository**.
4. Type a commit message (e.g. `Initial commit`) and click **✓ Commit**.
   If asked whether to stage all changes, say **Yes**.
5. Click **Publish Branch** (may appear as **Publish to GitHub**).
   The first time, a browser opens to sign in to GitHub as **AjT67**.
6. Choose **Public**, keep the name `writeups`, and it pushes everything up.

VS Code shows a link to the new repo when it's done.

---

## Option B — PowerShell with GitHub CLI

Install GitHub CLI once (https://cli.github.com/ or `winget install GitHub.cli`),
then from inside this folder:

```powershell
cd C:\path\to\writeups-repo     # change to wherever you unzipped it
gh auth login                    # GitHub.com -> HTTPS -> login with browser (as AjT67)
git init
git add -A
git commit -m "Initial commit"
git branch -M main
gh repo create writeups --public --source=. --push
```

The last line creates the repo on your account **and** pushes in one step — no
password or token to manage.

---

## Turn on the website (GitHub Pages)

Once the code is pushed, on github.com:

1. Go to the **writeups** repo → **Settings** → **Pages**.
2. Under **Build and deployment → Source**, choose **Deploy from a branch**.
3. Branch: **main**, folder: **/(root)**. Click **Save**.
4. Wait ~1 minute. Your site is live at:

   **https://ajt67.github.io/writeups/**

---

## Working from Kali Linux

If you're doing the boxes on Kali, it's easiest to write and push straight from
there rather than copying files between machines. Git is already installed on
Kali.

### One-time setup on Kali

```bash
# tell git who you are (once)
git config --global user.name  "AjT67"
git config --global user.email "ajnataylor@gmail.com"

# get the repo onto the Kali box
cd ~
git clone https://github.com/AjT67/writeups.git
cd writeups
```

For pushing, the least-friction auth is GitHub CLI:

```bash
sudo apt update && sudo apt install gh -y
gh auth login        # GitHub.com -> HTTPS -> login with browser (as AjT67)
```

After `gh auth login`, normal `git push` just works — no password or token to
paste each time.

### Writing a box up on Kali

```bash
cd ~/writeups
cp TEMPLATE.md writeups/2026-09-boxname.md
# fill it in as you go — write the dead ends while they still sting
```

**Screenshots and evidence.** Put images in a folder named after the box so the
repo stays tidy, and reference them with a relative path from inside the writeup:

```bash
mkdir -p writeups/img/boxname
# save your screenshots into that folder, then in the .md:
#   ![foothold](img/boxname/foothold.png)
```

### Before you commit — sanitise

The `.gitignore` already blocks `.ovpn`, pcaps, keystores and anything matching
`*_creds*`, but check by eye every time — this repo is public:

- no flag values, passwords, hashes, tokens or SSH keys in the text or images
- crop or blur anything in a screenshot that shows a credential or your VPN IP
- confirm the target is **retired**, not just expired (see `writeups/README.md`)

### Commit and push from Kali

```bash
python3 tools/build_index.py     # rebuild the index (only counts published posts)
git add -A
git status                       # last look at exactly what's going up
git commit -m "Add boxname writeup"
git push
```

Because you cloned over HTTPS with `gh` logged in, `git push` sends it straight
to GitHub and the site updates within a minute or two.

> Tip: keep the machine you write on and the machine you attack from separate in
> your head. It's fine to draft notes on Kali during the box, but do the final
> tidy-up and the sanitise pass deliberately before pushing — it's the step
> that stops a flag or a key ending up in public history, which is very hard to
> fully undo once pushed.

---

## Day-to-day: adding a writeup later

```powershell
copy TEMPLATE.md writeups\2026-09-targetname.md
# write it, then change `status: draft` to `status: published` in the frontmatter
python tools\build_index.py        # rebuilds the index table in README.md
git add -A
git commit -m "Add targetname writeup"
git push
```

The index also rebuilds automatically on GitHub after each push (via the Action
in `.github/workflows/`), so if you forget `build_index.py` locally it still
gets fixed server-side.
