# Using the WG_Update script

# Prerequisites
### Python3
Create a python3 virtual env: `python3 -m venv Env`
Activate virtual env: `source Env/bin/activate`
Install requirements: `pip install -r reuqirements`

### Selenium / Webcontent
We are using Google Chrome. So Chrome needs to be installed on your machine.
1. Download the correct version on: `https://www.google.com/chrome/`.
2. Install Chrome via console: `sudo apt install ~/Downloads/google-chrome-stable_current_amd64.deb`
Once Chrome is downloaded, you need the `ChromeDriver`.
Find out your current Google-Chrome version: `google-chrome --version`

### ChromeDriver
The `ChromeDriver` makes it possible for the Selenium package to interact with the browser.
1. Download the CORRECT version ChromeDriver from the official chromedriver webpage: `https://sites.google.com/chromium.org/driver/` (Latest stable release. Download the chromedriver_linux64.zip)
2. Unzip the ChromeDriver `unzip ~/Downloads/chromedriver_linux64.zip`
3. Move the ChromeDriver into the PATH variable with: `sudo mv chromedriver /usr/local/bin` (Type in the root password)

# How to use
After the installation stuff above, do this:

1. Insert your `email`, `password` and `wg-gesucht change URL` into the login_data.json
2. Load your python3 virtual environment `source Env/bin/activate`
3. Execute the python script `python3 update_wg_gesucht.py`
