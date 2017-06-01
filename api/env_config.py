# import os
# import configparser
# import socket

# # Read in config file
# config = configparser.ConfigParser()
# config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

# env = socket.gethostname()

# # Same accross all envs
# access_token = config['wit.ai']['access_token']

# # Env specific vars
# if 'ip' in env: #We are in production env (EC2 hostname begins with ip, no dev boxes do)
# 	path_to_db = os.path.join(os.path.dirname(__file__), config['prod']['path_to_db'])

# else:
# 	path_to_db = os.path.join(os.path.dirname(__file__), config['dev']['path_to_db'])

access_token = 'IND2N4JZSL3GLEX4AIBOJQDYDTYSQALY'