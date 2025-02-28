# Jobs V2

A job platform built with Django, Django REST Framework, and Tailwind CSS.

### Prerequisites

- Python 3.x
- pip (Python package manager)
- Node.js and npm (for Tailwind CSS)

## 🛠️ Project Structure

jobs_v2/
├── jobs/ # Job listings and management
├── users/ # User authentication and profiles


## 🌟 Features

- User authentication with Django AllAuth
- Job listings and management
- User profiles and settings
- Search and filtering
- Responsive design with Tailwind CSS


## 📦 Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/jobs-v2.git
cd jobs-v2
```

2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
npm i -D daisyui@latest
```

4. Build Tailwind CSS

```bash
python manage.py tailwind build
```

5. Run the development server

```bash
python manage.py runserver
```

6. Open your browser and navigate to `http://localhost:8000`

