# Link Shortner

a simple link shortener, Users can enter their long links and get a short link.

### Technologies
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) ![FastAPI](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white)

## How to Run?
### Clone the project
```bash
git clone https://github.com/AFzOfficial/link-shortner.git

cd link-shortner
```

### Setup env
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install depends
```bash
pip install -r requirements.txt
```

### Run Development Server
```bash
uvicorn main:app
```

Open [127.0.0.1:8000/admin/docs](http://127.0.0.1:8000/admin/docs) in your browser
