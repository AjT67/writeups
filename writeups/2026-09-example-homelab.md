---
title: "Example — Home Lab VM"
platform: "Own lab"
target: "example-homelab"
os: "Linux"
difficulty: "Easy"
date: 2026-09-07
tags: [example, template-demo]
techniques: []
status: published
---

<!--
This is a FICTIONAL worked example on a self-built lab VM, included to show the
house style. It solves nothing real and breaches nobody's terms. Delete it once
you have a couple of genuine writeups, or keep it — it does no harm.

Note how much of the value below sits in "Dead ends" rather than in the parts
that worked.
-->

## Attack path

An outdated internal wiki was reachable on a high port that the obvious web
service on 80 distracted from. Its export feature accepted a path parameter that
wasn't confined to the export directory, which gave arbitrary file read as the
service account — enough to recover an SSH key. The service account could run a
backup script as root via sudo, and that script called `tar` with a wildcard,
which is trivially turned into command execution.

`port 8080 wiki → path traversal → SSH key → sudo tar wildcard → root`

---

## Recon

Full TCP sweep rather than the default top-1000, which is the only reason 8080
turned up at all.

```
22/tcp   open  ssh      OpenSSH 8.9p1
80/tcp   open  http     nginx 1.18.0
8080/tcp open  http-alt (wiki software, version banner suppressed)
```

**What stood out:** the version banner on 8080 was deliberately stripped while
80 advertised itself freely. Someone had thought about hiding 8080 specifically,
which is usually a sign it's the interesting one.

**What I deliberately ignored, and why:** port 80 served a static brochure site
with no forms, no login, and nothing dynamic in the page source. I spent about
ten minutes confirming that and then left it alone. In hindsight that was the
single best decision of the session — I'd have burned an hour fuzzing it
otherwise, because it *looks* like the intended entry point.

---

## Enumeration

**Hypothesis I was testing:** if the banner on 8080 was suppressed on purpose,
the version is probably old enough to matter.

**What I found:** the page footer still leaked a release string that the HTTP
headers didn't. Cross-referencing it against the project's changelog put the
install about