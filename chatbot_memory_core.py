#!/usr/bin/env python3
"""
CycleKernel Chatbot Memory Core
- Maps chat interactions to simulation events
- Uses Universe/Civilization state as LLM context
- Implements 'Memory Crystallization' via Myths
"""

import os, json, uuid, logging
from datetime import datetime

class ChatMemoryBridge:
    def __init__(self, kernel, universes):
        self.kernel = kernel
        self.universes = universes
        self.chat_to_civ_map = {} # Maps user_id to a civilization_id
        
    def process_interaction(self, user_id, message, response):
        """
        Converts a chat interaction into simulation events
        """
        # 1. Ensure user has a civilization in U1 (the 'Primary Memory Universe')
        u1 = self.universes.get("U1")
        if not u1: return
        
        civ_id = self.chat_to_civ_map.get(user_id)
        if not civ_id or civ_id not in u1.civilizations:
            civ_id = f"user_{user_id[:6]}"
            from full_cyclekernel_buildA_FH_complete import civ_template
            u1.civilizations[civ_id] = civ_template(civ_id)
            self.chat_to_civ_map[user_id] = civ_id
            
        civ = u1.civilizations[civ_id]
        
        # 2. Interaction consumes 'Attention' but can increase 'Compute' (knowledge)
        civ["resources"]["attention"] = min(100, civ["resources"]["attention"] + 5)
        civ["resources"]["compute"] += 2
        
        # 3. Message content influences 'Belief'
        # Simple heuristic: longer messages = more 'truth' (effort), 
        # but we can use LLM to analyze sentiment/truth later
        if len(message) > 50:
            civ["belief"]["truth"] = min(1.0, civ["belief"]["truth"] + 0.01)
        
        # 4. Log the interaction as a 'Memory Event' in the Kernel
        event = {
            "type": "chat_interaction",
            "user_id": user_id,
            "timestamp": datetime.now().isoformat(),
            "impact": {
                "civ_id": civ_id,
                "attention_delta": 5,
                "compute_delta": 2
            }
        }
        self.kernel.audit_logs.append(event)
        
        return civ_id

    def get_context_from_memory(self, user_id):
        """
        Retrieves simulation state to use as LLM context
        """
        civ_id = self.chat_to_civ_map.get(user_id)
        if not civ_id:
            return "No prior memory found."
            
        u1 = self.universes.get("U1")
        civ = u1.civilizations.get(civ_id)
        
        # Find myths (crystallized memories) related to the user's faction
        related_myths = []
        if civ and civ["faction"]:
            related_myths = [m for m in u1.myths.values() if m["faction"] == civ["faction"]]
            
        context = {
            "user_state": civ,
            "crystallized_memories": related_myths,
            "universe_vibe": {
                "total_civs": len(u1.civilizations),
                "active_factions": len(u1.factions)
            }
        }
        return context

# This will be integrated into the main app
