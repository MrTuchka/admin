from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

DEPLOYMENT_SERVER_SSH_KEY_PATH = env.str("DEPLOYMENT_SERVER_SSH_KEY_PATH")
DEPLOYMENT_SERVER_SSH_KEY_PASSPHRASE = env.str("DEPLOYMENT_SERVER_SSH_KEY_PASSPHRASE")

bot_deployer_connection_config = {
    "host": "159.223.20.147",
    "user": "botrunner",
    "connect_kwargs": {
        "key_filename": DEPLOYMENT_SERVER_SSH_KEY_PATH,
        "passphrase": DEPLOYMENT_SERVER_SSH_KEY_PASSPHRASE
    }
}

dp_api = {
  "type": "service_account",
  "project_id": "admin-db680",
  "private_key_id": "4359719644cd920fe26c44152a436e4aee4645fa",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDJ324pyfeE5aLz\nPPMoWFNqcrObxPhqVpBN38uMzyKLsZdlMJW51XrA0/2oWYJRlsQZwJKtTqJ66rLl\n9LztLfXFHyBs5ugmAXhD/XcD4Nrv9+8pOIlSrL45eqW5j7GbEZfUDJctCzJmNpx0\nWzLke8eRa7rc64ahWBVcgF4yc162YoL5Uw0ca06di1MemfZmI6e1r89nkb24BP82\nfYoSw/bWGDPedwLZYo6v/qkP5jieZ+DwbyDpiNGIYV59hXPwQMcSmb3o/zbcN/wp\nFiRaPp9dM+kfgut02GBhQjcg/ftRRw8uqUyDRoKljWp+Ikx7qiXaTk0XDIyT65xE\nBnd+fTZzAgMBAAECggEAQGsE617glk71BatwaHJvA+vgNpfPMZe36rG8cY1zl6Iv\nDoJHdQqTZk7/haYyeLikkRcrdxQ9sv2L4ueLFiBxadq57SZt9BrJ9uA+B0XMd4Dl\nl4DMCU7IUO07TxB0e2hMy8TMxPnqtkU8/cBQaCq7j0MSWQbrajcCcgcgh/baxVXu\n+ipDV8WUFanuqryqiPruu3dM2Itv7OWrkvEsa4ui5RL6Xg30Z4uCGoV2Yr1rZUj6\nQ4RNQG15kJchVZ0mDiZCndcbwJvRvZ82M+ryQrThUMbl+YE3uQc9q6gWHeevP6nr\nmH3KzQIpd5L/ld4Y+RgPTQbitfnN2MzMChjJB0zjKQKBgQDuCgaqPXMLURt43aPp\nz7b664oHmCyw7olgKEFApGKSy4n+N6Cg+9gSWuRDdnISQno+g+uJqHvB8+yqWJ5R\nOFtlUfzNyByEgTOmALV9zAPXJNyAAYeprcY4sOsA8/ZuF1I84LFU9k7Dhc937Wzr\nsZGRkaIrX3Uetcm9zY2z/qqKXwKBgQDZGtAYXuQj31sAc0fUSE7JFh2yj7NKNZC4\nJ6B23JZQ+RbBMEowyMsP77PRHH9+6ly3b5qn9FObX51Ivjrn+B8moE/ZFO5e2lzU\ni+JkjiqsJJsk535beAeuJbZQ8o5GvMN8gENO1TD0wYDsWS+0zGJ8mJrmOgb/Xw+V\nJs7nRFs0bQKBgQCbDzbmQJ8nWQ8/PYnf7enxK+u/JLbADrK4S6Ct/ickHqhmTFA7\nbbKDymd1Nrv5/wnonUCabIEph767/HwsxjxrFOxMFDXXbt55HW8cYgCCbkWgsN5x\nfnxoQ37iIQl/D3wHogqCIOyP2yOZqLTSF9qOa8Kq5ETD24FuPW84OAVZmwKBgEHU\nf4TkQQkfkNhyHDWiN0GCEz8xk4vM8jTkzyM7f9jNrrili9l/CROr+zpNCdvR9Isq\nrBqBW1ihhW+pPvNXqRptQcjxL9ZTIBLS17Ll6MqJzwFBsG7L1ohXpxCke7+3PQ9j\nVQVyX4XXpuADqxOHZdWh8FYfAkAs8uym99XoRD+BAoGBANKTLzoJbH6RnRFJuHnW\nVBOVETnhXGu7CWFJI2scY0aIq5TLME1PzGS9uKzcWoeOtw+2aWOVIN0kKUCFO5II\no9ouXfer+p60YD1nZ4PI/DTceJlQj46S7KHRWkAqOzsF0DsHVtTdcNtP5Sf/nS0P\nMOEliIynZLpEhtoAT3iO41Xz\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-zrhyh@admin-db680.iam.gserviceaccount.com",
  "client_id": "104798609848461421348",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-zrhyh%40admin-db680.iam.gserviceaccount.com"
}