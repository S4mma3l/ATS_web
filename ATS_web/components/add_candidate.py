import reflex as rx


from supabase import create_client, Client
from ATS_web.keys.keys import SUPABASE_KEY, SUPABASE_URL

url = SUPABASE_URL
key = SUPABASE_KEY
supabase: Client = create_client(url, key)


class CanState(rx.State):
    first_name: str = ""
    last_name: str = ""
    email: str = ""
    skills: str = ""
    resume_url: str = ""

    def add_can(self):
        try:
            response = (
                supabase.table("candidates")
                .insert(
                    {
                        "first_name": self.first_name,
                        "last_name": self.last_name,
                        "email": self.email,
                        "skills": self.skills,
                        "resume_url": self.resume_url,
                    }
                )
                .execute()
            )

            # Verificar si la inserción fue exitosa
            if response.status_code == 201:  # Cambiado a response.status_code
                print(f"Candidate '{self.first_name}' added successfully!")
                return response.data  # Retornar los datos de la respuesta
            else:
                print(f"Error adding candidate: {response.error_message}")  # Manejar el error
                return None
        except Exception as e:
            print(f"An error occurred: {str(e)}")  # Capturar excepciones
            return None


# Definir el componente JobForm
def CanForm():
    return (
        rx.vstack(
            rx.box(
                rx.heading("Candidate Management")
            ),
            rx.input(
                placeholder="First Name",
                value=CanState.first_name,
                on_change=lambda val: CanState.set_first_name(val),
                size="3",
                color_scheme="iris",
                variant="soft",
            ),
            rx.input(
                placeholder="Last Name",
                value=CanState.last_name,
                on_change=lambda val: CanState.set_last_name(val),
                size="3",
                color_scheme="iris",
                variant="soft",
            ),
            rx.input(
                placeholder="Email",
                value=CanState.email,
                on_change=lambda val: CanState.set_email(val),
                size="3",
                color_scheme="iris",
                variant="soft",
            ),
            rx.input(
                placeholder="Skills",
                value=CanState.skills,
                on_change=lambda val: CanState.set_skills(val),
                size="3",
                color_scheme="iris",
                variant="soft",
            ),
            rx.input(
                placeholder="Resume URl",
                value=CanState.resume_url,
                on_change=lambda val: CanState.set_resume_url(val),
                size="3",
                color_scheme="iris",
                variant="soft",
            ),
            rx.container(
                rx.center(
                    rx.button(
                        "Submit",
                        on_click=lambda: CanState.add_can(),
                        size="3",
                        variant="solid",
                        color_scheme="red"
                    ),   
                ),                
            ),
            align="center",
        ),
    )
