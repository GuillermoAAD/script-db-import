# Virtual enviroment

## Virtual environment

### 1. Create virtual environment

```bash
# Unix/MacOS
python3 -m venv venv

# Windows
python -m venv venv
```

### 5. Activate virtual environment

```bash
# Unix/MacOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### Deactivate virtual environment

```bash
deactivate
```

---

## Dependencies

Install dependencies

```sh
pip install -r requirements.txt
```

Update requirements.txt

```sh
pip freeze > requirements.txt
```
