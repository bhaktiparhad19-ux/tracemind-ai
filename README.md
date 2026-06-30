# 🛡️ TraceMind AI

### AI-Powered Digital Forensics & Incident Response Platform

TraceMind AI is an AI-assisted Digital Forensics and Incident Response (DFIR) platform that automatically analyzes Linux authentication logs, detects suspicious activity, identifies attack patterns, and generates professional incident reports using Google's Gemini AI.

Built for the **Global Tech Innovation 2026 Hackathon** under the **Cybersecurity & Privacy** track.

---

# 🚀 Features

- Authentication log analysis
- Automatic log parsing
- Brute-force attack detection
- Successful compromise detection
- Privilege escalation detection
- Indicators of Compromise (IOCs)
- AI-generated DFIR incident reports
- Interactive Streamlit dashboard
- Sample attack datasets included

---

# 🏗 Project Architecture

```
Authentication Logs
        │
        ▼
Evidence Collector
        │
        ▼
Log Parser
        │
        ▼
Threat Detector
        │
        ▼
Threat Intelligence
        │
        ▼
Gemini AI Analyst
        │
        ▼
Professional Incident Report
```

---

# 📂 Project Structure

```
tracemind-ai/
│
├── app.py
├── analyzer.py
├── config.py
├── requirements.txt
├── README.md
│
├── logs/
│   ├── auth.log
│   ├── bruteforce.log
│   ├── mixed_attack.log
│   ├── normal_activity.log
│   └── privilege_escalation.log
│
├── modules/
│   ├── ai_analyst.py
│   ├── evidence_collector.py
│   ├── log_parser.py
│   ├── report_exporter.py
│   ├── security_event.py
│   └── threat_detector.py
│
└── reports/
```

---

# 🧠 Detection Capabilities

TraceMind AI currently detects:

- Multiple Failed Login Attempts
- Brute Force Attacks
- Successful Login After Brute Force
- Privilege Escalation (sudo)
- Suspicious IP Addresses
- Target User Accounts

---

# 🤖 AI Integration

TraceMind AI integrates with **Google Gemini 2.5 Flash** to automatically generate:

- Executive Summary
- Attack Analysis
- Indicators of Compromise
- Risk Assessment
- Recommended Actions

The AI report is generated only from detected evidence without inventing unsupported events.

---

# 🖥 Technologies Used

- Python 3
- Streamlit
- Google Gemini API
- Regular Expressions
- Dataclasses
- Object-Oriented Programming

---

# ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/bhaktiparhad19-ux/tracemind-ai.git

cd tracemind-ai
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

# ▶ Running the Application

Run the Streamlit application

```bash
streamlit run app.py
```

Or run the command-line version

```bash
python analyzer.py
```

---

# 📊 Sample Workflow

1. Upload a Linux authentication log.
2. Parse authentication events.
3. Detect attack patterns.
4. Identify Indicators of Compromise.
5. Generate an AI incident report.
6. Review investigation results.

---

# 📷 Screenshots

Add screenshots here before submitting to the hackathon.

Suggested screenshots:

- Home Page
- Upload Log
- Threat Summary
- AI Incident Report

---

# 🎯 Hackathon Track

**Cybersecurity & Privacy**

Global Tech Innovation 2026

---

# 🔮 Future Improvements

- Multiple log source support
- Windows Event Log analysis
- MITRE ATT&CK Mapping
- Sigma Rule Detection
- PDF Report Export
- IOC Export (JSON)
- VirusTotal Integration
- Threat Intelligence Feeds
- Email Alerts
- Timeline Visualization
- Dashboard Analytics
- Docker Deployment

---

# 👩‍💻 Author

**Bhakti Parhad**

Cybersecurity Student

GitHub:
https://github.com/bhaktiparhad19-ux

---

# ⚠ Disclaimer

This project is intended solely for educational, research, and demonstration purposes.

The author is not responsible for any misuse of this software.

---

# © Copyright

Copyright © 2026 Bhakti Parhad

All Rights Reserved.

This repository and its source code are the intellectual property of the author.

No part of this project may be copied, modified, redistributed, or used in other projects, commercial products, academic submissions, or competitions without prior written permission from the author.

Unauthorized reproduction or distribution of this software is prohibited.
