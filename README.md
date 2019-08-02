# Useful Python Scripts

This repository holds some useful python Scripts

## Getting Started

Each folder groups useful python scripts and is self-contained. To make it very easy for you to use
there is a `requirements.txt` file in each folder. So to run the scripts follow the steps
in the [Installation](#installation) section.

## Prerequisites

The only prerequisite is `Python3`


## Installing

Clone this repository:

```git clone git@github.com:zwoefler/UsefulPythonScripts.git```

Change to the directory with your desired script, e.g. `GitHub-Scripts`:

```cd UsefulPythonScripts/GitHub-Scripts/```

Create a **Virtual Environment** in the folder.
Choose a name for oyur environment and end it with `env` to keep the project naming conventions.:

```python3 -m venv GHenv```

Activate your **Virtual Environment**:

```source GHVenv/bin/activate```
Can be deavtivated: `deactivate`

Install the requirements in the `requirements.txt`:

```pip install -r requirements.txt```

Execute the Python Script of your desire:

```python3 create_new_git_repo.py MyNewRepo Username Password```



## Built With

* [Python3](http://www.python.org) - Python is a programming language that lets you work quickly and integrate systems more effectively
* [Selenium](https://www.seleniumhq.org/) - Selenium Automates Browsers

## Authors

* **[@zwoelfer](https://github.com/zwoefler)**

## Acknowledgments

* [README-Template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) from [@PurpleBooth](https://github.com/PurpleBooth/)
