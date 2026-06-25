from web3 import Web3

RPC_URL = "https://rpc.example.com"
PRIVATE_KEY = "YOUR_PRIVATE_KEY"
ACCOUNT = "0xYourAddress"

w3 = Web3(Web3.HTTPProvider(RPC_URL))

contract = w3.eth.contract(
    address="0xContractAddress",
    abi=ABI
)

tx = contract.functions.claim().build_transaction({
    "from": ACCOUNT,
    "nonce": w3.eth.get_transaction_count(ACCOUNT),
    "gas": 200000,
    "gasPrice": w3.eth.gas_price,
    "chainId": 1
})

signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

print(f"Tx sent: {tx_hash.hex()}")
#This comment is a test to do for my 17th commit
