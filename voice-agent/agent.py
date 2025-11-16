from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions, inference
from livekit.plugins import noise_cancellation, silero, openai
from livekit.plugins.turn_detector.multilingual import MultilingualModel
from prompt import AGENT_INSTRUCTIONS, SESSION_INSTRUCTIONS

load_dotenv(".env")


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=AGENT_INSTRUCTIONS,
        )


async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        stt="assemblyai/universal-streaming:en",
        llm=openai.LLM(
            model="gpt-5-nano-2025-08-07",
            reasoning_effort="minimal",
            store=True,
            verbosity="low",
        ),
        tts="elevenlabs/eleven_turbo_v2_5:iP95p4xoKVk53GoZ742B",
        vad=silero.VAD.load(),
        turn_detection=MultilingualModel(),
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    await session.generate_reply(instructions=SESSION_INSTRUCTIONS)


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
