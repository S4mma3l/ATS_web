import reflex as rx

from ATS_web.models.candidato import Candidate

def candidate_filter():
    return rx.input(placeholder="Skill", on_change=rx.set_state("filter_skill"))

def filtered_candidates():
    skill_filter = rx.get_state("filter_skill")
    candidates = Candidate.query().all()
    filtered = [
        candidate for candidate in candidates
        if skill_filter.lower() in candidate.skills.lower()
    ]
    
    return rx.vstack(
        *[
            rx.text(f"{c.first_name} {c.last_name}: {c.skills}")
            for c in filtered
        ]
    )
