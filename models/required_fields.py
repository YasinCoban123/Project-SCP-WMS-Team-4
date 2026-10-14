REQUIRED_FIELDS = {
    "items": [
        "id", "code", "description", "barcode", "model_number",
        "commodity_code", "unit_weight", "item_line_id",
        "item_group_id", "item_type_id", "min_purchase_qty",
        "case_size", "packaging_type", "order_multiple",
        "supplier_id", "supplier_sku"
    ],

    "item_types": ["id", "name", "description"],
    "item_lines": ["id", "name", "description"],
    "item_groups": ["id", "name", "description"],

    "locations": ["id", "warehouse_id", "code", "name"],

    "warehouses": [
        "id", "code", "name", "address", "city", "zip_code",
        "province", "country", "contact_name",
        "contact_phone", "contact_email"
    ],

    "clients": [
        "id", "name", "address", "city", "zip_code",
        "province", "country", "contact_name",
        "contact_phone", "contact_email"
    ],

    "suppliers": [
        "id", "code", "name", "address", "city", "zip_code",
        "province", "country", "contact_name",
        "phone_number", "reference"
    ],

    "inventories": [
        "item_id", "location_id", "quantity_on_hand",
        "quantity_expected", "quantity_ordered",
        "quantity_allocated"
    ],

    "orders": [
        "id", "client_id", "order_date", "request_date",
        "reference", "customer_po_number", "order_status",
        "shipping_notes", "warehouse_id",
        "ship_to_client_id", "bill_to_client_id", "items"
    ],

    "shipments": [
        "id", "reference", "order_id", "shipment_date",
        "shipment_type", "shipment_status", "carrier_name",
        "shipping_method", "payment_type", "items"
    ],

    "transfers": [
        "id", "reference", "from_location_id",
        "to_location_id", "items"
    ],
}