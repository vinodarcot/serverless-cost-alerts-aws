import boto3


class EmailClient:
    SENDER = "AWS Cost Alert <vinodbhargav@ensarsolutions.com>"
    SUBJECT = "Info AWS Account Billing Report"
    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = """AWS Billing Alerts \r\n
    Daily billing report\r\n
    {daily_billing_report}\r\n
    Monthly billing report\r\n
    {monthly_billing_report}\r\n
    """

    # The HTML body of the email.
    BODY_HTML = """<html>
    <head></head>
    <body>
    <h1>AWS Billing Alert</h1>
    <hr/>
    <h3>Daily Billing in $</h3>
    <p>{daily_billing_report}</p>
    <hr/>
    <h3>Monthly Billing in $</h3>
    <p>{monthly_billing_report}</p>
    </body>
    </html>
    """
    # The character encoding for the email.
    CHARSET = "UTF-8"

    # recipient email address
    #recipients = ['Recipient One <vinodbhargav0033@gmail.com>', 'vinodbhargav@ensarsolutions.com']


    def __init__(self):
        self.client = boto3.client("ses")

    def send(self, daily_billing_report, monthly_billing_report):
        """Send an email which contains AWS billing data"""
        email_text = self.BODY_TEXT.format(
            daily_billing_report=daily_billing_report,
            monthly_billing_report=monthly_billing_report
        )

        email_html = self.BODY_HTML.format(
            daily_billing_report=daily_billing_report,
            monthly_billing_report=monthly_billing_report
        )
        response = self.client.send_email(
            Destination={'ToAddresses': ['sujith@ensarsolutions.com'],
            'CcAddresses':['vinodbhargav@ensarsolutions.com']},
            Message={
                "Body": {
                    "Html": {
                        "Charset": self.CHARSET,
                        "Data": email_html
                    },
                    "Text": {
                        "Charset": self.CHARSET,
                        "Data": email_text,
                    },
                },
                "Subject": {
                    "Charset": self.CHARSET,
                    "Data": self.SUBJECT,
                },
            },
            Source=self.SENDER,
        )