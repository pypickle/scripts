import argparse
import os
import shutil
import subprocess
from pathlib import Path


def delete_migrations(root_path=None, ignored_roots=None):
    if ignored_roots is None:
        ignored_roots = []

    if root_path is None:
        # Use the current working directory if root_path is not provided
        root_path = Path(__file__).parent
        print(f"Root is None, using {root_path}")

    for root, dirs, files in os.walk(root_path):
        # Exclude ignored roots
        if any(ignored_root in root for ignored_root in ignored_roots):
            continue

        # Delete migration files
        migrations_dirs = [d for d in dirs if d == "migrations"]
        for migration in migrations_dirs:
            migration_path = os.path.join(root, migration)
            shutil.rmtree(migration_path)
            print(f"Deleted: {migration_path}")

        # Delete __pycache__ directories
        pycache_dirs = [d for d in dirs if d == '__pycache__']
        for pycache_dir in pycache_dirs:
            pycache_path = os.path.join(root, pycache_dir)
            shutil.rmtree(pycache_path)
            print(f"Deleted: {pycache_path}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Delete migration files and __pycache__ directories.')
    parser.add_argument('--root', type=str, default=None,
                        help='Root directory to start deletion from')
    parser.add_argument('--ignore', nargs='+', default=[],
                        help='Directories to ignore (space-separated)')

    args = parser.parse_args()
    root_directory = args.root
    ignored_directories = args.ignore
    ignored_directories += ["postgresql"]

    delete_migrations(root_directory, ignored_directories)
    subprocess.run(["./manage.py", "makemigrations"], check=True)
