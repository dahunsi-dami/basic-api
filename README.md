# Basic Public API

## Overview
This simple public API returns some basic information in JSON format (my email, this GitHub repo URL, and the current time in ISO 8601 format). It's an exercise from Stage 0 of the HNG Internship for back-end developers. You can [visit HNG to hire the best Python developers](https://hng.tech/hire/python-developers) in the world.

## Technologies Used
- Programming Language: Python
- Framework: Flask
- Deployment: Railway
- CORS Handling: using Flask-CORS
- Caching: using Flask Caching
- Deployment: Railway

## API Documentation

### Endpoint
`GET /`

### Response Format
```JSON
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}
```

### Response Details
- `email`: My registered email on HNG-12 Slack.
- `current_datetime`: The current datetime in ISO 8601 UTC format.
- `github_url`: My GitHub repository URL for this project.

## Deployment
This API is publicly accessible at:
`https://basic-api-py.up.railway.app/`

## Running this API Locally
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
```
