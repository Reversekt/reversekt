def greeting(name: str) -> str:
    """Return a short greeting, using a default for blank names."""
    name = name.strip()
    return f"Hello, {name or 'there'}!"