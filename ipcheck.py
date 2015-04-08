import os
import smtplib
import urllib

class Ip_check:
    def send_email(self, message):
        # Credentials for the email
        username = 'username'
        password = 'password'
        fromaddr = 'username@gmail.com'
        toaddrs  = 'dst_addr@gmail.com'
        subject  = 'New IP!'
        msg = 'Subject: %s\n\n%s' % (subject, message)

        # The actual mail send
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()

    def write_ip(self, ip):
        f = open('/Path/to/ip.txt', 'w')
        f.seek(0)
        f.truncate()
        f.write(ip)
        f.close()

    def read_ip(self):
        if os.path.exists('/Path/to/ip.txt'):
            f = open('/Path/to/ip.txt', "r")
        else:
            f = open('/Path/to/ip.txt', "w+")
        ip = f.readline()
        f.close()
        return ip

    def __init__(self):
        ip_new = urllib.urlopen('http://api.ipify.org').read()
        ip_old = self.read_ip()
        if ip_new != ip_old:
            print 'NEW IP'
            self.write_ip(ip_new)
            self.send_email(ip_new)
        else:
            print 'OLD IP'

Ip_check()

