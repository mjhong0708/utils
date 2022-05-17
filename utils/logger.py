from datetime import datetime
from typing import Optional

import termcolor


def log(msg: str, task: str = "MAIN", filename: Optional[str] = None):
    """Simple logging function.
    Not for serious logging, but ok for simple usage.

    Args:
        msg: Log message
        task: The name of task
        filename: Optional. If set, appends message to designated file.
    """
    curr_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg_all = f"[{curr_time}] - {task}\t{msg}"
    msg_colored = termcolor.colored(f"[{curr_time}]", "green")
    msg_colored += f" - {termcolor.colored(task, 'blue')}"
    msg_colored += f"\t{msg}"
    print(msg_colored)
    if filename is not None:
        with open(filename, "a") as f:
            f.write(msg_all + "\n")


def make_progbar(num_done, total_length):
    num_done_syms = int((num_done + 1) / total_length * 30)
    if total_length > 1 and num_done == 0:
        progbar = "[" + ">".ljust(30, ".") + "]"
    elif num_done < total_length - 1:
        progbar = "[" + "=" * num_done_syms + ">".ljust(30 - num_done_syms, ".") + "]"
    else:
        progbar = "[" + ">".rjust(30, "=") + "]"

    return progbar
