# Huawei LTE Band Selector

A Python script for selecting LTE frequency bands on a Huawei LTE router using the `huawei-lte-api` library.

## Features

- Connects to the Huawei router through its web management interface.
- Reads and displays the current signal information when supported by the router.
- Selects a specific LTE band, a combination of bands, or automatic band selection.
- Displays the LTE band mask applied to the router.
- Uses the router's API to apply network settings.

## Requirements

- Python 3.8 or later.
- A compatible Huawei LTE router with API access enabled.
- A computer connected to the router's network.
- Router administrator credentials.

## Installation

### 1. Check Python

Open Command Prompt or PowerShell and run:

```bash
python --version
```

If that command does not work, try:

```bash
py --version
```

### 2. Install the required library

```bash
python -m pip install huawei-lte-api
```

If you use the Python launcher instead:

```bash
py -m pip install huawei-lte-api
```

## Configuration

Edit the configuration section at the beginning of the Python script:

```python
ROUTER_IP = "192.168.8.1"
USERNAME = "admin"
PASSWORD = "YOUR_ROUTER_PASSWORD"

TARGET = "B8"

SUPPORTED_BANDS = {1, 3, 5, 8, 40, 41}
AUTO_MASK = "7FFFFFFFFFFFFFFF"
```

| Setting | Description |
|---|---|
| `ROUTER_IP` | Router management IP address |
| `USERNAME` | Router administrator username |
| `PASSWORD` | Router administrator password |
| `TARGET` | LTE band or combination of bands to select |
| `SUPPORTED_BANDS` | Bands accepted by the script |
| `AUTO_MASK` | LTE band mask used for automatic selection |

**Security:** Keep your router password private. Avoid publishing credentials in source code or sharing them through version control.

## Supported Band Selection

Change `TARGET` to one of the following examples:

| Target | Description |
|---|---|
| `AUTO` | Automatic LTE band selection using the configured automatic mask |
| `B1` | LTE Band 1 |
| `B3` | LTE Band 3 |
| `B5` | LTE Band 5 |
| `B8` | LTE Band 8 |
| `B40` | LTE Band 40 |
| `B41` | LTE Band 41 |
| `B1+B8` | LTE Bands 1 and 8 |
| `B1+B3+B40` | LTE Bands 1, 3, and 40 |

The script validates the requested band numbers before attempting to change the router configuration.

**Note:** The bands listed above are the bands permitted by this script, not a guarantee that your router supports every band or carrier aggregation combination. Actual support depends on the router hardware, firmware, and mobile network.

## Usage

### 1. Save the script

Save your Python code as:

```text
huawei_band_selector.py
```

### 2. Configure the target band

For example, to select LTE Band 8:

```python
TARGET = "B8"
```

To use automatic selection:

```python
TARGET = "AUTO"
```

### 3. Run the script

Open Command Prompt in the folder containing the script and run:

```bash
python huawei_band_selector.py
```

Alternatively:

```bash
py huawei_band_selector.py
```

### 4. Check the output

Example output:

```text
Before: RSRP -85dBm | SINR 12dB | Band B3
Setting B8 (mask 0x80)...
Applied! The router may disconnect for 10-30 seconds while it reattaches.
```

The signal values above are illustrative. The actual output depends on your router's API response.

The script may temporarily lose connectivity while the router reconnects to the mobile network.

## How It Works

1. Builds a bitmask from the requested LTE band selection.
2. Connects to the router using `huawei-lte-api`.
3. Attempts to read the current signal information.
4. Calls `client.net.set_net_mode()` to apply the requested LTE band mask and network mode.
5. Prints a message indicating that the API call completed.

The script uses the following network settings:

```python
client.net.set_net_mode(
    lteband=mask,
    networkband="3FFFFFFF",
    networkmode="03",
)
```

The meanings of `networkband` and `networkmode`, and the behavior of the LTE mask, may depend on the router model and firmware. Verify that these values are appropriate for your device before using the script.

## Troubleshooting

### Cannot connect to the router

- Verify that the computer is connected to the router.
- Confirm the router IP address.
- Check the administrator username and password.
- Check whether the router permits API access.

### Python module not found

Run:

```bash
python -m pip install huawei-lte-api
```

Ensure that the package is installed in the same Python environment used to execute the script.

### Invalid or unsupported band

Check the `SUPPORTED_BANDS` set and ensure that `TARGET` uses the expected format, such as `B8` or `B1+B8`.

### Router disconnects after applying a band

A temporary disconnection may be expected while the router reattaches to the mobile network. If it does not reconnect, verify that the selected band is available in your area and supported by the router.

### Signal information is unavailable

The signal endpoint may return different fields depending on the router model and firmware. The script catches errors when reading signal information, but the band-selection request may still fail independently.

## Important Notes

- This script changes the router's network configuration.
- Selecting a band that is unavailable at your location may result in no mobile connection.
- The script's `AUTO_MASK` value should not be assumed to represent every LTE band supported by every Huawei router.
- Successful execution of the API call does not necessarily confirm that the router applied the requested band. Verify the active band through the router interface or its status API.

## Disclaimer

Use this script on a router you own or are authorized to administer. Keep your administrator credentials secure and verify your router's supported LTE bands before changing network settings.
