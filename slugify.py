import re
import unicodedata


def slugify(value, separator="-"):
    """Create stable, Unicode-preserving heading IDs for MkDocs."""
    value = unicodedata.normalize("NFKC", str(value)).strip().lower()
    value = re.sub(r"[^\w\s-]", "", value, flags=re.UNICODE)
    value = re.sub(r"[\s-]+", separator, value, flags=re.UNICODE)
    return value.strip(separator)