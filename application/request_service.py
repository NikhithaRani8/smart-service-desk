from domain.exceptions import DuplicateRequestError, RequestNotFoundError
from domain.service_request import ServiceRequest


class RequestService:
    """Application layer: the use cases of the Service Desk.

    It receives a repository from outside (dependency injection), so it
    does not depend on how or where the data is stored.
    """

    def __init__(self, repository):
        self.repository = repository
        self.requests = self.repository.load_all()

    def create_request(self, request_id, employee_name, issue, priority):
        new_request = ServiceRequest(
            request_id, employee_name, issue, priority)

        if self._find(new_request.request_id) is not None:
            raise DuplicateRequestError(
                f"Request ID {new_request.request_id} already exists.")

        self.requests.append(new_request)
        self.repository.save_all(self.requests)
        return new_request

    def view_requests(self):
        return list(self.requests)

    def search_request(self, request_id):
        request = self._find(request_id)
        if request is None:
            raise RequestNotFoundError(
                f"Request {request_id.strip().upper()} not found.")
        return request

    def resolve_request(self, request_id):
        request = self.search_request(request_id)
        request.resolve()
        self.repository.save_all(self.requests)
        return request

    def _find(self, request_id):
        request_id = request_id.strip().upper()
        for request in self.requests:
            if request.request_id == request_id:
                return request
        return None