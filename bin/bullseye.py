import os
import Bullseye.Server

if __name__ == "__main__":
	path = os.path.join(os.path.expanduser('~'), "Desktop", "bullseye-code")
	Bullseye.Server.go('localhost', 4567, path)
