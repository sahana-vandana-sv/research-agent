
def mock_search(query:str)->str:
    # This is a mock search function that simulates searching for information.
    # In a real implementation, this could be an API call to a search engine or a database query.
    return (
        f"Search results for: '{query}'\n"
        "---\n"
        "Finding 1: Sleep deprivation impairs prefrontal cortex function, "
        "reducing decision-making and attention span after 17-19 hours awake.\n"
        "Finding 2: Chronic sleep loss (<6 hrs/night) raises cortisol levels "
        "and increases risk of type 2 diabetes and cardiovascular disease.\n"
        "Finding 3: REM sleep is critical for memory consolidation; "
        "disruption impairs learning retention by up to 40%."
    )

