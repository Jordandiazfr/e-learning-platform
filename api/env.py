import os
# Set environment variables


def set_env():
    os.environ['MYSQL_USER'] = 'root'
    os.environ['MYSQL_PASS'] = '1234'
    os.environ['MYSQL_HOST'] = 'dbserver'
    #os.environ['MYSQL_DATABASE'] = 'testpy'
    return "env setted"

# Get environment variables
#USER = os.getenv('API_USER')
