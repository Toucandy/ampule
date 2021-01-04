from setuptools import setup

setup(
   name = 'ampule',
   packages = ['ampule'],
   version = '0.9',
   description='Ampule (Automated MatPlotLib) -- serial non-interactive processing and plotting of tabular data',
   #url = 'https://github.com/Toucandy/ampule',
   #download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
   license='MIT',
   author = 'Ilya Pershin',
   author_email='pershin2010@gmail.com',
   install_requires = ['matplotlib', 'pandas', 'parse'],
   data_files=[('ampule', ['Makefile', 'ampule_config.mk'])],
   keywords = ['matplotlib', 'plotting', 'pandas'],
   classifiers=[
     'Development Status :: 4 - Beta',
     'Intended Audience :: Science/Research',
     'Topic :: Scientific/Engineering :: Information Analysis',
     'License :: OSI Approved :: MIT License',
     'Programming Language :: Python :: 3',
  ],
)
