# Internal variable to hold the CV in memory
_cv_data = None

def save_cv(cv_dict: dict) -> None:
    """Saves a CV dictionary to the in-memory store."""
    global _cv_data
    _cv_data = cv_dict

def get_cv() -> dict | None:
    """Retrieves the CV dictionary from the in-memory store."""
    return _cv_data

def clear_cv() -> None:
    """Clears the CV dictionary from the in-memory store."""
    global _cv_data
    _cv_data = None

def is_cv_loaded() -> bool:
    """Returns True if a CV is currently loaded, False otherwise."""
    return _cv_data is not None
