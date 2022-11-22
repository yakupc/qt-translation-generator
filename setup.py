from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(name='qttranslationgenerator',
      version='0.0.2',
      description='qt translation generator',
      long_description=readme,
      url='https://github.com/yakupc/qt-translation-generator',
      download_url='https://github.com/yakupc/qt-translation-generator.git',
      author='Yakup Cengiz',
      author_email='yakupcengiz@gmail.com',
      license=license,
      packages=find_packages(exclude=('test', 'doc')),
      zip_safe=False)