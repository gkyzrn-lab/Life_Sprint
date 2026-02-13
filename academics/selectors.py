import random
from typing import List, Tuple, Set, Dict

from academics.curriculum import CURRICULUM


def get_semester_courses_and_tags(college_id: str, major_id: str, semester: int) -> List[Tuple[str, List[str]]]:
    sem = CURRICULUM.get(college_id, {}).get(major_id, {}).get(semester)
    if not sem:
        return []

    out: List[Tuple[str, List[str]]] = []
    for course in sem.courses:
        tags: List[str] = []
        for topic in course.topics:
            tags.extend(topic.exam_tags or [])

        # de-dupe per course
        seen = set()
        tags_dedup: List[str] = []
        for t in tags:
            if t and t not in seen:
                seen.add(t)
                tags_dedup.append(t)

        out.append((course.id, tags_dedup))

    return out


def get_semester_exam_tags(college_id: str, major_id: str, semester: int) -> List[str]:
    pairs = get_semester_courses_and_tags(college_id, major_id, semester)
    seen = set()
    out: List[str] = []
    for _, tags in pairs:
        for t in tags:
            if t not in seen:
                seen.add(t)
                out.append(t)
    return out


def select_exam_questions_with_course_coverage(pool: List, course_tags: List[Tuple[str, List[str]]], n: int = 3) -> List:
    """
    Goal:
      - If possible, pick >=1 question per course (up to n).
      - Then fill remaining from best tag-matching questions.
      - Fallback safely if tags are sparse.

    pool questions should have: q.id, q.choices, and q.tags: List[str] (optional).
    """
    if not pool:
        return []

    q_tags_map: Dict[str, Set[str]] = {q.id: set(getattr(q, "tags", []) or []) for q in pool}
    chosen_ids: Set[str] = set()
    chosen: List = []

    # Phase 1: one-per-course coverage
    shuffled_courses = course_tags[:]
    random.shuffle(shuffled_courses)

    for _, tags in shuffled_courses:
        if len(chosen) >= n:
            break
        if not tags:
            continue

        tset = set(tags)
        candidates = [q for q in pool if q.id not in chosen_ids and (q_tags_map[q.id] & tset)]
        if candidates:
            pick = random.choice(candidates)
            chosen.append(pick)
            chosen_ids.add(pick.id)

    # Phase 2: fill remaining based on overlap with all semester tags
    if len(chosen) < n:
        all_target: Set[str] = set()
        for _, tags in course_tags:
            all_target.update(tags)

        remaining = [q for q in pool if q.id not in chosen_ids]

        if all_target:
            scored = []
            for q in remaining:
                overlap = len(q_tags_map[q.id] & all_target)
                scored.append((overlap, q))
            scored.sort(key=lambda x: x[0], reverse=True)

            if scored:
                max_overlap = scored[0][0]
                top_band = [q for s, q in scored if s >= max(1, max_overlap - 1)]

                while len(chosen) < n and top_band:
                    pick = random.choice(top_band)
                    top_band.remove(pick)
                    chosen.append(pick)
                    chosen_ids.add(pick.id)
        else:
            while len(chosen) < n and remaining:
                pick = random.choice(remaining)
                remaining.remove(pick)
                chosen.append(pick)
                chosen_ids.add(pick.id)

    # Phase 3: ultimate fallback
    if len(chosen) < n:
        remaining = [q for q in pool if q.id not in chosen_ids]
        while len(chosen) < n and remaining:
            pick = random.choice(remaining)
            remaining.remove(pick)
            chosen.append(pick)
            chosen_ids.add(pick.id)

    return chosen[:n]
