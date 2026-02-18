"""
Compound Self-Model Configuration (Template)

Generic observation contexts for any software project.
Customize these to match your project's domain and priorities.

This file is loaded by compound.py from the Clarity API repo.
Point compound.py here with: --config-dir ./scripts
Or set: COMPOUND_CONFIG_DIR=./scripts
"""

import json
from pathlib import Path

# ---------------------------------------------------------------------------
# 9 Observation Contexts across 5 Pillars
#
# These are generic software project health dimensions.
# Customize the descriptions and possible_states for your domain.
# ---------------------------------------------------------------------------

OBSERVATION_CONTEXTS = {
    "architecture_quality": {
        "domain": "technical_health",
        "description": "Codebase health, pattern consistency, tech debt level",
        "possible_states": ["fragile", "functional", "clean", "elegant"],
    },
    "test_coverage": {
        "domain": "technical_health",
        "description": "Test infrastructure maturity and coverage",
        "possible_states": ["manual", "automated", "gated", "predictive"],
    },
    "technical_debt": {
        "domain": "technical_health",
        "description": "Accumulated shortcuts, workarounds, and deferred cleanup",
        "possible_states": ["overwhelming", "managed", "minimal", "zero"],
    },
    "feature_completeness": {
        "domain": "product_health",
        "description": "How complete the product is relative to target scope",
        "possible_states": ["mvp", "partial", "functional", "complete"],
    },
    "user_experience": {
        "domain": "product_health",
        "description": "Quality of the end-user experience",
        "possible_states": ["broken", "usable", "polished", "delightful"],
    },
    "developer_velocity": {
        "domain": "process_health",
        "description": "Speed and ease of shipping changes",
        "possible_states": ["blocked", "slow", "steady", "fast"],
    },
    "knowledge_distribution": {
        "domain": "team_health",
        "description": "How well knowledge is shared across the team",
        "possible_states": ["siloed", "documented", "shared", "redundant"],
    },
    "customer_alignment": {
        "domain": "business_health",
        "description": "How well the product serves actual customer needs",
        "possible_states": ["assumed", "observed", "validated", "predictive"],
    },
    "documentation_quality": {
        "domain": "team_health",
        "description": "Quality and completeness of project documentation",
        "possible_states": ["absent", "sparse", "adequate", "comprehensive"],
    },
}


# ---------------------------------------------------------------------------
# Sprint -> Observation Context Mapping
#
# Map your PRs/sprints to observation contexts.
# This tells compound.py which context each PR advanced.
#
# Example (uncomment and customize):
# ---------------------------------------------------------------------------

SPRINT_CONTEXT_MAP = {
    # 0: {
    #     "primary": "architecture_quality",
    #     "secondary": ["test_coverage"],
    #     "transition": ("fragile", "functional"),
    #     "title": "Initial Architecture Setup",
    #     "pr": 1,
    # },
}


# ---------------------------------------------------------------------------
# CLEAR Mode Definitions
# ---------------------------------------------------------------------------

CLEAR_MODES = {
    "create": {
        "name": "Create",
        "description": "Synthesizing, designing, writing new code/docs",
    },
    "learn": {
        "name": "Learn",
        "description": "Understanding existing code, reading docs, studying needs",
    },
    "explore": {
        "name": "Explore",
        "description": "Discovering gaps, trying approaches, debugging",
    },
    "act": {
        "name": "Act",
        "description": "Executing plans, making commits, running tests",
    },
    "recover": {
        "name": "Recover",
        "description": "Reflecting on quality, consolidating learnings",
    },
}


# ---------------------------------------------------------------------------
# View Definitions
# ---------------------------------------------------------------------------

VIEW_DEFINITIONS = {
    "being": {
        "name": "Being",
        "description": "Current project state - observation context set-points",
        "role": "being",
    },
    "becoming": {
        "name": "Becoming",
        "description": "Trajectory across PRs - set-point changes over time",
        "role": "becoming",
        "horizon_days": 90,
    },
    "telos": {
        "name": "Telos",
        "description": "Target state - where the project is headed",
        "role": "telos",
    },
    "archetype": {
        "name": "Archetype",
        "description": "Builder engagement pattern classification",
        "role": "archetype",
    },
}


# ---------------------------------------------------------------------------
# Target States (for gap analysis in reports)
#
# Where you want each observation context to be.
# Customize these for your project goals.
# ---------------------------------------------------------------------------

TARGET_STATES = {
    "architecture_quality": "elegant",
    "test_coverage": "gated",
    "technical_debt": "minimal",
    "feature_completeness": "complete",
    "user_experience": "polished",
    "developer_velocity": "fast",
    "knowledge_distribution": "shared",
    "customer_alignment": "validated",
    "documentation_quality": "comprehensive",
}


