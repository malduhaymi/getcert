import requests

f = open("C:\\ips.txt", "r")
for ip in f:
    
      try:
        #getting the IP 
        newIP=ip.strip()
        #HTTPS request 
        requests.get("https://"+newIP)
      except requests.exceptions.SSLError:
            try:
                import ssl
                import OpenSSL
                cert = ssl.get_server_certificate((newIP, 443))
                #getting the cert info
                cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
                #print IP & issued to  
                print newIP+" || "+cert.get_subject().get_components()[-1][1]
            except Exception,e:
                print e

