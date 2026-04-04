Ingest a new source file into the knowledge pipeline.

Usage: /ingest <filepath>  OR  /ingest (to see status of all raw/ files)

Steps:
1. If no argument given: run `python agent/ingest.py` and show the status table
2. If a file path is given:
   a. If the file is not yet in raw/, copy or move it there (ask user which)
   b. Run `python agent/ingest.py --mark <filename>` to create sidecar
   c. Run `python agent/compile.py --stub <filename>` to create a summary stub
   d. Ask the user: "Do you want me to fill in the summary now?"
   e. If yes: read the raw file and write a complete wiki/summaries/ page using schemas/summary.md
