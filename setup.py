from setuptools import setup
import serializers

thing = setup(
  name = serializers.__title__,
  packages = [serializers.__title__],
  version = serializers.__version__,
  description = 'A minimal port of rails\' ActiveModel Serializer',
  author = 'Greg Orlov',
  author_email = 'gaorlov@gmail.com',
  url = 'https://github.com/gaorlov/serializer',
  download_url = "https://github.com/gaorlov/serializer/archive/" + serializers.__version__ + ".tar.gz",
  install_requires=['future'],
  keywords = ['serializer', 'serializing', 'serialization', 'json', 'active model serializer'],
  classifiers = [
    'Development Status :: 3 - Alpha',
    'Environment :: Web Environment',
    'Natural Language :: English',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.6',
    'Topic :: Utilities',
  ],
)
