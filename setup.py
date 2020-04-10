from distutils.core import setup

setup(
  name = 'CodeDrop',
  packages = ['CodeDrop'],
  version = '0.1',
  license='MIT',
  description = 'Upload python files directly from your script to dropbox.',
  author = 'Pritom Sarker',
  author_email = 'pritoms@gmail.com',
  url = 'https://github.com/pritoms/CodeDrop',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['dropbox api', 'code upload', 'dropbox code upload', 'python script dropbox', 'python code upload dropbox'],
  install_requires=[
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)