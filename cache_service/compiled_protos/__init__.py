import sys
from pathlib import Path

# Append current directory to sys.path so that the compiled protos can be imported.
sys.path.append(str(Path(__file__).parent))
