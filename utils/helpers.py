def normalize_name(name: str) -> str:
    """Normalise un nom en minuscule, sans espaces ni tirets"""
    return name.lower().replace(" ", "").replace("-", "")
