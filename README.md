# SCC Networking Xmas Reminder Script

Usage: `python3 main.py`


You will need to make a json file called `config.json` to connect to a SMTP server following this syntax:

```json
{
    "smtp_server" : "smtp.server.ac.uk",
    "port" : 25,
    "email" : "sender@server.ac.uk",
    "preamble" : "This is an automated email reminding you of the SCC Networking Group Christmas meal, as well as your menu choices.",
    "event_detail" : "Today at 6:30pm",
    "from" : "Eleanor"

}
```
