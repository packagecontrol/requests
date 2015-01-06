import os.path

from package_control import sys_path

dependency_dir = os.path.dirname(sys_path.generate_dependency_paths('requests')['ver'])

sys_path.add(os.path.join(dependency_dir, 'all'))
