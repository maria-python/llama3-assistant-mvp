# Llama3 Assistant MVP

Early MVP of a **local AI assistant powered by Meta Llama 3 (8B)** with persistent conversation memory.

The project explores how to build a lightweight assistant that runs a local LLM, maintains conversation context, and organizes the system into modular components such as the LLM interface, memory management, and application loop.

This repository focuses on experimenting with local LLM interaction, simple memory persistence, and assistant architecture.

## Features

* Local **Meta Llama 3 8B** model support
* Persistent memory storage
* Modular architecture
* JSON-based memory system

## Project Structure

```
mvp/
│
├── main.py          # Entry point
├── llm.py           # LLM interaction layer
├── memory.py        # Memory management
├── memory.json      # Stored memory
├── schemas.py       # Data schemas
│
├── models/
│   └── meta-llama-3-8B/
│
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```
git clone https://github.com/yourname/llama3-assistant-mvp.git
cd llama3-assistant-mvp
```

Create virtual environment:

```
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

## Run

```
python main.py
```

## Notes

This repository represents an **early MVP prototype** and is still under development.

Future improvements may include:

* improved memory system
* conversation context management
* API interface
* better model integration

## License

MIT
