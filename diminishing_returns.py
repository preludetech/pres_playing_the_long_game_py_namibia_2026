import random
from collections import defaultdict
from rich.console import Console
from rich.table import Table
from rich.text import Text

console = Console()

chance_of_success = [
    0.5, 0.6, 0.7
]

task_count = 100
runs = 1

console.print(f"\n[bold]Number of tasks: {task_count}, averaged over {runs} runs[/bold]\n")
for chance in chance_of_success:
    total_lengths = defaultdict(float)

    for _ in range(runs):
        success = int(chance * task_count)
        tasks = ['1'] * success + ['0'] * (task_count - success)
        random.shuffle(tasks)
        tasks = ''.join(tasks)

        chains = tasks.split('0')
        chains = [c for c in chains if len(c) > 0]

        lengths = {}
        for c in chains:
            lengths[len(c)] = lengths.get(len(c), 0) + 1

        for length, count in lengths.items():
            total_lengths[length] += count

    avg_lengths = {k: v / runs for k, v in total_lengths.items()}

    console.print(f"[bold cyan]Chance of success: {int(chance * 100)}%[/bold cyan]")

    # Sample task sequence for visual
    success = int(chance * task_count)
    tasks = ['1'] * success + ['0'] * (task_count - success)
    random.shuffle(tasks)
    tasks = ''.join(tasks)

    task_display = Text()
    for ch in tasks:
        if ch == '1':
            task_display.append("█", style="green")
        else:
            task_display.append("░", style="red")
    console.print(task_display)

    # Table for average chain length distribution
    table = Table(show_header=True, header_style="bold magenta", padding=(0, 1))
    table.add_column("Chain Length", justify="center")
    table.add_column("Avg Count", justify="center")
    table.add_column("Visual", justify="left")
    for length, avg_count in sorted(avg_lengths.items()):
        table.add_row(
            str(length),
            f"{avg_count:.1f}",
            "●" * int(round(avg_count)),
        )
    console.print(table)
    console.print()
