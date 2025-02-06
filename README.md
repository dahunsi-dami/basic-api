# Basic Public API

## Overview
This simple public API returns some basic information in JSON format (my email, this GitHub repo URL, and the current time in ISO 8601 format). It's an exercise from Stage 0 of the HNG Internship for back-end developers. You can [visit HNG to hire the best Python developers](https://hng.tech/hire/python-developers) in the world.

## Project Requirements
- Programming Language/Framework: Use any of the following: See Sharp (C#), PHP, Python, Go, Java, JavaScript/TypeScript.
- Deployment: The API must be deployed to a publicly accessible endpoint.
- CORS Handling: Ensure the API handles Cross-Origin Resource Sharing (CORS) appropriately.
- Response Format: All responses must be in JSON format.
- Endpoint `GET <your-url>`.
- The required JSON Response Format (200 OK).
- The API must accept GET requests and return the required JSON response.
- The `current_datetime` field must be dynamically generated in ISO 8601 format (UTC).
- It provides appropriate HTTP status code.

## Technologies Used
- Programming Language: Python
- Framework: Flask
- CORS Handling: using Flask-CORS
- Caching: using Flask Caching for improved performance
- Deployment: Railway

## API Documentation

### API Endpoint
`GET /`

### Public API Endpoint
`https://basic-api-py.up.railway.app/`

### Sample Usage
Here's the request format:
`curl -X GET https://basic-api-py.up.railway.app/`

### Response Format
```JSON
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/dahunsi-dami/basic-api-py"
}
```

### Response Details
- `email`: My registered email on HNG-12 Slack.
- `current_datetime`: The current datetime in ISO 8601 UTC format.
- `github_url`: My GitHub repository URL for this project.

## Deployment
Again, this API is publicly accessible at:
`https://basic-api-py.up.railway.app/`

## How To Run this API Locally
Ensure you have:
- Python 3 installed.
- `pip` package manager.

```Bash
# Clone the repository
git clone https://github.com/dahunsi-dami/basic-api-py.git
cd basic-api-py

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the API locally
python app.py

# Test the API
curl -X GET http://127.0.0.1:5000/
```

## Deploying This API on Railway
```Bash
# Push code to GitHub
git add .
git commit -m "Initial commit"
git push origin main

# Deploy on Railway
# 1. Go to Railway (https://railway.app/)
# 2. Create a new project
# 3. Link your GitHub repository
# 4. Set the start command:
gunicorn -w 4 -b 0.0.0.0:5000 app:app
# 5. Deploy 🚀
# 6. Go to Settings and Generate Domain under Network to get your publicly accessible API URL.
```
