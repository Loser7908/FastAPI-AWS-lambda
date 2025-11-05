# Serverless Notes API

A serverless REST API built with FastAPI and AWS Lambda that demonstrates modern serverless application development and cloud architecture skills. This project implements a simple yet powerful notes management system using cutting-edge technologies and best practices.

## 🚀 Live Demo

The API is deployed and accessible at:
- Base URL: https://erca840m37.execute-api.us-east-1.amazonaws.com/default/serverless-notes-api

## 🛠️ Tech Stack

- **FastAPI**: Modern, fast web framework for building APIs with Python
- **AWS Lambda**: Serverless compute service
- **AWS DynamoDB**: NoSQL database service
- **Mangum**: AWS Lambda handler for ASGI applications
- **Pydantic**: Data validation using Python type annotations
- **Python 3.9+**: Latest Python features and type hints

## 🔥 Features

- **Serverless Architecture**: Zero server management, auto-scaling, and pay-per-use pricing
- **RESTful API Design**: Clean and intuitive API endpoints
- **CRUD Operations**: Complete notes management functionality
- **Data Validation**: Automatic request/response validation using Pydantic
- **Error Handling**: Proper HTTP status codes and error messages
- **DynamoDB Integration**: Efficient NoSQL database operations

## 📡 API Endpoints

### Base URL
```
https://erca840m37.execute-api.us-east-1.amazonaws.com/default/serverless-notes-api
```

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/` or `/serverless-notes-api` | Health check |
| GET    | `/serverless-notes-api/notes` | List all notes |
| POST   | `/serverless-notes-api/notes` | Create a new note |
| GET    | `/serverless-notes-api/notes/{note_id}` | Get a specific note |
| PUT    | `/serverless-notes-api/notes/{note_id}` | Update a note |
| DELETE | `/serverless-notes-api/notes/{note_id}` | Delete a note |

## 📝 Data Models

### Note Input Model
```python
{
    "title": "string",
    "content": "string"
}
```

### Note Response Model
```python
{
    "id": "string",
    "title": "string",
    "content": "string"
}
```

## 🏗️ Architecture

- **API Gateway**: Routes HTTP requests to Lambda function
- **Lambda Function**: Runs FastAPI application using Mangum adapter
- **DynamoDB**: Stores note data with automatic scaling
- **IAM Roles**: Manages secure access between services

## 💡 Key Skills Demonstrated

1. **Modern Python Development**
   - FastAPI framework usage
   - Type hints and Pydantic models
   - Async/await patterns

2. **AWS Cloud Services**
   - Lambda function deployment
   - DynamoDB integration
   - API Gateway configuration
   - IAM role management

3. **API Development**
   - RESTful design principles
   - Status code handling
   - Error management
   - Data validation

4. **Serverless Architecture**
   - Event-driven design
   - Stateless application structure
   - Cloud-native patterns

## 🔒 Security

- API Gateway handles request validation
- IAM roles restrict service access
- DynamoDB encryption at rest
- HTTPS endpoints only

## ⚡ Performance

- Serverless auto-scaling
- DynamoDB on-demand capacity
- FastAPI's high-performance framework
- Efficient database operations

This project showcases practical implementation of modern serverless architecture, combining the speed and ease of FastAPI with the scalability and reliability of AWS services.