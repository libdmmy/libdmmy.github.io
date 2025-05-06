import shutil
import os

def copy_wellknown(config, **kwargs):
    site_dir = config['site_dir']
    shutil.copytree(".well-known", os.path.join(site_dir, '.well-known'), dirs_exist_ok=True)