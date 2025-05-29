# README.md

# Model Evaluation Framework

An open-source tool to help you evaluate different LLMs and prompts for your specific use case using OpenRouter.

## Features

- 🚀 Simple YAML-based test configuration
- 🎯 Must-have/must-not-have evaluation criteria
- 📊 Real-time progress visualization
- 💾 Export results to JSON and CSV
- 🔧 Easily customizable for any use case
- 🔐 Secure API key management with .env files

## Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/model-eval-framework.git
   cd model-eval-framework
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**
   Create a `.env` file in the project root:
   ```bash
   echo "OPENROUTER_API_KEY=your_api_key_here" > .env
   ```
   Replace `your_api_key_here` with your actual OpenRouter API key.

4. **Run the evaluation**
   ```bash
   python main.py
   ```

## Configuration

The application uses two configuration files:
- `.env` - For sensitive data like API keys (not tracked in git)
- `config.yaml` - For application settings like model choice and prompts
