# Launch Post

## Russian

Я выложил на GitHub **AI Agent Team Reliability Kit**.

Это не фреймворк агентов и не еще одна Kanban-доска. Это операционный слой вокруг агентной команды: контракты задач, границы доступа, правила approval, verification gate и нормальные done/blocked отчеты.

Зачем это нужно?

Агентные команды чаще ломаются не потому, что модель плохая. Они ломаются из-за скучных вещей: непонятный владелец задачи, расплывчатое "проверь это", агент лезет не в те файлы, внешние действия не ограничены, а отчет "готово" не говорит, что реально было сделано.

Внутри:

- dispatcher/worker operating model;
- task contract template;
- privacy и side-effect boundaries;
- verification gate;
- done/blocked report templates;
- memory/wiki/report decision rule;
- небольшой CLI для проверки task markdown и public repo hygiene.

Я собирал это из реального local-first контура с Hermes, Codex, OpenClaw и публичными GitHub-релизами. Потом вычистил приватный контекст и оставил то, что можно переиспользовать в любой агентной команде.

Репозиторий:
https://github.com/AlekseiUL/ai-agent-team-reliability-kit

Если у вас агенты читают файлы, запускают shell, отправляют сообщения, публикуют в GitHub или трогают живые сервисы, вам нужен не только хороший промпт. Вам нужен операционный контракт вокруг работы.

## English

I published **AI Agent Team Reliability Kit** on GitHub.

It is not another agent framework or another Kanban board. It is an operating layer around an agent team: task contracts, access boundaries, approval rules, verification gates, and clear done/blocked reports.

Why does this matter?

Agent teams usually do not fail because the model is bad. They fail for boring reasons: unclear task ownership, vague prompts like "check this", agents touching the wrong files, unbounded external side effects, and "done" reports that do not say what actually happened.

Inside:

- dispatcher/worker operating model;
- task contract template;
- privacy and side-effect boundaries;
- verification gate;
- done/blocked report templates;
- memory/wiki/report decision rule;
- a small CLI for task markdown and public repo hygiene checks.

I built it from a real local-first workflow with Hermes, Codex, OpenClaw, and public GitHub releases. Then I removed the private context and kept the parts other teams can reuse.

Repository:
https://github.com/AlekseiUL/ai-agent-team-reliability-kit

If your agents can read files, run shell commands, send messages, publish to GitHub, or touch live services, a good prompt is not enough. You need an operating contract around the work.
