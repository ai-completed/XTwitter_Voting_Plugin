
# email_invitations.py
# Automates the process of sending out email invitations for the VoteX system.

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailInvitationSender:
    def __init__(self, server_info, sender_email):
        self.server = smtplib.SMTP(server_info['host'], server_info['port'])
        self.server.starttls()  # Upgrade the connection to secure
        self.server.login(sender_email, server_info['password'])
        self.sender_email = sender_email

    def send_invitation(self, recipient_email, invitation_body):
        # Create a multipart message
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = recipient_email
        message["Subject"] = "Invitation to Participate in VoteX Pilot"

        # Attach the HTML and plain-text versions of the message
        message.attach(MIMEText(invitation_body, 'html'))

        try:
            self.server.send_message(message)
            print(f"Invitation sent to {recipient_email}")
        except Exception as e:
            print(f"Failed to send invitation to {recipient_email}: {e}")

    def close_connection(self):
        self.server.quit()

# Main execution
if __name__ == "__main__":
    # Server information and sender credentials (to be replaced with real values or environment variables)
    server_info = {
        "host": "smtp.example.com",
        "port": 587,
        "password": "securepassword"
    }
    sender_email = "vote-x@example.com"
    
    # Instantiate the email sender
    email_sender = EmailInvitationSender(server_info, sender_email)
    
    # List of recipients and the invitation body (to be populated with real data)
    recipients = ["recipient1@example.com", "recipient2@example.com"]  # Placeholder for recipients
    invitation_body = """
    <html>
    <body>
    <p>Hello,</p>
    <p>You are invited to participate in the VoteX pilot program...</p>
    <p>Best regards,</p>
    <p>VoteX Team</p>
    </body>
    </html>
    """
    
    # Send out invitations
    for recipient in recipients:
        email_sender.send_invitation(recipient, invitation_body)
    
    # Close the connection
    email_sender.close_connection()
