# auto-toggle-importer

A program to simplify and automate exporting [Toggl Track](https://track.toggl.com/) time entries and then import them into OpusVL Timelogger. 

## Prequisites

You will need to install dependcies from requirements.txt

Accounts for both Toggl and OpusVL Timelogger are required.

Additionally, you will need to get hold of your Toggl API key and add this to the config file, alongside Timelogger username and password (example config file included.)

## Installation

In a directory of your choice run:

    git clone git@github.com:jmcharter/auto-toggl-importer.git

## Usage

To use, simply run `main.py` with your selected date as an argument. The date must be in the format "yyyy-mm-dd".

e.g.

    python3 main.py 2021-10-11

If no date is provided, then the program will default to today's date.

