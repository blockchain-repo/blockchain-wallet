# unichain-client

####0.[`install.sh`](./install.sh)

Install requirement with `./install.sh`


####1.[`create_account.py`](./create_account.py)

The role of this module is to create an account and write to the '.account' file

```
~/unichain-account$ python3 create_account.py MIKE
{
    "username": "MIKE",
    "verifying_key": "3yLFxcMPnc3ozT82Csn9EDbw1vBVSqYJq6oxF9FHwF7Y",
    "signing_key": "3JMBk1Qsrj6psv697CLVNxS7C3t9ZW4Zf5aweHVZCMZz"
}
```


####2.[`create_asset_tx.py`](./create_asset_tx.py)

A simple way to generate a `CREATE` transaction.

```
~/unichain-account$ python3 create_asset_tx.py 1000
{
    "transaction": {
        "metadata": {
            "id": "d06368b3-b72f-4f39-bede-ecca4f8bab96",
            "data": {
                "planet": "earth"
            }
        },
        "timestamp": "1489373697905",
        "fulfillments": [
            {
                "fulfillment": "cf:4:LCWslQuppEihgphGm0R7v0jHLd67v4JIQGvuQqbo6aME_LdhO4-yM-CK2qyKcFy7llAB5pSbMa2NFWDHTLd3WminowKHAotztu8bpwQX9-buPH9Ha79poFRTOa1luswL",
                "input": null,
                "owners_before": [
                    "3yLFxcMPnc3ozT82Csn9EDbw1vBVSqYJq6oxF9FHwF7Y"
                ],
                "fid": 0
            }
        ],
        "operation": "CREATE",
        "conditions": [
            {
                "owners_after": [
                    "3yLFxcMPnc3ozT82Csn9EDbw1vBVSqYJq6oxF9FHwF7Y"
                ],
                "amount": 1000,
                "cid": 0,
                "condition": {
                    "details": {
                        "type": "fulfillment",
                        "signature": null,
                        "public_key": "3yLFxcMPnc3ozT82Csn9EDbw1vBVSqYJq6oxF9FHwF7Y",
                        "bitmask": 32,
                        "type_id": 4
                    },
                    "uri": "cc:4:20:LCWslQuppEihgphGm0R7v0jHLd67v4JIQGvuQqbo6aM:96"
                }
            }
        ],
        "asset": {
            "id": "1",
            "updatable": false,
            "refillable": false,
            "divisible": true,
            "data": {
                "money": "RMB"
            }
        }
    },
    "id": "573fbfdc672714fbb4318e61f704d7ab479faa1319ba831b5f2015b03e4cf8dd",
    "version": 1
}
```

####3.[`transfer_asset_tx.py`](./transfer_asset_tx.py)

A simple way to generate a `TRANSFER` transaction.

```
~/unichain-account$ python3 transfer_asset_tx.py 5E5mXSHUX4mLJyL3jpbNhpoNputENJ9Wud7wyhBjT31X 200
{
    "id": "42d67b67c675370ccf160751c7d882910a9370959ec0b136f35f29ccbd56eb22",
    "version": 1,
    "transaction": {
        "operation": "TRANSFER",
        "metadata": null,
        "timestamp": "1489373829003",
        "asset": {
            "id": "1"
        },
        "fulfillments": [
            {
                "fulfillment": "cf:4:LCWslQuppEihgphGm0R7v0jHLd67v4JIQGvuQqbo6aOuI6SQkVlSsXZAopLAiPwwIq4R8QPzkhj1xBsh-ZI2nggI7WNW9vkI59aVtmn_Mfuch31R3q4Er3u6a-1JlO8E",
                "fid": 0,
                "input": {
                    "cid": 0,
                    "txid": "573fbfdc672714fbb4318e61f704d7ab479faa1319ba831b5f2015b03e4cf8dd"
                },
                "owners_before": [
                    "3yLFxcMPnc3ozT82Csn9EDbw1vBVSqYJq6oxF9FHwF7Y"
                ]
            }
        ],
        "conditions": [
            {
                "owners_after": [
                    "5E5mXSHUX4mLJyL3jpbNhpoNputENJ9Wud7wyhBjT31X"
                ],
                "condition": {
                    "details": {
                        "type": "fulfillment",
                        "signature": null,
                        "public_key": "5E5mXSHUX4mLJyL3jpbNhpoNputENJ9Wud7wyhBjT31X",
                        "bitmask": 32,
                        "type_id": 4
                    },
                    "uri": "cc:4:20:PsiwZR_uYx613wh4xbPSpdZ_Xzdu1gZQEqgWAk9w11Y:96"
                },
                "cid": 0,
                "amount": 200
            },
            {
                "owners_after": [
                    "3yLFxcMPnc3ozT82Csn9EDbw1vBVSqYJq6oxF9FHwF7Y"
                ],
                "condition": {
                    "details": {
                        "type": "fulfillment",
                        "signature": null,
                        "public_key": "3yLFxcMPnc3ozT82Csn9EDbw1vBVSqYJq6oxF9FHwF7Y",
                        "bitmask": 32,
                        "type_id": 4
                    },
                    "uri": "cc:4:20:LCWslQuppEihgphGm0R7v0jHLd67v4JIQGvuQqbo6aM:96"
                },
                "cid": 1,
                "amount": 800
            }
        ]
    }
}
```

