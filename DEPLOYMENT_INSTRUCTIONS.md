# How to Manage Your Deployment

## Accessing the Application
- **Dashboard**: [http://localhost:5001](http://localhost:5001)
- **Health Check**: [http://localhost:5001/health](http://localhost:5001/health)

## Managing the Deployment
Run these commands in the project directory:

**Stop the Server**
```bash
docker-compose down
```

**Restart the Server**
```bash
docker-compose up -d
```

**View Logs**
```bash
docker-compose logs -f cyclekernel
```

## Environment Configuration
The `.env` file or `docker-compose.yml` controls the configuration:
- `CK_SEED`: Set an integer for reproducible runs.
- `CK_UNIVERSES`: Number of parallel universes (default: 2).
- `OPENAI_API_KEY`: Set your API key in the host environment or .env file.
