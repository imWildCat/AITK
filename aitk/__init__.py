__package__ = 'AITK'

# Versioning code from NLTK, Apache License, Version 2.0:
try:
    # If a VERSION file exists, use it
    version_file = os.path.join(os.path.dirname(__file__), 'VERSION')
    with open(version_file, 'r') as infile:
        __version__ = infile.read().strip()
except NameError:
    __version__ = 'unknown (running code interactively?)'
except IOError as ex:
    __version__ = "unknown (%s)" % ex
