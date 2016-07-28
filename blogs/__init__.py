if __name__ == "__main__" and __package__ is None:
	from sys import path
	from os.path import direname
	path.append(direname(path[0]))
	__package__ = "settings"