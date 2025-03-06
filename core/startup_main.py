from core.database.session import get_db, Base


def startup_main():
    db = next(get_db())
    engine = db.get_bind()

    # Datenbanktabellen erstellen
    Base.metadata.create_all(bind=engine)
