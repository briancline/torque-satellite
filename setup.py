from setuptools import setup


setup(
    name='torque-satellite',
    version='0.1.0',
    author='Brian Cline',
    author_email='brian.cline@gmail.com',
    description='A web-based frontend with requisite back-end components '
                'to process real time GPS/OBDII updates from the Torque Pro '
                'and Torque Lite apps on Android.',
    long_description=open('README.md').read(),
    license='MIT',
    keywords='torque api push car gps obdii obd',
    url='https://github.com/briancline/torque-satellite',
    packages=['torque-satellite'],
    install_requires=['msgpack', 'mosquitto'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Other Audience',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
    ],
)
