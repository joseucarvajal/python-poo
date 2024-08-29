# Technical instructions

## Create and activate Python virtual environment
```bash
    python3 -m venv venv
    source venv/bin/activate
```

## Install dependencies
Create file *requirements.txt*

```bash
    pip3 install -r requirements.txt
```

## Run streamlit project

```bash
    chmod +x run_mac.sh
    ./run_mac.sh
```


# Utilities

## Steps to remove virtual environment
```bash
    deactivate
    rm -rf venv
```

## Common errors:
ERROR: Could not install packages due to an OSError: Could not find a suitable TLS CA certificate bundle, invalid path: /Users/dev/ai/ai-agent-extract-data-from-image/venv/lib/python3.12/site-packages/certifi/cacert.pem
```bash
    (security find-certificate -a -p ls /System/Library/Keychains/SystemRootCertificates.keychain &&  security find-certificate -a -p ls /Library/Keychains/System.keychain) > $HOME/.mac-ca-roots
```
```bash
    export REQUESTS_CA_BUNDLE="$HOME/.mac-ca-roots"
```