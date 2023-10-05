head = {
    'value': 11,  # 1st node
    'next': {
        'value': 3,  # 2nd node
        'next': {
            'value': 23,  # 3rd node
            'next': {
                'value': 7,  # 4th node
                'next': None
            }
        }
    }
}

print(head['next']['next']['value'])
