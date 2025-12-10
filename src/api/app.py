import logging

from fastapi import FastAPI
from fastrtc import Stream

from .routes import router, set_stream

logger = logging.getLogger(__name__)


def create_app(stream: Stream) -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="FastRTC OpenAI Realtime",
        description="Real-time voice chat with OpenAI",
        version="0.1.0",
    )

    # Set stream for routes
    set_stream(stream)

    # Mount FastRTC WebRTC endpoints
    stream.mount(app)

    # Include API routes
    app.include_router(router)

    logger.info("FastAPI application created")
    return app
