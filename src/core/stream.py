import logging

import gradio as gr
from fastrtc import Stream, get_twilio_turn_credentials
from gradio.utils import get_space

from .handler import OpenAIRealtimeHandler

logger = logging.getLogger(__name__)


def update_chatbot(chatbot: list[dict], response: dict) -> list[dict]:
    """Update chatbot with new message."""
    chatbot.append(response)
    return chatbot


def create_stream() -> Stream:
    """Create and configure the FastRTC stream."""
    chatbot = gr.Chatbot(type="messages")

    stream = Stream(
        OpenAIRealtimeHandler(),
        mode="send-receive",
        modality="audio",
        additional_inputs=[chatbot],
        additional_outputs=[chatbot],
        additional_outputs_handler=update_chatbot,
        rtc_configuration=get_twilio_turn_credentials() if get_space() else None,
        concurrency_limit=5 if get_space() else None,
        time_limit=90 if get_space() else None,
    )

    logger.info("FastRTC stream created")
    return stream
