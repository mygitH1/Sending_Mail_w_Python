import smtplib  # import smtp library
# 587 is the port we are working with and is required
conn = smtplib.SMTP('smtp.gmail.com', 587)
# print(type(conn)) # Gives you the time from smtplib
# print(conn) # Same result as above
print(conn.ehlo())  # This is only printed to see the connection with the IP address
print(conn.starttls())  # This is only printed to see the "ready to start" message
# Note that starttls is for encryption. Most Modern email systems requires encryption.
x = input("Enter your gmail\n")
y = input("Enter your password\n")
z = input("Enter the gmail you want to send a message too\n")
v = input("Please enter the message you would like to send. Example: Subject: Hello, Dear Self etc....\n")

conn.login(x, y)  # email and then password
# print(conn.sendmail(''))
conn.sendmail(z, x, v)
# email from, email to, Body of the email


# REFERENCE HERE BELOW

# --------------------------------------------------
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# --------------------------------------------------


# EMAIL PROVIDERS and THEIR SMTP Servers

# Provider           SMTP server domain name
# GMAIL                      smtp.gmail.com
# Outlook.com/Hotmail.com    smtp-mail.outlook.com
# Yahoo Mail                 smtp.mail.yahoo.com
# AT&T                       smpt.mail.att.net (port 465)
# Comcast                    smtp.comcast.net
# Verizon                    smtp.verison.net (port 465)


# --------------------------------------------------
