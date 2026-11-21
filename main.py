from application.request_service import RequestService
from domain.exceptions import (
    DuplicateRequestError,
    InvalidPriorityError,
    RequestAlreadyResolvedError,
    RequestNotFoundError,
)
from infrastructure.file_repository import FileRepository


def show_menu():
    print()
    print("SMART SERVICE DESK SYSTEM")
    print("1. Create Service Request")
    print("2. View All Requests")
    print("3. Search Request")
    print("4. Resolve Request")
    print("5. Exit")


def create_request(service):
    request_id = input("Enter Request ID: ")
    employee_name = input("Enter Employee Name: ")
    issue = input("Enter Issue: ")
    priority = input("Enter Priority: ")

    try:
        service.create_request(request_id, employee_name, issue, priority)
        print("Service Request created successfully.")
    except DuplicateRequestError as error:
        print(f"Error: {error}")
    except InvalidPriorityError as error:
        print(f"Error: {error}")
    except ValueError as error:
        print(f"Error: {error}")


def view_requests(service):
    requests = service.view_requests()
    if not requests:
        print("No service requests found.")
        return
    for request in requests:
        print(request)


def search_request(service):
    request_id = input("Enter Request ID: ")
    try:
        request = service.search_request(request_id)
        print(f"Request ID     : {request.request_id}")
        print(f"Employee Name  : {request.employee_name}")
        print(f"Issue          : {request.issue}")
        print(f"Priority       : {request.priority}")
        print(f"Status         : {request.status}")
    except RequestNotFoundError:
        print("Request not found.")


def resolve_request(service):
    request_id = input("Enter Request ID: ")
    try:
        service.resolve_request(request_id)
        print("Request resolved successfully.")
    except RequestNotFoundError:
        print("Request not found.")
    except RequestAlreadyResolvedError as error:
        print(error)


def main():
    repository = FileRepository()
    service = RequestService(repository)

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_request(service)
        elif choice == "2":
            view_requests(service)
        elif choice == "3":
            search_request(service)
        elif choice == "4":
            resolve_request(service)
        elif choice == "5":
            print("Thank you. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()