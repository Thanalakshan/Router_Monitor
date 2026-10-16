from huawei_lte_api.Client import Client
from huawei_lte_api.Connection import Connection

# --- CONFIGURATION ---
ROUTER_IP = "192.168.8.1"
USERNAME = "admin"
PASSWORD = "@thana132"

# Examples: "AUTO", "B8", "B1+B8", "B1+B3+B40"
TARGET = "B8"

SUPPORTED_BANDS = {1, 3, 5, 8, 40, 41}   # B38 removed
AUTO_MASK = "7FFFFFFFFFFFFFFF"           # all LTE bands = device auto mode


def build_mask(text):
    t = text.strip().upper().replace(" ", "")
    if t == "AUTO":
        return AUTO_MASK

    mask = 0
    for part in t.replace(",", "+").split("+"):
        if not part.startswith("B") or not part[1:].isdigit():
            raise ValueError(f"Invalid band '{part}'")
        n = int(part[1:])
        if n not in SUPPORTED_BANDS:
            raise ValueError(f"B{n} not supported. Allowed: {sorted(SUPPORTED_BANDS)}")
        mask |= 1 << (n - 1)
    return format(mask, "X")


def main():
    try:
        mask = build_mask(TARGET)
    except ValueError as e:
        print(f"Config error: {e}")
        return

    with Connection(f"http://{ROUTER_IP}/", username=USERNAME, password=PASSWORD) as connection:
        client = Client(connection)

        try:
            sig = client.device.signal()
            print(f"Before: RSRP {sig.get('rsrp', 'N/A')} | SINR {sig.get('sinr', 'N/A')} | Band {sig.get('band', 'N/A')}")
        except Exception as e:
            print(f"Could not read signal info: {e}")

        print(f"Setting {TARGET} (mask 0x{mask})...")
        client.net.set_net_mode(
            lteband=mask,
            networkband="3FFFFFFF",
            networkmode="03",
        )
        print("Applied! The router may disconnect for 10-30 seconds while it reattaches.")


if __name__ == "__main__":
    main()