#!/usr/bin/env python3
"""Index a directory for semantic search using the same code path as the MCP tool."""

import sys
import argparse
import logging
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from mcp_server.code_search_server import CodeSearchServer


def main():
    parser = argparse.ArgumentParser(
        description="Index a directory for semantic search (no MCP timeout)"
    )
    parser.add_argument("directory", help="Directory to index")
    parser.add_argument("--name", help="Project name (default: directory name)")
    parser.add_argument("--full", action="store_true", help="Force full reindex")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    directory = str(Path(args.directory).resolve())
    if not Path(directory).exists():
        print(f"Error: {directory} does not exist", file=sys.stderr)
        sys.exit(1)

    print(f"Indexing: {directory}")
    srv = CodeSearchServer()
    result = srv.index_directory(
        directory,
        project_name=args.name,
        incremental=not args.full,
    )
    print(result)


if __name__ == "__main__":
    main()
