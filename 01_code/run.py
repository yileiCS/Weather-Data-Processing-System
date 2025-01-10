import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.api import start_api

if __name__ == "__main__":
    start_api() 