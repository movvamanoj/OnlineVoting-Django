import os

ALLOWED_HOSTS = [
    os.getenv('EC2_HOST'),
    f'http://{os.getenv("EC2_HOST")}/'
]
