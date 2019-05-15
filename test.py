import sys

FILE_NAME = sys.argv[0].split('/')[-1]
FILE_PATH = '/'.join(sys.argv[0].split('/')[:-1])

print(FILE_PATH + '/' + FILE_NAME)

print(sys.argv[0])