from distutils.core import setup

long_description = \
'''Documentation, usage, and implementation can be found on the Github_.

.. _Github: http://github.com/citruspi/V.I.R.A.
'''

setup(
    name='vira',
    version='0.0.1',
    author='Mihir Singh',
    author_email='me@mihirsingh.com',
    packages=['vira'],
    url='http://github.com/citruspi/V.I.R.A.',
    license='MIT License',
    description='Virtual Information Retrieval Assistant',
    long_description=long_description,
    install_requires=[
                        'wordnik',
                        'requests',
                        'twilio',
                        'wolframalpha'
                     ],
    classifiers=[
                    'Development Status :: 3 - Alpha',
                    'Intended Audience :: Developers',
                    'License :: OSI Approved :: MIT License',
                    'Programming Language :: Python',
                    'Topic :: System :: Networking',
                    'Topic :: Internet'
                ]
)