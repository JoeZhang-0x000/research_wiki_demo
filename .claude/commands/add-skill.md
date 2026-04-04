Add a new skill to the skills/ directory.

Usage: /add-skill <skill-name> <description>

Steps:
1. Check skills/README.md to confirm the skill doesn't already exist
2. Create skills/<skill-name>.py using the template in skills/README.md
   - Write a complete, functional script (not a stub) if the task is well-defined
   - Include argparse with --help
   - Include a module-level docstring with: purpose, inputs, outputs, dependencies
3. Add an entry to the skills table in skills/README.md
4. Optionally create .claude/commands/<skill-name>.md if the skill is frequently invoked interactively
5. Confirm the script runs: python skills/<skill-name>.py --help
