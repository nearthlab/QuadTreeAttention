#!/usr/bin/env python

from distutils.core import setup

setup(name='QTA',
      version='1.0',
      description='QuadTreeAttention modules for Nearthlab',
      author='Hyeokjoon Kwon',
      author_email='dsazz801@gmail.com',
      packages=['FeatureMatching', 'QuadtreeAttention',
      'QuadtreeAttention.functions', 'FeatureMatching.src.utils',
      'FeatureMatching.src.lightning', 'FeatureMatching.src.config'],
      package_dir={
            'FeatureMatching':'FeatureMatching',
      'QuadtreeAttention': 'QuadTreeAttention/QuadtreeAttention'},
     )

