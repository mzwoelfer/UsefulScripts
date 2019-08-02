"""Deletes an existing GitHub Repository. Credentials are getting read
from the ../Additional_Data/credentials.txt file. Executing the script requires
the name of the repo to be deleted."""

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


def remove_repo_from_github(reponame, git_username, git_password):
    """Removes a given repository from GitHub"""
    login = BROWSER.find_elements_by_xpath("//input[@name='login']")[0]
    login.send_keys(git_username)
    in_password = BROWSER.find_elements_by_xpath("//input[@name='password']")[0]
    in_password.send_keys(git_password)
    login_button = BROWSER.find_elements_by_xpath("//input[@name='commit']")[0]
    login_button.click()
    # Visits the website of the Repo
    BROWSER.get('https://github.com/' + git_username + '/' + reponame + '/settings')

    delete_repo = BROWSER.find_elements_by_xpath(
        '//*[@id="options_bucket"]/div[8]/ul/li[4]/details/summary')[0]
    delete_repo.click()
    remove_repo_input = BROWSER.find_elements_by_xpath(
        '//*[@id="options_bucket"]/div[8]/ul/li[4]/details/details-dialog/div[3]/form/p/input')[0]
    remove_repo_input.send_keys(reponame)
    delete_button = BROWSER.find_element_by_xpath(
        '//*[@id="options_bucket"]/div[8]/ul/li[4]/details/details-dialog/div[3]/form/button')
    delete_button.click()
    BROWSER.quit()


def main():
    """The main function of delete_git_repo.py"""
    credentials = get_login_credentials(LOGIN_CREDENTIALS_FILE)
    trimmed_credentials = trim_credentials(credentials)
    remove_repo_from_github(ARGS.repository_name, trimmed_credentials[0], trimmed_credentials[1])


if __name__ == "__main__":
    main()
