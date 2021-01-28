#
# Parse example code
#
# https://docs.python.org/3.9/howto/argparse.html
#
import argparse
import socket

def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-s", "--server", help="defaults to localhost", default="localhost")
    args = parser.parse_args()

    h=socket.gethostname()
    print('hostname = {0}'.format(h))
    l=socket.gethostbyname(h)
    print('IP = {0}'.format(l))

    url = "http://{0}".format(args.server)
    print("url = {0}".format(url))

if __name__ == "__main__":
    main()
