from modules.evidence_collector import EvidenceCollector


def main():

    collector = EvidenceCollector("logs/auth.log")

    logs = collector.collect()

    print(logs)


if __name__ == "__main__":
    main()