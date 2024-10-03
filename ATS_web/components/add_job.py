import reflex as rx


from supabase import create_client, Client
from ATS_web.keys.keys import SUPABASE_KEY, SUPABASE_URL

url = SUPABASE_URL
key = SUPABASE_KEY
supabase: Client = create_client(url, key)


class JobState(rx.State):
    title: str = ""
    description: str = ""
    company: str = ""
    location: str = ""
    requirements: str = ""

    def add_job(self):
        try:
            response = (
                supabase.table("jobs")
                .insert(
                    {
                        "title": self.title,
                        "description": self.description,
                        "company": self.company,
                        "location": self.location,
                        "requirements": self.requirements,
                    }
                )
                .execute()
            )

            # Verificar si la inserción fue exitosa
            if response.status_code == 201:  # Cambiado a response.status_code
                print(f"Job '{self.title}' added successfully!")
                return response.data  # Retornar los datos de la respuesta
            else:
                print(f"Error adding job: {response.error_message}")  # Manejar el error
                return None
        except Exception as e:
            print(f"An error occurred: {str(e)}")  # Capturar excepciones
            return None


# Definir el componente JobForm
def JobForm():
    return (
        rx.vstack(
            rx.box(rx.heading("Job Management", align="center")),
            rx.vstack(
                rx.input(
                    placeholder="Job Title",
                    value=JobState.title,
                    on_change=lambda val: JobState.set_title(val),
                    size="3",
                    color_scheme="iris",
                    variant="soft",
                ),
                rx.input(
                    placeholder="Job Description",
                    value=JobState.description,
                    on_change=lambda val: JobState.set_description(val),
                    size="3",
                    color_scheme="iris",
                    variant="soft",
                ),
                rx.input(
                    placeholder="Company",
                    value=JobState.company,
                    on_change=lambda val: JobState.set_company(val),
                    size="3",
                    color_scheme="iris",
                    variant="soft",
                ),
                rx.input(
                    placeholder="Location",
                    value=JobState.location,
                    on_change=lambda val: JobState.set_location(val),
                    size="3",
                    color_scheme="iris",
                    variant="soft",
                ),
                rx.input(
                    placeholder="Requirements",
                    value=JobState.requirements,
                    on_change=lambda val: JobState.set_requirements(val),
                    size="3",
                    color_scheme="iris",
                    variant="soft",
                ),
                rx.container(
                    rx.center(
                        rx.button(
                            "Submit",
                            on_click=lambda: JobState.add_job(),
                            size="3",
                            variant="solid",
                            color_scheme="red",
                        ),
                    ),   
                ),
                align="center",
            ),
        ),
    )
