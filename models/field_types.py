FIELD_TYPES = {
    "item_types": {
        "id": int,
        "name": str,
        "description": str
    },

    "item_lines": {
        "id": int,
        "name": str,
        "description": str
    },

    "item_groups": {
        "id": int,
        "name": str,
        "description": str
    },

    "items": {
        "id": int,
        "code": str,
        "description": str,
        "barcode": str,
        "model_number": str,
        "commodity_code": int,
        "unit_weight": (int, float),
        "item_line_id": int,
        "item_group_id": int,
        "item_type_id": int,
        "min_purchase_qty": int,
        "case_size": int,
        "packaging_type": str,
        "order_multiple": int,
        "supplier_id": int,
        "supplier_sku": str
    },

    "locations": {
        "id": int,
        "warehouse_id": int,
        "code": str,
        "name": str
    },

    "warehouses": {
        "id": int,
        "code": str,
        "name": str,
        "address": str,
        "city": str,
        "zip_code": str,
        "province": str,
        "country": str,
        "contact_name": str,
        "contact_phone": str,
        "contact_email": str
    },

    "clients": {
        "id": int,
        "name": str,
        "address": str,
        "city": str,
        "zip_code": str,
        "province": str,
        "country": str,
        "contact_name": str,
        "contact_phone": str,
        "contact_email": str
    },

    "suppliers": {
        "id": int,
        "code": str,
        "name": str,
        "address": str,
        "city": str,
        "zip_code": str,
        "province": str,
        "country": str,
        "contact_name": str,
        "phone_number": str,
        "reference": str
    },

    "inventories": {
        "item_id": int,
        "location_id": int,
        "quantity_on_hand": int,
        "quantity_expected": int,
        "quantity_ordered": int,
        "quantity_allocated": int
    },

    "orders": {
        "id": int,
        "client_id": int,
        "order_date": str,
        "request_date": str,
        "reference": str,
        "customer_po_number": str,
        "order_status": str,
        "shipping_notes": (str, type(None)),
        "warehouse_id": int,
        "ship_to_client_id": int,
        "bill_to_client_id": int,
        "items": list
    },

    "shipments": {
        "id": int,
        "reference": str,
        "order_id": int,
        "shipment_date": str,
        "shipment_type": str,
        "shipment_status": str,
        "carrier_name": str,
        "shipping_method": str,
        "payment_type": str,
        "items": list
    },

    "transfers": {
        "id": int,
        "reference": str,
        "from_location_id": int,
        "to_location_id": int,
        "items": list
    }
}

ORDER_ITEM_TYPES = {
    "item_id": int,
    "amount": int
}