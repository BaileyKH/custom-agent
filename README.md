# Custom AI Agent

A command-line AI agent powered by Google's Gemini 2.5 Flash mode

## Setup

1. Install [uv](https://docs.astral.sh/uv/) if you haven't already:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Install dependencies:

```bash
uv sync
```

3. Create a `.env` file in the project root and add your Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

## Usage

```bash
uv run main.py "Your prompt here"
```

Use the `--verbose` flag to see token usage and the original prompt:

```bash
uv run main.py "Your prompt here" --verbose
```

## Requirements

- [uv](https://docs.astral.sh/uv/)
- A valid [Gemini API key](https://ai.google.dev/)
