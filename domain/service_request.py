from domain.exceptions import InvalidPriorityError, RequestAlreadyResolvedError


class ServiceRequest:
    """Domain class: holds the data and the business rules of one request."""

    VALID_PRIORITIES = ("LOW", "MEDIUM", "HIGH")
    STATUS_OPEN = "OPEN"
    STATUS_RESOLVED = "RESOLVED"

    def __init__(self, request_id, employee_name, issue, priority,
                 status="OPEN"):
        request_id = request_id.strip().upper()
        employee_name = employee_name.strip()
        issue = issue.strip()
        priority = priority.strip().upper()
        status = status.strip().upper()

        if not request_id or not employee_name or not issue:
            raise ValueError(
                "Request ID, employee name and issue cannot be empty.")

        if priority not in self.VALID_PRIORITIES:
            raise InvalidPriorityError(
                "Priority must be LOW, MEDIUM or HIGH")

        if status not in (self.STATUS_OPEN, self.STATUS_RESOLVED):
            raise ValueError("Status must be OPEN or RESOLVED.")

        self.request_id = request_id
        self.employee_name = employee_name
        self.issue = issue
        self.priority = priority
        self._status = status

    @property
    def status(self):
        return self._status

    def resolve(self):
        """Business rule: OPEN -> RESOLVED. Already resolved is an error."""
        if self._status == self.STATUS_RESOLVED:
            raise RequestAlreadyResolvedError(
                f"Request {self.request_id} is already RESOLVED.")
        self._status = self.STATUS_RESOLVED

    def to_dict(self):
        return {
            "request_id": self.request_id,
            "employee_name": self.employee_name,
            "issue": self.issue,
            "priority": self.priority,
            "status": self._status,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["request_id"],
            data["employee_name"],
            data["issue"],
            data["priority"],
            data["status"],
        )

    def __str__(self):
        return (f"{self.request_id} | {self.employee_name} | "
                f"{self.issue} | {self.priority} | {self._status}")