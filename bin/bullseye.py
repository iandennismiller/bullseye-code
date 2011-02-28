import sys
sys.path.append("/Users/idm/Code/academic/bullseye-code/lib")
sys.path.append("/Users/idm/Code/academic/bullseye-code/dep")
import Bullseye.Server

if __name__ == "__main__":
	path = "/Users/idm/Code/academic/bullseye-code"
	Bullseye.Server.go('localhost', 4567, path)
