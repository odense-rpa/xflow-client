# XFlow Client

Python-klient til XFlow — wrapper om XFlow's REST API.

> Denne klient er ikke officielt støttet eller godkendt af XFlow. Brug på eget ansvar.

## Nuværende funktionalitet

- Dokumenter
- Processer og processkabeloner
- Rettighedsgrupper
- Brugere
- Værdilister

## Installation

```bash
uv add git+https://github.com/odense-rpa/xflow-client
```

## Forudsætninger

- Python ≥ 3.13
- XFlow-instans med API-token

## Brug

```python
from xflow_client import XFlowClient, ProcessClient

client = XFlowClient(instance="din-kommune", token="dit-token")
processer = ProcessClient(client)
```

## Konfiguration

| Variabel | Beskrivelse |
|---|---|
| `INSTANCE` | XFlow-instansnavnet (f.eks. `odense`) |
| `TOKEN` | XFlow API-token |

## Licens

MIT
