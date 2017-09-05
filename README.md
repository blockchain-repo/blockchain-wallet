# unichain-client

### Quick Start

```
[optional]sudo apt-get update
[optional]sudo apt-get install g++ python3-dev libffi-dev build-essential libssl-dev
[optional]sudo apt-get install python3-pip
[optional]sudo pip3 install --upgrade pip setuptools

sudo pip3 install -r requirements.txt
[optional]python3 config.py
[optional]vim .unichain-account <modify the default config and save>
python3 manage.py
```

Then, open `localhost:5000` in your browser

### Default Config (.unichain-account)

```
{
    "server": {
        "port": "9984",
        "host": "localhost"
    },
    "username": "user",
    "keypair": {
        "public":  "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "private": "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
    }
}
```