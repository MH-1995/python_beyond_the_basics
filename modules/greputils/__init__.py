from .files import (
    grepfile,
    grepfilei,
)

from .contain import (
    contains,
    containsi,
)

# following works, but we have repreated code in both
# __init__.py files.  It is useful if
# second ./net/__init__.py is empty
# (doesn't expose any interfaces)

# from .net.html import (
#     grep_html,
#     grep_html_as_text,
# )

# from .net.json import (
#     grep_json,
# )

# from .net.text import (
#     grep_text
# )

# this only works if ./net/__init__.py exposes
# those function
from .net import (
    grep_html,
    grep_html_as_text,
    grep_json,
    grep_text,
)
