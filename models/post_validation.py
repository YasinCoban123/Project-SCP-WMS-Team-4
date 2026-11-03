def has_required_fields(data, required_fields):
    if not isinstance(data, dict):
        return False
    for field in required_fields:
        if field not in data:
            return False
    return True


def id_exists(existing_data, new_id):
    for record in existing_data:
        if record["id"] == new_id:
            return True
    return False

def has_correct_types(data, field_types):
    for field, expected_type in field_types.items():
        if field not in data:
            continue
        if isinstance(expected_type, tuple):
            allowed_types = expected_type
        else:
            allowed_types = (expected_type,)

        if type(data[field]) not in allowed_types:
            return False

    return True

def has_valid_items(items, item_types):
    if not isinstance(items, list):
        return False

    for item in items:
        if not has_required_fields(item, item_types):
            return False

        if not has_correct_types(item, item_types):
            return False
   # set_items_for_order allows unit_price to be omitted.
# If provided, it must be an int or float.
        if "unit_price" in item:  
            if type(item["unit_price"]) not in (int, float):
                return False

    return True