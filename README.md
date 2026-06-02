# AI Agent Team Reliability Kit

Operating contracts, task templates, safety gates, and audit scripts for running multi-agent AI teams without chaos.

This is **not another agent framework** and **not another Kanban board**. It is a reliability layer you put around any agent team so tasks have owners, boundaries, approval rules, verification, and clean handoffs.

Built from a real local-first AI agent team workflow and sanitized for public reuse.

## Why this exists

Most multi-agent systems do not fail because the model is stupid.
They fail for boring reasons:

- no clear owner for a task;
- vague task bodies like “check this”;
- agents touching the wrong files;
- hidden external side effects;
- no approval boundary;
- no verification gate;
- “done” reports that do not say what was actually done;
- memory polluted with temporary task noise;
- public repos accidentally leaking local paths, secrets, screenshots, recordings, or private context.

This kit fixes those boring parts.

## What you get

- A **dispatcher/worker operating model** for agent teams.
- A strict **task contract** template.
- Privacy and side-effect boundaries.
- Verification gates for code, research, documents, and public releases.
- Done / blocked report formats.
- A memory/wiki/report decision bridge.
- A small CLI that audits task markdown files and public repo hygiene.
- Ready-to-copy examples for coding, research, and release work.

## Who is this for?

This kit is for people who run or build:

- multi-agent AI teams;
- Claude Code / Codex / Hermes / OpenClaw / custom agent workflows;
- local-first automation systems;
- research, coding, content, or ops agent pipelines;
- public GitHub agent/tool repositories that need privacy-safe release checks.

It is especially useful if your agents can read files, run shell commands, publish to GitHub, send messages, or mutate live systems.

## What this is not

- Not a replacement for Hermes, Claude Code, Codex, OpenClaw, LangGraph, CrewAI, AutoGen, or any other agent runtime.
- Not a full enterprise policy engine.
- Not a magic safety guarantee.
- Not legal advice.

It is a practical operating layer: templates, rules, scripts, and examples.

## Install the CLI

Requires Python 3.10+.

From source:

```bash
python -m pip install -e .
agent-team-reliability --help
```

Run checks:

```bash
agent-team-reliability doctor
agent-team-reliability audit-tasks examples/tasks/good-coding-task.md
agent-team-reliability scan-repo .
```

To see the checker catch a broken task contract, run:

```bash
agent-team-reliability audit-tasks examples/tasks/bad-task.md
```

That example is intentionally incomplete and should fail.

## Quick start

1. Copy `templates/task-contract.md` into your task board, issue, or agent queue.
2. Fill in owner, allowed paths, forbidden paths, privacy level, side-effect policy, and verification.
3. Give the task to an agent.
4. Require `templates/done-summary.md` or `templates/blocked-report.md` before closing.
5. Run:

```bash
agent-team-reliability audit-tasks path/to/tasks
```

## Core idea

```text
human goal
  -> dispatcher / coordinator
  -> task contract
  -> specialist worker
  -> verification gate
  -> done or blocked report
  -> memory/wiki/report decision
```

## Framework compatibility

The templates are runtime-agnostic. The scripts are simple Python and can be used with any filesystem-based workflow.

Native fit:

- Hermes Agent Kanban
- Claude Code / Codex task queues
- OpenClaw-style agent teams
- GitHub Issues / Projects
- Linear / Trello / local Markdown boards
- custom MCP/task-board systems

## Public repo release hygiene

If your agent team publishes public GitHub repos, start with:

- `docs/PUBLIC_RELEASE_GATE.md`
- `templates/public-release-checklist.md`
- `agent-team-reliability scan-repo .`

The scanner looks for common public-release mistakes: private local paths, bytecode, runtime media outside allowed public assets, hardcoded secret-shaped strings, and dangerous accusation wording.

## Repository layout

```text
docs/       Operating contracts and explanations
templates/  Copy-paste task, report, and release templates
examples/   Good and bad task examples
src/        Small audit CLI
tests/      Offline regression tests
```

## Public links

- YouTube: https://youtube.com/@alekseiulianov
- Telegram channel: https://t.me/Sprut_AI
- Telegram chat: https://t.me/+eH-qNIDmud8zNDZi
- AI Операционка: https://t.me/tribute/app?startapp=sJyg

## Canonical source

This project is maintained by Aleksei Ulianov / Sprut_AI.
Original repository: https://github.com/AlekseiUL/ai-agent-team-reliability-kit

If you found this project mirrored, repackaged, or redistributed elsewhere, check this repository as the source of truth.

## Attribution

Where permitted by the applicable license, if you reuse, fork, modify, package, or publish this work, keep the original copyright and license notice and link back to the canonical repository.

## License

MIT. See `LICENSE`.

---

# Русская версия

**AI Agent Team Reliability Kit** — это набор операционных контрактов, шаблонов задач, safety-gates и audit-скриптов для агентных команд.

Это **не очередной фреймворк агентов** и **не новая Kanban-доска**. Это слой надёжности вокруг уже существующей агентной системы.

## Зачем это нужно

Агентные команды чаще ломаются не из-за “плохой модели”, а из-за скучных вещей:

- непонятно, кто владелец задачи;
- задача написана как “проверь это”;
- агент лезет не в те файлы;
- внешние действия не ограничены;
- нет approval boundary;
- нет проверки результата;
- “готово” не объясняет, что сделано;
- память агента превращается в свалку;
- public GitHub repo случайно тащит локальные пути, секреты или приватный runtime-мусор.

Этот kit закрывает именно эти скучные, но критичные места.

## Что внутри

- модель “диспетчер → специалист”;
- строгий шаблон карточки задачи;
- privacy и side-effect policy;
- verification gate;
- формат blocked/done отчётов;
- правило, что переносить в memory/wiki/reports;
- CLI для проверки task markdown и public repo hygiene;
- примеры хороших и плохих задач.

## Для кого

Для тех, кто строит или использует:

- AI-agent команды;
- Hermes / Claude Code / Codex / OpenClaw / кастомные agent workflows;
- локальные автоматизации;
- research/coding/content/ops pipeline’ы;
- public GitHub инструменты с проверкой приватности перед публикацией.

## Быстрый старт

Нужен Python 3.10+.

```bash
python -m pip install -e .
agent-team-reliability doctor
agent-team-reliability audit-tasks examples/tasks/good-coding-task.md
agent-team-reliability scan-repo .
```

Чтобы увидеть, как проверка ловит плохую карточку:

```bash
agent-team-reliability audit-tasks examples/tasks/bad-task.md
```

Этот пример специально неполный и должен завершаться ошибкой.

Главный принцип простой:

```text
цель человека
  -> диспетчер
  -> task contract
  -> специалист
  -> проверка
  -> done/blocked report
  -> решение: memory/wiki/report/ничего
```

## Авторские ссылки

- YouTube: https://youtube.com/@alekseiulianov
- Telegram-канал Sprut AI: https://t.me/Sprut_AI
- Чат Telegram-канала Sprut AI: https://t.me/+eH-qNIDmud8zNDZi
- AI Операционка: https://t.me/tribute/app?startapp=sJyg

## Канонический источник

Проект поддерживает Aleksei Ulianov / Sprut_AI.
Оригинальный репозиторий: https://github.com/AlekseiUL/ai-agent-team-reliability-kit
