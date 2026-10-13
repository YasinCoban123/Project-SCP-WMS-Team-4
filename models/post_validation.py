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