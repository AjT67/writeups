---
title: "Appointment"
platform: "HTB"            # HTB | TryHackMe | VulnHub | Proving Grounds | Own lab
target: "Appointment"
os: "Linux"                # Linux | Windows | Other
difficulty: "Easy"         # Easy | Medium | Hard | Insane
date: 2026-01-09           # date you finished it, YYYY-MM-DD
tags: [sql-injection, sqli, authentication-bypass, owasp-top-10, a03-injection]
techniques: [web-enumeration, login-bypass, comment-injection]             # optional: MITRE ATT&CK IDs, e.g. [T1190, T1078]
status: published              # draft | published
---

## Attack path

Nmap scan revealed port 80 open. SQL injection. Entered admin' # as the username with password blank.

---

## Recon

Nmap scan with port 80 opened, checked website.

---

## Enumeration

Identified a login form as the sole entry point on the web app, tested for SQL injection, confiming the # comment character could be used to bypass the password check.

---

## Foothold

Successfully authenticated as admin via SQL comment injection, without ever knowing the real password.

---

## Privilege escalation

SQL comment injeciton.

---

## Lessons

Basic SQL injection on web app bypassing password.


