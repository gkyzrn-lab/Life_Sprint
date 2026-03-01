# app/core/__init__.py
"""
Core domain models + in-memory store for Life Sprint backend.
"""

# Import quest and skill rating modules first to ensure Player model is fully built
import core_domain.quests
