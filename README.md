<div align="center">
  <img src="banner.svg" alt="Gowtham M S, 7th-semester Computer Science student at REVA University. Animated terminal running real commands against his project repositories." width="100%" />

[![GitHub](https://img.shields.io/badge/GITHUB-Gowtham232004-19d3c5?style=for-the-badge&labelColor=0b1a24&logo=github&logoColor=white)](https://github.com/Gowtham232004)
[![SkillProof](https://img.shields.io/badge/FLAGSHIP-SkillProof-19d3c5?style=for-the-badge&labelColor=0b1a24)](https://github.com/Gowtham232004/Skill_Proof)
[![GitHub Auditor](https://img.shields.io/badge/PROJECT-GitHub_Auditor-19d3c5?style=for-the-badge&labelColor=0b1a24)](https://github.com/Gowtham232004/github-auditor)

<!--START_STATS-->
**5** original repositories · **11** languages · **1,280 KB** of code · refreshed `14 Nov 2026` (UTC)
<!--END_STATS-->

</div>

## 👨‍💻 About

7th-semester B.Tech CSE student at **REVA University** (CGPA 8.5). I built **SkillProof** (Spring Boot, FastAPI, Next.js, Docker) and **GitHub Auditor** (FastAPI, Next.js), and I care about how backend systems get abused and how to make that harder.

**Right now:** exploring Kubernetes, TypeScript and RAG. Looking for backend and DevOps internships.

---

## ⚡ Proof in 60 seconds

Each row is a claim and the exact place in the code where you can check it.

| I claim | Check it yourself |
|---|---|
| Untrusted code runs with **no network, a read-only filesystem, 1 CPU, a 128-process cap** | [`DockerExecutionService.java`](https://github.com/Gowtham232004/Skill_Proof/blob/main/backend-core/src/main/java/com/skillproof/backend_core/service/DockerExecutionService.java#L165-L190) |
| Badges are **HMAC-SHA256** tokens over `userId : repo : score : timestamp`, so editing any field invalidates them | [`HmacUtil.java`](https://github.com/Gowtham232004/Skill_Proof/blob/main/backend-core/src/main/java/com/skillproof/backend_core/util/HmacUtil.java#L14-L40) |
| Auth is **GitHub OAuth + JWT** with role enforcement | [`JwtAuthFilter.java`](https://github.com/Gowtham232004/Skill_Proof/blob/main/backend-core/src/main/java/com/skillproof/backend_core/config/JwtAuthFilter.java) · [`SecurityConfig.java`](https://github.com/Gowtham232004/Skill_Proof/blob/main/backend-core/src/main/java/com/skillproof/backend_core/config/SecurityConfig.java) |
| Candidate answers carry **integrity telemetry**: tab switches, paste count, answer timing, stored with the badge | [`SubmitAnswersRequest.java`](https://github.com/Gowtham232004/Skill_Proof/blob/main/backend-core/src/main/java/com/skillproof/backend_core/dto/request/SubmitAnswersRequest.java) · [`Badge.java`](https://github.com/Gowtham232004/Skill_Proof/blob/main/backend-core/src/main/java/com/skillproof/backend_core/model/Badge.java) |
| I **test** the trust logic: badges, verification, live sessions, confidence tiers, recruiter endpoints | [`src/test`](https://github.com/Gowtham232004/Skill_Proof/tree/main/backend-core/src/test/java/com/skillproof/backend_core) (8 test classes) |
| I found hard-coded secrets in my own config on day 3 and removed them | [commit `8be4efa`](https://github.com/Gowtham232004/Skill_Proof/commit/8be4efa) |
| A second system detects **7 kinds of suspicious commit patterns** | [`git_analyzer.py`](https://github.com/Gowtham232004/github-auditor/blob/main/git_analyzer.py#L195-L277) |
| Public endpoints are **rate limited per IP** | [`rate_limiter.py`](https://github.com/Gowtham232004/github-auditor/blob/main/rate_limiter.py) |

---

## 🗄️ Case files

Each case lists the problem, what I built, my role and an honest status.

### 🛡️ Case 001 · SkillProof `WORKING` `FLAGSHIP`

<div align="center">
  <img src=".github/skillproof.svg" alt="Terminal session for SkillProof" width="100%" />
</div>

> **Resumes are claims. SkillProof makes them evidence.**

| | |
|---|---|
| **Problem** | Resumes and portfolios are easy to inflate, and once AI evaluates answers, generic AI-written answers can look convincing. In my first version they scored too high. |
| **What it does** | GitHub OAuth → repo ingestion → questions grounded in *your* code → AI evaluation with a rubric and guardrails → confidence tier → signed badge. Recruiters get a dashboard with evidence, decisions (`VERIFIED`, `NEEDS_LIVE_INTERVIEW`, `REJECT`), candidate compare, live validation sessions and Jitsi video rooms. Coding challenges run against hidden tests in a Docker sandbox. |
| **Size** | About 13,000 lines of Java across 101 files, 2,000 lines of Python, 9,000 lines of TypeScript, 43 REST endpoints (by mapping annotation count), 92 commits |
| **My role** | Team of 3. I wrote the large majority of `backend-core`, `backend-ai` and the frontend (`git shortlog` shows it). Teammates handled documentation, weekly reports and parts of the frontend. |
| **Stack** | Java 21 · Spring Boot 3 · FastAPI (Python 3.11) · Groq Llama 3.1 · Next.js 14 · TypeScript · MySQL 8 · Docker |
| **Timeline** | 19 Mar 2026 → 25 Apr 2026 |
| **Status** | Runs locally across three services. No public deployment linked, no CI yet. See [what's next](#-whats-next). |

```mermaid
flowchart LR
    A[Candidate] -->|GitHub OAuth| B[Next.js 14]
    B -->|JWT| C[Spring Boot 3<br/>auth, orchestration, RBAC]
    C -->|repo-aware questions,<br/>evaluation| D[FastAPI AI service<br/>Groq Llama 3.1]
    C -->|hidden tests| E[Docker sandbox<br/>no network, read-only]
    C --> F[(MySQL 8)]
    C -->|HMAC-SHA256| G[Signed badge<br/>public badge page]
    H[Recruiter] -->|dashboard, live sessions| C
```

**The real badge token logic**, straight from [`HmacUtil.java`](https://github.com/Gowtham232004/Skill_Proof/blob/main/backend-core/src/main/java/com/skillproof/backend_core/util/HmacUtil.java):

```java
// Token = HMAC-SHA256(secret, userId + repoName + score + timestamp)
// Any tampering with badge data invalidates this token.
String data = userId + ":" + repoName + ":" + score + ":" + timestamp;
return "sp_" + hmacSha256(data);
```

**Attack → defense map**

| Attack | Defense | Where |
|---|---|---|
| Generic AI-written answers | Questions generated from the candidate's own repo, mixed code-grounded and conceptual, weighted scoring, rubric guardrails | `backend-ai`, `VerificationService` |
| Pasting or outsourcing answers | Integrity telemetry (tab switches, paste count, answer timing) sent with every submission and stored on the badge for recruiter review | `SubmitAnswersRequest`, `Badge` |
| Hostile or cheating code | Hidden tests in a container with `--network none --read-only --pids-limit 128` and a memory cap | `DockerExecutionService` |
| Forged or edited badge | HMAC-SHA256 signed token verified server-side | `HmacUtil`, `BadgeService` |

[![Repo](https://img.shields.io/badge/Source-Skill__Proof-19d3c5?style=for-the-badge&labelColor=0b1a24&logo=github&logoColor=white)](https://github.com/Gowtham232004/Skill_Proof)

> 🧨 **Think you can get a generic answer past it?** Open an issue on [Skill_Proof](https://github.com/Gowtham232004/Skill_Proof/issues).

---

### 🔎 Case 002 · GitHub Auditor `WORKING`

<div align="center">
  <img src=".github/auditor.svg" alt="Terminal session for GitHub Auditor" width="100%" />
</div>

| | |
|---|---|
| **Problem** | A GitHub profile can look impressive without the work behind it. Commit history shows patterns that a green contribution graph hides. |
| **What it does** | Clones a user's repositories, analyses commit behaviour and scores authenticity from 0 to 100. Seven red-flag detectors: `bulk_upload`, `burst_activity`, `dominated_repo`, `generic_messages`, `low_activity`, `no_collaboration`, `suspicious_timing`. AI-written insights with a rule-based fallback if the AI call fails. Emailed reports. |
| **Backend** | FastAPI · about 2,800 lines of Python · 14 distinct API routes · SQLite history · per-IP rate limiting · health monitor · structured logging · Docker |
| **Frontend** | [`github-auditor-frontend`](https://github.com/Gowtham232004/github-auditor-frontend): Next.js 16 · React 19 · Tailwind 4 · Recharts · Framer Motion. Pages: analyze, results, compare, history, shareable badge. |
| **My role** | Built both repos (21 of 23 backend commits and 17 of 17 frontend commits are mine). |
| **Real-world lesson** | SMTP email wasn't compatible with my host (Render). Over one day of commits I moved from Gmail SMTP to Resend, hit domain-verification errors, and ended on SendGrid. |
| **Status** | Working. Frontend [deployed on Vercel](https://github-auditor-frontend.vercel.app); backend ships with Docker and Railway configuration. |

[![Backend](https://img.shields.io/badge/Backend-github--auditor-19d3c5?style=for-the-badge&labelColor=0b1a24&logo=github&logoColor=white)](https://github.com/Gowtham232004/github-auditor) [![Frontend](https://img.shields.io/badge/Frontend-github--auditor--frontend-19d3c5?style=for-the-badge&labelColor=0b1a24&logo=github&logoColor=white)](https://github.com/Gowtham232004/github-auditor-frontend)

---

### 🧪 Case 003 · Smaller builds

<div align="center">
  <img src=".github/tracker.svg" alt="Terminal session for the Salesforce Internship Tracker" width="100%" />
</div>

<div align="center">
  <img src=".github/dish.svg" alt="Terminal session for the Dish Management System" width="100%" />
</div>

| Build | What's actually there | Status |
|---|---|---|
| [**Salesforce Internship Tracker**](https://github.com/Gowtham232004/Salesforce_Internship_Tracker) | Tracks companies, internship positions, applications and interview rounds. 4 custom objects, 3 Apex triggers, 5 Apex classes (including an offer-expiration batch job), 3 validation rules. | Built and documented |
| [**Dish Management System**](https://github.com/Gowtham232004/Dish_Management_System) | Starter layout: Spring Boot 3.2 backend with Security, JPA and JWT dependencies, React 19 client, Express prototype. | Scaffold only. No business logic yet. |

---

### 📐 Case 004 · Designed, not built

<div align="center">
  <img src=".github/designed.svg" alt="Terminal session for the designed projects" width="100%" />
</div>

| Design | Idea | Status |
|---|---|---|
| **PipelineIQ** | Developer productivity intelligence for CI/CD: pipeline health score, failure pattern intelligence, commit risk scoring, repository fragility index, weekly AI digest. | Fully documented, not implemented |
| **RentSahay** | AI analysis of rental agreements against state-specific Indian rent law, using RAG with ChromaDB and Google Gemini. | Documented, not implemented |

---

## 🧭 Build log

Dates come from first commits in git history.

```mermaid
timeline
    title What I shipped, in order
    2025-10 : GitHub Auditor backend : Authenticity score from commit patterns
    2025-11 : Auditor dashboard : Compare, history, badges, email reports
    2026-03 : SkillProof : Repo-grounded assessment, sandbox, signed badges
    2026-06 : Salesforce Internship Tracker : Dish Management starter
```

Both flagship projects ask the same question from two angles: **does this developer's profile match what they can actually do?** The Auditor reads the history. SkillProof tests the understanding.

---

## 🧰 Stack with receipts

| Technology | Where I used it | Proof |
|---|---|---|
| Java 21 · Spring Boot 3 | SkillProof core service: auth, orchestration, recruiter APIs, challenge execution | [`backend-core`](https://github.com/Gowtham232004/Skill_Proof/tree/main/backend-core) |
| Spring Security · JWT | Role-based access in SkillProof, JWT dependencies in the Dish starter | [`config/`](https://github.com/Gowtham232004/Skill_Proof/tree/main/backend-core/src/main/java/com/skillproof/backend_core/config) |
| Python · FastAPI | SkillProof AI service, GitHub Auditor API | [`backend-ai`](https://github.com/Gowtham232004/Skill_Proof/tree/main/backend-ai) · [`main.py`](https://github.com/Gowtham232004/github-auditor/blob/main/main.py) |
| Next.js · TypeScript · React | SkillProof UI (Next 14), Auditor dashboard (Next 16, React 19) | [`frontend`](https://github.com/Gowtham232004/Skill_Proof/tree/main/frontend) · [`src/app`](https://github.com/Gowtham232004/github-auditor-frontend/tree/main/src/app) |
| MySQL 8 | SkillProof persistence | [`setup-db.sql`](https://github.com/Gowtham232004/Skill_Proof/blob/main/setup-db.sql) |
| SQLite | Auditor analysis history | [`database.py`](https://github.com/Gowtham232004/github-auditor/blob/main/database.py) |
| Docker | SkillProof code sandbox, Auditor container config | [`DockerExecutionService`](https://github.com/Gowtham232004/Skill_Proof/blob/main/backend-core/src/main/java/com/skillproof/backend_core/service/DockerExecutionService.java) · [`Dockerfile`](https://github.com/Gowtham232004/github-auditor/blob/main/Dockerfile) |
| Groq (Llama 3.1) | SkillProof question generation and evaluation | [`backend-ai/app/main.py`](https://github.com/Gowtham232004/Skill_Proof/blob/main/backend-ai/app/main.py) |
| OpenAI API | Auditor AI insights, with a rule-based fallback | [`ai_insights.py`](https://github.com/Gowtham232004/github-auditor/blob/main/ai_insights.py) |
| Recharts · Framer Motion · Tailwind 4 | Auditor dashboard charts, animation, styling | [`package.json`](https://github.com/Gowtham232004/github-auditor-frontend/blob/main/package.json) |
| Salesforce Apex | Triggers, handlers and a batch job in the Internship Tracker | [repo](https://github.com/Gowtham232004/Salesforce_Internship_Tracker) |

---

## 📡 Live from my GitHub

Everything in this section is regenerated by a GitHub Action every 6 hours. Forks, duplicates and other people's projects are excluded.

### 🗂️ Every repo I built

<!--START_PROJECTS-->
| Project | What it is | Stack | Last push |
|---|---|---|---|
| [**Dish_Management_System**](https://github.com/Gowtham232004/Dish_Management_System) | Starter layout for a dish and menu platform: Spring Boot 3.2 backend (Security, JPA, JWT dependencies) and a React 19 client. Business logic not built yet. | HTML | `2026-10-23` |
| [**github-auditor-frontend**](https://github.com/Gowtham232004/github-auditor-frontend) | Next.js 16 dashboard for GitHub Auditor: results, profile compare, history and shareable badge pages. | TypeScript | `2026-10-23` |
| [**github-auditor**](https://github.com/Gowtham232004/github-auditor) | FastAPI service that scores how authentic a GitHub profile looks from its commit history, with 7 red-flag detectors and AI insights. | Python | `2026-10-23` |
| [**Salesforce_Internship_Tracker**](https://github.com/Gowtham232004/Salesforce_Internship_Tracker) | Salesforce internship tracker: 4 custom objects, 3 Apex triggers, 5 Apex classes and 3 validation rules. | Apex | `2026-06-06` |
| [**Skill_Proof**](https://github.com/Gowtham232004/Skill_Proof) | Developer credibility platform: repo-grounded assessment, Docker-sandboxed challenges, HMAC-signed badges. Team of 3. | Java | `2026-06-06` |
<!--END_PROJECTS-->

### 🧬 Code DNA

<!--START_DNA-->
```text
TypeScript   █████████░░░░░░░░░░░ 44.6%
Java         ████████░░░░░░░░░░░░ 39.6%
Python       ██░░░░░░░░░░░░░░░░░░ 12.3%
Apex         ░░░░░░░░░░░░░░░░░░░░  2.1%
PowerShell   ░░░░░░░░░░░░░░░░░░░░  0.4%
Shell        ░░░░░░░░░░░░░░░░░░░░  0.3%
```
<!--END_DNA-->

### 🧾 My latest commits

<!--START_COMMITS-->
| Date | Repo | Commit | What changed |
|---|---|---|---|
| `2026-10-23` | github-auditor-frontend | [`ec205fb`](https://github.com/Gowtham232004/github-auditor-frontend/commit/ec205fb0b05a51059409a8ceb5378aee979d1811) | Update README.md |
| `2026-10-23` | github-auditor | [`79a9da7`](https://github.com/Gowtham232004/github-auditor/commit/79a9da73a3f59f08e467f6aebc8e5e755e125085) | Update README.md |
| `2026-06-18` | Dish_Management_System | [`89cbec7`](https://github.com/Gowtham232004/Dish_Management_System/commit/89cbec724bf1ee9888ea2572aa20d0d7351f0768) | chore: Initialize Spring Boot dishbackend project structure |
| `2026-06-17` | Dish_Management_System | [`366d57f`](https://github.com/Gowtham232004/Dish_Management_System/commit/366d57f4187e3ca08260fe1dec93bc0cf7ffac4a) | feat: add Express server for AI code explanation |
| `2026-06-15` | Dish_Management_System | [`f10dc76`](https://github.com/Gowtham232004/Dish_Management_System/commit/f10dc761df1903ca3e7eaa6bafeb2d7cd3f33e41) | Initialize React frontend base setup |
| `2026-06-06` | Salesforce_Internship_Tracker | [`2a6a785`](https://github.com/Gowtham232004/Salesforce_Internship_Tracker/commit/2a6a785a95d3424669ea9fe762e491e3d343e5af) | Update README.md |
<!--END_COMMITS-->

---

## 🔭 What's next

I'd rather list my gaps than have you find them.

| Gap | Why it matters | Status |
|---|---|---|
| CI for SkillProof | No automated build or test run on push yet | Next |
| Containerise all three SkillProof services | `docker-compose.yml` runs MySQL only today | Next |
| Tests for the Docker execution service | The 8 test classes cover badges, verification, live sessions, tiers and recruiter endpoints, not the sandbox runner | Next |
| Deploy SkillProof | It runs locally only | Planned |
| Build out the Dish Management domain layer | Currently a scaffold | Planned |

---

## 🏆 Milestones

| | |
|---|---|
| 🏁 **Hackathons** | RNSIT Grand Hackathon: built a developer-focused security and tooling project in a 24-hour team challenge. REVA 24-hour AutoML Hackathon: built an automated machine-learning pipeline prototype. |
| 🌍 **Open source** | Selected as a GSSoC 2026 contributor |
| 🦈 **GitHub** | Pull Shark achievement, awarded by GitHub for merged pull requests |
| 🎓 **Academics** | B.Tech Computer Science, REVA University (2023-2027), CGPA 8.5 / 10 |
| 🎯 **Looking for** | Java / Spring Boot backend and DevOps internships and entry-level roles |

---

## 🤝 Let's talk

If you read one thing, read [`DockerExecutionService.java`](https://github.com/Gowtham232004/Skill_Proof/blob/main/backend-core/src/main/java/com/skillproof/backend_core/service/DockerExecutionService.java#L165-L190) and implementation right here. Let's see what you've built.

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-Gowtham232004-181717?style=for-the-badge&logo=github)](https://github.com/Gowtham232004)
[![Issues](https://img.shields.io/badge/Break_SkillProof-open_an_issue-19d3c5?style=for-the-badge&labelColor=0b1a24&logo=github)](https://github.com/Gowtham232004/Skill_Proof/issues)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-gowthamm--s-19d3c5?style=for-the-badge&labelColor=0b1a24&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gowtham-m-s-82b758294/)
[![Email](https://img.shields.io/badge/Email-gowthamms034@gmail.com-19d3c5?style=for-the-badge&labelColor=0b1a24&logo=gmail&logoColor=white)](mailto:gowthamms034@gmail.com)

</div>
