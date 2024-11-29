from setuptools import find_packages, setup

package_name = 'turtle_navigation'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='efliao',
    maintainer_email='efliao@cs.nctu.edu.tw',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'motion_controller_node = turtle_navigation.motion_controller_node:main',
            'obstacle_detector_node = turtle_navigation.obstacle_detector_node:main',
        ],
    },
)
