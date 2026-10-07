import socketserver
import http.server
import json

from providers import auth_provider
from providers import data_provider

from processors import notification_processor

class ApiRequestHandler(http.server.BaseHTTPRequestHandler):
    
    def handle_post_version_1(self, paths, user):
        if not auth_provider.has_access(user, paths, "post"):
            self._send_status(403)
            return

        adders = {
            "warehouses": (data_provider.fetch_warehouse_pool, "add_warehouse"),
            "locations": (data_provider.fetch_location_pool, "add_location"),
            "transfers": (data_provider.fetch_transfer_pool, "add_transfer"),
            "items": (data_provider.fetch_item_pool, "add_item"),
            "item_lines": (data_provider.fetch_item_line_pool, "add_item_line"),
            "item_groups": (data_provider.fetch_item_group_pool, "add_item_group"),
            "item_types": (data_provider.fetch_item_type_pool, "add_item_type"),
            "inventories": (data_provider.fetch_inventory_pool, "add_inventory"),
            "suppliers": (data_provider.fetch_supplier_pool, "add_supplier"),
            "orders": (data_provider.fetch_order_pool, "add_order"),
            "clients": (data_provider.fetch_client_pool, "add_client"),
            "shipments": (data_provider.fetch_shipment_pool, "add_shipment"),
        }

        if paths[0] not in adders:
            self._send_status(404)
            return

        fetch_pool, add_name = adders[paths[0]]
        content_length = int(self.headers["Content-Length"])
        new_data = json.loads(self.rfile.read(content_length).decode())
        pool = fetch_pool()
        getattr(pool, add_name)(new_data)
        pool.save()
        notification_processor.push(f"Scheduled batch transfer {new_data['id']}")
        self._send_status(201)
       
    def do_GET(self):
        api_key = self.headers.get("API_KEY")
        user = auth_provider.get_user(api_key)

        if user is None:
            self._send_status(401)
            return

        try:
            paths = self.path.split("/")
            if len(paths) > 3 and paths[1] == "api" and paths[2] == "v1":
                self.handle_get_version_1(paths[3:], user)
            else:
                self._send_status(404)
        except Exception:
            self._send_status(500)

    def handle_get_version_1(self, paths, user):
        if not auth_provider.has_access(user, paths, "get"):
            self._send_status(403)
            return

        handlers = {
            "warehouses": self._get_warehouses,
            "locations": self._get_locations,
            "transfers": self._get_transfers,
            "items": self._get_items,
            "item_lines": self._get_item_lines,
            "item_groups": self._get_item_groups,
            "item_types": self._get_item_types,
            "inventories": self._get_inventories,
            "suppliers": self._get_suppliers,
            "orders": self._get_orders,
            "clients": self._get_clients,
            "shipments": self._get_shipments,
        }

        if not paths or paths[0] not in handlers:
            self._send_status(404)
            return

        handlers[paths[0]](paths)

    def _get_warehouses(self, paths):
        pool = data_provider.fetch_warehouse_pool()

        if len(paths) == 1:
            self._send_json(pool.get_warehouses())
        elif len(paths) == 2:
            self._send_json(pool.get_warehouse(int(paths[1])))
        elif len(paths) == 3 and paths[2] == "locations":
            locations = data_provider.fetch_location_pool()
            self._send_json(locations.get_locations_in_warehouse(int(paths[1])))
        else:
            self._send_status(404)

    def _get_locations(self, paths):
        pool = data_provider.fetch_location_pool()

        if len(paths) == 1:
            self._send_json(pool.get_locations())
        elif len(paths) == 2:
            self._send_json(pool.get_location(int(paths[1])))
        else:
            self._send_status(404)

    def _get_transfers(self, paths):
        pool = data_provider.fetch_transfer_pool()

        if len(paths) == 1:
            self._send_json(pool.get_transfers())
        elif len(paths) == 2:
            self._send_json(pool.get_transfer(int(paths[1])))
        elif len(paths) == 3 and paths[2] == "items":
            self._send_json(pool.get_items_in_transfer(int(paths[1])))
        else:
            self._send_status(404)

    def _get_items(self, paths):
        pool = data_provider.fetch_item_pool()

        if len(paths) == 1:
            self._send_json(pool.get_items())
        elif len(paths) == 2:
            self._send_json(pool.get_item(int(paths[1])))
        elif len(paths) == 3 and paths[2] == "inventory":
            inventory = data_provider.fetch_inventory_pool()
            self._send_json(inventory.get_inventories_for_item(int(paths[1])))
        elif len(paths) == 4 and paths[2:] == ["inventory", "totals"]:
            inventory = data_provider.fetch_inventory_pool()
            self._send_json(inventory.get_inventory_totals_for_item(int(paths[1])))
        else:
            self._send_status(404)

    def _get_item_lines(self, paths):
        pool = data_provider.fetch_item_line_pool()

        if len(paths) == 1:
            self._send_json(pool.get_item_lines())
        elif len(paths) == 2:
            self._send_json(pool.get_item_line(int(paths[1])))
        elif len(paths) == 3 and paths[2] == "items":
            items = data_provider.fetch_item_pool()
            self._send_json(items.get_items_for_item_line(int(paths[1])))
        else:
            self._send_status(404)

    def _get_item_groups(self, paths):
        pool = data_provider.fetch_item_group_pool()

        if len(paths) == 1:
            self._send_json(pool.get_item_groups())
        elif len(paths) == 2:
            self._send_json(pool.get_item_group(int(paths[1])))
        elif len(paths) == 3 and paths[2] == "items":
            items = data_provider.fetch_item_pool()
            self._send_json(items.get_items_for_item_group(int(paths[1])))
        else:
            self._send_status(404)

    def _get_item_types(self, paths):
        pool = data_provider.fetch_item_type_pool()

        if len(paths) == 1:
            self._send_json(pool.get_item_types())
        elif len(paths) == 2:
            self._send_json(pool.get_item_type(int(paths[1])))
        elif len(paths) == 3 and paths[2] == "items":
            items = data_provider.fetch_item_pool()
            self._send_json(items.get_items_for_item_type(int(paths[1])))
        else:
            self._send_status(404)

    def _get_inventories(self, paths):
        if len(paths) == 1:
            pool = data_provider.fetch_inventory_pool()
            self._send_json(pool.get_inventories())
        else:
            self._send_status(404)

    def _get_suppliers(self, paths):
        pool = data_provider.fetch_supplier_pool()

        if len(paths) == 1:
            self._send_json(pool.get_suppliers())
        elif len(paths) == 2:
            self._send_json(pool.get_supplier(int(paths[1])))
        elif len(paths) == 3 and paths[2] == "items":
            items = data_provider.fetch_item_pool()
            self._send_json(items.get_items_for_supplier(int(paths[1])))
        else:
            self._send_status(404)

    def _get_orders(self, paths):
        pool = data_provider.fetch_order_pool()

        if len(paths) == 1:
            self._send_json(pool.get_orders())
        elif len(paths) == 2:
            self._send_json(pool.get_order(int(paths[1])))
        elif len(paths) == 3 and paths[2] == "items":
            self._send_json(pool.get_items_in_order(int(paths[1])))
        else:
            self._send_status(404)

    def _get_clients(self, paths):
        pool = data_provider.fetch_client_pool()

        if len(paths) == 1:
            self._send_json(pool.get_clients())
        elif len(paths) == 2:
            self._send_json(pool.get_client(int(paths[1])))
        elif len(paths) == 3 and paths[2] == "orders":
            orders = data_provider.fetch_order_pool()
            self._send_json(orders.get_orders_for_client(int(paths[1])))
        else:
            self._send_status(404)

    def _get_shipments(self, paths):
        pool = data_provider.fetch_shipment_pool()

        if len(paths) == 1:
            self._send_json(pool.get_shipments())
        elif len(paths) == 2:
            self._send_json(pool.get_shipment(int(paths[1])))
        elif len(paths) == 3 and paths[2] == "orders":
            self._send_json(pool.get_order_ids_in_shipment(int(paths[1])))
        elif len(paths) == 3 and paths[2] == "items":
            self._send_json(pool.get_items_in_shipment(int(paths[1])))
        else:
            self._send_status(404)

    def _send_json(self, value):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(value).encode("utf-8"))

    def _send_status(self, status_code):
        self.send_response(status_code)
        self.end_headers()

    def _read_json_body(self):
        content_length = int(self.headers.get("Content-Length", 0))
        if content_length <= 0:
            return {}
        post_data = self.rfile.read(content_length)
        return json.loads(post_data.decode())

    def _save_and_respond(self, pool):
        pool.save()
        self.send_response(200)
        self.end_headers()
    
    def _update_and_respond(self, pool, resource_id, payload, update_handler):
        update_handler(resource_id, payload)
        self._save_and_respond(pool)
        
    def do_POST(self):
        api_key = self.headers.get("API_KEY")
        user = auth_provider.get_user(api_key)
        if user is None:
            self.send_response(401)
            self.end_headers()
        else:
            try:
                paths = self.path.split("/")
                if len(paths) > 3 and paths[1] == "api" and paths[2] == "v1":
                    self.handle_post_version_1(paths[3:], user)
            except Exception:
                self.send_response(500)
                self.end_headers()

    def handle_put_version_1(self, paths, user):
        if not auth_provider.has_access(user, paths, "put"):
            self._send_status(403)
            return

        handlers = {
            "transfers": self._put_transfers,
            "orders": self._put_orders,
            "shipments": self._put_shipments,
        }

        if paths[0] in handlers:
            handlers[paths[0]](paths)
        else:
            self._put_simple(paths)

    def _put_simple(self, paths):
        updaters = {
            "warehouses": (data_provider.fetch_warehouse_pool, "update_warehouse"),
            "locations": (data_provider.fetch_location_pool, "update_location"),
            "items": (data_provider.fetch_item_pool, "update_item"),
            "item_lines": (data_provider.fetch_item_line_pool, "update_item_line"),
            "item_groups": (data_provider.fetch_item_group_pool, "update_item_group"),
            "item_types": (data_provider.fetch_item_type_pool, "update_item_type"),
            "suppliers": (data_provider.fetch_supplier_pool, "update_supplier"),
            "clients": (data_provider.fetch_client_pool, "update_client"),
        }

        if paths[0] not in updaters or len(paths) != 2:
            self._send_status(404)
            return

        fetch_pool, update_name = updaters[paths[0]]
        pool = fetch_pool()
        self._update_and_respond(pool, int(paths[1]), self._read_json_body(), getattr(pool, update_name))

    def _put_transfers(self, paths):
        if len(paths) == 2:
            pool = data_provider.fetch_transfer_pool()
            self._update_and_respond(pool, int(paths[1]), self._read_json_body(), pool.update_transfer)
        elif len(paths) == 3 and paths[2] == "commit":
            self._commit_transfer(int(paths[1]))
        else:
            self._send_status(404)

    def _commit_transfer(self, transfer_id):
        transfer_pool = data_provider.fetch_transfer_pool()
        inventory_pool = data_provider.fetch_inventory_pool()
        transfer = transfer_pool.get_transfer(transfer_id)

        for x in transfer["items"]:
            self._move_inventory(
                inventory_pool,
                x["item_id"],
                transfer["from_location_id"],
                transfer["to_location_id"],
                x["amount"],
            )

        transfer["transfer_status"] = "Processed"
        transfer.pop("items", None)
        transfer_pool.update_transfer(transfer_id, transfer)
        notification_processor.push(f"Processed batch transfer with id:{transfer['id']}")
        transfer_pool.save()
        inventory_pool.save()
        self._send_status(200)

    def _move_inventory(self, inventory_pool, item_id, from_location_id, to_location_id, amount):
        src = inventory_pool.get_inventory(item_id, from_location_id)
        if src is not None:
            src["quantity_on_hand"] -= amount
            inventory_pool.update_inventory(item_id, from_location_id, src)

        dst = inventory_pool.get_inventory(item_id, to_location_id)
        if dst is not None:
            dst["quantity_on_hand"] += amount
            inventory_pool.update_inventory(item_id, to_location_id, dst)
        else:
            inventory_pool.add_inventory(
                {
                    "item_id": item_id,
                    "location_id": to_location_id,
                    "quantity_on_hand": amount,
                    "quantity_expected": 0,
                    "quantity_ordered": 0,
                    "quantity_allocated": 0,
                }
            )

    def _put_orders(self, paths):
        pool = data_provider.fetch_order_pool()

        if len(paths) == 2:
            self._update_and_respond(pool, int(paths[1]), self._read_json_body(), pool.update_order)
        elif len(paths) == 3 and paths[2] == "items":
            self._update_and_respond(pool, int(paths[1]), self._read_json_body(), pool.update_items_in_order)
        else:
            self._send_status(404)

    def _put_shipments(self, paths):
        pool = data_provider.fetch_shipment_pool()

        if len(paths) == 2:
            self._update_and_respond(pool, int(paths[1]), self._read_json_body(), pool.update_shipment)
        elif len(paths) == 3 and paths[2] == "orders":
            self._update_and_respond(pool, int(paths[1]), self._read_json_body(), pool.update_orders_in_shipment)
        elif len(paths) == 3 and paths[2] == "items":
            self._update_and_respond(pool, int(paths[1]), self._read_json_body(), pool.update_items_in_shipment)
        else:
            self._send_status(404)
            
    def handle_delete_version_1(self, paths, user):
        if not auth_provider.has_access(user, paths, "delete"):
            self._send_status(403)
            return

        removers = {
            "warehouses": (data_provider.fetch_warehouse_pool, "remove_warehouse"),
            "locations": (data_provider.fetch_location_pool, "remove_location"),
            "transfers": (data_provider.fetch_transfer_pool, "remove_transfer"),
            "items": (data_provider.fetch_item_pool, "remove_item"),
            "item_lines": (data_provider.fetch_item_line_pool, "remove_item_line"),
            "item_groups": (data_provider.fetch_item_group_pool, "remove_item_group"),
            "item_types": (data_provider.fetch_item_type_pool, "remove_item_type"),
            "suppliers": (data_provider.fetch_supplier_pool, "remove_supplier"),
            "orders": (data_provider.fetch_order_pool, "remove_order"),
            "clients": (data_provider.fetch_client_pool, "remove_client"),
            "shipments": (data_provider.fetch_shipment_pool, "remove_shipment"),
        }

        if paths[0] not in removers or len(paths) < 2:
            self._send_status(404)
            return

        fetch_pool, remove_name = removers[paths[0]]
        pool = fetch_pool()
        getattr(pool, remove_name)(int(paths[1]))
        self._save_and_respond(pool)

    def do_PUT(self):
        api_key = self.headers.get("API_KEY")
        user = auth_provider.get_user(api_key)
        if user is None:
            self.send_response(401)
            self.end_headers()
        else:
            try:
                paths = self.path.split("/")
                if len(paths) > 3 and paths[1] == "api" and paths[2] == "v1":
                    self.handle_put_version_1(paths[3:], user)
            except Exception:
                self.send_response(500)
                self.end_headers()


    def do_DELETE(self):
        api_key = self.headers.get("API_KEY")
        user = auth_provider.get_user(api_key)
        if user is None:
            self.send_response(401)
            self.end_headers()
        else:
            try:
                paths = self.path.split("/")
                if len(paths) > 3 and paths[1] == "api" and paths[2] == "v1":
                    self.handle_delete_version_1(paths[3:], user)
            except Exception:
                self.send_response(500)
                self.end_headers()

if __name__ == "__main__":
    PORT = 3000
    with socketserver.TCPServer(("", PORT), ApiRequestHandler) as httpd:
        notification_processor.start()
        print(f"Serving on port {PORT}...")
        httpd.serve_forever()