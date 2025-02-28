# Jobs V2

A job platform built with Django, Django REST Framework, and Tailwind CSS.

## 🚀 Getting Started

You can run this application either with Docker (recommended) or manually.

### Docker Setup (Recommended)

1. Make sure you have Docker and Make installed
2. Run the following commands:

```bash
# Build and start the application
make build
make up

# Or start in detached mode
make up-d
```

The application will be available at `http://localhost:8000`

### Development Commands

We provide a Makefile with common commands for development:

```bash
# View all available commands
make help

# Common commands:
make build          # Build Docker images
make up             # Start the application
make up-d           # Start in detached mode
make down           # Stop the application
make logs           # View logs
make shell          # Access container shell
make django-shell   # Access Django shell
make test           # Run tests
make migrate        # Run migrations
make makemigrations # Create migrations
make static         # Collect static files
make clean          # Remove all containers and images
```

### Manual Setup

If you prefer to run without Docker:

#### Prerequisites

- Python 3.x
- pip (Python package manager)
- Node.js and npm (for Tailwind CSS)

#### Installation Steps

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

## 🛠️ Project Structure

jobs_v2/
├── jobs/ # Job listings and management
├── users/ # User authentication and profiles
├── Dockerfile          # Docker configuration
├── docker-compose.yml  # Docker services configuration
├── Makefile           # Development commands
└── requirements.txt    # Python dependencies

## 🌟 Features

- User authentication with Django AllAuth
- Job listings and management
- User profiles and settings
- Search and filtering
- Responsive design with Tailwind CSS
- Containerized development environment with Docker
- PostgreSQL database support

## 🐳 Docker Configuration

The application uses Docker for development and includes:

- **Web Application**: Django application with hot-reloading
- **Database**: PostgreSQL instance
- **Volumes**: Persistent storage and development file mounting
- **Environment**: Combined Python/Node.js environment

### Environment Variables

The following environment variables are configured in `docker-compose.yml`:

```yaml
DEBUG=1
DATABASE_URL=postgresql://postgres:postgres@db:5432/jobs_v2
POSTGRES_DB=jobs_v2
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

You can override these by creating a `.env` file in the project root.

## 📝 Development Notes

- The Docker setup includes hot-reloading, so changes to your code will be reflected immediately
- Database data persists between container restarts via Docker volumes
- Use `make logs` to view application logs in real-time
- Access the Django shell with `make django-shell` for debugging
- Run tests with `make test`

