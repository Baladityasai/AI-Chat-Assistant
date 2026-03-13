<p align="center">
  <h1 align="center">🤖 AI Chat Assistant</h1>
  <p align="center">
    <em>A prompt-engineered conversational AI powered by Google Gemini &amp; LangChain</em>
  </p>
  <p align="center">
    <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/LLM-Google%20Gemini-4285F4?logo=google&logoColor=white" alt="Gemini">
    <img src="https://img.shields.io/badge/Framework-LangChain-00A67E?logo=chainlink&logoColor=white" alt="LangChain">
    <img src="https://img.shields.io/badge/Cost-Free%20Tier-brightgreen" alt="Free Tier">
    <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License">
  </p>
</p>

---

An interactive CLI-based AI assistant that goes beyond simple chat by leveraging **advanced prompt engineering techniques** — role-based personas, few-shot learning, multi-step prompt chaining, and self-evaluating responses — all running on Google Gemini's free tier.

## ✨ Features

| Feature | Description |
|---|---|
| 🎭 **Role-Based Prompting** | Switch between 5 specialized personas — General Assistant, Software Engineer, Tutor, Data Analyst, and Creative Writer — each with tailored system prompts and behavioral rules. |
| 📚 **Few-Shot Learning** | Curated in-context examples across coding, reasoning, summarization, and Q&A categories guide the model toward structured, high-quality outputs. |
| 🧠 **Conversation Memory** | Sliding-window memory retains the last 10 conversation turns (configurable), maintaining context without exceeding token limits. |
| ⛓️ **Prompt Chaining** | Complex queries are automatically routed through a multi-step pipeline: _Intent Classification → Task Decomposition → Chain-of-Thought Reasoning → Response Synthesis_. |
| 📊 **Self-Evaluation & Retry** | Every response is scored on relevance, accuracy, completeness, and clarity. Low-confidence answers are automatically refined and regenerated. |
| 🔧 **Fully Configurable** | Customize the model, temperature, token limits, memory window, chaining behavior, and evaluation thresholds via environment variables. |

## 🏗️ Architecture

```
AI Chat Assistant/
├── main.py                      # CLI entry point & interactive loop
├── config.py                    # Centralized configuration (env-driven)
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment variable template
│
├── agent/
│   ├── chat_agent.py            # Core orchestrator (memory, chaining, eval)
│   ├── prompt_chain.py          # Multi-step reasoning pipeline
│   └── response_evaluator.py    # Quality scoring & prompt refinement
│
├── prompts/
│   ├── system_prompt.py         # Role-based system prompt templates
│   ├── few_shot_examples.py     # In-context learning examples
│   └── task_prompts.py          # Chaining & evaluation prompt templates
│
└── tests/
    ├── test_agent.py            # Agent unit tests
    └── test_prompts.py          # Prompt template tests
```

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+**
- A **Google Gemini API key** (free) — [Get one here](https://aistudio.google.com/apikey)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/ai-chat-assistant.git
cd ai-chat-assistant

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
.venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure your API key
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY
```

### Run

```bash
python main.py
```

## 💬 CLI Commands

| Command | Description |
|---|---|
| `/help` | Show available commands |
| `/mode <role>` | Switch persona (`default`, `coder`, `tutor`, `analyst`, `creative`) |
| `/chain` | Toggle prompt chaining on/off |
| `/eval` | Toggle self-evaluation on/off |
| `/status` | Display current agent configuration |
| `/clear` | Clear conversation memory |
| `/exit` | Exit the assistant |

## ⚙️ Configuration

All settings can be overridden via environment variables in your `.env` file:

| Variable | Default | Description |
|---|---|---|
| `GOOGLE_API_KEY` | — | **(Required)** Your Gemini API key |
| `MODEL_NAME` | `gemini-2.0-flash` | Gemini model to use |
| `TEMPERATURE` | `0.7` | Response creativity (0.0 – 1.0) |
| `MAX_TOKENS` | `1024` | Maximum output token length |

Internal defaults (set in `config.py`):

| Setting | Default | Description |
|---|---|---|
| `MEMORY_WINDOW_SIZE` | `10` | Conversation turns retained |
| `ENABLE_PROMPT_CHAINING` | `True` | Auto-chain complex queries |
| `ENABLE_SELF_EVALUATION` | `True` | Score & retry low-quality responses |
| `CONFIDENCE_THRESHOLD` | `0.7` | Minimum quality score to accept |
| `MAX_RETRIES` | `2` | Retry attempts for low-confidence answers |

## 🔬 Prompt Engineering Techniques Used

1. **System Prompting** — Detailed role definitions with behavioral rules, output formatting guidelines, and anti-hallucination guardrails.
2. **Few-Shot Prompting** — Curated input/output examples teach the model desired response structure and reasoning patterns.
3. **Prompt Chaining** — Sequential multi-step pipeline that classifies intent, decomposes tasks, reasons step-by-step, and synthesizes a polished answer.
4. **Chain-of-Thought (CoT)** — Explicit step-by-step reasoning for complex logic and analytical queries.
5. **Self-Evaluation** — Automated quality scoring (relevance, accuracy, completeness, clarity) with prompt refinement and retry on low-confidence outputs.
6. **Role-Based Persona Switching** — Dynamic system prompt swapping to specialize the assistant's behavior on the fly.

## 🧪 Testing

```bash
# Run all tests
python -m pytest tests/ -v
```

## 🛠️ Tech Stack

- **[LangChain](https://www.langchain.com/)** — LLM orchestration & prompt templating
- **[Google Gemini](https://ai.google.dev/)** — LLM provider (free tier)
- **[Colorama](https://pypi.org/project/colorama/)** — Rich terminal output
- **[python-dotenv](https://pypi.org/project/python-dotenv/)** — Environment configuration

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Built with ❤️ and prompt engineering
</p>

