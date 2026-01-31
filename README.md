# Setup & Running the Project

### 1. Clone Repository
```bash
git clone https://github.com/Darsh-Rawat/video-recommendation-system.git
cd your-repo-name
```

### 2. Backend Setup
Install uv (if not already installed)
```bash
pip install uv
```

Install dependencies
```bash
cd backend
uv sync
```

Run the following command **only once** during the initial setup:<br/>
This will populate the vector DB

```bash
uv run core/db.py
```

Starting server
```bash
uv run main.py
```

### 3. Frontend Setup
Make sure to be in the root directory of the project (if not)
```bash
cd ..
```
Then
```bash
cd frontend
npm install
npm run dev
```
