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

## Vision

### Current Capabilities

Currently, this framework processes OpenRouter agents and provides a foundation for LLM evaluation.

**Example use cases:**
- Testing accuracy of a search model, like Perplexity Sonar-Pro
- Ensuring a customer service bot maintains appropriate tone
- Evaluating prompt effectiveness across different models

### Future Roadmap

**Core Goals:**
- **Quick evaluator setup**: Jumpstart an evaluator for testing complex agents with minimal configuration
- **Developer-focused**: Allow developers to focus purely on writing clever eval functions and providing sample data
- **Template library**: Create a diverse library of evaluation templates including:
  - Coding ability assessment functions
  - MCP evaluators for AI agents
  - Custom evaluation templates from the community
- **Community contributions**: Enable developers to add their own eval functions and templates to the library

### Enterprise Integration

This framework could be particularly useful for platforms like Theoriq.ai, where creating hundreds of custom evaluators for agents is a core part of the business model. Potential integrations include:
- Theoriq SDK compatibility
- Hashing and caching mechanisms for crypto style communication and reputation scores
- Custom metric tracking