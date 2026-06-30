import json
class ReportExporter:
    """
    Saves investigation reports to files.
    """

    def __init__(self, report: dict):
        self.report = report

    def save_json(self):
        """
        Saves the investigation report as a JSON file.
        """
        with open("reports/investigation.json", "w") as file:
            json.dump(self.report, file, indent=4)