class RequestNotFoundError(Exception):
    """Raised when a service request ID does not exist."""
    pass


class DuplicateRequestError(Exception):
    """Raised when a service request ID already exists."""
    pass


class InvalidPriorityError(Exception):
    """Raised when the priority is not LOW, MEDIUM or HIGH."""
    pass


class RequestAlreadyResolvedError(Exception):
    """Raised when trying to resolve a request that is already RESOLVED."""
    pass