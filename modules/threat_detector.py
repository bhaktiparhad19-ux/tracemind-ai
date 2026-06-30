from collections import defaultdict
from typing import List

from modules.security_event import SecurityEvent
from config import FAILED_LOGIN_THRESHOLD


class ThreatDetector:
    """
    Detects malicious behavior from structured security events.
    """

    def __init__(self, events: List[SecurityEvent]):
        self.events = events

    def analyze(self):

        failed_logins = defaultdict(int)
        sudo_events = 0

        attack_chain = []
        suspicious_ips = set()
        target_users = set()

        # --------------------------
        # Step 1: Analyze events
        # --------------------------
        for event in self.events:

            if event.event_type == "failed_login":
                if event.ip_address:
                    failed_logins[event.ip_address] += 1
                    suspicious_ips.add(event.ip_address)

                if event.username:
                    target_users.add(event.username)

            elif event.event_type == "successful_login" :
                 if event.ip_address:
                      suspicious_ips.add(event.ip_address)

                 if event.username:
                      target_users.add(event.username)

            elif event.event_type == "sudo_command":
                sudo_events += 1
                if event.username:
                    target_users.add(event.username)


        # --------------------------
        # Step 2: Detection rules
        # --------------------------
        attack_type = "No Threat Detected"
        severity = "Low"
        confidence = 0

        # Rule 1 — brute force detection
        brute_force_ips = set()

        for ip, count in failed_logins.items():
             if count >= FAILED_LOGIN_THRESHOLD:
               brute_force_ips.add(ip)

               attack_chain.append(
                  f"{count} failed login attempts from {ip}"
                )
               attack_type = "Possible Brute Force Attack"
               severity = "Medium"
               confidence = 60
               

        # Rule 2 — successful login after failures
        for event in self.events:
             if (
                event.event_type == "successful_login"
                and event.ip_address in brute_force_ips
            ):

                attack_type = "Successful Brute Force Attack"
                severity = "High"
                confidence = 90

                attack_chain.append(
                    f"Successful login after brute force from {event.ip_address}"
                )

        # Rule 3 — privilege escalation
        if sudo_events > 0:
            attack_chain.append(
                f"Privilege escalation detected ({sudo_events} sudo commands)"
         )
            if severity == "High":
                severity = "Critical"
                confidence = 95
        # --------------------------
        # Step 3: Final report
        # --------------------------
        return {
            "attack_type": attack_type,
            "severity": severity,
            "confidence": confidence,
            "attack_chain": attack_chain,
            "ioc": {
                "suspicious_ips": list(suspicious_ips),
                "target_users": list(target_users)
            }
        }
        