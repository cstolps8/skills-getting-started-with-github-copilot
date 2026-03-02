# Getting Started with GitHub Copilot

<img src="https://octodex.github.com/images/Professortocat_v2.png" align="right" height="200px" />

Hey cstolps8!

Mona here. I'm done preparing your exercise. Hope you enjoy! 💚

Remember, it's self-paced so feel free to take a break! ☕️

[![](https://img.shields.io/badge/Go%20to%20Exercise-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/cstolps8/skills-getting-started-with-github-copilot/issues/1)

---

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup & Run

1. **Create a virtual environment:**
   ```bash
   python3 -m venv .venv
   ```

2. **Activate the virtual environment:**
   ```bash
   # On macOS/Linux:
   source .venv/bin/activate
   
   # On Windows:
   .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the application:**
   ```bash
   uvicorn src.app:app --reload --host 0.0.0.0 --port 8000
   ```

5. **Open in your browser:**
   - Navigate to `http://localhost:8000/static/index.html`

The application will automatically reload when you make code changes (due to the `--reload` flag).

### Running Tests
```bash
pytest
```

---

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)

