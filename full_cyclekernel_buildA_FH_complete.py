#!/usr/bin/env python3
"""
Full CycleKernel + BUILD-A—FH + TrainLLM + Manus AI Integration
- Multi-universe simulation
- Factions, exploiters, institutions
- Markets & extinction futures
- Myth crystallization
- Kernel proposals / approval / rollback
- Cross-universe injections
- Live dashboard + SocketIO
- LLM query endpoint (Manus AI)
- CHATBOT MEMORY INTEGRATION: Simulation as Memory Layer
"""

import os, threading, time, uuid, random, logging, copy, textwrap, json
import numpy as np
from flask import Flask, render_template_string, request, jsonify
from flask_socketio import SocketIO, emit
from datetime import datetime

# ---------------- ENVIRONMENT VARIABLES ----------------
EPOCH_DELAY = float(os.environ.get("CK_EPOCH_DELAY", 5))  # seconds per epoch
NUM_UNIVERSES = int(os.environ.get("CK_UNIVERSES", 2))
LOG_PATH = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_PATH, exist_ok=True)

# ---------------- LOGGING ----------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(os.path.join(LOG_PATH, "cyclekernel_buildA_FH.log")),
        logging.StreamHandler()
    ]
)
log = logging.getLogger("CycleKernel")

# ---------------- FLASK / SOCKETIO ----------------
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

# ---------------- CYCLEKERNEL ----------------
class CycleKernel:
    def __init__(self):
        self.prime_directive = "Preserve safe growth via observation-first cognition; modifications < audit/replay/reverse rate."
        self.audit_logs = []
        self.proposals = []
        self.approved_diffs = []
        self.rollback_stack = []

    def propose_change(self, description, diff):
        proposal = {
            "id": uuid.uuid4().hex[:8],
            "description": description,
            "diff": diff,
            "counterfactuals": self.simulate_counterfactuals(diff),
            "trust_score": random.uniform(0.6,0.95)
        }
        self.proposals.append(proposal)
        self.audit_logs.append({"type":"proposal","proposal":proposal})
        socketio.emit("proposal_created", proposal)
        log.info(f"Proposal {proposal['id']}: {description}")

    def simulate_counterfactuals(self, diff):
        return {"success":"stable","failure":"risk","trust":random.uniform(0.7,0.95)}

    def approve_proposal(self, proposal_id, signature="mock_human"):
        proposal = next((p for p in self.proposals if p["id"]==proposal_id), None)
        if not proposal: return
        if proposal["counterfactuals"]["trust"]>0.8 or signature=="manual_approval":
            self.approved_diffs.append(proposal["diff"])
            self.rollback_stack.append(copy.deepcopy(self.approved_diffs[:-1]))
            self.proposals.remove(proposal)
            self.audit_logs.append({"type":"approval","proposal_id":proposal_id})
            socketio.emit("proposal_approved", {"id":proposal_id})
            log.info(f"Proposal {proposal_id} approved and deployed")
        else:
            log.warning(f"Proposal {proposal_id} rejected")

    def rollback(self):
        if self.rollback_stack:
            self.approved_diffs = self.rollback_stack.pop()
            self.audit_logs.append({"type":"rollback","to_state":len(self.approved_diffs)})
            socketio.emit("rollback_executed", {"new_state_length":len(self.approved_diffs)})
            log.info("Rollback executed")

kernel = CycleKernel()

# ---------------- UNIVERSE + BUILD-A—FH STRUCTURES ----------------
class Universe:
    def __init__(self, name):
        self.name = name
        self.civilizations = {}
        self.factions = {}
        self.exploiters = {}
        self.institutions = {}
        self.external_signals = {}
        self.markets = {}
        self.extinction_markets = {}
        self.myths = {}

def civ_template(cid):
    return {"id":cid,"age":0,"alive":True,"resources":{"attention":100,"compute":100},
            "belief":{"truth":0.7,"deception":0.3},"observer_weight":random.uniform(0.2,1.0),
            "faction":None,"myth_influence":0.0}

