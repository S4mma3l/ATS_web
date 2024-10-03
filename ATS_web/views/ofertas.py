import reflex as rx

from ATS_web.models.publicar_oferta import submit_job

def job_form():
    return rx.vstack(
        rx.input(placeholder="Job Title", on_change=rx.set_state("title")),
        rx.text_area(placeholder="Description", on_change=rx.set_state("description")),
        rx.input(placeholder="Company", on_change=rx.set_state("company")),
        rx.input(placeholder="Location", on_change=rx.set_state("location")),
        rx.text_area(placeholder="Requirements", on_change=rx.set_state("requirements")),
        rx.button("Post Job", on_click=submit_job),
    )
