import sys
from pathlib import Path

# Ensure the package root is importable when running this script directly
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from shared.config.settings import settings

print(settings.APP_NAME)
print(settings.APP_VERSION)
print(settings.PORT)