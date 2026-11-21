import json
import os

from domain.service_request import ServiceRequest


class FileRepository:
    """Infrastructure class: the only place that reads/writes the JSON file."""

    def __init__(self, file_path=None):
        if file_path is None:
            base_dir = os.path.dirname(
                os.path.dirname(os.path.abspath(__file__)))
            file_path = os.path.join(base_dir, "data", "requests.json")
        self.file_path = file_path

    def load_all(self):
        """Return a list of ServiceRequest objects from the JSON file.

        A missing, empty or unreadable file safely gives an empty list.
        """
        if not os.path.exists(self.file_path):
            return []

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                content = file.read().strip()
            if not content:
                return []
            data = json.loads(content)
        except (json.JSONDecodeError, OSError):
            return []

        return [ServiceRequest.from_dict(item) for item in data]

    def save_all(self, requests):
        """Write a list of ServiceRequest objects to the JSON file."""
        folder = os.path.dirname(self.file_path)
        if folder:
            os.makedirs(folder, exist_ok=True)

        data = [request.to_dict() for request in requests]
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)