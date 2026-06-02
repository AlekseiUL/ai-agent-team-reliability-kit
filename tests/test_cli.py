from pathlib import Path

from agent_team_reliability.cli import audit_tasks, scan_repo, main


def test_good_task_passes():
    result = audit_tasks(Path("examples/tasks/good-coding-task.md"))
    assert result["ok"] is True


def test_bad_task_fails():
    result = audit_tasks(Path("examples/tasks/bad-task.md"))
    assert result["ok"] is False
    assert result["findings"]


def test_done_summary_passes():
    result = audit_tasks(Path("examples/tasks/done-summary-example.md"))
    assert result["ok"] is True


def test_repo_scan_current_tree_ok():
    result = scan_repo(Path("."))
    assert result["ok"] is True, result["findings"][:5]


def test_doctor_command(capsys):
    assert main(["doctor"]) == 0
    out = capsys.readouterr().out
    assert '"ok": true' in out.lower()
