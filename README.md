# CycleKernel + BUILD-A-FH + TrainLLM + Manus AI Integration

A comprehensive multi-universe simulation system with autonomous AI governance, featuring civilizations, factions, exploiters, institutions, markets, and myth crystallization.

## 🌟 Features

### Core Simulation
- **Multi-Universe Architecture**: Parallel universes with independent civilizations
- **Civilizations**: Dynamic entities with resources (attention, compute), beliefs (truth/deception), and lifecycle management
- **Factions**: Groups of civilizations with shared beliefs, compute pools, and reputation systems
- **Exploiters**: Strategic actors that create institutions and participate in markets
- **Institutions**: Proof-of-work systems with lock mechanisms and active/inactive states
- **Markets**: Prediction markets for external signals and extinction events
- **Myths**: Crystallized belief systems that emerge from faction consensus

### CycleKernel Governance
- **Proposal System**: Automated proposal generation with counterfactual simulation
- **Approval Mechanism**: Trust-based approval with human-in-the-loop capability
- **Rollback System**: Full audit trail with state rollback functionality
- **Prime Directive**: "Preserve safe growth via observation-first cognition"

### Manus AI Integration
- **Real-time Analysis**: Continuous observation of macro-patterns across universes
- **LLM-Powered Insights**: OpenAI GPT-4 integration for intelligent analysis
- **Proposal Generation**: AI-driven suggestions for system optimization
- **Interactive Queries**: Natural language interface for simulation exploration

### Live Dashboard
- **Real-time Updates**: WebSocket-based live event streaming
- **Universe Statistics**: Comprehensive metrics for all universes
- **Event Log**: Chronological tracking of all simulation events
- **AI Chat Interface**: Direct interaction with Manus AI

## 📋 Prerequisites

- **Docker** and **Docker Compose** (recommended)
- **Python 3.11+** (for local development)
- **OpenAI API Key** (for Manus AI functionality)

## 🚀 Quick Start

### Option 1: Docker Deployment (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/doitupsolutions810-crow/TrainLLM.git
   cd TrainLLM
   ```

2. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   nano .env
   ```

3. **Build and run**
   ```bash
   docker-compose up --build
   ```

4. **Access the dashboard**
   Open your browser to: http://localhost:5000

### Option 2: Local Python Development

1. **Clone and setup**
   ```bash
   git clone https://github.com/doitupsolutions810-crow/TrainLLM.git
   cd TrainLLM
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**
   ```bash
   export CK_EPOCH_DELAY=5
   export CK_UNIVERSES=2
   export OPENAI_API_KEY="your_api_key_here"
   ```

4. **Run the simulation**
   ```bash
   python full_cyclekernel_buildA_FH_complete.py
   ```

5. **Access the dashboard**
   Open your browser to: http://localhost:5000

## ⚙️ Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `CK_EPOCH_DELAY` | 5 | Seconds per simulation epoch |
| `CK_UNIVERSES` | 2 | Number of parallel universes |
| `OPENAI_API_KEY` | - | OpenAI API key for Manus AI |

### Docker Compose Configuration

Edit `docker-compose.yml` to customize:
- Port mappings
- Volume mounts
- Resource limits
- Restart policies

## 📊 System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      CycleKernel                            │
│  (Proposals, Approvals, Rollbacks, Audit Logs)             │
└─────────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
   ┌────▼────┐        ┌────▼────┐        ┌────▼────┐
   │ Universe│        │ Universe│        │ Universe│
   │    1    │◄──────►│    2    │◄──────►│   ...   │
   └─────────┘        └─────────┘        └─────────┘
        │                   │                   │
   ┌────▼────────────────────▼───────────────────▼────┐
   │  • Civilizations (resources, beliefs, lifecycle)  │
   │  • Factions (members, compute pools, reputation)  │
   │  • Exploiters (policies, memory, dominance)       │
   │  • Institutions (lock, proof history, active)     │
   │  • Markets (signals, bets, resolution)            │
   │  • Myths (strength, believers, influence)         │
   └───────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
   ┌────▼────┐        ┌────▼────┐        ┌────▼────┐
   │  Flask  │        │SocketIO │        │ Manus AI│
   │   API   │        │Dashboard│        │   LLM   │
   └─────────┘        └─────────┘        └─────────┘
```

## 🔌 API Endpoints

### REST API

- `GET /` - Dashboard web interface
- `GET /state` - Get complete simulation state (JSON)
- `GET /proposals` - Get current kernel proposals
- `POST /approve/<proposal_id>` - Manually approve a proposal
- `POST /rollback` - Trigger kernel rollback
- `POST /query_llm` - Query Manus AI with JSON body: `{"prompt": "your question"}`

### WebSocket Events

**Client → Server:**
- `connect` - Establish connection
- `disconnect` - Close connection

**Server → Client:**
- `connected` - Connection established with current epoch
- `epoch_update` - New epoch with state summary
- `event` - General simulation event
- `proposal_created` - New kernel proposal
- `proposal_approved` - Proposal approved
- `rollback_executed` - Rollback completed

