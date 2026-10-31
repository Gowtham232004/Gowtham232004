<div align="center">
  <img src="assets/banner.svg" alt="Gowtham M S terminal banner" width="100%" />
</div>

<br/>

**I'm Gowtham, a Java / Spring Boot backend developer (B.Tech CSE, REVA University '27).**
The most useful thing I've learned so far: *if a system can be gamed, someone will game it.* I learned it by getting beaten by my own platform's users.

---

## 🚨 Incident 001: my platform got beaten by generic AI answers

[**SkillProof**](https://github.com/Gowtham232004/Skill_Proof) is my final-year capstone. It verifies developer skill instead of trusting a resume: GitHub OAuth → code analysis → questions grounded in *your* code → sandboxed execution → a signed badge.

The first version had a hole. Fluent, generic AI-written answers scored too high. I treated that as a security incident, not a bug.

| | |
|---|---|
| **Impact** | Evaluation could be passed without understanding the code |
| **Root cause** | The evaluator rewarded plausible-sounding answers instead of verifiable ones |
| **Fix** | See below |
| **Status** | ✅ Hardened, still testing it |

**What changed**

| Attack | Defense |
|---|---|
| Generic answers that sound right | Questions grounded in the candidate's own repository, plus prompt constraints that harden the evaluator |
| Pasting an answer without writing code | Docker sandbox that runs code against **hidden test cases** |
| Calling out from inside the sandbox | Network isolation |
| Forging a result | **HMAC-SHA256** signed badge tokens, public badge page |

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

**Under the hood:** Spring Boot 3 (Java 21) core API · isolated Python FastAPI service calling Groq Llama 3.1 · Next.js 14 · MySQL · Docker · JWT + RBAC · recruiter live mode · Jitsi pair programming.

> 🧨 **Think you can get a generic answer past it?** Open an issue on [Skill_Proof](https://github.com/Gowtham232004/Skill_Proof/issues). Breaking it is the best feedback I can get.

---

## 📡 Live from the repo

Auto-updated every 6 hours from the latest commits to SkillProof. Nothing here is typed by hand.

<!--START_COMMITS-->
*Waiting for the first workflow run...*
<!--END_COMMITS-->

---

## 🧪 Designed, not shipped

I keep these separate from shipped work on purpose.

- **PipelineIQ**: developer productivity intelligence for CI/CD: pipeline health score, failure pattern intelligence, commit risk scoring, repository fragility index, weekly AI digest.
- **RentSahay**: AI analysis of rental agreements against state-specific Indian rent law, using RAG, ChromaDB and Gemini.

---

## 🤝 Open to

Java / Spring Boot backend and DevOps internships and roles. Also contributing through **GSSoC 2026**.

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/YOUR-LINKEDIN/)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:YOUR-EMAIL@example.com)

</div>
