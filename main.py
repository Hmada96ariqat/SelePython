# main.py

from dockerhub.fixture import setup_driver, teardown_driver
from dockerhub.create_delete_repo import create_repo, delete_repo
from utils.utils import generate_random_string
from dockerhub.login import log_in

def main():
    driver, wait = setup_driver()
    try:
        repo_name = create_repo(driver, wait, generate_random_string, log_in)
        delete_repo(driver, wait, repo_name)
    finally:
        teardown_driver(driver)

if __name__ == "__main__":
    main()
