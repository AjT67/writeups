# Methodology

A living checklist. The point is not to have a perfect process on day one — it
is to add a line every time a box teaches you something, so that six months of
labs compounds into a repeatable method instead of evaporating.

When a writeup's **Lessons** section produces something reusable, it goes here.

## Recon

- [ ] Full TCP port scan, then targeted service/version scan on what's open
- [ ] UDP scan on the usual suspects if TCP is thin
- [ ] Note every service *and* what I chose not to chase, with a reason

## Web

- [ ] Directory and vhost enumeration
- [ ] Check source, comments, JS files, and any `/robots.txt` or sitemap
- [ ] Identify the stack and version; look up known CVEs before hand-testing
- [ ] Test inputs for injection systematically rather than at random

## Foothold

- [ ] Understand *why* the exploit works before running it, not just that it does
- [ ] Keep a copy of any PoC I modify, with a note on what I changed

## Post-exploitation / privesc

- [ ] Automated enumeration (linpeas / winpeas) AND read the output, don't just grep for green
- [ ] `sudo -l`, SUID binaries, cron, writable paths, service configs
- [ ] Credentials reuse — check everything I've already found against everything else

## Reporting habit

- [ ] Screenshot / log as I go, not afterwards from memory
- [ ] Write the dead ends down while they still sting — they're useless reconstructed later

---

## Lessons log

_Newest first. One line each: the thing, and the box that taught it._

- 
