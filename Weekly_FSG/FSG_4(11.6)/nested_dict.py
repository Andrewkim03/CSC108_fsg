def update_resident(country: str, province: str, city: str, resident_name: str, details: dict, geography: dict) -> None:
    """Update or add a resident's information in the geography dictionary.
    
    If the resident already exists, update their details. If the resident does not exist,
    add them with the provided details.
    
    >>> update_resident('Canada', 'Ontario', 'Toronto', 'Alice', {'age': 31, 'occupation': 'Senior Engineer'}, geography)
    >>> geography['Canada']['Ontario']['Toronto']['residents']['Alice']
    {'age': 31, 'occupation': 'Senior Engineer'}
    """
    
def add_city(country: str, province: str, city: str, geography: dict) -> None:
    """Add a city to the geography dictionary.
    If the country or province does not exist, create them.
    
    >>> add_city('Canada', 'Alberta', 'Calgary', geography)
    >>> geography['Canada']['Alberta']
    {'Calgary': {}}
    """

def city_exists(country: str, province: str, city: str, geography: dict) -> bool:
    """Return True if the city exists in the specified country and province.
    
    >>> city_exists('Canada', 'Ontario', 'Toronto', geography)
    True
    >>> city_exists('Canada', 'Ontario', 'Calgary', geography)
    False
    """
geography = {
    'Canada': {
        'Ontario': {
            'Toronto': {
                    'Alice': {'age': 30, 'occupation': 'Engineer'},
                    'Bob': {'age': 25, 'occupation': 'Designer'},
            },
            'Ottawa': {},
            'Hamilton': {}
        },
        'British Columbia': {
            'Vancouver': {},
            'Victoria': {},
            'Burnaby': {}
        }
    },
    'USA': {
        'California': {
            'Los Angeles': {},
            'San Francisco': {},
            'San Diego': {}
        },
        'Texas': {
            'Houston': {},
            'Dallas': {},
            'Austin': {}
        }
    }
}

# Testing the functions
add_city('Canada', 'Ontario', 'Mississuagua', geography)