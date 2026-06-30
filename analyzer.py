from modules.evidence_collector import EvidenceCollector
from modules.log_parser import AuthenticationLogParser
from modules.threat_detector import ThreatDetector
from modules.ai_analyst import AIAnalyst
from modules.report_exporter import ReportExporter
from pprint import pprint


def main():

    logs = EvidenceCollector("logs/auth.log").collect()

    events = AuthenticationLogParser(logs).parse()

    threat = ThreatDetector(events).analyze()

    print("\n========== THREAT REPORT ==========\n")
    pprint(threat)

    ai = AIAnalyst(threat)
    report = ai.analyze()

    print("\n========== AI INCIDENT REPORT ==========\n")
    print(report)


if __name__ == "__main__":
    main()