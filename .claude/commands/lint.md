Run the wiki linter to check for structural issues.

Usage: /lint

Steps:
1. Run `python agent/lint.py`
2. For each issue category with findings:
   - Broken links: offer to create stub pages for missing targets
   - Orphan pages: offer to add them to wiki/index.md
   - Missing frontmatter: offer to add the missing fields
   - [UNVERIFIED] in stable pages: ask if you should attempt to resolve them
3. After fixes, re-run `python agent/lint.py` to confirm clean
