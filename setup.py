from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'del_jrs'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')), 
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Deli Laszlo',
    maintainer_email='deli.laszlo.viktor@hallgato.sze.hu',
    description='AJR Kis feleves beadando turtlesim pine tree drawing package',
    license='GNU General Public License v3.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cmd_gen_node = del_jrs.cmd_gen_node:main',
        ],
    },
)
