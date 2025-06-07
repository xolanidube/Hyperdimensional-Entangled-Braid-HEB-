from heb import HEB


def demo_database_lookup():
    print("=== Ultra-fast lookups in massive databases ===")
    db = HEB()
    db.insert("customer:42", {"name": "Alice"})
    print("Inserted record for customer 42")
    result = db.search("customer:42")
    print("Lookup for customer 42 ->", result)


def demo_directory_index():
    print("\n=== Rapid indexing in large-scale directory structures ===")
    index = HEB()
    index.insert("/usr/bin/python", "python executable")
    print("Indexed /usr/bin/python")
    print("Lookup ->", index.search("/usr/bin/python"))


def demo_financial_data():
    print("\n=== High-frequency financial data retrieval ===")
    trades = HEB()
    trades.insert("AAPL", {"price": 192.5})
    print("Inserted trade for AAPL")
    print("Retrieve ->", trades.search("AAPL"))


def demo_routing_table():
    print("\n=== Accelerated network routing table lookups ===")
    routes = HEB()
    routes.insert("10.0.0.0/24", "gateway-1")
    print("Route for 10.0.0.0/24 added")
    print("Lookup ->", routes.search("10.0.0.0/24"))


if __name__ == "__main__":
    demo_database_lookup()
    demo_directory_index()
    demo_financial_data()
    demo_routing_table()
