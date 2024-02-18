# from backend.vector_database import Vector_Database
import sys
from streamlit.web import cli


if __name__ == '__main__':
    sys.argv = ["streamlit", "run", "frontend/Test.py"]
    sys.exit(cli.main())