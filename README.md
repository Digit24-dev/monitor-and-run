# process monitor

Have you ever experienced that the installation or compilling your code is too long to run other process or job?

Here is the solution! This 'monitor-and-run' is a program that async your second program after the installation or the compilation.

Enter the pid of the long-running task and the pid of what to run next.

We provide GUI and CUI versions of the program.

## How to use?

### CUI

```
-p --pid: PID of the process to monitor

-e --execute: Command to execute after process completion

-v --version: Show program version
```