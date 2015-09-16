import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
LINER = "-----------------------------------------------"
TITLE = "LEARN PYTHON"
PROBLEMS = os.listdir(os.path.join(ROOT_DIR,'problems'))
# print BASE_DIR
