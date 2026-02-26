from utils.db import get_db_session, init_db
from services.ingestion_service import IngestionService

def main():
    init_db()

    with get_db_session() as session:
        ingestion = IngestionService(session)
        res = ingestion.ingest_summary_stats_only()
        print("Ingestion Summary")
        print(f"Summary stats: {res}")

if __name__ == "__main__":
    main()