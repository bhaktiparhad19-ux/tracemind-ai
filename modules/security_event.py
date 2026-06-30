from dataclasses import dataclass
from typing import Optional


@dataclass
class SecurityEvent:
    """
    Standard structure for all security-related log events.
    """

    timestamp: Optional[str]
    event_type: str
    username: Optional[str]
    ip_address: Optional[str]
    raw_log: str