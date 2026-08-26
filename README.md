<picture>
  <source media="(prefers-color-scheme: dark)" srcset="dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="light.svg">
  <img alt="Mohammed Rashique Shuraim — Applied AI Engineer" src="dark.svg" width="100%">
</picture>

<div align="center">

**I ship AI as product systems, not notebook demos.**

RAG that cites the document. Voice that routes a command or answers. Agents that know the user’s portfolio before they speak.

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonwebservices&logoColor=FF9900)](https://aws.amazon.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)](https://nextjs.org/)
[![Groq](https://img.shields.io/badge/Groq-Whisper%20%2B%20LLMs-F55036?style=for-the-badge)](https://groq.com/)

[LexCloud](https://github.com/MohammedShuraim/LexCloud) · [Sentellent AI](https://github.com/MohammedShuraim/sentinel-ai) · [Sarah](https://github.com/MohammedShuraim/sarah-voice-assistant) · [Email](mailto:mohammed.rashique2022@vitstudent.ac.in)

</div>

---

## What I actually build

Most GitHub profiles list tools. Mine lists **systems I designed end-to-end**: retrieval, model choice, APIs, UI, cloud, and the product loop a real user walks through.

| System | Domain | What it does | Proof |
| --- | --- | --- | --- |
| **[LexCloud](https://github.com/MohammedShuraim/LexCloud)** | Legal AI · India | Serverless counsel: PDF upload, **grounded RAG**, full-document translation (Hindi / Tamil / Telugu / Malayalam / Kannada), **Whisper in**, **Amazon Polly out**. AWS Amplify + Lambda + Groq. | [Live](https://main.d2pw2pic3w5m1.amplifyapp.com) · [Demo](https://www.loom.com/share/ed575fdabd3142d5bef7168b4414385a) |
| **[Sentellent AI](https://github.com/MohammedShuraim/sentinel-ai)** | Markets · NSE | Investor profiling, ranked recommendations, paper trading, watchlists, news, and a **RAG chat analyst that already knows holdings**. Next.js + FastAPI + PostgreSQL/pgvector on AWS. | [Live](http://sentellent007.duckdns.org:3000) · [Demo](https://www.loom.com/share/ff398d09217c42568d1778d3608317ee) |
| **[Sarah](https://github.com/MohammedShuraim/sarah-voice-assistant)** | Voice agents | Desktop assistant: wake word, silence-aware recording, 34 spoken OS commands, conversational fallback on Groq GPT-OSS, React push-to-talk client. | [Demo](https://www.loom.com/share/d10d493df9b44a54be501d36abeffb75) |

How I think about the work:

- **Grounding first.** If the source did not say it, the model should not invent it. LexCloud retrieves from the uploaded PDF; Sentellent injects portfolio and watchlist into the prompt.
- **One product loop, not five demos.** Upload → retrieve → answer → speak. Profile → rank → trade → ask. Listen → route → reply.
- **Cloud is part of the design.** Amplify, Lambda, API Gateway, S3, DynamoDB, EC2, RDS, ECR, Terraform, GitHub Actions — the system is what runs, not what runs on my laptop.

---

## How I work an AI feature

```text
user signal  →  retrieve / transcribe  →  constrained generation  →  structured response  →  UI
     ↑                                         |                              |
     └──────── memory / holdings / PDF ────────┘                              └── voice / chart / citation
```

I care about the failure modes that show up in production:

1. **Hallucination** — extra facts that were never in the source.
2. **Transcription drift** — the wrong word at the start of the pipeline.
3. **Stale context** — chat that forgets the portfolio, document, or last command.
4. **Latency** — voice and RAG are unusable if the round-trip feels like a batch job.

That is why these repos have real APIs, tests, and deployed frontends — not a single `app.py` with a hardcoded prompt.

---

## Stack I use in shipped work

Badges below are from systems I have actually built. I do not list a tool because it looks impressive.

### Languages
<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
  <img src="https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white" alt="SQL" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3" />
</p>

### Applied AI
<p>
  <img src="https://img.shields.io/badge/RAG-00C7B7?style=for-the-badge" alt="RAG" />
  <img src="https://img.shields.io/badge/Groq-Whisper-F55036?style=for-the-badge" alt="Groq Whisper" />
  <img src="https://img.shields.io/badge/Groq-GPT--OSS-F55036?style=for-the-badge" alt="Groq GPT-OSS" />
  <img src="https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=googlegemini&logoColor=white" alt="Gemini" />
  <img src="https://img.shields.io/badge/pgvector-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="pgvector" />
  <img src="https://img.shields.io/badge/Amazon%20Polly-4B72B0?style=for-the-badge&logo=amazonaws&logoColor=white" alt="Amazon Polly" />
</p>

### Product & backend
<p>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" />
  <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white" alt="Next.js" />
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=111827" alt="React" />
  <img src="https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white" alt="Vite" />
  <img src="https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="pytest" />
</p>

### Cloud & data
<p>
  <img src="https://img.shields.io/badge/AWS-Lambda-FF9900?style=for-the-badge&logo=awslambda&logoColor=white" alt="Lambda" />
  <img src="https://img.shields.io/badge/API%20Gateway-FF4F8B?style=for-the-badge&logo=amazonapigateway&logoColor=white" alt="API Gateway" />
  <img src="https://img.shields.io/badge/S3-569A31?style=for-the-badge&logo=amazons3&logoColor=white" alt="S3" />
  <img src="https://img.shields.io/badge/DynamoDB-4053D6?style=for-the-badge&logo=amazondynamodb&logoColor=white" alt="DynamoDB" />
  <img src="https://img.shields.io/badge/Amplify-FF9900?style=for-the-badge&logo=awsamplify&logoColor=white" alt="Amplify" />
  <img src="https://img.shields.io/badge/EC2%20%2B%20RDS%20%2B%20ECR-FF9900?style=for-the-badge&logo=amazonec2&logoColor=white" alt="EC2 RDS ECR" />
  <img src="https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white" alt="Terraform" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" alt="GitHub Actions" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
</p>

---

## Activity

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=MohammedShuraim&hide_border=true&background=070B12&stroke=38D8F0&ring=C9A227&fire=10B981&currStreakLabel=38D8F0&sideLabels=94A3B8&currStreakNum=F8FAFC&sideNums=F8FAFC&dates=64748B&title_color=38D8F0" />
  <img width="100%" src="https://streak-stats.demolab.com?user=MohammedShuraim&hide_border=true&background=F7F4EE&stroke=0E7490&ring=A16207&fire=059669&currStreakLabel=0E7490&sideLabels=475569&currStreakNum=0F172A&sideNums=0F172A&dates=94A3B8&title_color=0E7490" alt="GitHub streak" />
</picture>

<br/>

<a href="https://github.com/MohammedShuraim">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api?username=MohammedShuraim&show_icons=true&include_all_commits=true&hide_rank=true&hide_border=true&title_color=38D8F0&icon_color=C9A227&text_color=94A3B8&bg_color=070B12" />
    <img height="165" src="https://github-readme-stats.vercel.app/api?username=MohammedShuraim&show_icons=true&include_all_commits=true&hide_rank=true&hide_border=true&title_color=0E7490&icon_color=A16207&text_color=0F172A&bg_color=F7F4EE" alt="GitHub stats" />
  </picture>
</a>
<a href="https://github.com/MohammedShuraim">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=MohammedShuraim&layout=compact&langs_count=8&hide_border=true&title_color=38D8F0&text_color=94A3B8&bg_color=070B12" />
    <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=MohammedShuraim&layout=compact&langs_count=8&hide_border=true&title_color=0E7490&text_color=0F172A&bg_color=F7F4EE" alt="Top languages" />
  </picture>
</a>

</div>

---

## Currently

- Building production **RAG + voice** products for Indian-language and Indian-market problems.
- Studying at **VIT Chennai** (`22MIS1040`).
- Open to applied AI / ML engineering roles where retrieval, evaluation, and deployment matter as much as the model name.

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-MohammedShuraim-070B12?style=for-the-badge&logo=github)](https://github.com/MohammedShuraim)
[![Email](https://img.shields.io/badge/Email-mohammed.rashique2022@vitstudent.ac.in-070B12?style=for-the-badge&logo=gmail&logoColor=EA4335)](mailto:mohammed.rashique2022@vitstudent.ac.in)

</div>
