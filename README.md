# Python.PH Jobs Board

A job board platform for Python developers in the Philippines.

## Development Setup

### Using Docker (Recommended)

1. Clone the repository
```bash
git clone <repository-url>
cd <project-directory>
```

2. Build and run with Docker Compose
```bash
docker-compose up --build
```

The site will be available at `http://localhost:8000`

### Manual Setup

1. Clone the repository
```bash
git clone <repository-url>
cd <project-directory>
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies
```bash
# For development (includes all dependencies)
pip install -r requirements.txt

# For production (only production dependencies)
pip install -r requirements.txt --no-deps
```

4. Run migrations
```bash
python manage.py migrate
```

5. Install and build Tailwind CSS
```bash
python manage.py tailwind install
python manage.py tailwind build
```

## Project Dependencies

The project uses separate requirements files for production and development:

- `requirements.txt`: Contains production dependencies
- `requirements-dev.txt`: Contains development and testing dependencies

### Production Dependencies
- Django>=5.0.0
- django-tailwind>=3.8.0

### Development Dependencies
- Faker>=22.0.0

## Development

### Populating Sample Data

The project includes a management command to populate the database with sample job listings using Faker:

```bash
# Create default 20 jobs
python manage.py populate_jobs

# Or specify a custom number of jobs
python manage.py populate_jobs --count 50
```

The command will generate realistic job listings with:
- Tech job titles with seniority levels
- Company names
- Locations in major Philippine cities
- Salary ranges in PHP
- Detailed job descriptions
- Remote work status

### Running the Development Server

```bash
# Using Docker
docker-compose up

# Manual
python manage.py runserver
```

### Docker Commands

```bash
# Build and start services
docker-compose up --build

# Start services in background
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f

# Run commands in container
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py populate_jobs
```

## Features

- Job listings with detailed information
- Tailwind CSS with DaisyUI for styling
- Responsive design
- Sample data generation
- Docker support for easy development and deployment
- Separate production and development dependencies

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

[Add your license information here]

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

