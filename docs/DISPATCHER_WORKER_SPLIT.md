# Dispatcher / Worker Split

The most stable agent-team shape is boring:

```text
one dispatcher/coordinator
many specialist workers
```

## Dispatcher owns

- intake;
- decomposition;
- routing;
- approval boundaries;
- final synthesis.

## Worker owns

- one assigned task;
- scoped execution;
- verification;
- blocked/done report.

## Why this matters

If every specialist can also dispatch broadly, the system can create duplicate work, unclear ownership, and race conditions. Keep routing authority explicit.
