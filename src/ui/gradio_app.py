import logging

from fastrtc import Stream

from ..config import settings

logger = logging.getLogger(__name__)


def create_gradio_ui(stream: Stream):
    """Create and return the Gradio UI from the stream."""
    logger.info("Creating Gradio UI")
    return stream.ui


def launch_gradio(stream: Stream) -> None:
    """Launch the Gradio UI."""
    ui = create_gradio_ui(stream)
    logger.info(f"Launching Gradio UI on port {settings.port}")
    ui.launch(server_port=settings.port)
