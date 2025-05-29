# test.py
import os
import sys
import time
from datetime import datetime
import json
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.panel import Panel
from rich.layout import Layout
from rich.live import Live

from config import Config
from openrouter_client import OpenRouterClient
from evaluator import Evaluator

console = Console()

class ModelTester:
    def __init__(self):
        self.config = Config()
        self.client = OpenRouterClient(self.config.openrouter_api_key, self.config.openrouter_model)
        self.evaluator = Evaluator(self.config.test_file_path)
        self.results = []
    
    def run_tests(self):
        console.clear()
        console.print(Panel.fit(f"[bold cyan]Model Evaluation Framework[/bold cyan]\n"
                               f"Model: {self.config.openrouter_model}\n"
                               f"Test Suite: {self.evaluator.tests['name']}"))
        
        total_tests = len(self.evaluator.tests['tests'])
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=console
        ) as progress:
            
            task = progress.add_task("[cyan]Running tests...", total=total_tests)
            
            for i, test in enumerate(self.evaluator.tests['tests']):
                progress.update(task, description=f"[cyan]Running: {test['name']}...")
                
                # Run the model
                response = self.client.complete(self.config.system_prompt, test['input'])
                
                # Evaluate the response
                score, details = self.evaluator.evaluate_response(
                    response,
                    test.get('must_have', []),
                    test.get('must_not_have', [])
                )
                
                self.results.append({
                    'test_name': test['name'],
                    'input': test['input'],
                    'response': response,
                    'score': score,
                    'details': details
                })
                
                progress.update(task, advance=1)
                time.sleep(0.5)  # Rate limiting
        
        self.display_results()
        self.save_results()
    
    def display_results(self):
        console.print("\n[bold green]Test Results[/bold green]\n")
        
        # Create summary table
        table = Table(title="Test Summary")
        table.add_column("Test Name", style="cyan")
        table.add_column("Score", style="magenta")
        table.add_column("Status", style="green")
        
        total_score = 0
        for result in self.results:
            score = result['score']
            total_score += score
            status = "✅ PASS" if score >= 7 else "⚠️  WARN" if score >= 5 else "❌ FAIL"
            table.add_row(result['test_name'], f"{score:.1f}/10", status)
        
        console.print(table)
        
        avg_score = total_score / len(self.results) if self.results else 0
        console.print(f"\n[bold]Average Score: {avg_score:.1f}/10[/bold]")
        
        # Show detailed results
        console.print("\n[bold]Detailed Results:[/bold]")
        for result in self.results:
            console.print(f"\n[cyan]{result['test_name']}[/cyan]")
            console.print(f"Input: {result['input']}")
            console.print(f"Score: {result['score']:.1f}/10")
            
            if result['details']['missing_required']:
                console.print(f"[red]Missing required:[/red] {', '.join(result['details']['missing_required'])}")
            if result['details']['found_forbidden']:
                console.print(f"[red]Found forbidden:[/red] {', '.join(result['details']['found_forbidden'])}")
    
    def save_results(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"results/evaluation_{self.config.openrouter_model.replace('/', '_')}_{timestamp}.json"
        
        os.makedirs("results", exist_ok=True)
        
        output = {
            'timestamp': timestamp,
            'model': self.config.openrouter_model,
            'system_prompt': self.config.system_prompt,
            'test_suite': self.evaluator.tests['name'],
            'results': self.results,
            'summary': {
                'total_tests': len(self.results),
                'average_score': sum(r['score'] for r in self.results) / len(self.results) if self.results else 0
            }
        }
        
        with open(filename, 'w') as f:
            json.dump(output, f, indent=2)
        
        console.print(f"\n[green]Results saved to: {filename}[/green]")
        
        # Ask if user wants to export to different format
        export = console.input("\nExport results to CSV? (y/n): ")
        if export.lower() == 'y':
            self.export_to_csv(timestamp)
    
    def export_to_csv(self, timestamp):
        import csv
        filename = f"results/evaluation_{self.config.openrouter_model.replace('/', '_')}_{timestamp}.csv"
        
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Test Name', 'Input', 'Score', 'Response'])
            
            for result in self.results:
                writer.writerow([
                    result['test_name'],
                    result['input'],
                    result['score'],
                    result['response'][:100] + '...' if len(result['response']) > 100 else result['response']
                ])
        
        console.print(f"[green]CSV exported to: {filename}[/green]")

def main():
    try:
        tester = ModelTester()
        
        if not tester.config.openrouter_api_key or tester.config.openrouter_api_key == 'YOUR_OPENROUTER_API_KEY_HERE':
            console.print("[bold red]Error:[/bold red] Please set your OpenRouter API key in config.yaml")
            sys.exit(1)
        
        tester.run_tests()
        
    except FileNotFoundError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        console.print("Make sure the test file exists in the path specified in config.yaml")
        sys.exit(1)
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
