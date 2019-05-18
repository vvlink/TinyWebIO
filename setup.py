from setuptools import setup
import sdist_upip

setup(name='mpython-tinywebio',
      version='0.0.8',
      description='App Inventor TinyWebDB server port to mPython',
      long_description='This is a module ported from CPython standard library to be compatible with\nmPython interpreter. ',
      url='https://gitee.com/roadlabs/TinyWebIO',
      author='roadlabs',
      author_email='roadlabs@gmail.com',
      license='Public Domain',
      cmdclass={'sdist': sdist_upip.sdist},
      py_modules=['tinywebio'])
