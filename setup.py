import os
import glob
from setuptools import setup
from setuptools import find_packages

setup(name='deiman',
      version="0.1",
      url='http://syslog.tv/deiman',
      author="Kura",
      author_email="kura@kura.io",
      description="Deiman is a Python utility class for daemonizing a process. It provides start and stop methods, as well as a method for retrieving running status information. Linux/Unix-only.",
      long_description=file(
          os.path.join(
              os.path.dirname(__file__),
              'README.rst'
          )
      ).read(),
      license='BSD',
      platforms=['linux'],
      packages=find_packages(exclude=["*.tests"]),
      install_requires=file(os.path.join(os.path.dirname(__file__),
                                         'requirements.txt')).read(),
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Topic :: Utilities',
      ],
      zip_safe=False,
)
