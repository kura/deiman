import os
from setuptools import setup
from setuptools import find_packages


version = __import__('deiman').__version__

setup(name='deiman',
      version=version,
      url='http://syslog.tv/deiman',
      author="Kura",
      author_email="kura@kura.io",
      maintainer="Kura",
      maintainer_email="kura@kura.io",
      description="Deiman is a Python utility class for daemonizing a process. It provides start and stop methods, as well as a method for retrieving running status information. Linux/Unix-only.",
      long_description=open('README.rst').read(),
      license=open('LICENSE').read(),
      platforms=['linux'],
      packages=find_packages(exclude=["*.tests"]),
      install_requires=[],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Operating System :: POSIX',
          'Operating System :: POSIX :: Linux',
          'Operating System :: Unix',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities',
      ],
      zip_safe=True,
)
