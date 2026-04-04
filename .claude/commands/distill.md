Distill findings from an output report back into the wiki knowledge base.

Usage: /distill <output-report-path>

Steps:
1. Run `python agent/distill.py <output-report-path>` to generate the distillation plan
2. Read the plan carefully
3. For each MISSING page listed:
   - Create the page in wiki/concepts/ or wiki/topics/ using the appropriate schema from schemas/
   - Fill in all sections with real content synthesized from the report and linked pages
4. For each [UNVERIFIED] claim listed:
   - Check if the raw sources can confirm or refute the claim
   - Either resolve it (remove [UNVERIFIED], cite source) or flag it as "disputed"
5. Update wiki/index.md with any new pages
6. Run `python agent/lint.py` to verify no new issues were introduced
7. Commit: git add wiki/ && git commit -m "distill: <topic summary>"
8. Push: git push
