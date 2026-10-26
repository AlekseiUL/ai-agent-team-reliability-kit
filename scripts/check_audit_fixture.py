"""Require the intended negative CLI result, not an arbitrary failure."""
import json
import subprocess
import sys

p = subprocess.run([sys.executable, '-m', 'agent_team_reliability.cli',
                    'audit-tasks', 'examples/tasks'], capture_output=True, text=True)
assert p.returncode == 1, (p.returncode, p.stderr)
receipt = json.loads(p.stdout)
assert receipt['ok'] is False and receipt['files_checked'] == 4, receipt
expected = {'Owner', 'Goal', 'Allowed paths', 'Forbidden paths', 'Privacy level',
            'External side-effect policy', 'Verification required', 'Expected final summary/report'}
assert len(receipt['findings']) == len(expected), receipt
assert {f['missing'] for f in receipt['findings']} == expected, receipt
assert all(f['file'] == 'examples/tasks/bad-task.md' and f['kind'] == 'task_contract'
           for f in receipt['findings']), receipt
print('Expected exit=1 and exact negative-fixture receipt verified.')
