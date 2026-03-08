AWS Deployment Setup – CogniviseAI

This document explains how CogniviseAI is deployed and executed using AWS EC2.

⸻

1. Launch EC2 Instance
	1.	Login to AWS Console
	2.	Navigate to EC2 → Instances
	3.	Click Launch Instance

Configuration used:
	•	Name: cognivise-backend
	•	AMI: Ubuntu Server 22.04 LTS
	•	Instance type: t2.micro
	•	Key pair: cognivise-key.pem
	•	Security Group:
	•	Allow SSH (Port 22)
	•	Allow HTTP (Port 80)
	•	Allow Custom TCP (Port 8000)

⸻

2. Connect to EC2 Instance

Use SSH from the terminal:
ssh -i cognivise-key.pem ubuntu@YOUR_ELASTIC_IP


⸻

3. Install Required Software

Update the server:
sudo apt update

⸻

4. Clone the Project Repository

Clone the GitHub project

⸻

5. Install Backend Dependencies

Install required Python packages:
pip install -r requirements.txt

⸻

6. Run the Backend Server

Start the FastAPI server:
uvicorn backend.main:app --host 0.0.0.0 --port 8000

⸻

7. Access API Documentation

FastAPI provides automatic API documentation.

Open in browser:
http://YOUR_ELASTIC_IP:8000/docs

⸻

8. Deployment Architecture

User Browser
↓
Frontend Interface
↓
AWS EC2 Instance
↓
FastAPI Backend
↓
AI Engine (Confusion Analysis)

⸻

Notes
	•	Ensure port 8000 is open in EC2 security group
	•	Elastic IP keeps the server address constant
	•	Backend must run with host 0.0.0.0 for external access
:::

⸻