####4.[`tx_record.py`](./tx_record.py)

The role of this module is to get transaction list of the account

```
~/unichain-account$ python3 tx_record.py
[
    {
        "amount": 1000,
        "owners_after": "3yLFxcMPnc3ozT82Csn9EDbw1vBVSqYJq6oxF9FHwF7Y",
        "owner_before": "3yLFxcMPnc3ozT82Csn9EDbw1vBVSqYJq6oxF9FHwF7Y",
        "timestamp": "2017-03-13 10:54:57",
        "operation": "CREATE"
    },
    {
        "amount": 200,
        "owners_after": "5E5mXSHUX4mLJyL3jpbNhpoNputENJ9Wud7wyhBjT31X",
        "owner_before": "3yLFxcMPnc3ozT82Csn9EDbw1vBVSqYJq6oxF9FHwF7Y",
        "timestamp": "2017-03-13 10:57:09",
        "operation": "TRANSFER"
    }
]
```

####5.[`account_utxo_balance.py`](./account_utxo_balance.py)

The role of this module is to get UTXO(unspent transaction output) of the account

```
~/unichain-account$ python3 account_utxo_balance.py
[
    {
        "txid": "a784445834b37caf74af8ad3a88f7b64c1e0b80c0235b08a5673957f02842c00",
        "cid": 1,
        "amount": 8000
    }
]
```

####6.[`merge_utxo.py`](./merge_utxo.py)

The role of this module is to merge UTXO(unspent transaction output)

 **Before merge:** 
```
$ python3 account_utxo_balance.py 
[
    {
        "txid": "36632526da8fdf31934158a6aacd1c21ee26003858d184fb979ced9df2d07062",
        "cid": 0,
        "amount": 2000
    },
    {
        "txid": "675afce0e8633017270bea6743ef28ae09aeb702743790b4255f237d7d1c4796",
        "cid": 0,
        "amount": 100
    }
]
```

```
~/unichain-account$ python3 merge_utxo.py 
{
    "id": "a96bef931c04eab65c2dc48ef19f83c5c3d0ddd0fed1d7c2da46f30f399d3729",
    "version": 1,
    "transaction": {
        "conditions": [
            {
                "owners_after": [
                    "C4ZFz1GVjeeEG2QK6yeHdUifff7ZGzBzgnzAi9DBw4qj"
                ],
                "amount": 2100,
                "condition": {
                    "uri": "cc:4:20:pFnF8dORD4qxWr5ySk1lHLthiCKphx2WVJHPzemVDIY:96",
                    "details": {
                        "type_id": 4,
                        "bitmask": 32,
                        "signature": null,
                        "type": "fulfillment",
                        "public_key": "C4ZFz1GVjeeEG2QK6yeHdUifff7ZGzBzgnzAi9DBw4qj"
                    }
                },
                "cid": 0
            }
        ],
        "fulfillments": [
            {
                "fulfillment": "cf:4:pFnF8dORD4qxWr5ySk1lHLthiCKphx2WVJHPzemVDIYCrA4PFrMsKaJ25K2x-PRs9Qv15zdK2A-ZuWr8CNg3F7_sa4MGstjh0ewjm3-HBpunRQq8XVcuSBy0aMceSVMJ",
                "fid": 0,
                "input": {
                    "txid": "36632526da8fdf31934158a6aacd1c21ee26003858d184fb979ced9df2d07062",
                    "cid": 0
                },
                "owners_before": [
                    "C4ZFz1GVjeeEG2QK6yeHdUifff7ZGzBzgnzAi9DBw4qj"
                ]
            },
            {
                "fulfillment": {
                    "type_id": 4,
                    "bitmask": 32,
                    "signature": null,
                    "type": "fulfillment",
                    "public_key": "C4ZFz1GVjeeEG2QK6yeHdUifff7ZGzBzgnzAi9DBw4qj"
                },
                "fid": 1,
                "input": {
                    "txid": "675afce0e8633017270bea6743ef28ae09aeb702743790b4255f237d7d1c4796",
                    "cid": 0
                },
                "owners_before": [
                    "C4ZFz1GVjeeEG2QK6yeHdUifff7ZGzBzgnzAi9DBw4qj"
                ]
            }
        ],
        "metadata": null,
        "timestamp": "1489397107315",
        "asset": {
            "id": "1"
        },
        "operation": "TRANSFER"
    }
}
```


 **After merge:** 
```
~/unichain-account$ python3 account_utxo_balance.py 
[
    {
        "amount": 2100,
        "txid": "a96bef931c04eab65c2dc48ef19f83c5c3d0ddd0fed1d7c2da46f30f399d3729",
        "cid": 0
    }
]
```