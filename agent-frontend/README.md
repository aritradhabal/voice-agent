# Voice Agent

### Features:

- Speech To Text using Assembly AI
- LLM Integration using OpenAI gpt-5-nano
- Text To Speech using Elevenlabs

### Project structure

```
/
├── app/
│   ├── (app)/
│   ├── api/
│   ├── components/
│   ├── fonts/
│   ├── globals.css
│   └── layout.tsx
├── components/
│   ├── livekit/
│   ├── ui/
│   ├── app.tsx
│   ├── session-view.tsx
│   └── welcome.tsx
├── hooks/
├── lib/
├── public/
└── package.json
```

Run the app with:

```bash
pnpm install
pnpm dev
```

And open http://localhost:3000 in your browser.

You'll need to configure your credentials in `.env`:

```env
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
LIVEKIT_URL=https://your-livekit-server-url
```
