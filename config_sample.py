TERM_INIT_CONFIG = {
    # instead of local server running this web terminal service
    # "domain" is the target that you want to access through local server (with this web terminal)
    # and before doing so - make sure you have username and port (on the "domain") to implement remote access
    'domain': '192.168.56.3', # or ip address like 192.168.10.11
    'client_path': {
        'telnet': '/usr/bin/telnet', # confirmed location of your client binary (with cmd like 'which telnet')
        'ssh': '/usr/bin/ssh'
    }
}