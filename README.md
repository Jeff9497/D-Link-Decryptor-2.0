# D-Link Firmware Decryptor

## Description

This script transforms the binary code from D-Link router firmware `.bin` files into human-readable assembly language. It aids in understanding the low-level operations of the firmware by converting the binary instructions into a more interpretable format.

## Requirements

- Python 3
- Radare2
- r2dec

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/dlink-firmware-decryptor.git](https://github.com/Jeff9497/D-Link-Decryptor-2.0
    cd D-link-Decryptor-2.0
    ```

2. Install Radare2:

    ```bash
    git clone https://github.com/radareorg/radare2.git
    cd radare2
    sys/install.sh
    ```

3. Install r2dec:

    ```bash
    r2pm init
    r2pm update
    r2pm install r2dec
    ```

## Usage

1. Place your D-Link firmware `.bin` file in the project directory.
2. Run the decryption script:

    ```bash
    python3 dlink-dec.py 
    ```

## Example

```bash
python3 dlink-dec.py 
```
You will then be required to state the name of the .bin file 

This will decrypt the specified firmware file and output the assembly code.

## Contributing

Feel free to submit issues or pull requests if you have any improvements or suggestions.

---
