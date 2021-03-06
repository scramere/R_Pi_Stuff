#!/usr/bin/python

from time import gmtime, strftime
import sys
import smtplib

#so I want this to be on permanently until I give it an order to shut down
#I have a plan that I want to use this for later, hence why it's here
on = True
sendEmail = False

while (on):
    from_addr = 'myEmail@host.com'
    to_addrs = ['yourEmail@host.com']

    m = int(strftime("%M", gmtime()))

# I didn't write this part
    """
    This module is designed to fetch your external IP address from the internet.
    It is used mostly when behind a NAT.
    It picks your IP randomly from a serverlist to minimize request
    overhead on a single server
    If you want to add or remove your server from the list contact me on github
    API Usage
    =========
        >>> import ipgetter
        >>> myip = ipgetter.myip()
        >>> myip
        '8.8.8.8'
        >>> ipgetter.IPgetter().test()
        Number of servers: 47
        IP's :
        8.8.8.8 = 47 ocurrencies
    Copyright 2014 phoemur@gmail.com
    This work is free. You can redistribute it and/or modify it under the
    terms of the Do What The Fuck You Want To Public License, Version 2,
    as published by Sam Hocevar. See http://www.wtfpl.net/ for more details.
    """

    import re
    import random

    from sys import version_info

    PY3K = version_info >= (3, 0)

    if PY3K:
        import urllib.request as urllib
    else:
        import urllib2 as urllib

    __version__ = "0.6"


    def myip():
        return IPgetter().get_externalip()


    class IPgetter(object):

        '''
        This class is designed to fetch your external IP address from the internet.
        It is used mostly when behind a NAT.
        It picks your IP randomly from a serverlist to minimize request overhead
        on a single server
        '''

        def __init__(self):
            self.server_list = ['http://ip.dnsexit.com',
                                'http://ifconfig.me/ip',
                                'http://echoip.com',
                                'http://ipecho.net/plain',
                                'http://checkip.dyndns.org/plain',
                                'http://ipogre.com/linux.php',
                                'http://whatismyipaddress.com/',
                                'http://websiteipaddress.com/WhatIsMyIp',
                                'http://getmyipaddress.org/',
                                'http://www.my-ip-address.net/',
                                'http://myexternalip.com/raw',
                                'http://www.canyouseeme.org/',
                                'http://www.trackip.net/',
                                'http://icanhazip.com/',
                                'http://www.iplocation.net/',
                                'http://www.howtofindmyipaddress.com/',
                                'http://www.ipchicken.com/',
                                'http://whatsmyip.net/',
                                'http://www.ip-adress.com/',
                                'http://checkmyip.com/',
                                'http://www.tracemyip.org/',
                                'http://www.lawrencegoetz.com/programs/ipinfo/',
                                'http://www.findmyip.co/',
                                'http://ip-lookup.net/',
                                'http://www.dslreports.com/whois',
                                'http://www.mon-ip.com/en/my-ip/',
                                'http://www.myip.ru',
                                'http://ipgoat.com/',
                                'http://www.myipnumber.com/my-ip-address.asp',
                                'http://www.whatsmyipaddress.net/',
                                'http://formyip.com/',
                                'https://check.torproject.org/',
                                'http://www.displaymyip.com/',
                                'http://www.bobborst.com/tools/whatsmyip/',
                                'http://www.geoiptool.com/',
                                'https://www.whatsmydns.net/whats-my-ip-address.html',
                                'https://www.privateinternetaccess.com/pages/whats-my-ip/',
                                'http://checkip.dyndns.com/',
                                'http://myexternalip.com/',
                                'http://www.ip-adress.eu/',
                                'http://www.infosniper.net/',
                                'https://wtfismyip.com/text',
                                'http://ipinfo.io/',
                                'http://httpbin.org/ip',
                                'http://ip.ajn.me',
                                'https://diagnostic.opendns.com/myip',
                                'https://api.ipify.org']

        def get_externalip(self):
            '''
            This function gets your IP from a random server
            '''

            myip = ''
            for i in range(7):
                myip = self.fetch(random.choice(self.server_list))
                if myip != '':
                    return myip
                else:
                    continue
            return ''

        def fetch(self, server):
            '''
            This function gets your IP from a specific server.
            '''
            url = None
            opener = urllib.build_opener()
            opener.addheaders = [('User-agent',
                                  "Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0")]

            try:
                url = opener.open(server, timeout=2)
                content = url.read()

                # Didn't want to import chardet. Prefered to stick to stdlib
                if PY3K:
                    try:
                        content = content.decode('UTF-8')
                    except UnicodeDecodeError:
                        content = content.decode('ISO-8859-1')

                m = re.search(
                    '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)',
                    content)
                myip = m.group(0)
                return myip if len(myip) > 0 else ''
            except Exception:
                return ''
            finally:
                if url:
                    url.close()

        def test(self):
            '''
            This functions tests the consistency of the servers
            on the list when retrieving your IP.
            All results should be the same.
            '''

            resultdict = {}
            for server in self.server_list:
                resultdict.update(**{server: self.fetch(server)})

            ips = sorted(resultdict.values())
            ips_set = set(ips)
            print('\nNumber of servers: {}'.format(len(self.server_list)))
            print("IP's :")
            for ip, ocorrencia in zip(ips_set, map(lambda x: ips.count(x), ips_set)):
                print('{0} = {1} ocurrenc{2}'.format(ip if len(ip) > 0 else 'broken server', ocorrencia, 'y' if ocorrencia == 1 else 'ies'))
            print('\n')
            print(resultdict)

    msg = """From: Sender
    To: Recipient
    Subject: This is the message subject

    This is the message body.
    """

    msg = msg + myip()

    if((m == 10) and sendEmail):
        try:
            s = smtplib.SMTP('smtp.gmail.com:587')
            s.ehlo()
            s.starttls()
            s.login('myEmail@host.com', 'myPassword')
            s.sendmail(from_addr, to_addrs, msg)
            s.quit()
	    sendEmail = False
        except smtplib.SMTPException:
            print ("Error: " +  sys.exc_info()[0])
    if((m == 50) and not sendEmail):
	sendEmail = True
