<p align="center">
  <img src="assets/banner.png" alt="DebugAI Banner" width="800">
</p>

# 🛠️ DebugAI: AI-Powered Terminal Error Fixer

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Gemini 2.5](https://img.shields.io/badge/AI-Gemini%202.5%20Flash-green.svg)](https://ai.google.dev/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/username/debug-ai/graphs/commit-activity)

**DebugAI** is a lightning-fast CLI tool that uses Google's Gemini 2.5 Flash to instantly explain and fix your terminal errors. Stop wasting time Googling stack traces—just type `fix` and get back to coding.

---

## ✨ Features

- **🚀 Instant Fixes**: Get a one-sentence solution for any terminal error in seconds.
- **🧠 Powered by Gemini 2.5 Flash**: Leverages the latest in multimodal AI for high-accuracy reasoning.
- **💻 Cross-Platform**: Optimized for Windows, macOS, and Linux.
- **⚡ Minimalist CLI**: No complex flags, just zero-friction debugging.
- **🔧 Easy Setup**: Install via pip and you're ready to go.

---

## 📦 Installation

Install DebugAI directly from your project directory:

```bash
pip install -e .
```

---

## ⚙️ Configuration

Set up your Gemini API key to start using DebugAI:

### Windows (PowerShell)
```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

### Linux / macOS
```bash
export GEMINI_API_KEY="your_api_key_here"
```

> [!TIP]
> Add the export command to your `.bashrc` or `.zshrc` to make it permanent!

---

## 🚀 Usage

Whenever you encounter an error in your terminal, simply wrap it in quotes and pass it to the `fix` command:

```bash
fix "SyntaxError: invalid syntax"
```

### Example Output:
```text
Fix: Review your code for typos or incorrect indentation in the preceding lines.
```

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<p align="center">
  Developed with ❤️ by <a href="https://github.com/yourusername">Shihab</a>
</p>
