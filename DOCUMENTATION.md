# API DOCUMENTATION

Welcome to the documentation for the HNGx Person API. This API provides basic CRUD operations for managing persons.
Hosted URL: [Person API](https://hogbunike.onrender.com)

## Table Of Contents
- [API Endpoints](#api-endpoints)
  - [Create a New Person](#create-a-new-person)
  - [Fetch Details of a Person](#fetch-details-of-a-person)
  - [Update Details of a Person](#update-details-of-a-person)
  - [Remove a Person](#remove-a-person)
- [Request and Response Formats](#request-and-response-formats)
- [UML Diagram](#uml-diagram)
- [Known Limitations](#known-limitations)
- [How to install](#how-to-install)

## API Endpoints

### Create a New Person

**Endpoint:** `/api`

**Method:** POST

**Request Format:**
```json
{
  "name": "Henry Ogbunike"
}
```
**Response Format (Success - HTTP 201 Created):**
```json
{
  "name": "John Doe"
}

![image](https://github.com/Hogbunike/restapi/assets/105209315/af1adacf-4bbb-48f3-8116-647db3160726)

**When Trying A Number**
**Method:** POST

**Request Format:**
```json
{
  "name": 44
}
```
**Response Format (Error - HTTP 400 Bad Request):**
```json
{
    "name": "Name must be a string."

}

![image](https://github.com/Hogbunike/restapi/assets/105209315/15f1d00e-0ab7-45bf-8178-3fc8def4178d)

## Fetch Details of a Person
**Endpoint:** /api/<person_id>

**Method:** GET

**Response Format (Success - HTTP 200 OK):**
```json
{
  "id": 4,
  "name": "Henry Ogbunike"
}
```
![image](https://github.com/Hogbunike/restapi/assets/105209315/530c458c-bf14-41ee-bdf1-ea7d4e7a31e7)

## Update Details of a Person
**Endpoint:** /api/<person_id>

**Method:** PUT or PATCH

**Request Format:**
```json
{
  "name": "Henry"
}
```

**Response Format (Success - HTTP 200 OK):**
```json
{
  "id": 4,
  "name": "Henry"
}
```
![image](https://github.com/Hogbunike/restapi/assets/105209315/32a706b5-7836-42b6-90e8-65bb042dbbb1)

## Remove a Person
**Endpoint:** /api/<person_id>

**Method:** DELETE

**Response Format (Success - HTTP 204 No Content):**

No response body.
![image](https://github.com/Hogbunike/restapi/assets/105209315/f6c5d4fa-b7c6-4a75-aa52-1774c929ee59)

## Request and Response Formats
All API endpoints accept and return data in JSON format.
Ensure that the request and response data adhere to the specified formats mentioned above.

## Known Limitations

- The API does not support pagination.
- The API does not support filtering.
- The API does not support sorting.
- This documentation assumes a local development setup.
- Authentication and authorization mechanisms are not implemented





## How to install
Consult the [README](https://github.com/Hogbunike/endpoint/blob/a75e89812ae2d394b60e5cdd30e2309d8f7686ee/README.md)





