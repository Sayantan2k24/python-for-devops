with open("server.conf", "r") as file:
    lines = file.readlines()
    print(lines)

'''    
$ python test3.py
['# Server Configuration File\n', '\n', '# Network Settings\n', 'PORT = 8080\n', 'MAX_CONNECTIONS=600\n', 'TIMEOUT = 30\n', '\n', '# 
Security Settings\n', 'SSL_ENABLED = true\n', 'SSL_CERT = /path/to/certificate.pem\n', '\n', '# Logging Settings\n', 'LOG_LEVEL = INFO\n', 'LOG_FILE = /var/log/server.log\n', '\n', '# Other Settings\n', 'ENABLE_FEATURE_X = true']

'''

