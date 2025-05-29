# README.md

# Model Evaluation Framework

An open-source tool to help you evaluate LLMs and prompts for your specific use case using OpenRouter.

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
   git clone https://github.com/aly-001/eval-forge
   cd eval-forge
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

# Vision

## Current 

### Processes Openrouter agents

### Example use cases
- Testing accuracy of a search model, like perplexity sonar-pro
- Ensuring a customer service bot maintains appropriate tone

## Future capabilities 

### Be able to jumpstart an evaluator for testing complex agents
### Developers can focus purely on writing a clever eval function and providing the sample data.
### Also, I want to create a diverse library of templates. For example, a coding ability assessment eval function, or an MCP evaluator for AI agents. I also want to be able to collect templates from other devs so that people can add their own eval functions and templates to the library.

## This could be useful for something like Theoriq.ai where creating hundreds of custom evaluators for agents is large part of the business model. It could integrate with Theoriq SDK, manage hashing, etc.