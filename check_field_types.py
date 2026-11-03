from models.required_fields import REQUIRED_FIELDS
from models.field_types import FIELD_TYPES

for resource in REQUIRED_FIELDS:
    required_fields = REQUIRED_FIELDS[resource]
    defined_types = FIELD_TYPES[resource]

    for i in required_fields:
        if i not in defined_types:
            print(resource, i)