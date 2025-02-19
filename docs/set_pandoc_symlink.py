"""Set the required symbolic link to `pandoc` binary.

This sets a symbolic link from the `bin` directory of the nox session's env to the
pandoc binary which was installed via pip install of the package `pypandoc-binary`.
"""

import pathlib
import sys

python_version = sys.version_info

p = pathlib.Path("../.nox/docs/bin/pandoc")
if not p.exists():
    p.symlink_to(pathlib.Path("../lib/site-packages/pypandoc/files/pandoc"))
