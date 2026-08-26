<!-- Theme: Ink #070A12 · Brass #D4AF6A · Signal cyan #38D8F0 · Neural violet #7C6CFF -->

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="hero-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="hero-light.png">
  <img src="hero-dark.png" alt="Mohammed Rashique Shuraim — Applied AI Engineer" width="100%">
</picture>
</div>

---

<div align="center">
<img src="mark.png" width="96" alt="Applied AI mark">

<p><b>Mohammed Rashique Shuraim</b></p>
<p>Applied AI Engineer</p>

I design <b>production AI systems</b> — retrieval that cites the document, voice that routes a command or answers, agents that already know the user’s context.

**Theme** · Ink (`#070A12`) · Brass (`#D4AF6A`) · Signal cyan (`#38D8F0`) · Neural violet (`#7C6CFF`)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-070A12?style=for-the-badge&logo=linkedin&logoColor=D4AF6A)](https://www.linkedin.com/in/mohammed-rashique-shuraim-4b36b9279)
[![GitHub](https://img.shields.io/badge/GitHub-MohammedShuraim-070A12?style=for-the-badge&logo=github&logoColor=38D8F0)](https://github.com/MohammedShuraim)
[![Email](https://img.shields.io/badge/Email-vitstudent-070A12?style=for-the-badge&logo=gmail&logoColor=D4AF6A)](mailto:mohammed.rashique2022@vitstudent.ac.in)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonwebservices&logoColor=FF9900)](https://aws.amazon.com/)

[LexCloud](https://github.com/MohammedShuraim/LexCloud) · [Sentellent AI](https://github.com/MohammedShuraim/sentinel-ai) · [Sarah](https://github.com/MohammedShuraim/sarah-voice-assistant)

</div>

---

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="light.svg">
  <img src="dark.svg" alt="Particle identity plate" width="100%">
</picture>

</div>

---

## What I ship

These are not notebooks. Each one is a product loop: interface, model, retrieval or speech, API, and a cloud path a stranger can open.

<table>
<tr>
<td width="33%" valign="top">

### LexCloud
**Indian-law counsel on AWS**

Upload a statute or contract. Ask from the **PDF (RAG)**. Translate the full document into Hindi, Tamil, Telugu, Malayalam, or Kannada. **Whisper** in. **Amazon Polly** out.

Amplify · Lambda · API Gateway · S3 · DynamoDB · Groq

[Repository](https://github.com/MohammedShuraim/LexCloud) · [Live](https://main.d2pw2pic3w5m1.amplifyapp.com) · [Watch](https://www.loom.com/share/ed575fdabd3142d5bef7168b4414385a)

</td>
<td width="33%" valign="top">

### Sentellent AI
**NSE investment desk**

Investor profile → ranked picks → paper trade → watchlist → news. The analyst chat is injected with **holdings and watchlist**, so it cannot forget what you already own.

Next.js · FastAPI · PostgreSQL / pgvector · Docker · Terraform · Gemini

[Repository](https://github.com/MohammedShuraim/sentinel-ai) · [Live](http://sentellent007.duckdns.org:3000) · [Watch](https://www.loom.com/share/ff398d09217c42568d1778d3608317ee)

</td>
<td width="33%" valign="top">

### Sarah
**Desktop voice agent**

Wake word. Silence-aware recording. 34 spoken OS commands. Conversational fallback on Groq GPT-OSS. The same `Assistant` class drives CLI and the React push-to-talk client.

Python · Flask · React 19 · Vite · Whisper · gTTS

[Repository](https://github.com/MohammedShuraim/sarah-voice-assistant) · [Watch](https://www.loom.com/share/d10d493df9b44a54be501d36abeffb75)

</td>
</tr>
</table>

---

## How I treat a model

```text
signal → retrieve or transcribe → constrained generation → structured reply → interface
              ↑                         |
              └── PDF / holdings / last command
```

Four failure modes I design against:

1. **Hallucination** — a sentence the source never supported.
2. **Transcription drift** — the wrong word at the start of the pipeline.
3. **Stale context** — chat that forgets the document, portfolio, or last command.
4. **Latency** — RAG and voice die if the round-trip feels like a batch job.

If the source did not say it, the model does not get to invent it.

---

## Stack from shipped systems

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white" alt="Next.js">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=111827" alt="React">
  <img src="https://img.shields.io/badge/RAG-38D8F0?style=for-the-badge&logoColor=070A12" alt="RAG">
  <img src="https://img.shields.io/badge/Groq-Whisper%20%2B%20LLMs-F55036?style=for-the-badge" alt="Groq">
  <img src="https://img.shields.io/badge/Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white" alt="Gemini">
  <img src="https://img.shields.io/badge/pgvector-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="pgvector">
  <img src="https://img.shields.io/badge/AWS-Lambda%20·%20S3%20·%20DynamoDB%20·%20Amplify-FF9900?style=for-the-badge&logo=amazonwebservices&logoColor=white" alt="AWS">
  <img src="https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white" alt="Terraform">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
</p>

---

## Signal

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=MohammedShuraim&hide_border=true&background=070A12&stroke=38D8F0&ring=D4AF6A&fire=38D8F0&currStreakLabel=D4AF6A&sideLabels=8B93A7&currStreakNum=E8ECF4&sideNums=E8ECF4&dates=8B93A7&title_color=38D8F0" />
  <img width="100%" src="https://streak-stats.demolab.com?user=MohammedShuraim&hide_border=true&background=F4F0E8&stroke=0E7490&ring=A16207&fire=0E7490&currStreakLabel=A16207&sideLabels=5C564C&currStreakNum=14110C&sideNums=14110C&dates=5C564C&title_color=0E7490" alt="GitHub streak">
</picture>

<a href="https://github.com/MohammedShuraim">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api?username=MohammedShuraim&show_icons=true&include_all_commits=true&hide_rank=true&hide_border=true&title_color=D4AF6A&icon_color=38D8F0&text_color=8B93A7&bg_color=070A12" />
    <img height="158" src="https://github-readme-stats.vercel.app/api?username=MohammedShuraim&show_icons=true&include_all_commits=true&hide_rank=true&hide_border=true&title_color=A16207&icon_color=0E7490&text_color=14110C&bg_color=F4F0E8" alt="GitHub stats">
  </picture>
</a>
<a href="https://github.com/MohammedShuraim">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=MohammedShuraim&layout=compact&langs_count=6&hide_border=true&title_color=D4AF6A&text_color=8B93A7&bg_color=070A12" />
    <img height="158" src="https://github-readme-stats.vercel.app/api/top-langs/?username=MohammedShuraim&layout=compact&langs_count=6&hide_border=true&title_color=A16207&text_color=14110C&bg_color=F4F0E8" alt="Top languages">
  </picture>
</a>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MohammedShuraim/MohammedShuraim/output/github-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/MohammedShuraim/MohammedShuraim/output/github-snake.svg" />
  <img alt="Contribution snake" src="https://raw.githubusercontent.com/MohammedShuraim/MohammedShuraim/output/github-snake.svg">
</picture>

</div>

---

<div align="center">

Studying at **VIT Chennai** (`22MIS1040`). Building applied AI for Indian-language and Indian-market problems.

[LinkedIn](https://www.linkedin.com/in/mohammed-rashique-shuraim-4b36b9279) · [Email](mailto:mohammed.rashique2022@vitstudent.ac.in) · [GitHub](https://github.com/MohammedShuraim)

</div>
