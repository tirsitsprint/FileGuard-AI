# FileGuard AI – Intelligent File Integrity Monitoring System

## 1. Project Overview

FileGuard AI is a Python-based file integrity monitoring system designed to detect unauthorized or unexpected changes to important files.

The system uses the SHA-256 hashing algorithm to create a unique fingerprint for each registered file. When a file is verified, FileGuard AI compares its current hash with the originally stored hash to identify whether the file has been modified or deleted.

It also records security events, assigns risk levels, and uses Google's Gemini AI to explain detected events and provide security recommendations.

## 2. Features

- **File Registration:** Register files and store their SHA-256 fingerprints.
- **File Integrity Verification:** Detect changes in registered files.
- **File Deletion Detection:** Identify when a registered file no longer exists.
- **Security Event Logging:** Record detected events with timestamps.
- **Risk Assessment:** Classify security events as LOW, MEDIUM, or HIGH.
- **Gemini AI Analysis:** Analyze the latest security event and provide explanations and recommendations.
- **JSON Storage:** Store file fingerprints and security event records locally.

## 3. Technologies Used

- Python
- SHA-256 (Hashlib)
- JSON
- Google Gemini API
- Google Gen AI Python SDK
- Python-dotenv

## 4. Project Structure

```text
FileGuard-AI/
│
├── main.py
├── integrity.py
├── storage.py
├── security.py
├── ai_analyzer.py
├── config.py
├── database.json
├── logs.json
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## 5. Installation and Setup

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the project folder

```bash
cd FileGuard-AI
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure the Gemini API key

Create a `.env` file in the project root directory:

```env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=your_supported_gemini_model
```

Replace the placeholders with your own Gemini API key and supported model name.

**Important:** Never share or upload your actual API key.

### Step 5: Run the application

```bash
python main.py
```

## 6. How to Use

1. Run the application.
2. Select **Register a file** to register a file.
3. Select **Verify file integrity** to check whether the file has changed.
4. Select **View security event history** to see recorded security events.
5. Select **AI security analysis** to receive an explanation of the latest security event.
6. Select **Exit** to close the application.

## 7. Risk Classification

| Event | Risk Level |
|---|---|
| File modified | MEDIUM |
| File deleted | HIGH |
| Other event types | LOW |

## 8. Limitations

- File verification is performed manually by the user; continuous background monitoring is not implemented.
- File fingerprints and event records are stored locally in JSON files.
- The local database can be modified by someone with access to the project files.
- Gemini AI recommendations are advisory and should not be treated as proof of a cyberattack.

## 9. Future Improvements

- Real-time file monitoring.
- Email or desktop security notifications.
- Stronger protection for stored file fingerprints.
- Improved security reporting and visualization.
- More advanced threat detection.

## 10. Disclaimer

FileGuard AI is an educational cybersecurity project developed to demonstrate file integrity monitoring, hashing, security event logging, and AI-assisted security analysis.

---

**Developed as a Python cybersecurity project.**
