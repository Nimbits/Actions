import os
import subprocess
import json
import sys

def fetch_secrets(vault_url, secret_path):
    os.environ['VAULT_ADDR'] = vault_url
    vault_token = os.environ.get('VAULT_TOKEN')

    try:
        # Authenticate to Vault
        subprocess.run(['vault', 'login', vault_token], check=True)

        # Fetch secrets
        result = subprocess.run(['vault', 'kv', 'get', '-format=json', secret_path],
                                check=True, stdout=subprocess.PIPE)
        secrets = json.loads(result.stdout)

        # Set outputs
        for key in secrets['data']['data']:
            print(f"::set-output name={key}::{secrets['data']['data'][key]}")
    except Exception as e:
        print(f"Error fetching secrets: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    VAULT_URL = sys.argv[1]
    SECRET_PATH = sys.argv[2]

    fetch_secrets(VAULT_URL, SECRET_PATH)