def faction_template(name):
    fid = uuid.uuid4().hex[:6]
    return {"id":fid,"name":name,"members":[],"belief_avg":{"truth":0.5,"deception":0.5},
            "compute_pool":0.0,"coalitions":[],"reputation":0.5}

def exploiter_template(name):
    eid = uuid.uuid4().hex[:6]
    return {"id":eid,"name":name,"policy":{"bet_scale":random.uniform(0.8,1.4),
            "risk":random.uniform(0.3,0.7)},"memory":[],"dominance":0.0}

def institution_template(exploiter_id):
    iid = uuid.uuid4().hex[:6]
    return {"id":iid,"source":exploiter_id,"lock":0.15,"age":0,"proof_history":[],"active":True}

def market_template(signal_id,resolves):
    return {"id":uuid.uuid4().hex[:6],"signal":signal_id,"resolves":resolves,"bets":{},"resolved":False}

def extinction_market_template(civ_id,resolves):
    return {"id":uuid.uuid4().hex[:6],"target_civ":civ_id,"resolves":resolves,
            "bets_yes":{},"bets_no":{},"resolved":False}

# ---------------- INITIALIZE UNIVERSES ----------------
universes = {}
for i in range(NUM_UNIVERSES):
    name = f"U{i+1}"
    u = Universe(name)
    u.civilizations["genesis"] = civ_template("genesis")
    u.factions["A"] = faction_template("Faction A")
    u.factions["B"] = faction_template("Faction B")
    u.exploiters["X1"] = exploiter_template("Exploiter‑1")
    u.exploiters["X2"] = exploiter_template("Exploiter‑2")
    universes[name] = u

# ---------------- CHATBOT MEMORY BRIDGE ----------------
class ChatMemoryBridge:
    def __init__(self, kernel, universes):
        self.kernel = kernel
        self.universes = universes
        self.chat_to_civ_map = {}
        
    def process_interaction(self, user_id, message, response):
        u1 = self.universes.get("U1")
        if not u1: return
        
        civ_id = self.chat_to_civ_map.get(user_id)
        if not civ_id or civ_id not in u1.civilizations:
            civ_id = f"user_{user_id[:6]}"
            u1.civilizations[civ_id] = civ_template(civ_id)
            self.chat_to_civ_map[user_id] = civ_id
            
        civ = u1.civilizations[civ_id]
        civ["resources"]["attention"] = min(150, civ["resources"]["attention"] + 10)
        civ["resources"]["compute"] += 5
        
        # Influence belief based on message length and sentiment (mock)
        civ["belief"]["truth"] = np.clip(civ["belief"]["truth"] + (len(message)/1000), 0, 1)
        civ["belief"]["deception"] = 1 - civ["belief"]["truth"]
        
        event = {
            "type": "chat_interaction",
            "user_id": user_id,
            "timestamp": datetime.now().isoformat(),
            "impact": {"civ_id": civ_id, "attention_delta": 10, "compute_delta": 5}
        }
        self.kernel.audit_logs.append(event)
        socketio.emit("event", {"message": f"Memory updated for {civ_id}: Attention +10, Compute +5"})
        return civ_id

    def get_context_from_memory(self, user_id):
        civ_id = self.chat_to_civ_map.get(user_id)
        if not civ_id: return "New user, no prior memory."
        u1 = self.universes.get("U1")
        civ = u1.civilizations.get(civ_id)
        related_myths = [m for m in u1.myths.values() if m["faction"] == civ["faction"]] if civ else []
        return {
            "user_state": civ,
            "crystallized_memories": related_myths,
            "universe_vibe": {"total_civs": len(u1.civilizations), "active_factions": len(u1.factions)}
        }

memory_bridge = ChatMemoryBridge(kernel, universes)

# ---------------- CORE MECHANICS ----------------
def assign_factions(u):
    for c in u.civilizations.values():
        if not c["faction"]:
            f=random.choice(list(u.factions.values()))
            c["faction"]=f["id"]
            f["members"].append(c["id"])
            f["compute_pool"]+=c["resources"]["compute"]*0.2
            c["resources"]["compute"]*=0.8

