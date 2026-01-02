# 🔐 Security Policy — SecretScout

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=26&duration=3000&pause=900&color=00FF00&center=true&vCenter=true&width=900&height=70&lines=Defensive+Security+Only;Responsible+Disclosure;Privacy+First+by+Design" alt="SecretScout Security Policy">
</p>

<p align="center">
  <b>Security, privacy, and responsible disclosure</b><br>
  <em>Built for prevention • Designed for trust • Defensive by default</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Security-Policy-purple?style=flat-square" alt="Security Policy">
  <img src="https://img.shields.io/badge/Disclosure-Responsible-green?style=flat-square" alt="Responsible Disclosure">
  <img src="https://img.shields.io/badge/Mode-Offline--First-blue?style=flat-square" alt="Offline First">
</p>

<p align="center">
  <a href="#-supported-versions">Supported Versions</a> •
  <a href="#-reporting-a-vulnerability">Reporting</a> •
  <a href="#-security-design">Security Design</a> •
  <a href="#-disclosure-process">Disclosure Process</a>
</p>

---

## 🛡️ Security Philosophy

> **SecretScout is a defensive security tool.**  
> It is designed to prevent accidental secret exposure — not to enable offensive or malicious activity.

Security and privacy are **core design principles** of this project:
- No network calls
- No telemetry
- No secret exfiltration
- Redaction by default

---

## ✅ Supported Versions

The following versions currently receive security updates:

| Version | Supported |
|--------|-----------|
| 0.2.x  | ✅ Yes     |
| < 0.2  | ❌ No      |

Users are encouraged to stay on the latest release.

---

## 🚨 Reporting a Vulnerability

If you believe you have found a security vulnerability, **please do not open a public issue**.

### Responsible Disclosure

1. Go to **GitHub → Security → Advisories**
2. Click **“New draft security advisory”**
3. Include:
   - Clear description of the issue
   - Steps to reproduce (use **dummy secrets only**)
   - Potential impact
   - Suggested mitigation (if available)

We aim to acknowledge valid reports as soon as possible.

---

## 🔍 What Qualifies as a Security Issue

Examples of valid security issues include:
- Crashes or exceptions caused by crafted input
- Leakage of secret material via logs, output, or reports
- Bypassing redaction or masking mechanisms
- Unexpected file access outside the scan scope
- Logic flaws that allow secrets to be missed or exposed

---

## ❌ What Does NOT Qualify

The following are **not** considered security vulnerabilities:
- False positives or false negatives in detection rules
- Feature requests or usability issues
- Performance concerns
- Misuse of the tool
- Reports containing **real secrets or credentials**

---

## 🔐 Handling of Secrets

SecretScout is **privacy-first** by design:

- 🔒 **Offline-only** — no outbound connections
- 🧠 **In-memory processing** — secrets are not persisted
- ✂️ **Redaction** — secrets are never printed in full
- 🧾 **Cache safety** — cache stores fingerprints only, never raw secrets

At no point does SecretScout transmit scanned content.

---

## 🔄 Disclosure Process

Once a vulnerability report is received and validated:

1. Impact and severity are assessed
2. A fix is prepared (if required)
3. A patched release is published
4. The reporter may be credited (optional)

Disclosure timelines depend on severity and complexity.

---

## ⚠️ Responsible Use

SecretScout is intended **exclusively for defensive security**.

Any attempts to:
- promote offensive usage,
- collect or exfiltrate secrets,
- or bypass user consent

may result in refusal to support or removal of access.

---

## 📄 Policy Updates

This Security Policy may be updated as the project evolves.
Changes will be documented in release notes when applicable.

---

<p align="center">
  <b>Thank you for helping keep SecretScout secure 🛡️</b><br>
  <sub>Defensive security starts with responsible disclosure.</sub>
</p>