# ---------------------------------------------------------------------------
# Current States (initial baseline)
#
# Set these to your project's starting state.
# compound.py report will track changes from here.
# ---------------------------------------------------------------------------

CURRENT_STATES_POST_SPRINT8 = {
    "architecture_quality": "fragile",
    "test_coverage": "manual",
    "technical_debt": "managed",
    "feature_completeness": "mvp",
    "user_experience": "usable",
    "developer_velocity": "slow",
    "knowledge_distribution": "siloed",
    "customer_alignment": "assumed",
    "documentation_quality": "sparse",
}


# ---------------------------------------------------------------------------
# JTBD Definitions (optional)
#
# Define your product's jobs-to-be-done.
# Map sprints to jobs in SPRINT_JTBD_MAP below.
# ---------------------------------------------------------------------------

JTBD_DEFINITIONS = {
    # "job1": "Your first job-to-be-done",
    # "job2": "Your second job-to-be-done",
}

SPRINT_JTBD_MAP = {
    # 0: "job1",
}


# ---------------------------------------------------------------------------
# Stakeholder Definitions (for stakeholder alignment)
#
# Define your stakeholders here, or use .stakeholders.json override.
# self_model_id is populated after running:
#   python $CLARITY_API_PATH/scripts/stakeholder_setup.py
# ---------------------------------------------------------------------------

STAKEHOLDER_DEFINITIONS = {
    # "Alice": {
    #     "email": "alice@example.com",
    #     "app_id": "my-project",
    #     "role": "tech-lead",
    #     "self_model_id": None,  # Set after stakeholder_setup.py
    # },
    # "Bob": {
    #     "email": "bob@example.com",
    #     "app_id": "my-project",
    #     "role": "product-manager",
    #     "self_model_id": None,
    # },
}


# ---------------------------------------------------------------------------
# Stakeholder Weights (for aggregate alignment scoring)
# ---------------------------------------------------------------------------

STAKEHOLDER_WEIGHTS = {
    # "Alice": {"weight_source": "technical_health", "base_weight": 0.50},
    # "Bob": {"weight_source": "product_health", "base_weight": 0.50},
}


# ---------------------------------------------------------------------------
# Self-Model Definition Template (for init command)
# ---------------------------------------------------------------------------

def build_self_model_definition(name: str) -> dict:
    """Build the self-model definition for the builder."""
    return {
        "app_id": "my-project",  # Change to your app_id
        "name": name,
        "domains": [
            {
                "domain_id": ctx_data["domain"],
                "name": ctx_data["domain"].replace("_", " ").title(),
                "description": f"Pillar: {ctx_data['domain']}",
            }
            for ctx_id, ctx_data in OBSERVATION_CONTEXTS.items()
            # deduplicate domains
            if ctx_id == next(
                k for k, v in OBSERVATION_CONTEXTS.items()
                if v["domain"] == ctx_data["domain"]
            )
        ],
        "modes": [
            {"mode_id": mode_id, **mode_data}
            for mode_id, mode_data in CLEAR_MODES.items()
        ],
        "views": [
            {"view_id": view_id, **view_data}
            for view_id, view_data in VIEW_DEFINITIONS.items()
        ],
        "observation_contexts": [
            {
                "context_id": ctx_id,
                "domain_id": ctx_data["domain"],
                "description": ctx_data["description"],
                "possible_states": ctx_data["possible_states"],
            }
            for ctx_id, ctx_data in OBSERVATION_CONTEXTS.items()
        ],
    }


# ---------------------------------------------------------------------------
# Per-Builder Overrides (optional)
# If .stakeholders.json exists in the project root, override defaults.
# See .stakeholders.json.example for the expected format.
# ---------------------------------------------------------------------------

def _load_stakeholder_overrides():
    """Load per-builder stakeholder overrides from .stakeholders.json."""
    override_path = Path(__file__).resolve().parent.parent / ".stakeholders.json"
    if not override_path.exists():
        return

    try:
        data = json.loads(override_path.read_text())

        if "definitions" in data:
            global STAKEHOLDER_DEFINITIONS
            STAKEHOLDER_DEFINITIONS = data["definitions"]

        if "weights" in data:
            global STAKEHOLDER_WEIGHTS
            STAKEHOLDER_WEIGHTS = data["weights"]

    except (json.JSONDecodeError, KeyError) as e:
        import sys
        print(f"WARNING: Invalid .stakeholders.json: {e}", file=sys.stderr)

_load_stakeholder_overrides()
