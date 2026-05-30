import sys
import BrainFuck
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run.py <file.bf>")
        sys.exit(1)
    with open(sys.argv[1], 'r') as f:
        BrainFuck.run(f.read())