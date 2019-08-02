"""Deletes an existing GitHub Repository. Credentials are getting read
from the ../Additional_Data/credentials.txt file. Executing the script requires
the name of the repo to be deleted."""

import argparse
from selenium import webdriver


PARSER = argparse.ArgumentParser(
    description='Gets the name of the repository that you want to create')
PARSER.add_argument('repository_name', type=str, help='The name of the repository')
PARSER.add_argument('git_username', type=str, help='Your GitHub Username to login')
PARSER.add_argument('git_password', type=str, help='Your GitHub Password to login')
ARGS = PARSER.parse_args()
LOGIN_CREDENTIALS_FILE = '../Additional_Data/credentials.txt'
BROWSER = webdriver.Firefox()
BROWSER.get('http://github.com/login')


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
    remove_repo_from_github(ARGS.repository_name, ARGS.git_username, ARGS.git_password)


if __name__ == "__main__":
    main()
