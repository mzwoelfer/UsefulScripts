"""This module creates a new GitHub Repository with your credentials. They are getting
pulled from the '../Additional_Data/Credentials.txt' file"""
import argparse
from selenium import webdriver


PARSER = argparse.ArgumentParser(
        description='Gets the name of the repository that you want to create')
PARSER.add_argument('repository_name', type=str, help='The name of the repository')
ARGS = PARSER.parse_args()
LOGIN_CREDENTIALS_FILE = '../Additional_Data/credentials.txt'
BROWSER = webdriver.Firefox()
BROWSER.get('http://github.com/login')


def get_login_credentials(credentials_file):
    """Reads in the login credentials"""
    with open(credentials_file, 'r') as file:
        return file.readlines()


def trim_credentials(creds):
    """Trims all whitespaces from the credentials and returns the username and password"""
    return [cred.strip() for cred in creds]


def create_repo(repo_name, git_username, git_password):
    """Automatically creates a new github repo"""
    login_input = BROWSER.find_elements_by_xpath("//input[@name='login']")[0]
    login_input.send_keys(git_username)
    password_input = BROWSER.find_elements_by_xpath("//input[@name='password']")[0]
    password_input.send_keys(git_password)
    login_button = BROWSER.find_elements_by_xpath("//input[@name='commit']")[0]
    login_button.click()
    BROWSER.get('https://github.com/new')
    repository_name_input = BROWSER.find_elements_by_xpath("//input[@name='repository[name]']")[0]
    repository_name_input.send_keys(repo_name)
    create_button = BROWSER.find_element_by_css_selector('button.first-in-line')
    create_button.submit()
    BROWSER.quit()


def main():
    """The Main function of the create_new_git_repo.py"""
    credentials = get_login_credentials(LOGIN_CREDENTIALS_FILE)
    trimmed_credentials = trim_credentials(credentials)
    create_repo(ARGS.repository_name, trimmed_credentials[0], trimmed_credentials[1])


if __name__ == "__main__":
    main()
