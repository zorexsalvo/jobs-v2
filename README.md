# PythonPH Jobs Board

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
make migrate        # Run migrations
make makemigrations # Create migrations
make static         # Collect static files
make clean          # Remove all containers and images
make twbuild        # Rebuild Tailwind CSS files
```

### Manual Setup

If you prefer to run without Docker:

#### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Node.js 18+ and npm (for Tailwind CSS)
- PostgreSQL 15+

#### Installation Steps

1. Clone the repository

```bash
git clone https://github.com/yourusername/jobs-v2.git
cd jobs-v2
```

2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
npm i -D daisyui@latest
```

4. Set up environment variables

Create a `.env` file in the project root:
```bash
DEBUG=1
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/jobs_v2
POSTGRES_DB=jobs_v2
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

5. Setup database and static files

```bash
python manage.py migrate
python manage.py tailwind install
python manage.py tailwind build
```

6. Run the development server

```bash
python manage.py runserver
```

7. Open your browser and navigate to `http://localhost:8000`

## 📦 Tech Stack

- Django 5.1.6
- Django REST Framework 3.15.2
- django-allauth 0.65.4
- Tailwind CSS with DaisyUI
- PostgreSQL 15
- Docker & Docker Compose

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

## ❓ FAQ

### Static files not loading properly?

There is a known issue with building static files during initial setup. If you encounter this issue:

1. Start the application normally:
```bash
make up
```

2. Then run the Tailwind build command:
```bash
make twbuild
```

This will rebuild the static files and resolve the styling issues.

### Database connection issues?

If you're having trouble connecting to the database:

1. Ensure PostgreSQL is running
2. Check your environment variables
3. Try resetting the database:
```bash
make down
docker volume rm jobs-v2_postgres_data
make up
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please make sure to follow the existing coding style.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

