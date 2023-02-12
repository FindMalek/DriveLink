import shutil
import os
from logging import log


log = log.getLogger(__name__)

def delete_pycache_folders(directory):
    for root, dirs, files in os.walk(directory):
        if "__pycache__" in dirs:
            shutil.rmtree(os.path.join(root, "__pycache__"))
            log.debug(f'Deleted __pycache__ folder in {os.path.join(root, "__pycache__")}')