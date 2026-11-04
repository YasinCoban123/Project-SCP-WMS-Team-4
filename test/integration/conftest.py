# import pytest


# # Alle integration tests gebruiken de json files in deze map
# DATA_TEST_DIR = "../../data_test"
# JSON_FILES = [
#     DATA_TEST_DIR + "/client.json",
#     DATA_TEST_DIR + "/inventory.json",
#     DATA_TEST_DIR + "/item.json",
#     DATA_TEST_DIR + "/item_group.json",
#     DATA_TEST_DIR + "/item_line.json",
#     DATA_TEST_DIR + "/item_type.json",
#     DATA_TEST_DIR + "/location.json",
#     DATA_TEST_DIR + "/order.json",
#     DATA_TEST_DIR + "/order_item.json",
#     DATA_TEST_DIR + "/shipment.json",
#     DATA_TEST_DIR + "/shipment_item.json",
#     DATA_TEST_DIR + "/supplier.json",
#     DATA_TEST_DIR + "/transfer.json",
#     DATA_TEST_DIR + "/transfer_item.json",
#     DATA_TEST_DIR + "/user.json",
#     DATA_TEST_DIR + "/warehouse.json",
# ]


# # Door auto use voert pytest deze fixture automatisch uit voor elke integration test
# @pytest.fixture(autouse=True)
# def reset_test_data():
#     # Bewaar de oorspronkelijke inhoud voordat de test data wijzigt
#     original_data = {
#         file: open(file, "rb").read()
#         for file in JSON_FILES
#     }

#     yield

#     # Zet de oorspronkelijke inhoud terug 
#     # zodat tests elkaar niet beinvloeden en data niet word gewijzigd
#     for file, data in original_data.items():
#         open(file, "wb").write(data)