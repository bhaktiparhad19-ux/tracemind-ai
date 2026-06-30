import re
from typing import List, Optional

from modules.security_event import SecurityEvent


class AuthenticationLogParser:
    """
    Converts raw authentication logs into structured SecurityEvent objects.
    """

    def __init__(self, raw_logs: str):
        self.raw_logs = raw_logs

    def parse(self) -> List[SecurityEvent]:
        events: List[SecurityEvent] = []

        for line in self.raw_logs.splitlines():

            timestamp = self._extract_time(line)
            ip = self._extract_ip(line)

            # -------------------------
            # Failed login
            # -------------------------
            if "Failed password" in line:
                username = self._extract_failed_user(line)

                events.append(SecurityEvent(
                    timestamp=timestamp,
                    event_type="failed_login",
                    username=username,
                    ip_address=ip,
                    raw_log=line
                ))

            # -------------------------
            # Successful login
            # -------------------------
            elif "Accepted password" in line:
                username = self._extract_success_user(line)

                events.append(SecurityEvent(
                    timestamp=timestamp,
                    event_type="successful_login",
                    username=username,
                    ip_address=ip,
                    raw_log=line
                ))

            # -------------------------
            # sudo command
            # -------------------------
            elif "sudo:" in line:
                username = self._extract_sudo_user(line)

                events.append(SecurityEvent(
                    timestamp=timestamp,
                    event_type="sudo_command",
                    username=username,
                    ip_address=None,
                    raw_log=line
                ))

        return events

    # -----------------------------
    # Helper methods
    # -----------------------------

    def _extract_time(self, line: str) -> Optional[str]:
        match = re.search(r"\d{2}:\d{2}:\d{2}", line)
        return match.group() if match else None

    def _extract_ip(self, line: str) -> Optional[str]:
        match = re.search(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", line)
        return match.group() if match else None

    def _extract_failed_user(self, line: str) -> Optional[str]:
        match = re.search(r"invalid user (\w+)", line)
        return match.group(1) if match else None

    def _extract_success_user(self, line: str) -> Optional[str]:
        match = re.search(r"Accepted password for (\w+)", line)
        return match.group(1) if match else None

    def _extract_sudo_user(self, line: str) -> Optional[str]:
        match = re.search(r"sudo:\s*(\w+)", line)
        return match.group(1) if match else None