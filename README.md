## D&D Combat Tracker

A (hopefully) easy-to-use command line combat tracker for Dungeons and Dragons.

## What it does:

- Set up and keep track of initiative
- Keep track of NPC health
- Keep track of NPC status effects

## How to use:

### Starting up

Simply open your favorite terminal, navigate to the directory where you store the file, and type `python combat.py`<sup>[1](#footnote1)</sup>

### Initializing creatures

The program will prompt you for the creature type. There are two options: PC and NPC.

**PC** creatures are very simple: all they have is a name and an initiative. I assume players can keep track of their own statuses and health (although you never know).

**NPC** creatures are a little more complex. They have names, initiatives, health, and status effects (which, in turn, have durations).

To create a new PC, type `PC`, `pc`, or `p`, followed by a return.

To create a new NPC, type `NPC`, `npc`, or `n`, followed by a return.

After selecting PC or NPC, the program will prompt you for its relevant stats; simply enter these as asked followed by a return. When you're all done creating creatures, enter `done` to proceed to combat.

### Combat

A table will appear with the creatures listed in order of initiative, with the current creature at the top. A prompt below the table will ask you for a command. Here is the list of options:

- `end` or `done`: finishes combat and closes the program.
- `next turn`, `next`, or `n`: proceeds to the next turn, killing all 0 hp creatures.
- `hit` or `damage`: prompts for a target, then a damage number. Deals damage to the target. If the damage is greater than the target's current HP, the target's HP is set to 0. Upon progressing to the next turn, it will be killed and removed from the table.
- `kill` or `remove`: prompts for a target, and slates it for death. Upon progressing to the next turn, it will be killed and removed from the table.
- `add status` or `stat`: prompts for a target, status, and duration. For infinite duration, enter `-`. Statuses with finite durations will tick down each time it is the creature's turn. *NOTE:* does not work for PCs.
- `remove status` or `unstat`: prompts for a target and a status. Removes the status immediately from the target.
- `heal`: prompts for a target and a heal amount. Heals the target by that amount, or to max if health after heal would be over the creature's maximum HP.
- `add temp hp` or `temp`: prompts for a target and an amount of temporary hp to add. Adds that to the target's existing pool of temporary hit points.

### Upcoming Features

Bug fixes

Mid-combat creature additions, modifications

### Footnotes
<a name="footnote1">1</a>: If you aren't used to using a terminal, here's a nice introduction to [Unix](https://computers.tutsplus.com/tutorials/navigating-the-terminal-a-gentle-introduction--mac-3855) and [Windows](https://www.bleepingcomputer.com/tutorials/windows-command-prompt-introduction/). All you really need is the directory commands (cd and ls in Unix, cd and dir in Windows).
