def build_summary(items: list[str]) -> str:
    """Describe how many demo items were provided."""
    count = sum(bool(item.strip()) for item in items)
    return f"Demo summary: {count} item(s)"