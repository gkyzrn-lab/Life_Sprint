from typing import Dict, Optional

from app.college.selection import generate_college_options
from app.college.curriculum_preview import get_curriculum_preview
from app.college.exams import run_semester_exams

from app.work.selection import get_available_work
from app.work.effects import apply_work_effects
from app.work.internship_selection import attempt_internship


# =================================================
# GAME CORE
# =================================================

class GameCore:
    """
    Central game orchestrator for Life Sprint.
    """

    def __init__(self, player):
        self.player = player
        self.phase = "college"
        self.turn = 0

    # =================================================
    # GAME START
    # =================================================

    def start_game(self) -> Dict:
        """
        Initial game payload.
        """
        return {
            "phase": self.phase,
            "semester": self.player.semester,
            "player_snapshot": self._player_snapshot(),
        }

    # =================================================
    # COLLEGE FLOW
    # =================================================

    def get_college_options(self) -> Dict:
        """
        Show college choices.
        """
        options = generate_college_options(self.player)
        return {
            "type": "college_selection",
            "options": options,
        }

    def select_college(self, college_data: Dict):
        """
        Lock in college selection.
        """
        self.player.college = college_data
        self.player.semester = 1

    def run_college_semester(self) -> Dict:
        """
        Run one full college semester.
        """

        # -------------------------
        # Curriculum preview (UI)
        # -------------------------
        preview = get_curriculum_preview(
            self.player.college["id"],
            self.player.major,
            self.player.semester,
        )

        # -------------------------
        # Exams (logic)
        # -------------------------
        exam_results = run_semester_exams(self.player)
        self.player.stats.gpa = exam_results["gpa"]

        # -------------------------
        # Work opportunities
        # -------------------------
        available_work = get_available_work(self.player)

        # -------------------------
        # Advance semester
        # -------------------------
        self.player.semester += 1
        self.turn += 1

        payload = {
            "phase": "college",
            "semester_completed": self.player.semester - 1,
            "curriculum_preview": preview,
            "exam_results": exam_results,
            "available_work": available_work,
            "player_snapshot": self._player_snapshot(),
        }

        self._log_history("college_semester_completed", payload)
        return payload

    # =================================================
    # WORK & INTERNSHIPS
    # =================================================

    def take_part_time_work(self, job: Dict) -> Dict:
        """
        Apply part-time job effects.
        """
        apply_work_effects(self.player, job)

        payload = {
            "type": "part_time_job_taken",
            "job": job["name"],
            "player_snapshot": self._player_snapshot(),
        }

        self._log_history("part_time_job", payload)
        return payload

    def attempt_internship(self, internship_id: str, answers: Dict[int, int]) -> Dict:
        """
        Attempt an internship with interview answers.
        """
        result = attempt_internship(self.player, internship_id, answers)

        if result["accepted"]:
            payload = {
                "type": "internship_accepted",
                "internship": result["internship"]["company"],
                "player_snapshot": self._player_snapshot(),
            }
        else:
            payload = {
                "type": "internship_rejected",
                "internship": result["internship"]["company"],
                "feedback": result["feedback"],
                "player_snapshot": self._player_snapshot(),
            }

        self._log_history(payload["type"], payload)
        return payload

    # =================================================
    # INTERNAL UTILITIES
    # =================================================

    def _player_snapshot(self) -> Dict:
        """
        UI-safe snapshot of player state.
        """
        return {
            "semester": self.player.semester,
            "college": self.player.college.get("name") if self.player.college else None,
            "major": self.player.major,
            "gpa": round(self.player.stats.gpa, 2),
            "stress": self.player.stats.stress,
            "personality": self.player.personality,
            "modern_skills": vars(self.player.modern_skills),
            "finance": {
                "balance": self.player.finance.balance,
            },
        }

    def _log_history(self, event_type: str, payload: Dict):
        """
        Central history logging.
        """
        self.player.history.append({
            "turn": self.turn,
            "event_type": event_type,
            "data": payload,
        })
