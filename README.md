# Voice Agent

A real-time voice assistant that enables natural voice conversations with an AI agent.
This project consists of a Next.js frontend and a Python backend agent that handles speech-to-text, LLM processing, and text-to-speech.

## Features

-   **Speech-to-Text** using AssemblyAI Universal Streaming
-   **LLM Integration** using OpenAI GPT-5-nano
-   **Text-to-Speech** using ElevenLabs Turbo v2.5
-   **Voice Activity Detection** using Silero VAD
-   **Turn Detection** with Multilingual Model
-   **Noise Cancellation** using BVC (Broad Voice Cancellation)
-   **Real-time Chat** interface with LiveKit

## Architecture

```
┌─────────────────┐         ┌──────────────────┐         ┌─────────────────┐
│   Next.js App   │◄───────►│      LiveKit     │◄───────►│  Python Agent   │
│   (Frontend)    │         │      Server      │         │   (Backend)     │
└─────────────────┘         └──────────────────┘         └─────────────────┘
                                    │
                                    ▼
                         ┌──────────────────┐
                         │    AssemblyAI    │
                         │       +          │
                         │     OpenAI       │
                         │       +          │
                         │    ElevenLabs    │
                         └──────────────────┘
```

## Prerequisites

-   **Node.js** 18+ and **pnpm** 9.15.9+
-   **Python** 3.11+
-   **LiveKit Server** (cloud or self-hosted)
-   API keys for:
    -   LiveKit (API Key & Secret)
    -   AssemblyAI
    -   OpenAI
    -   ElevenLabs

## Project Structure

```
voice-agent/
├── agent-frontend/
│   ├── app/
│   ├── components/
│   │   ├── app/
│   │   └── livekit/
│   ├── hooks/
│   ├── lib/
│   └── package.json
│
├── voice-agent/
│   ├── agent.py
│   ├── prompt.py
│   ├── pyproject.toml
│   ├── livekit.toml
│   └── Dockerfile
│
└── README.md
```

## Setup

### 1. Frontend Setup

Navigate to the frontend directory and install dependencies:

```bash
cd agent-frontend
pnpm install
```

Create a `.env` file in `agent-frontend/`:

```env
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
LIVEKIT_URL=https://your-livekit-server-url
```

### 2. Backend Agent Setup

Navigate to the agent directory and set up Python environment:

```bash
cd voice-agent
# Using uv
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e .

# Or using pip
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

Create a `.env` file in `voice-agent/`:

```env
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
LIVEKIT_URL=wss://your-livekit-server-url

# AssemblyAI
ASSEMBLYAI_API_KEY=your_assemblyai_api_key

# OpenAI
OPENAI_API_KEY=your_openai_api_key

# ElevenLabs
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```

## Running the Application

### Start the Frontend

```bash
cd agent-frontend
pnpm dev
```

The frontend will be available at `http://localhost:3000`

### Start the Backend Agent

```bash
cd voice-agent
source .venv/bin/activate  # Activate virtual environment
python agent.py dev
```

## Technologies Used

### Frontend

-   **Next.js** 15.5.2 - React framework
-   **LiveKit Components React** - Real-time communication UI
-   **Tailwind CSS** - Styling
-   **TypeScript** - Type safety
-   **Shadcn** - Accessible component primitives

### Backend

-   **LiveKit Agents** - Agent framework
-   **Python 3.11+** - Programming language
-   **OpenAI** - LLM provider
-   **AssemblyAI** - Speech-to-text
-   **ElevenLabs** - Text-to-speech
-   **Silero** - Voice activity detection
