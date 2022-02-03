from setuptools import setup, find_packages

setup(name='pathology',
      version='1.0',
      url='https://github.com/itttgg/botting_py',
      license='MIT',
      author='itttgg',
      author_email='aitiiigg1@gmail.com',
      description='Creating bots for yourself',
      packages=find_packages(exclude=['bottingpy']),
      long_description=open('README.md').read(),
      zip_safe=False)