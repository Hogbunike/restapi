# API Documentation

Welcome to the documentation for the **HNGx Person API**. This API provides basic CRUD operations for managing persons.
hosted url - [Person API](https://hogbunike.onrender.com)
## Table of Contents

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
  "id": 6,
  "name": "Henry Ogbunike"
}
```
![image](https://github.com/Hogbunike/restapi/assets/105209315/89ea41a9-0281-456c-9d1e-1b9496579a56)


**When Trying A Number**
```json
{
    "name": "Name must be a string."

}
```
![image](https://github.com/Hogbunike/restapi/assets/105209315/02cc101d-01c8-4acf-bd97-134972a11269)


## Fetch Details of a Person
**Endpoint:** /api/<person_id>

**Method:** GET

**Response Format (Success - HTTP 200 OK):**
```json
{
  "id": 6,
  "name": "Henry Ogbunike"
}
```
![image](https://github.com/Hogbunike/restapi/assets/105209315/13a8bffe-84eb-4f3a-9259-4eb77996ac59)



## Update Details of a Person
**Endpoint:** /api/<person_id>

**Method:** PUT or PATCH

**Request Format:**
```json
{
  "name": "Henry Ogbunike Updated"
  
}
```
**Request Format:**
```json
{
  "id": 6,
  "name": "Henry Ogbunike Updated"
}
```
![image](https://github.com/Hogbunike/restapi/assets/105209315/ecc54996-ffba-404c-9bff-ea8d08ac5f72)


## Remove a Person
**Endpoint:** /api/<person_id>

**Method:** DELETE

**Response Format (Success - HTTP 204 No Content):**

No response body.

**Response Format (Error - HTTP 404 Not Found):**

![image](https://github.com/Hogbunike/restapi/assets/105209315/78c12784-0ba8-44eb-aa22-c7596cae09b0)


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
Check the [README](https://github.com/Hogbunike/restapi/blob/a824ac1ba7e89498055239649f9794530f5a4be6/README.md)






