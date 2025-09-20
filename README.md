# R2 Pharos BOT
R2 Pharos BOT

- Register Here : [R2 Money](https://www.r2.money/)
- Connect Same Wallet With Pharos

## Features

  - Auto Get Account Information
  - Auto Run With Private Proxy - `Choose 1`
  - Auto Run Without Proxy - `Choose 2`
  - Auto Make R2 Swap Tx
  - Auto Make R2 Earn Tx
  - Multi Accounts
  - **Check Token Balances Before Running Main Script**  
    *(Added by [zerosocialcode](https://github.com/zerosocialcode))*  
    - Use the new `balance.py` script to check the balances of available tokens before starting `bot.py`.

## Requiremnets

- Make sure you have Python3.9 or higher installed and pip.

## Instalation

1. **Clone The Repositories:**
   ```bash
   git clone https://github.com/vonssy/R2-Pharos-BOT.git
   ```
   ```bash
   cd R2-Pharos-BOT
   ```

2. **Install Requirements:**
   ```bash
   pip install -r requirements.txt #or pip3 install -r requirements.txt
   ```

### Note: Check your web3 and eth-account libraries version first. If not same with version in requirements.txt, u must uninstall that library.
- **Check Library Version**
  ```bash
    pip show libary_name
  ```
- **Uninstall Library**
  ```bash
    pip uninstall libary_name
  ```
- **Install Library With Version**
  ```bash
    pip install libary_name==version
  ```

## Configuration

- **accounts.txt:** You will find the file `accounts.txt` inside the project directory. Make sure `accounts.txt` contains data that matches the format expected by the script. Here are examples of file[...]
  ```bash
    your_private_key_1
    your_private_key_2
  ```

- **proxy.txt:** You will find the file `proxy.txt` inside the project directory. Make sure `proxy.txt` contains data that matches the format expected by the script. Here are examples of file formats:
  ```bash
    ip:port # Default Protcol HTTP.
    protocol://ip:port
    protocol://user:pass@ip:port
  ```

## Run

1. **Check Balances First (Recommended):**
   ```bash
   python balance.py #or python3 balance.py
   ```
   This will check the balances of available tokens for all configured accounts before running the main bot.

2. **Run Main Bot:**
   ```bash
   python bot.py #or python3 bot.py
   ```

## Buy Me a Coffee

- **EVM:** 0xe3c9ef9a39e9eb0582e5b147026cae524338521a
- **TON:** UQBEFv58DC4FUrGqinBB5PAQS7TzXSm5c1Fn6nkiet8kmehB
- **SOL:** E1xkaJYmAFEj28NPHKhjbf7GcvfdjKdvXju8d8AeSunf
- **SUI:** 0xa03726ecbbe00b31df6a61d7a59d02a7eedc39fe269532ceab97852a04cf3347

Thank you for visiting this repository, don't forget to contribute in the form of follows and stars.
If you have questions, find an issue, or have suggestions for improvement, feel free to contact me or open an *issue* in this GitHub repository.

**vonssy**

**Update: balance.py script integration and README update by [zerosocialcode](https://github.com/zerosocialcode)**
