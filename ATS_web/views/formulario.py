import reflex as rx

from ATS_web.models.registro_candidato import submit_candidate

def candidate_form():
    return rx.vstack(
        rx.input(placeholder="First Name", on_change=rx.set_state("first_name")),
        rx.input(placeholder="Last Name", on_change=rx.set_state("last_name")),
        rx.input(placeholder="Email", on_change=rx.set_state("email")),
        rx.text_area(placeholder="Skills", on_change=rx.set_state("skills")),
        rx.file_input(on_change=rx.set_state("resume_url")),
        rx.button("Submit", on_click=submit_candidate),
    )
