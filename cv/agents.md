# CV Sync Guide

This document serves as the source of truth for keeping Isaac's professional presence consistent across all platforms.

## Files to keep in sync

| File | Purpose | Format |
|------|---------|--------|
| `cv/isaac-hernandez-cv.md` | Source of truth CV in Markdown | Markdown |
| `cv/isaac-hernandez-cv.html` | Printable CV (open in browser → Cmd+P → PDF) | HTML |
| `index.html` | Website at axiom-of-choice.github.io | HTML |
| GitHub Profile README | github.com/axiom-of-choice | Markdown (via `gh api`) |

## External platforms (manual update required)

| Platform | URL | Notes |
|----------|-----|-------|
| LinkedIn | https://www.linkedin.com/in/isaac-hernandez-garcia-9905/ | No write API — update manually |
| Canva CV | https://canva.link/wqgr898v53m9fnv | Visual version, update manually from .md |

## Sync workflow

When updating CV information:

1. **Edit `cv/isaac-hernandez-cv.md`** — this is the source of truth
2. **Propagate changes to:**
   - `cv/isaac-hernandez-cv.html` — same content, HTML formatted
   - `index.html` — relevant sections (header, experience, skills, certifications)
   - GitHub Profile README — via `gh api repos/axiom-of-choice/axiom-of-choice/contents/README.md`
3. **Manual updates:**
   - LinkedIn (copy relevant sections)
   - Canva CV (redesign if layout changed)

## Key facts to keep consistent

### Current role
- **Staff AI Engineer** @ VerveMarket (June 2025 - Present)

### Company descriptors (verified)
- **VerveMarket** → "AI-powered grocery delivery platform personalized by dietary needs. Founded by Andrés, Anthony, and Jason" — https://shop.vervemarket.com
- **Nubank** → "Largest digital bank in LATAM, 130M+ customers across Brazil, Mexico, and Colombia" — https://nubank.com.br/en/
- **Citigroup** → "Top 3 US bank, global presence in 160+ countries" — https://www.citigroup.com
- **BBVA AI Factory** → "Largest bank in Mexico by customers" — https://www.bbvaaifactory.com
- **Contpaqi** → "Mexico's leading accounting and enterprise software company (contabilidad, facturación electrónica, nómina, inventarios). SAT-compliant" — https://www.contpaqi.com
- **Cargamos** → "Top 10 LinkedIn Startups Mexico"
- **SoftServe** → "Global digital engineering company, 14K+ employees. Elite AWS/NVIDIA/Google Cloud/Microsoft partner. HQ Austin, TX" — https://www.softserveinc.com/en-us
- **Telepatia AI** → "AI startup for healthcare, AI-assisted medical documentation" — https://www.telepatia.ai/es
- **Botco AI** → "US-based GenAI chatbot platform for healthcare & government. RAG framework, HIPAA/SOC2 compliant" — https://botco.ai

### Languages
- English: C1 (TOEFL Certified)
- Spanish: Native
- Portuguese: Currently learning

### Education
- Bachelor of Mathematics, UNAM, 2017-2021, GPA 92/100

### Key skills to always mention
- Python, Scala, SQL, Golang
- PyTorch, TensorFlow (Certified Developer)
- LLMs & Agents: LangGraph, Haystack, CrewAI, LlamaIndex
- LLM Observability: Arize, LangSmith, OpenTelemetry, Guardrails
- RAG, Fine-tuning, vLLM, HuggingFace, OpenAI API
- AWS, GCP, Azure (AZ-900)
- Docker, Kubernetes, Spark, Airflow, Kafka
- Snowflake, PostgreSQL, MongoDB, Pinecone

### Tone & messaging
- "Highly self-driven and self-managed — shaped by startup environments"
- Focus on end-to-end delivery: from data pipelines to production inference
- Emphasize real business impact (e.g., 80% → 97% operational success at Cargamos)
- Mathematics background as differentiator

## How to run a sync session

Tell the agent:
> "Sync my CV. The source of truth is `cv/isaac-hernandez-cv.md`. Propagate any changes to the HTML CV, the website, and the GitHub profile README."

The agent should:
1. Read `cv/isaac-hernandez-cv.md`
2. Diff against each target
3. Update targets to match
4. Push website changes to master
5. Update GitHub README via `gh api`
