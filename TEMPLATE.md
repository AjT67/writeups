---
title: "Machine Name"
platform: "HTB"            # HTB | TryHackMe | VulnHub | Proving Grounds | Own lab
target: "machine-name"
os: "Linux"                # Linux | Windows | Other
difficulty: "Easy"         # Easy | Medium | Hard | Insane
date: 2026-01-01           # date you finished it, YYYY-MM-DD
tags: [web, sqli, lateral-movement, sudo-misconfig]
techniques: []             # optional: MITRE ATT&CK IDs, e.g. [T1190, T1078]
status: draft              # draft | published
---

<!--
PUBLISHING CHECK — do not remove until you have ticked it.

[ ] This target is RETIRED (or Starting Point / Tier 0 Academy / free Academy course).
    HTB permits solutions only for retired content. A machine can be EXPIRED (no
    longer scoring seasonal points) while still being ACTIVE — check the official
    retirement status, not the season status.
    https://help.hackthebox.com/en/articles/5188925-streaming-writeups-walkthrough-guidelines

[ ] No credentials, tokens, or flag values are pasted below.
[ ] Nothing here identifies another user's infrastructure.
-->

## Attack path

> One paragraph, plain language. Someone should be able to read this alone and
> know how the box fell. Write it LAST, once you know which parts mattered.

`recon → foothold → pivot → root`, as a single line.

---

## Recon

What I scanned, and what came back. Keep the output trimmed to what was
actually relevant — a full nmap dump proves nothing.

**What stood out:**

**What I deliberately ignored, and why:**

> This second prompt is the point of the section. Anyone can list open ports.
> Explaining why you walked past three of them is the part that reads like
> judgement.

---

## Enumeration

The reasoning, not just the commands.

**Hypothesis I was testing:**

**What I found:**

**What it told me to try next:**

---

## Foothold

How initial access happened.

**The vulnerability:**

**Why it was exploitable here specifically:**

**What I had to change from the public PoC, and why:**

> If you used an off-the-shelf exploit unmodified, say so plainly. If you had to
> fix an offset, swap a payload, or work out why it silently failed the first
> three times — that is the most valuable paragraph in the whole writeup.

---

## Privilege escalation

**What I enumerated post-foothold:**

**The misconfiguration / vulnerability:**

**The escalation:**

---

## Dead ends

> Mandatory section. Do not skip it because the writeup looks cleaner without it.
>
> A walkthrough that runs straight from nmap to root shows you can follow a path
> someone else already found. The dead ends are what show how you think when
> nobody has found the path yet — and that is the thing being assessed.

- **What I tried:** …
  **Why I thought it would work:** …
  **Why it didn't:** …
  **What it ruled out:** …

- **Where I got stuck longest:** …
  **What unstuck me:** …

- **Did I use a hint or a walkthrough?** If yes, say where and what you'd missed.
  Nobody is fooled by a flawless record, and admitting it costs you nothing.

---

## Lessons

**What I'd do differently next time:**

**What I now check earlier in my process:**

**Anything that went into `notes/methodology.md` as a result:**

---

## Detection and mitigation

> Optional but worth doing. Two or three lines on what this attack would look
> like in logs, and what would have prevented it.
>
> Offensive work that shows an understanding of the defensive side reads as
> considerably more mature — and it is what separates "I did the box" from
> "I understand the system".

**What this looks like from the defender's side:**

**What would have stopped it:**

---

## References

- 