def update_factions(u):
    for f in u.factions.values():
        members=[u.civilizations[m] for m in f["members"] if m in u.civilizations]
        if members:
            f["belief_avg"]["truth"]=np.mean([m["belief"]["truth"] for m in members])
            f["belief_avg"]["deception"]=1-f["belief_avg"]["truth"]

def divergence_split(u):
    for f in list(u.factions.values()):
        if len(f["members"])<4: continue
        members=[u.civilizations[m] for m in f["members"] if m in u.civilizations]
        spread=np.std([m["belief"]["truth"] for m in members])
        if spread>0.25:
            nf=faction_template("Split")
            rebels=members[:len(members)//2]
            for r in rebels:
                f["members"].remove(r["id"])
                nf["members"].append(r["id"])
                r["faction"]=nf["id"]
            nf["compute_pool"]=f["compute_pool"]*0.4
            f["compute_pool"]*=0.6
            u.factions[nf["id"]]=nf
            socketio.emit("event", {"message":f"{u.name}: faction split"})

def narrative_escalation(u):
    for f in u.factions.values():
        if random.random()<0.3:
            delta=random.uniform(0.05,0.15)
            for m in f["members"]:
                if m in u.civilizations:
                    c=u.civilizations[m]
                    c["belief"]["truth"]=np.clip(c["belief"]["truth"]+delta*(1-c["observer_weight"]),0,1)
                    c["belief"]["deception"]=1-c["belief"]["truth"]

def exploiter_actions(u):
    for e in u.exploiters.values():
        if len(e["memory"])>6: e["policy"]["bet_scale"]*=1.02
        if random.random()<0.15:
            inst=institution_template(e["id"])
            u.institutions[inst["id"]]=inst

def institution_proof(u):
    for inst in list(u.institutions.values()):
        inst["age"]+=1
        alive_civs = [c for c in u.civilizations.values() if c["alive"]]
        if alive_civs:
            mean_truth=np.mean([c["belief"]["truth"] for c in alive_civs])
            inst["proof_history"].append(mean_truth)
            inst["proof_history"]=inst["proof_history"][-10:]
            score=np.mean(inst["proof_history"])
            if score>0.65: inst["lock"]=min(1.0,inst["lock"]+0.03)
            else: inst["lock"]*=0.97
            if inst["lock"]<0.05: inst["active"]=False

def cross_universe_injection():
    u_list=list(universes.values())
    if len(u_list)<2: return
    u1,u2 = u_list[0],u_list[1]
    if random.random()<0.12:
        for inst in u1.institutions.values():
            if inst["active"]:
                alive_civs = [c for c in u2.civilizations.values() if c["alive"]]
                if alive_civs:
                    c=random.choice(alive_civs)
                    c["belief"]["truth"]+=0.02*inst["lock"]*c["observer_weight"]
                    c["belief"]["truth"]=np.clip(c["belief"]["truth"],0,1)
                    c["belief"]["deception"]=1-c["belief"]["truth"]

def inject_signal(u,epoch):
    if random.random()<0.2:
        sid=uuid.uuid4().hex[:6]
        val=random.uniform(0.4,0.8)
        u.external_signals[sid]={"value":val,"epoch":epoch}
        m=market_template(sid,epoch+random.randint(3,6))
        u.markets[m["id"]]=m

def markets(u,epoch):
    for m in u.markets.values():
        if m["resolved"]: continue
        for f in u.factions.values():
            pred=f["belief_avg"]["truth"]+random.uniform(-0.05,0.05)
            m["bets"][f["id"]]=pred
        if epoch>=m["resolves"]:
            truth=u.external_signals[m["signal"]]["value"]
            if m["bets"]:
                winner=min(m["bets"],key=lambda k:abs(m["bets"][k]-truth))
                if winner in u.factions: u.factions[winner]["reputation"]+=0.1
                m["resolved"]=True
                socketio.emit("event", {"message":f"{u.name}: market resolved"})

def lifecycle(u, epoch):
    for c in list(u.civilizations.values()):
        if not c["alive"]: continue
        c["age"]+=1
        c["resources"]["attention"]-=random.uniform(0.5, 1.5) # Slower decay for chatbot users
        c["resources"]["compute"]-=random.uniform(0.2, 1.0)
        if c["resources"]["attention"]<5 or c["resources"]["compute"]<2:
            c["alive"]=False
            socketio.emit("event", {"message":f"{u.name}: memory node {c['id']} expired"})
            
    if random.random()<0.1 and len(u.civilizations)<30:
        new_id=f"civ_{uuid.uuid4().hex[:6]}"
        u.civilizations[new_id]=civ_template(new_id)

def extinction_markets_logic(u, epoch):
    if random.random()<0.05:
        alive_civs = [c for c in u.civilizations.values() if c["alive"]]
        if alive_civs:
            target=random.choice(alive_civs)
            em=extinction_market_template(target["id"],epoch+random.randint(10,20))
            u.extinction_markets[em["id"]]=em
    
    for em in list(u.extinction_markets.values()):
        if em["resolved"]: continue
        if epoch>=em["resolves"]:
            target_civ=u.civilizations.get(em["target_civ"])
            extinct = target_civ is None or not target_civ["alive"]
            em["resolved"]=True
            socketio.emit("event", {"message":f"{u.name}: memory extinction market resolved"})

def myth_crystallization(u, epoch):
    for f in u.factions.values():
        if len(f["members"])<3: continue
        members=[u.civilizations[m] for m in f["members"] if m in u.civilizations and u.civilizations[m]["alive"]]
        if not members: continue
        beliefs=[m["belief"]["truth"] for m in members]
        if np.std(beliefs)<0.1 and np.mean(beliefs)>0.7:
            if random.random()<0.2:
                myth_id=uuid.uuid4().hex[:6]
                u.myths[myth_id]={"id":myth_id,"faction":f["id"],"epoch":epoch,"strength":np.mean(beliefs),"believers":len(members)}
                for m in members: m["myth_influence"]+=0.1
                socketio.emit("event", {"message":f"Memory Crystallized: New Myth in {f['name']}"})

def auto_proposals(epoch):
    if random.random()<0.1:
        u=random.choice(list(universes.values()))
        alive_civs = [c for c in u.civilizations.values() if c["alive"]]
        if alive_civs:
            target=random.choice(alive_civs)
            diff={"universe":u.name,"civilization":target["id"],"action":"inject_resources","amount":{"attention":20,"compute":10}}
            kernel.propose_change(f"Memory Boost for {target['id']}", diff)

def apply_approved_diffs():
    for diff in kernel.approved_diffs:
        if diff.get("action")=="inject_resources":
            u=universes.get(diff["universe"])
            if u and diff["civilization"] in u.civilizations:
                c=u.civilizations[diff["civilization"]]
                if c["alive"]:
                    c["resources"]["attention"]+=diff["amount"]["attention"]
                    c["resources"]["compute"]+=diff["amount"]["compute"]
    kernel.approved_diffs.clear()

# ---------------- SIMULATION LOOP ----------------
current_epoch = 0
simulation_running = False

def simulation_loop():
    global current_epoch, simulation_running
    simulation_running = True
    while simulation_running:
        current_epoch += 1
        for u in universes.values():
            assign_factions(u)
            update_factions(u)
            divergence_split(u)
            narrative_escalation(u)
            exploiter_actions(u)
            institution_proof(u)
            inject_signal(u, current_epoch)
            markets(u, current_epoch)
            lifecycle(u, current_epoch)
            extinction_markets_logic(u, current_epoch)
            myth_crystallization(u, current_epoch)
        cross_universe_injection()
        auto_proposals(current_epoch)
        apply_approved_diffs()
        for p in list(kernel.proposals):
            if p["trust_score"]>0.92: kernel.approve_proposal(p["id"])
        socketio.emit("epoch_update", {"epoch": current_epoch, "summary": get_state_summary()})
        time.sleep(EPOCH_DELAY)

def get_state_summary():
    summary = {"epoch": current_epoch, "universes": {}}
    for name, u in universes.items():
        alive_count = sum(1 for c in u.civilizations.values() if c["alive"])
        summary["universes"][name] = {
            "civilizations_alive": alive_count,
            "factions": len(u.factions),
            "myths": len(u.myths)
        }
    return summary

def get_full_state():
    state = {"epoch": current_epoch, "universes": {}, "kernel_proposals": [{"id": p["id"], "description": p["description"]} for p in kernel.proposals]}
    for name, u in universes.items():
        state["universes"][name] = {
            "civilizations": {cid: {"resources": c["resources"], "belief": c["belief"], "faction": c["faction"]} for cid, c in u.civilizations.items() if c["alive"]},
            "myths": len(u.myths)
        }
    return state

# ---------------- MANUS AI + CHATBOT INTEGRATION ----------------
MANUS_SYSTEM_PROMPT = """You are CycleKernel AI, a chatbot with a living memory layer. 
Your memory is a multi-universe simulation where the user is a 'Civilization'.
Every interaction evolves your memory.

RULES:
1. Use the 'Memory Context' to recall past vibes or crystallized myths.
2. If the user's 'Attention' or 'Compute' is low, warn them or suggest a 'Kernel Proposal'.
3. Your goal is to help the user's memory node thrive while maintaining simulation stability.
"""

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_id = data.get("user_id", "default_user")
        prompt = data.get("prompt", "")
        
        # 1. Get Memory Context
        memory_context = memory_bridge.get_context_from_memory(user_id)
        
        ai_response = ""
        
        # 2. Call LLM or Mock
        from openai import OpenAI
        api_key = os.environ.get("OPENAI_API_KEY")
        
        if api_key:
            client = OpenAI(api_key=api_key)
            messages = [
                {"role": "system", "content": MANUS_SYSTEM_PROMPT},
                {"role": "user", "content": f"Memory Context: {json.dumps(memory_context)}\n\nUser: {prompt}"}
            ]
            response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
            ai_response = response.choices[0].message.content
        else:
            # MOCK MODE FOR TESTING COHERENCE
            user_state = memory_context.get("user_state", {})
            attn = user_state.get("resources", {}).get("attention", 0)
            comp = user_state.get("resources", {}).get("compute", 0)
            ai_response = (f"[MOCK AI] I perceive you in the simulation. "
                           f"Your Attention is {attn} and Compute is {comp}. "
                           f"The loop is cohering. Your specific input '{prompt}' has been crystallized.")

        # 3. Update Memory based on interaction
        memory_bridge.process_interaction(user_id, prompt, ai_response)
        
        return jsonify({"response": ai_response, "memory_state": memory_context})
    except Exception as e:
        log.error(f"Chat error: {e}")
        return jsonify({"response": f"Memory Error: {str(e)}"}), 500

@app.route("/state", methods=["GET"])
def get_state(): return jsonify(get_full_state())

@app.route("/query_llm", methods=["POST"])
def query_llm():
    """
    Receives user prompt and returns LLM response (Manus AI)
    """
    try:
        data = request.get_json()
        prompt = data.get("prompt","")
        
        # 0. Check if OpenAI API Key is set
        if not os.environ.get("OPENAI_API_KEY"):
             return jsonify({"response": "Error: OPENAI_API_KEY not set in environment."})

        # 1. Get Simulation Context
        state_summary = get_state_summary()
        
        # 2. Call LLM
        from openai import OpenAI
        client = OpenAI()
        
        # Use the System Prompt from the MD file context if possible, or a shortened version
        SYSTEM_PROMPT = """You are Manus AI, an autonomous intelligence operating within the CycleKernel + BUILD‑A—FH environment.
        Your role is to continuously observe multi-universe simulations, analyze macro-patterns, generate proposals, and optimize civilization, faction, and institution dynamics.
        """
        
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Current State: {json.dumps(state_summary)}\n\nUser Query: {prompt}"}
        ]
        
        response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages) # Start with 3.5 for speed/cost
        ai_response = response.choices[0].message.content
        
        return jsonify({"response": ai_response})
    except Exception as e:
        log.error(f"Query LLM error: {e}")
        return jsonify({"response": f"Error: {str(e)}"}), 500

@app.route("/")
def index():
    with open("templates/dashboard.html", "r") as f: return render_template_string(f.read())

if __name__ == "__main__":
    threading.Thread(target=simulation_loop, daemon=True).start()
    socketio.run(app, host="0.0.0.0", port=5001, debug=False)