## 🧪 Example Queries for Manus AI

Try these queries in the dashboard chat interface:

1. **State Analysis**
   - "What are the current macro-patterns across universes?"
   - "Which civilizations are at risk of extinction?"
   - "Analyze the belief distribution in Universe 1"

2. **Proposal Requests**
   - "Suggest a resource injection to stabilize Universe 2"
   - "What interventions could increase faction diversity?"
   - "Propose a cross-universe injection strategy"

3. **Market Analysis**
   - "Which exploiters are dominating the extinction markets?"
   - "Analyze the accuracy of faction predictions"
   - "What myths have the strongest influence?"

## 📈 Monitoring and Logs

### Log Files

Logs are stored in `./logs/cyclekernel_buildA_FH.log` with:
- Timestamp
- Log level (INFO, WARNING, ERROR)
- Event description

### Dashboard Metrics

The dashboard displays:
- **Epoch Counter**: Current simulation epoch
- **Universe Statistics**: Per-universe metrics
  - Civilizations alive/total
  - Active factions
  - Active institutions
  - Active markets
  - Crystallized myths
- **Kernel Status**: Proposals, approvals, audit logs
- **Event Log**: Real-time event stream

## 🛠️ Development

### Project Structure

```
CycleKernel-BuildA-FH/
├── full_cyclekernel_buildA_FH_complete.py  # Main simulation
├── templates/
│   └── dashboard.html                       # Web dashboard
├── logs/                                    # Log files
├── Dockerfile                               # Container definition
├── docker-compose.yml                       # Orchestration
├── requirements.txt                         # Python dependencies
├── .env.example                             # Environment template
├── .gitignore                               # Git ignore rules
└── README.md                                # This file
```

### Adding New Features

1. **New Mechanics**: Add functions in the "CORE MECHANICS" section
2. **New Entities**: Create templates and update Universe class
3. **New API Endpoints**: Add routes in the Flask section
4. **New Dashboard Features**: Edit `templates/dashboard.html`

### Testing

```bash
# Run with verbose logging
export LOG_LEVEL=DEBUG
python full_cyclekernel_buildA_FH_complete.py

# Test API endpoints
curl http://localhost:5000/state
curl http://localhost:5000/proposals
curl -X POST http://localhost:5000/query_llm \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Analyze current state"}'
```

## 🐛 Troubleshooting

### Common Issues

**Dashboard not loading:**
- Check that port 5000 is not in use: `lsof -i :5000`
- Verify Flask is running: check logs for "Starting CycleKernel dashboard"

**Manus AI not responding:**
- Verify OpenAI API key is set: `echo $OPENAI_API_KEY`
- Check API key validity at https://platform.openai.com/api-keys
- Review logs for API errors

**Docker build fails:**
- Ensure Docker daemon is running: `docker info`
- Check disk space: `df -h`
- Try rebuilding without cache: `docker-compose build --no-cache`

**Simulation running too fast/slow:**
- Adjust `CK_EPOCH_DELAY` environment variable
- Default is 5 seconds per epoch

## 📚 Theoretical Background

### CycleKernel Philosophy

The CycleKernel implements a **safe-by-design** governance model:
- **Observation-First**: Changes are proposed, not executed immediately
- **Counterfactual Reasoning**: Every proposal includes "what-if" analysis
- **Audit Trail**: Complete history enables rollback and analysis
- **Trust Scoring**: Proposals are evaluated for safety before approval

### BUILD-A-FH Framework

**BUILD-A-FH** (Build-Up Institutional Learning Dynamics - Attention-Faction Hypothesis):
- **Attention Economy**: Civilizations compete for limited attention resources
- **Faction Dynamics**: Belief-based grouping with emergent properties
- **Institutional Lock**: Proof-of-work systems that stabilize or destabilize
- **Myth Crystallization**: Consensus beliefs that shape civilization behavior

### Multi-Universe Design

Parallel universes enable:
- **Comparative Analysis**: Cross-universe pattern detection
- **Controlled Experiments**: Isolated interventions
- **Injection Mechanics**: Knowledge transfer between universes
- **Diversity Preservation**: Multiple evolutionary paths

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

1. **New Mechanics**: Additional simulation dynamics
2. **Visualization**: Enhanced dashboard graphics
3. **AI Models**: Alternative LLM integrations
4. **Performance**: Optimization for larger scales
5. **Testing**: Unit and integration tests

## 📄 License

This project is provided as-is for research and educational purposes.

## 🔗 Links

- **GitHub Repository**: https://github.com/doitupsolutions810-crow/TrainLLM
- **OpenAI API**: https://platform.openai.com/docs
- **Flask Documentation**: https://flask.palletsprojects.com/
- **Socket.IO**: https://socket.io/docs/

## 📞 Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Review the troubleshooting section
- Check logs for detailed error messages

---

**Built with CycleKernel governance principles: Observe, Propose, Audit, Rollback.**
