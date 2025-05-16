from setuptools import setup, find_packages

package_name = 'object_counter'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your@email.com',
    description='Object Counter using Arduino and ROS2',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'object_counter_node = object_counter.object_counter_node:main',
        ],
    },
)

