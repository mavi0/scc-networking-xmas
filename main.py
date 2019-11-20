import os
import errno
import glob
import sys
import smtplib
import ssl
import json

config = {}


def load_json(filename):
    with open(filename) as f:
        return json.load(f)


def load_config():
    global config
    try:
        config = load_json("config.json")
    except:
        config = load_json("config-default.json")


def mail(receiver, subject, content):
    global config
    content = 'Subject: {}\n\n{}'.format(subject, content)
    server = smtplib.SMTP(config["smtp_server"], config["port"])
    server.sendmail(config["email"], receiver, content)


def main():
    load_config()
    choices = load_json("xmas.json")
    for choice in choices:
        content = "Hello " + choice["Full Name"] + \
            ", \n\nThis is an automated email reminding you of the SCC Networking Group Christmas meal, as well as your menu choices.\n" + \
            "\nDate of event: Tuesday 4th of December at 6:30pm at The White Cross Pub\n" + \
            "\nMenu Choices:\nStarter : " + \
            choice["Starter"] + "\nMain: " + choice["Main"] + \
            "\nDessert: " + choice["Dessert"]
        if not choice["Additional comment to pass to restaurant"] == "":
            content = content + "\nAdditional comment to pass to restaurant: " + \
                choice["Additional comment to pass to restaurant"]
        else:
            content = content + "\nYou left no additional comment to pass to the resturant."

        content = content + "\n\nBest wishes,\n\nEleanorbot"

        print(content)
        mail(choice["Email Address"],
             "SCC Networking Group Christmas Meal Reminder", content)


main()
