from pathlib import Path


class EvidenceCollector:
    """
    Reads forensic evidence from a log file.

    Responsibilities:
    - Validate the log file path.
    - Read the file safely.
    - Return the raw log contents.

    This class DOES NOT analyze logs.
    """

    def __init__(self, log_path: str) -> None:
        self.log_path = Path(log_path)

    def collect(self) -> str:
        """
        Read the log file and return its contents.

        Returns:
            str: Raw log file contents.

        Raises:
            FileNotFoundError:
                If the log file does not exist.

            PermissionError:
                If the file cannot be accessed.
        """

        if not self.log_path.exists():
            raise FileNotFoundError(
                f"Log file not found: {self.log_path}"
            )

        with self.log_path.open(
            mode="r",
            encoding="utf-8"
        ) as file:

            return file.read()