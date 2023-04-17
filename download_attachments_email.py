import imaplib, email, getpass

user = input('Enter your email:')
passwd = getpass.getpass('Enter your password:')
outputdir = input('Enter the path for the downloads:')
# Connect to an IMAP server
def connect(server, user, password):
    m = imaplib.IMAP4_SSL(server)
    m.login(user, password)
    m.select()
    return m

# Download all attachment files for a given email
def downloaAttachmentsInEmail(m, emailid, outputdir):
    resp, data = m.fetch(emailid, "(BODY.PEEK[])")
    email_body = data[0][1]
    mail = email.message_from_string(email_body.decode())
    if mail.get_content_maintype() != 'multipart':
        return
    for part in mail.walk():
        if part.get_content_maintype() != 'multipart' and part.get('Content-Disposition') is not None:
            open(outputdir + '/' + part.get_filename(), 'wb').write(part.get_payload(decode=True))

# Download all the attachment files for all emails in specific folder.
def downloadAllAttachmentsInInbox(server, user, password, outputdir):
    m = connect(server, user, password)
    resp, items = m.search(None, "(ALL)")
    items = items[0].split()
    for emailid in items:
        downloaAttachmentsInEmail(m, emailid, outputdir)

downloadAllAttachmentsInInbox(server="imap.gmail.com",user=user,password=passwd,outputdir=outputdir)
