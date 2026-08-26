<!-- Applied AI Engineer · Ink #070A12 · Brass #D4AF6A · Signal cyan #38D8F0 -->

<div align="center">
  <img src="hero-dark.png" alt="Mohammed Rashique Shuraim — Applied AI Engineer" width="100%">
</div>

---

<div align="center">
  <img src="mark.png" width="88" alt="Applied AI mark">

  <h2>Mohammed Rashique Shuraim</h2>
  <h3>Applied AI Engineer</h3>
</div>

I build **production AI systems** that have to be right in the real world: a lawyer asking a statute, an investor asking about holdings, an operator speaking a command to their desktop.

The model is never the product. The product is the loop around it — capture the signal, retrieve or transcribe, constrain the generation to sources that exist, return a structured answer, and put it in an interface a stranger can use.

I am studying at **VIT Chennai** (`22MIS1040`) and shipping applied AI for Indian-language and Indian-market problems.

<div align="center">

**GitHub** · [github.com/MohammedShuraim](https://github.com/MohammedShuraim)

**LinkedIn** · [linkedin.com/in/mohammed-rashique-shuraim-4b36b9279](https://www.linkedin.com/in/mohammed-rashique-shuraim-4b36b9279)

**Email** · [mohammed.rashique2022@vitstudent.ac.in](mailto:mohammed.rashique2022@vitstudent.ac.in)

[![GitHub](https://img.shields.io/badge/GitHub-MohammedShuraim-070A12?style=for-the-badge&logo=github&logoColor=38D8F0)](https://github.com/MohammedShuraim)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-070A12?style=for-the-badge&logo=linkedin&logoColor=D4AF6A)](https://www.linkedin.com/in/mohammed-rashique-shuraim-4b36b9279)
[![Gmail](https://img.shields.io/badge/Gmail-mohammed.rashique2022@vitstudent.ac.in-070A12?style=for-the-badge&logo=gmail&logoColor=D4AF6A)](mailto:mohammed.rashique2022@vitstudent.ac.in)

</div>

---

<div align="center">
  <img src="identity-plate.png" alt="Identity plate — GitHub, LinkedIn, Email" width="100%">
</div>

---

## What I ship

These are not notebooks. Each one is a full product: interface, model, retrieval or speech, API, and a cloud path.

<table>
<tr>
<td width="33%" valign="top">

### LexCloud
**Indian-law counsel on AWS**

Upload a statute or contract. Ask from the **PDF (RAG)**. Translate the full document into Hindi, Tamil, Telugu, Malayalam, or Kannada. **Whisper** in. **Amazon Polly** out.

[Repository](https://github.com/MohammedShuraim/LexCloud) · [Live](https://main.d2pw2pic3w5m1.amplifyapp.com) · [Watch](https://www.loom.com/share/ed575fdabd3142d5bef7168b4414385a)

</td>
<td width="33%" valign="top">

### Sentellent AI
**NSE investment desk**

Investor profile → ranked picks → paper trade → watchlist → news. Chat is injected with **holdings and watchlist**, so the analyst cannot forget what you already own.

[Repository](https://github.com/MohammedShuraim/sentinel-ai) · [Live](http://sentellent007.duckdns.org:3000) · [Watch](https://www.loom.com/share/ff398d09217c42568d1778d3608317ee)

</td>
<td width="33%" valign="top">

### Sarah
**Desktop voice agent**

Wake word. Silence-aware recording. 34 spoken OS commands. Conversational fallback on Groq GPT-OSS. One `Assistant` class drives CLI and the React push-to-talk client.

[Repository](https://github.com/MohammedShuraim/sarah-voice-assistant) · [Watch](https://www.loom.com/share/d10d493df9b44a54be501d36abeffb75)

</td>
</tr>
</table>

---

## How I treat a model

<div align="center">
  <img src="pipeline.svg" alt="Grounded generation pipeline" width="100%">
</div>

**If the source did not say it, the model does not get to invent it.**

I design against four failure modes:

| Failure | What it looks like | What I do |
| --- | --- | --- |
| **Hallucination** | A sentence the source never supported | Retrieve first. Bound the prompt. Cite. |
| **Transcription drift** | The wrong word at the start of the pipeline | Whisper in, then route; do not “clean up” facts with an unconstrained LLM |
| **Stale context** | Chat that forgets the PDF, portfolio, or last command | Inject holdings, watchlist, or document into every turn |
| **Latency** | RAG and voice that feel like a batch job | Serverless and Groq where the round-trip has to stay conversational |

---

## Stack from shipped systems

Not a wish list. This is what is actually in LexCloud, Sentellent AI, and Sarah.

### Languages
<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white" alt="SQL">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
</p>

### Applied AI
<p>
  <img src="https://img.shields.io/badge/RAG-38D8F0?style=for-the-badge&logoColor=070A12" alt="RAG">
  <img src="https://img.shields.io/badge/Groq-F55036?style=for-the-badge" alt="Groq">
  <img src="https://img.shields.io/badge/Whisper-STT-5A5A5A?style=for-the-badge" alt="Whisper">
  <img src="https://img.shields.io/badge/GPT--OSS-F55036?style=for-the-badge" alt="GPT-OSS">
  <img src="https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=googlegemini&logoColor=white" alt="Gemini">
  <img src="https://img.shields.io/badge/Amazon%20Polly-4B72B0?style=for-the-badge" alt="Amazon Polly">
  <img src="https://img.shields.io/badge/gTTS-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="gTTS">
  <img src="https://img.shields.io/badge/pgvector-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="pgvector">
</p>

### Product & backend
<p>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white" alt="Next.js">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=111827" alt="React">
  <img src="https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white" alt="Vite">
  <img src="https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="pytest">
  <img src="https://img.shields.io/badge/Google%20OAuth-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Google OAuth">
</p>

### Cloud & data
<p>
  <img src="https://img.shields.io/badge/AWS%20Lambda-FF9900?style=for-the-badge&logo=awslambda&logoColor=white" alt="Lambda">
  <img src="https://img.shields.io/badge/API%20Gateway-FF4F8B?style=for-the-badge&logo=amazonapigateway&logoColor=white" alt="API Gateway">
  <img src="https://img.shields.io/badge/S3-569A31?style=for-the-badge&logo=amazons3&logoColor=white" alt="S3">
  <img src="https://img.shields.io/badge/DynamoDB-4053D6?style=for-the-badge&logo=amazondynamodb&logoColor=white" alt="DynamoDB">
  <img src="https://img.shields.io/badge/Amplify-FF9900?style=for-the-badge&logo=awsamplify&logoColor=white" alt="Amplify">
  <img src="https://img.shields.io/badge/EC2-FF9900?style=for-the-badge&logo=amazonec2&logoColor=white" alt="EC2">
  <img src="https://img.shields.io/badge/RDS-527FFF?style=for-the-badge&logo=amazonrds&logoColor=white" alt="RDS">
  <img src="https://img.shields.io/badge/ECR-FF9900?style=for-the-badge" alt="ECR">
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white" alt="Terraform">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" alt="GitHub Actions">
</p>

---

## Signal

<div align="center">

<img src="https://streak-stats.demolab.com/?user=MohammedShuraim&hide_border=true&background=070A12&stroke=38D8F0&ring=D4AF6A&fire=38D8F0&currStreakLabel=D4AF6A&sideLabels=8B93A7&currStreakNum=E8ECF4&sideNums=E8ECF4&dates=8B93A7" alt="GitHub streak" width="100%">

<img src="https://github-readme-stats.vercel.app/api?username=MohammedShuraim&show_icons=true&include_all_commits=true&hide_rank=true&hide_border=true&title_color=D4AF6A&icon_color=38D8F0&text_color=E8ECF4&bg_color=070A12" alt="GitHub stats">
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=MohammedShuraim&layout=compact&langs_count=8&hide_border=true&title_color=D4AF6A&text_color=E8ECF4&bg_color=070A12" alt="Top languages">

<img src="https://raw.githubusercontent.com/MohammedShuraim/MohammedShuraim/output/github-snake-dark.svg" alt="Contribution snake">

</div>
