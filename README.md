# Smart Service Desk Management System

## Problem Statement
Employees raise IT support requests (laptop, network, password issues). This app lets support staff create, view, search and resolve these requests from the command line. Requests are saved in a JSON file so they are not lost when the app closes.

## Features
- Create a request (status starts as OPEN)
- View all requests
- Search a request by Request ID
- Resolve a request (OPEN to RESOLVED)
- Data is saved in data/requests.json and loaded again on restart
- Friendly messages for duplicate ID, request not found, wrong priority and wrong menu input

## Concepts Used
- OOP: ServiceRequest class with a resolve() method
- Exception handling: custom exceptions for duplicate, not found, invalid priority and already resolved
- File handling: requests stored in a JSON file; a missing or empty file is handled safely
- SOLID: each class has one job, and the service gets its repository from outside
- DDD: separate domain, application and infrastructure folders
- Git: development and main branches, with commits and a merge

## Folder Structure
```
smart-service-desk/
|-- domain/ (service_request.py, exceptions.py)
|-- application/ (request_service.py)
|-- infrastructure/ (file_repository.py)
|-- data/ (requests.json)
|-- main.py
|-- README.md
`-- .gitignore
```

## How to Run
```
python main.py
```

## Branches and Merge
I worked on the development branch and made a commit after each part (structure, domain, file repository, service, CLI, README). After testing, I merged development into main and pushed to GitHub.