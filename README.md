# FastRTC OpenAI Realtime Template

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/deploy/fastrtc?referralCode=jk_FgY&utm_medium=integration&utm_source=template&utm_campaign=generic)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)

A production-ready template for building real-time voice assistants using FastRTC, OpenAI Realtime API, and FastAPI.

## Features

- Real-time voice conversation with OpenAI's Realtime API
- WebRTC-based audio streaming (low latency)
- Server-side Voice Activity Detection (VAD)
- Configurable system prompts and voice settings
- Docker support for easy deployment

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager
- OpenAI API key with Realtime API access

## Quick Start

### 1. Clone and Install

```bash
git clone <your-repo-url>
cd FastRTC-Template

# Install dependencies
uv sync
```

### 2. Configure Environment

```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:

```bash
OPENAI_API_KEY=sk-your-api-key-here
```

### 3. Run the Server

```bash
uv run python main.py
```

Open http://localhost:7860 in your browser and click "Start Conversation".

## Run Modes

| Mode | Command | Description |
|------|---------|-------------|
| FastAPI (default) | `uv run python main.py` | Custom HTML interface |
| Gradio UI | `MODE=UI uv run python main.py` | Gradio-based interface |
| Phone | `MODE=PHONE uv run python main.py` | Phone integration mode |

## Project Structure

```
FastRTC-Template/
├── main.py                 # Entry point
├── pyproject.toml          # Dependencies
├── Dockerfile              # Docker configuration
├── static/
│   └── index.html          # WebRTC frontend
└── src/
    ├── config/
    │   ├── settings.py     # API keys, model config
    │   └── prompts.py      # System instructions, voice settings
    ├── core/
    │   ├── handler.py      # OpenAI Realtime handler
    │   └── stream.py       # FastRTC stream factory
    ├── api/
    │   ├── app.py          # FastAPI app factory
    │   └── routes.py       # HTTP endpoints
    └── ui/
        └── gradio_app.py   # Gradio UI
```

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENAI_API_KEY` | (required) | Your OpenAI API key |
| `OPENAI_REALTIME_MODEL` | `gpt-realtime-mini-2025-10-06` | Realtime model to use |
| `OPENAI_TRANSCRIPTION_MODEL` | `gpt-4o-mini-transcribe` | Transcription model for input audio |
| `LAMBDA_API_URL` | (optional) | Lambda API endpoint for future integration |
| `MODE` | (empty) | Run mode: `UI`, `PHONE`, or empty for FastAPI |

### System Prompt

Edit `src/config/prompts.py` to customize the assistant's behavior:

```python
SYSTEM_INSTRUCTIONS = """
Your custom instructions here...
"""

DEFAULT_VOICE = "alloy"  # Options: alloy, echo, fable, onyx, nova, shimmer
DEFAULT_TEMPERATURE = 0.8
```

### Available Voices

| Voice | Description |
|-------|-------------|
| `alloy` | Neutral, balanced |
| `echo` | Warm, conversational |
| `fable` | Expressive, storytelling |
| `onyx` | Deep, authoritative |
| `nova` | Friendly, upbeat |
| `shimmer` | Soft, gentle |

## Docker Deployment

### Build

```bash
docker build -t fastrtc-template .
```

### Run

```bash
docker run -p 7860:7860 -e OPENAI_API_KEY=sk-your-key fastrtc-template
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main HTML interface |
| `/webrtc/offer` | POST | WebRTC signaling |
| `/outputs` | GET | SSE stream for transcriptions |
| `/health` | GET | Health check |

## Extending the Template

### Custom Handler

Create a new handler in `src/core/` by extending `AsyncStreamHandler`:

```python
from fastrtc import AsyncStreamHandler

class CustomHandler(AsyncStreamHandler):
    async def start_up(self):
        # Initialize your connection
        pass

    async def receive(self, frame):
        # Handle incoming audio
        pass

    async def emit(self):
        # Return audio/data to client
        pass
```

### Adding Routes

Add new endpoints in `src/api/routes.py`:

```python
@router.get("/custom")
async def custom_endpoint():
    return {"message": "Hello"}
```

## Troubleshooting

### Connection Failed

1. Ensure you're accessing via `http://localhost:7860` (not `0.0.0.0`)
2. Allow microphone permissions in your browser
3. Check browser console for errors

### No Audio Response

1. Verify your OpenAI API key has Realtime API access
2. Check server logs for error messages
3. Ensure the model name is correct

### Transcription Not Working

The `gpt-4o-mini-transcribe` model is required for input transcription. Native realtime models (`gpt-realtime-mini-*`) don't support input transcription.

## License

MIT
