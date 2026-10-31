<div align="center">
  <img src="banner.svg" alt="Gowtham M S terminal banner" width="100%" />
</div>

<br/>

<div align="center">

**Java / Spring Boot backend developer · B.Tech CSE, REVA University '27 · CGPA 8.5**

[Case files](#-case-files) · [Stack](#-stack-by-layer) · [Live data](#-live-from-my-github) · [Milestones](#-milestones) · [Contact](#-lets-talk)

<!--START_STATS-->
**6** original repositories · **11** languages · **1,345 KB** of code · refreshed `31 Oct 2026` (UTC)
<!--END_STATS-->

</div>

---

## 👋 About

I build backend systems and I assume someone will try to abuse them. That habit comes from experience: the first version of my capstone was beaten by generic AI-written answers, and fixing it taught me more than any tutorial.

```yaml
name:        Gowtham M S
based_in:    Karnataka, India
studying:    B.Tech Computer Science, REVA University (2023-2027), CGPA 8.5/10
target_role: Java Spring Boot backend / DevOps
core_stack:  Java, Spring Boot, Python, FastAPI, Next.js, Docker, MySQL
how_i_learn: build first, read the docs when it breaks
open_to:     internships and entry-level backend / DevOps roles
```

---

## 🗄️ Case files

Every project below is written as a case: the problem, what I did, what it runs on, and its honest status. **Shipped** means the code is on my GitHub. **Designed** means documented but not built yet.

### 🛡️ Case 001: SkillProof `SHIPPED` `FLAGSHIP`

> **Resumes are claims. SkillProof makes them evidence.**

**Problem.** Anyone can write "Java expert" on a resume. Recruiters have no cheap way to check. And once I added AI evaluation, a second problem appeared: generic AI-written answers scored too high on my own platform.

**What it does.** GitHub OAuth → analyses your actual code → asks questions grounded in *your* repository → runs your code in a sandbox → issues a signed badge anyone can verify.

```mermaid
flowchart LR
    A[Developer] -->|GitHub OAuth| B[Next.js 14]
    B -->|JWT + RBAC| C[Spring Boot 3 API]
    C -->|grounded questions| D[FastAPI AI service]
    D -->|Groq Llama 3.1| E[(Evaluation)]
    C -->|hidden tests| F[Docker sandbox<br/>network-isolated]
    C --> G[(MySQL)]
    C -->|HMAC-SHA256| H[Signed badge]
    H --> I[Public badge page<br/>skill radar chart]
    J[Recruiter] -->|live mode| C
```

**The threat model.**

| Attack | Defense |
|---|---|
| Generic answers that sound right | Questions grounded in the candidate's own repository, plus prompt constraints that harden the evaluator |
| Pasting an answer without writing code | Docker sandbox that runs code against **hidden test cases** |
| Calling out from inside the sandbox | Network isolation |
| Forging a result | **HMAC-SHA256** signed badge tokens, public badge page |

**Features:** GitHub OAuth · JWT + role-based access control · recruiter live mode · public badge page with skill radar chart · Jitsi-based live pair programming.

**Stack:** Java 21 · Spring Boot 3 · Python FastAPI (isolated AI service) · Groq Llama 3.1 · Next.js 14 · MySQL · Docker

<details>
<summary><b>🔍 How signed badges are verified (simplified, illustrative)</b></summary>

```java
// A badge is only valid if its signature matches the payload.
// Compare in constant time so the check itself leaks nothing.
boolean verify(String payload, byte[] signature, SecretKey key) throws Exception {
    Mac mac = Mac.getInstance("HmacSHA256");
    mac.init(key);
    byte[] expected = mac.doFinal(payload.getBytes(StandardCharsets.UTF_8));
    return MessageDigest.isEqual(expected, signature);
}
```

Change one character in the payload and verification fails. That's the whole point.
</details>

[![Repo](https://img.shields.io/badge/Source-Skill__Proof-00f5a0?style=for-the-badge&logo=github&logoColor=black)](https://github.com/Gowtham232004/Skill_Proof)

> 🧨 **Think you can get a generic answer past it?** Open an issue on [Skill_Proof](https://github.com/Gowtham232004/Skill_Proof/issues). Breaking it is the best feedback I can get.

---

### 🔎 Case 002: GitHub Auditor `ON GITHUB`

A Python backend ([`github-auditor`](https://github.com/Gowtham232004/github-auditor)) paired with a TypeScript frontend ([`github-auditor-frontend`](https://github.com/Gowtham232004/github-auditor-frontend)). Details are in each repository.

---

### 📈 Case 003: PipelineIQ `DESIGNED`

**Problem.** CI/CD failures eat developer time, and most tools tell you *that* a build failed, not *what keeps failing and why*.

**Design.** A developer productivity intelligence platform with five pillars: **Pipeline Health Score**, **Failure Pattern Intelligence**, **Commit Risk Scoring**, **Repository Fragility Index** and a **Weekly AI Digest**.

**Why it's here.** It started as an over-scoped idea. I cut it down to a version I could actually build, and the full documentation is written. It isn't implemented yet and I'm saying so.

---

### 🏠 Case 004: RentSahay `DESIGNED`

**Problem.** Rental agreements are long, legal and different in every state, and tenants often sign without understanding them.

**Design.** An AI platform that analyses a rental agreement against **state-specific Indian rent law**, using **RAG** over a ChromaDB knowledge base with Google Gemini. Two versions of formal documentation are written. It isn't implemented yet.

---

### 🏁 Case 005: Hackathon builds `TEAM`

Team projects built under time pressure at the **24-hour AutoML Hackathon (REVA University)** and the **Solaris X Grand Hackathon (RNSIT Luminus 2026)**.

---

## 🧰 Stack by layer

| Layer | What I use |
|---|---|
| **Backend** | Java 21 · Spring Boot 3 · Python · FastAPI |
| **Frontend** | Next.js · React · TypeScript |
| **Data** | MySQL · ChromaDB |
| **Security** | JWT · RBAC · HMAC-SHA256 · Docker sandboxing |
| **DevOps** | Docker · GitHub Actions |
| **AI integration** | Groq (Llama 3.1) · Google Gemini · RAG |

<div align="center">

<img src="https://skillicons.dev/icons?i=java,spring,python,fastapi,nextjs,react,ts,mysql,docker,git,github,githubactions&theme=dark" alt="stack icons" />

</div>

---

## 📡 Live from my GitHub

Everything in this section is generated by a GitHub Action every 6 hours. Forks are excluded, so it's all my own code.

### 🗂️ Every repo I've built

<!--START_PROJECTS-->
| Project | What it is | Stack | Last push |
|---|---|---|---|
| [**Dish_Management_System**](https://github.com/Gowtham232004/Dish_Management_System) | — | HTML | `2026-10-23` |
| [**github_auditor**](https://github.com/Gowtham232004/github_auditor) | — | Python | `2026-10-23` |
| [**github-auditor-frontend**](https://github.com/Gowtham232004/github-auditor-frontend) | — | TypeScript | `2026-10-23` |
| [**github-auditor**](https://github.com/Gowtham232004/github-auditor) | — | Python | `2026-10-23` |
| [**Salesforce_Internship_Tracker**](https://github.com/Gowtham232004/Salesforce_Internship_Tracker) | — | Apex | `2026-06-06` |
| [**Skill_Proof**](https://github.com/Gowtham232004/Skill_Proof) | AI-powered developer credibility platform. GitHub OAuth → code analysis → grounded questions → HMAC badge. | Java | `2026-06-06` |
<!--END_PROJECTS-->

### 🧬 Code DNA

<!--START_DNA-->
```text
TypeScript   ████████░░░░░░░░░░░░ 42.4%
Java         ████████░░░░░░░░░░░░ 37.7%
Python       ███░░░░░░░░░░░░░░░░░ 16.5%
Apex         ░░░░░░░░░░░░░░░░░░░░  2.0%
PowerShell   ░░░░░░░░░░░░░░░░░░░░  0.3%
Shell        ░░░░░░░░░░░░░░░░░░░░  0.3%
```
<!--END_DNA-->

### 🧾 Latest commits

<!--START_COMMITS-->
| Date | Repo | Commit | What changed |
|---|---|---|---|
| `2026-10-23` | Dish_Management_System | [`83a7f56`](https://github.com/Gowtham232004/Dish_Management_System/commit/83a7f562d88964b12031e52b389c6a6d6d5ed6c0) | Merge pull request #1 from Gowtham232004/copilot/create-industry-stand |
| `2026-10-23` | Dish_Management_System | [`13de219`](https://github.com/Gowtham232004/Dish_Management_System/commit/13de219407497c8d4ae87ba0ca5e307576005537) | Add comprehensive project README documentation |
| `2026-10-23` | github_auditor | [`1f82efd`](https://github.com/Gowtham232004/github_auditor/commit/1f82efde4ce97c6fb160b3fc983deda239c4fd98) | Update README.md |
| `2026-10-23` | github-auditor-frontend | [`ec205fb`](https://github.com/Gowtham232004/github-auditor-frontend/commit/ec205fb0b05a51059409a8ceb5378aee979d1811) | Update README.md |
| `2026-10-23` | github-auditor | [`79a9da7`](https://github.com/Gowtham232004/github-auditor/commit/79a9da73a3f59f08e467f6aebc8e5e755e125085) | Update README.md |
| `2026-06-18` | Dish_Management_System | [`89cbec7`](https://github.com/Gowtham232004/Dish_Management_System/commit/89cbec724bf1ee9888ea2572aa20d0d7351f0768) | chore: Initialize Spring Boot dishbackend project structure |
<!--END_COMMITS-->

---

## 🏆 Milestones

| | |
|---|---|
| 🏁 **Hackathons** | Participated in 2: Solaris X Grand Hackathon (RNSIT Luminus 2026) and a 24-hour AutoML Hackathon (REVA University) |
| 🌍 **Open source** | Selected as a **GSSoC 2026** contributor |
| 🦈 **GitHub** | **Pull Shark** achievement, awarded by GitHub for merged pull requests |
| 🎓 **Academics** | B.Tech CSE at REVA University, CGPA **8.5 / 10** |
| 🛠️ **Capstone** | SkillProof: full-stack, multi-service, with a real threat model |

---

## 🧭 How I build

1. **Threat-model first.** Ask who benefits from breaking it, then design for that person.
2. **Isolate what you don't trust.** The AI service runs separately from the core API, and user code runs in a network-isolated sandbox.
3. **Make results verifiable.** A claim without a signature is just text.
4. **Cut scope honestly.** PipelineIQ shrank from a huge idea to five buildable pillars. Marking projects "designed" instead of "shipped" is part of the same habit.

---

## 🤝 Let's talk

I'm looking for **Java / Spring Boot backend and DevOps** internships and entry-level roles. If you want to talk about designing systems that resist abuse, say hi.

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/YOUR-LINKEDIN/)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:YOUR-EMAIL@example.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Gowtham232004)

</div>
