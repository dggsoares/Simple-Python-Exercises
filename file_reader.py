from requests import get as get_http

with open('file.txt', 'r') as f:
    data = f.read()
    print(data)

with open('file.txt', 'w') as f:
    data = 'Data to write in file'
    f.write(data)