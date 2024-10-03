import reflex as rx

from ATS_web.models.oferta import Job
from ATS_web.models.aplica_a_oferta import apply_to_job
from ATS_web.components.add_job import get_jobs

def job_list():
    jobs = get_jobs()  # Obtener todas las ofertas
    return rx.vstack(
        *[
            rx.box(
                rx.text(f"Title: {job.title}"),
                rx.text(f"Company: {job.company}"),
                rx.text(f"Location: {job.location}"),
                rx.text(f"Description: {job.description}"),
                rx.button("Apply", on_click=lambda: apply_to_job(job)),
                margin="10px",
                padding="10px",
                border="1px solid #ccc",
            )
            for job in jobs
        ]
    )

