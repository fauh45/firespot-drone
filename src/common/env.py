import os
from dotenv import load_dotenv

load_dotenv()

DEFAULT_LISTEN_ADDRESS: str = "tcp://*:5555"
SERVER_LISTEN_ADDRESS: str = os.getenv("SERVER_LISTEN_ADDRESSS", DEFAULT_LISTEN_ADDRESS)
EDGE_LISTEN_ADDRESS: str = os.getenv("EDGE_LISTEN_ADDRESS", DEFAULT_LISTEN_ADDRESS)
SEND_VIDEO_DATA: bool = os.getenv("SEND_VIDEO_DATA", "false") == "true"