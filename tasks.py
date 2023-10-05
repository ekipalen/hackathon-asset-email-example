import requests
from robocorp.tasks import task
from robocorp import vault
from RPA.Robocorp.Storage import Storage
import csv
import io

LEAD_ASSET = 'Hackathon Leads'
TEMPLATE_ASSET = 'Hackathon html template'
EMAIL_SUBJECT = 'Example email from the Control Room'
TESTING_MODE = 'Yes'  # Set to "No" to send emails for the actual recipients.
TEST_RECIPIENT = '<Your email address.>'
SENDER = 'You <you@example.com>'

@task
def minimal_task():
    storage = Storage()

    leads = storage.get_text_asset(LEAD_ASSET)
    leads = csv.DictReader(io.StringIO(leads))
    templatepath = storage.get_file_asset(TEMPLATE_ASSET, 'email_template.html', overwrite=True)
    with open(templatepath, 'r') as file:
        email_template = file.read()

    for lead in leads:
        email_body = email_template.replace('[FIRSTNAME]',lead['firstname'])
        email_body = email_body.replace('[COMPANY]',lead['company'])
        email_body = email_body.replace('[COMPANYUPPER]',lead['company'].upper())
        print(email_body)
        if TESTING_MODE == 'No':
            send_email(email_body,lead['email'])
    
    if TESTING_MODE == 'Yes':
        send_email(email_body,TEST_RECIPIENT)
    
def send_email(email_body,recipient):
    mailgun_secret = vault.get_secret('Mailgun')
    return requests.post(
        "https://api.mailgun.net/v3/"+mailgun_secret['domain']+"/messages",
        auth=("api", mailgun_secret['api_key']),
        data={"from": SENDER,
              "to": recipient,
              "subject": EMAIL_SUBJECT,
              "html": email_body})