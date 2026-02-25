import random
from rich.console import Console
from rich.table import Table
from rich.text import Text

console = Console()

chance_of_success = [
    0.5, 0.6, 0.7
]

task_count = 100

console.print(f"\n[bold]Number of tasks: {task_count}[/bold]\n")
for chance in chance_of_success:
    success = int(chance*task_count)
    tasks = ['1']*success + ['0']*(task_count-success)
    tasks.sort(key=lambda x:random.random())
    tasks = ''.join(tasks)

    chains = tasks.split('0')
    chains = [c for c in chains if len(c)>0]
    chains.sort(key=len)

    lengths = {}
    for c in chains:
        lengths[len(c)] = lengths.get(len(c),0)+1

    console.print(f"[bold cyan]Chance of success: {int(chance*100)}%[/bold cyan]")

    # Color-coded task sequence
    task_display = Text()
    for ch in tasks:
        if ch == '1':
            task_display.append("█", style="green")
        else:
            task_display.append("░", style="red")
    console.print(task_display)

    # Table for chain length distribution
    table = Table(show_header=True, header_style="bold magenta", padding=(0, 1))
    table.add_column("Chain Length", justify="center")
    table.add_column("Count", justify="center")
    table.add_column("Visual", justify="left")
    for length, count in sorted(lengths.items()):
        table.add_row(
            str(length),
            str(count),
            "●" * count,
        )
    console.print(table)
    console.print()