import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(BASE_DIR)
LINER = "-----------------------------------------------"
TITLE = "LEARN PYTHON"
PROBLEMS = os.listdir(os.path.join(PARENT_DIR,'problems'))