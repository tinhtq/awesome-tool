import base64
import yaml
import os

secretName = "domain-tls"
namespace = "traefik"

list_of_files = os.listdir('.')
for file in list_of_files:
    if file.endswith(".crt"):
        f = open(file, "r")
        cert = f.read()
        certBytes = cert.encode("utf-8")
        certEncode = base64.b64encode(certBytes).decode("utf-8")
        f.close()
    elif file.endswith(".key"):
        f = open(file, "r")
        key = f.read()
        keyBytes = key.encode("utf-8")
        keyEncode = base64.b64encode(keyBytes).decode("utf-8")
        f.close()

secret_yaml = {
    'apiVersion': 'v1',
    'data': {
        'tls.crt': certEncode,
        'tls.key': keyEncode
    },
    'kind': 'Secret',
    'metadata': {
        'name': secretName,
        'namespace': namespace
    },
    'type': 'kubernetes.io/tls'
}

with open('./cert.yaml', 'w') as file:
    documents = yaml.dump(secret_yaml, file)
 