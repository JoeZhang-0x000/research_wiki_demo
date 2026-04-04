Search the wiki knowledge base for a topic and generate a report.

Usage: /query <search terms>

This runs `python agent/query.py "<search terms>"` and writes a markdown report to output/.

Steps:
1. Run: python agent/query.py "$ARGUMENTS"
2. Print the path of the generated report
3. Show a brief summary of the top matching pages found
4. Ask the user if they want you to distill findings back into the wiki
