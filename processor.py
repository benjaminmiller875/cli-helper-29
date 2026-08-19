from typing import List, Dict, Any


def process_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Processes a list of data dictionaries.

    Args:
        data: A list of dictionaries to be processed.

    Returns:
        A list of processed dictionaries.
    """
    processed = []
    for item in data:
        processed_item = {k: v.strip() if isinstance(v, str) else v for k, v in item.items()}
        processed.append(processed_item)
    return processed


def summarize_data(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Summarizes a list of data dictionaries.

    Args:
        data: A list of dictionaries to be summarized.

    Returns:
        A dictionary containing summary data.
    """
    summary = {'total': len(data), 'fields': {}}
    for item in data:
        for k, v in item.items():
            if k not in summary['fields']:
                summary['fields'][k] = []
            summary['fields'][k].append(v)
    return summary
