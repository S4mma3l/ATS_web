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
    jobs: list = []  # Variable para almacenar los trabajos obtenidos

    def add_job(self):
        """Método para agregar un nuevo trabajo a la base de datos"""
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

            if response.status_code == 201:
                print(f"Job '{self.title}' added successfully!")
                return response.data
            else:
                print(f"Error adding job: {response.error_message}")
                return None
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

    def get_jobs(self):
        """Método para obtener trabajos de la base de datos"""
        try:
            response = supabase.table("jobs").select("*").execute()

            if response.status_code == 200:
                self.jobs = response.data  # Guardar los trabajos en el estado
                print(f"Jobs retrieved successfully: {self.jobs}")
            else:
                print(f"Error fetching jobs: {response.error_message}")
        except Exception as e:
            print(f"An error occurred while fetching jobs: {str(e)}")

    def load_jobs(self):
        """Carga los trabajos cuando se inicializa el estado"""
        self.get_jobs()  # Llama al método que obtiene los trabajos

def JobList():
    """Componente para mostrar la lista de trabajos"""

    # Cargar los trabajos al iniciar el componente
    JobState.load_jobs()

    # Usar rx.foreach para iterar sobre los trabajos
    return rx.vstack(
        rx.heading("Available Jobs", align="center"),
        rx.container(
            rx.foreach(JobState.jobs, lambda job: 
                rx.box(
                    rx.heading(job["title"], size="md"),
                    rx.text(f"Company: {job['company']}"),
                    rx.text(f"Location: {job['location']}"),
                    rx.text(f"Description: {job['description']}"),
                    rx.text(f"Requirements: {job['requirements']}"),
                    border="1px solid #ccc",
                    padding="10px",
                    margin="10px",
                )
            ),
            max_width="800px",
            padding="20px",
        ),
        align="center",
    )