import reflex as rx
import ATS_web.styles.styles as styles

from ATS_web.components.add_job import JobForm
from ATS_web.components.add_candidate import CanForm
from ATS_web.components.job_list import JobList



def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            JobForm(), 
            CanForm(),
            JobList(),
            )
        )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)
app.add_page(index)
