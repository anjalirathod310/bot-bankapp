# bankapp using doker with a  simple ui
## 🎯 Objective
To develop a simple, web-based Bank Application that allows users to:

- Create accounts with an initial balance

- View account balance

- Perform deposits and withdrawals

- View full transaction history

All this is served using Flask, styled with HTML/CSS, and Dockerized to simulate a production environment.

## 🛠️ Tech Stack
1.Backend	Python + Flask

2.Frontend	HTML, CSS

3.Containerization	Docker

4.Template Engine	Jinja2 (Flask’s default)

5.Server Port	5000 (Docker exposed)

## 🧭 Steps Included
Built Flask App with basic routing and in-memory logic using Python dictionary.

1.Created simple UI pages using HTML + CSS with form interactions.

2.Added Flask Jinja templates for dynamic rendering of values like balance and transaction history.

3.Dockerized the app:

- Created a Dockerfile.

- Installed dependencies via requirements.txt.

4.Built and ran the image using Docker CLI.

5.Ran the app on localhost:5000 (or other available ports) using container networking.

## 💡 Key Insights
- Understood how Flask integrates with HTML templates and handles POST/GET requests.

- Learned how Docker encapsulates an entire application into a portable container image.

- Got familiar with port mapping and container lifecycle management.

- Practiced troubleshooting common issues like port conflicts and missing templates.

## 🔧 How to Run (Locally via Docker)
- Build the Docker image:
docker build -t bank-app .

- Run the container:
docker run -p 5000:5000 bank-app

- Open in browser:
http://localhost:5000



