# config.py
import yaml
import os
from dotenv import load_dotenv

class Config:
    def __init__(self, config_path="config.yaml"):
        self.config_path = config_path
        # Load environment variables from .env file
        load_dotenv()
        self.load_config()
    
    def load_config(self):
        if not os.path.exists(self.config_path):
            self.create_default_config()
        
        with open(self.config_path, 'r') as f:
            config = yaml.safe_load(f)
        
        # Load API key from environment variable
        self.openrouter_api_key = os.getenv('OPENROUTER_API_KEY', '')
        self.openrouter_model = config.get('openrouter_model', 'openai/gpt-3.5-turbo')
        self.system_prompt = config.get('system_prompt', 'You are a helpful assistant.')
        self.test_file_path = config.get('test_file_path', 'test-files/example.yaml')
    
    def create_default_config(self):
        default_config = {
            'openrouter_model': 'openai/gpt-3.5-turbo',
            'system_prompt': 'You are a helpful assistant.',
            'test_file_path': 'test-files/competitive-intelligence.yaml'
        }
        
        with open(self.config_path, 'w') as f:
            yaml.dump(default_config, f, default_flow_style=False)
        
        print(f"Created default config file at {self.config_path}")
        print("Please create a .env file with your OPENROUTER_API_KEY and edit config.yaml with your preferences.")
