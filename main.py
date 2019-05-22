"""ToDo."""
from tasks.kyu6 import nba_cup, R


def run_nba_cup():
    """Run 6kyu task"""
    team = input('Enter the name of the team:   ')
    print(nba_cup(R, team))

if __name__ == '__main__':
    run_nba_cup()
