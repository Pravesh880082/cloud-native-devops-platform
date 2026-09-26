from fastapi import FastAPI
import psycopg2

app = FastAPI(title="DevOps Task Manager")


def get_db_connection():
    return psycopg2.connect(
        host="db",
        database="devopsdb",
        user="devops",
        password="devops123"
    )


@app.on_event("startup")
def startup():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            completed BOOLEAN DEFAULT FALSE
        )
    """)

    connection.commit()
    cursor.close()
    connection.close()


@app.get("/")
def home():
    return {
        "message": "Cloud-Native DevOps Platform is running!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/db-health")
def db_health():
    try:
        connection = get_db_connection()
        connection.close()
        return {"database": "connected"}
    except Exception as e:
        return {"database": "connection failed", "error": str(e)}


@app.get("/tasks")
def get_tasks():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT id, title, completed FROM tasks ORDER BY id")
    tasks = cursor.fetchall()

    cursor.close()
    connection.close()

    return {
        "tasks": [
            {
                "id": task[0],
                "title": task[1],
                "completed": task[2]
            }
            for task in tasks
        ]
    }


@app.post("/tasks")
def create_task(title: str):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO tasks (title) VALUES (%s) RETURNING id",
        (title,)
    )

    task_id = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()

    return {
        "message": "Task created",
        "id": task_id,
        "title": title
    }