# Isaac Hernandez

**Staff AI Engineer**

isadohergar@gmail.com | [LinkedIn](https://www.linkedin.com/in/isaac-hernandez-garcia-9905/) | [GitHub](https://github.com/axiom-of-choice) | [Website](https://axiom-of-choice.github.io)

---

## Summary

Staff AI Engineer who owns AI initiatives end-to-end — scoping the problem, designing the architecture, shipping to production, and measuring impact. I operate as a technical leader and force multiplier: making architectural bets, setting engineering standards, unblocking teams, and driving projects from zero-to-one.

Led cross-functional delivery across healthcare, fintech, and e-commerce — working directly with CTOs and stakeholders to define what to build, not just how to build it. Track record of taking full ownership of AI/Data strategy at early-stage startups and delivering production systems at top LATAM fintechs serving tens of millions of users. Have worked extensively with international, distributed teams across the US and LATAM.

Mathematics degree with strong fundamentals in ML theory, distributed systems, and software engineering. Shaped by years in early-stage startups and other high-autonomy environments where ownership, speed, and sound technical judgment define success.

---

## Work Experience

### Staff AI Engineer | VerveMarket
**June 2025 - Present**

AI-powered grocery delivery platform personalized by dietary needs. [shop.vervemarket.com](https://shop.vervemarket.com) — Own all AI/Data strategy and execution, reporting directly to CTO.

- Defined and delivered the product search experience end-to-end — hybrid semantic + keyword engine combining vector similarity (embeddings + reranking) with lexical retrieval, which became the core discovery mechanism, driving a 27% improvement in add-to-cart conversion; serves ~100K multi-retailer (multi-tenant) requests/day at ~1s p95
- Scoped, designed, and shipped product classification pipeline (LLM fine-tuning for NER), fully automating a previously manual cataloging process across 500K+ products — eliminating 100% of manual cataloging
- Established the company's AI/Data infrastructure from scratch: pipelines, model serving, inference APIs, vector store, and MCP servers exposing internal tools to agents — setting architectural standards for all future AI work
- Scaled LLM inference serving for production (vLLM, TGI), handling real-time and batch inference across text and multimodal models including image generation pipelines
- Built comprehensive evaluation infrastructure for LLM services — deterministic metrics (exact match, F1, BLEU, ROUGE), statistical significance testing, and LLM-as-judge pipelines — deployed across both batch evaluation and real-time serving, cutting the manual QA cycle from days to minutes
- Set the AI/Data technical direction company-wide: owned the model/architecture roadmap, defined build-vs-buy and infra standards adopted by every AI project, and made the calls that other engineers built against

### Lead AI Engineer (Contract) | Contpaqi
**September 2025 - February 2026**

Mexico's leading accounting and enterprise software company. [contpaqi.com](https://www.contpaqi.com) — Led the AI product initiative from concept to production, defining technical direction and driving delivery.

- Owned end-to-end architecture and delivery of multi-tool agents automating invoice generation, tax status certificates, and compliance workflows — cutting task turnaround from ~2 hours to under 10 minutes (~90% reduction)
- Designed and deployed MCP servers exposing the existing enterprise APIs as agent tools, and built the agent host consuming them as MCP clients — decoupling tool integrations from agent logic
- Ran self-hosted LLM inference (Ollama) for workloads requiring on-premise processing of sensitive financial data
- Made build-vs-buy decisions for LLM integrations and designed the service layer connecting agents to existing enterprise APIs

### Lead R&D Engineer in Agentic AI (Contract) | SoftServe
**July 2025 - November 2025**

[softserveinc.com](https://www.softserveinc.com/en-us) — Drove an agentic AI platform for healthcare from zero to production MVP.

- Owned technical architecture and delivery: multi-agent orchestration integrating OCR, STT, and LLM services for clinical document processing — reaching ~92% field extraction accuracy and cutting manual data entry by ~70%
- Defined integration patterns and standards for connecting agents to external healthcare APIs — built MCP servers for the tool layer and the multi-agent host acting as MCP client
- Deployed self-hosted LLM inference (Ollama) to keep protected health information within the client's infrastructure boundary
- Delivered production MVP in under 4 months, establishing the reference architecture for future agent projects

### Senior AI Engineer | Telepatia AI
**June 2025 - July 2025**

[telepatia.ai](https://www.telepatia.ai/es) — Owned end-to-end delivery of a hallucination and missing information detector for AI-assisted medical form filling from transcribed appointments (STT), flagging ~95% of hallucinated or missing fields. Scoped the problem, defined the approach, and shipped a working product in under 5 weeks.

### Senior Machine Learning Engineer | Nubank
**January 2024 - May 2025**

Largest digital bank in LATAM, 130M+ customers across Brazil, Mexico, and Colombia. [nubank.com.br](https://nubank.com.br/en/)

- Owned the full model lifecycle for underwriting risk models serving 3M+ monthly credit decisions at ~150ms p99 under a 99.9% uptime SLA — from data integration and training through production deployment and monitoring on K8s
- Designed and shipped a Scala-based data integrity framework adopted across 8+ teams to detect sudden shifts in business metrics datasets, cutting anomaly detection time from days to hours
- Operated autonomously across multiple squads, trusted to drive delivery end-to-end in a high-scale engineering culture

### Senior Data Engineer | Citigroup
**July 2023 - January 2024**

Top 3 US bank, global presence in 160+ countries. [citigroup.com](https://www.citigroup.com)

- Technical lead for a 4+ PB Data Lake migration (Hadoop/Hive → S3/Snowflake), defining the migration strategy and driving execution across teams while cutting query costs by ~35%
- Owned Spark job design and deployment on EKS clusters processing 30+ TB daily
- Established standardized pipeline patterns adopted across multiple business lines

### AI Engineer Consultant | Botco AI
**April 2023 - September 2025**

US-based tech startup, working with an international team on a contract basis — reporting directly to the CTO and VP of Engineering. [botco.ai](https://botco.ai)

- Owned the data extraction platform: designed, built, and maintained the web scraping microservice (Python/K8s) powering the company's content ingestion — scraping ~100K pages/week
- Architected and shipped document indexer API (HTML, PDF, Docx) with vector storage (PostgreSQL/pgvector) — the foundation of the RAG pipeline, indexing 1M+ documents at ~200ms p95 retrieval latency and serving 10+ customer chatbots across web app and Facebook
- Exposed the retrieval and ingestion layer as MCP servers, letting agents consume document search as a standard tool interface
- Drove LLM fine-tuning strategy (GPT, LLaMA 2, Gemini) for QA and summarization, improving answer relevance by ~30% across the product

### AI Engineer Consultant | Fundamentl Partners
**June 2023 - October 2023**

- Owned end-to-end delivery of a Generative QA and summarization product — from problem scoping through production deployment
- Designed the retrieval architecture: private data indexing into Vector DB with LLM-powered answer generation from the knowledge base

### Senior Machine Learning Engineer | BBVA AI Factory
**January 2023 - July 2023**

Largest bank in Mexico by customers. [bbvaaifactory.com](https://www.bbvaaifactory.com)

- Technical lead for anti-money-laundering detection system: architected and deployed graph-based community detection and similarity models processing 10M+ transactions, improving detection recall by ~25%
- Set engineering standards for the team's PySpark codebase — scalability, documentation, and code review practices
- Owned ETL pipeline design and ML model lifecycle: monitoring, evaluation, and retraining across Big Data stack (PySpark, Hadoop, Kafka, Hive)

### Data Scientist | Cargamos
**November 2021 - November 2022**

Tech/Logistics startup based in Mexico. Ranked in Top 10 LinkedIn Startups.

- Owned the fraud prevention system end-to-end: designed, built, and deployed real-time anomaly detection (Isolation Forest) on GCP
- Drove operational success rate from ~80% to 97% — owned analytics for finance and operations, directly influencing company-wide decisions
- Designed the data warehouse architecture and ETL/ELT pipelines (PySpark), improving data availability across all teams
- Maintained Deep CNN model for automated delivery evidence classification

---

## Open Source Contributions

- **vLLM (GGUF plugin)** — Enabled bfloat16 inference on Blackwell (sm_100) GPUs by removing a stale device-capability guard, after verifying both the Triton and CUDA dequantization backends handle bf16 output correctly. [PR #73](https://github.com/vllm-project/vllm-gguf-plugin/pull/73)
- **langchain-searchapi** — Authored and published a standalone LangChain integration package (PyPI) for SearchApi.io: multi-engine search tool with dynamic engine selection, a RAG retriever, and full async support. [PyPI](https://pypi.org/project/langchain-searchapi/) · [Code](https://github.com/axiom-of-choice/langchain-searchapi)
- **CrewAI** — Contributed `SearchApiSearchTool`, a multi-engine search tool (Google, YouTube, Bing, Baidu, and more) enabling dynamic engine switching within agent workflows. [PR #6434](https://github.com/crewAIInc/crewAI/pull/6434)
- **Model Context Protocol (MCP) Servers** — Added configurable timeout support, improving reliability for long-running tool calls. [PR #4459](https://github.com/modelcontextprotocol/servers/pull/4459)
- **LangChain Docs** — Authored the official SearchApi.io integration documentation covering tool usage, the RAG retriever, and agent examples. [PR #4703](https://github.com/langchain-ai/docs/pull/4703)

---

## Education

### Bachelor of Mathematics | National Autonomous University of Mexico (UNAM)
**August 2017 - August 2021** | GPA: 92/100

### NLP & Deep Learning Research Intern | IIMAS, UNAM
**March 2022 - January 2023**

Research at the Institute for Research in Applied Mathematics and Systems (IIMAS), UNAM's applied-math research institute.

- Designed and ran deep reinforcement learning experiments (PyTorch, OpenAI Baselines, Dopamine) — implementing and comparing agent architectures against published baselines
- Built the NLP data pipeline end-to-end: large-scale web scraping of newspaper corpora, cleaning, and annotation for downstream language-model training
- Worked alongside faculty researchers, translating recent DL/RL literature into reproducible experiments

### Research Summer Residency | CIMAT
**2020**

Advanced research topics in multiple fields of mathematics at the Research Center in Mathematics.

---

## Technical Skills

**Languages:** Python, Scala, SQL, Golang (familiar), Rust (familiar)

**AI/ML:** PyTorch, TensorFlow (Certified Developer), Scikit-learn, HuggingFace, OpenAI API

**LLM Serving & Optimization:** vLLM, TGI, Ollama, quantization (GGUF, MLX), LoRA / QLoRA, batch & real-time inference

**LLMs & Agents:** LangGraph, LlamaIndex, CrewAI, Haystack, MCP (servers & clients), RAG, Fine-tuning, Prompt Engineering

**Vector DBs & Retrieval:** pgvector, Pinecone, Qdrant, Weaviate, Milvus, Chroma, FAISS, embeddings, hybrid search, reranking

**Integrations & APIs:** FastAPI, Flask, REST APIs, GraphQL, Web Scraping, Data Extraction Pipelines

**LLM Observability:** Arize, LangSmith, OpenTelemetry, Guardrails

**Data Engineering:** Apache Spark (Python & Scala), Airflow, Kafka, Hadoop, Hive, dbt

**Cloud - AWS:** S3, DynamoDB, RDS, Step Functions, SageMaker, Athena, Glue, EC2, ECS, EKS, Redshift, Lambda

**Cloud - GCP:** BigQuery, App Engine, VertexAI, Dataflow, GKE, DataProc

**Cloud - Azure:** AZ-900 Certified, Azure Data Factory, Synapse Analytics, Databricks

**Databases:** PostgreSQL, MySQL, MongoDB, Snowflake, Redis

**Infrastructure:** Docker, Kubernetes, CI/CD (GitHub Actions, GitLab CI, BitBucket Pipelines)

**MLOps:** MLFlow, Airflow, dbt Cloud, Grafana, ElasticStack

---

## Certifications

- **TensorFlow Developer Certificate** | Google (May 2023)
- **Apache Airflow Fundamentals** | Astronomer (Nov 2023)
- **Microsoft Azure Fundamentals (AZ-900)** | Microsoft (Dec 2021)
- **MLOps | Machine Learning Operations Specialization** | Duke University / Coursera
- **Deep Learning Specialization** | DeepLearning.AI / Coursera (Sep 2022)
- **DeepLearning.AI TensorFlow Developer Specialization** | Coursera (Nov 2022)
- **Data Scientist With Python** | DataCamp (Nov 2021)
- **Data Analyst With Python** | DataCamp (Jan 2022)
- **NLP Specialization** | DeepLearning.AI / Coursera (In progress)

---

## Languages

- **English:** C1 Full Professional Proficiency (TOEFL Certified)
- **Spanish:** Native
- **Portuguese:** Currently learning

---

## Soft Skills

- Technical leadership: architecture reviews, engineering standards, unblocking teams
- Data-driven decision making & stakeholder management
- End-to-end project ownership — scoping, delivery, and post-launch iteration
- Cross-functional and international team collaboration
- Fast learner, proactive, and autonomous in high-ambiguity environments
