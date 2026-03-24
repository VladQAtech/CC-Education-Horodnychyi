Navigate to $ARGUMENTS using Playwright MCP, take a screenshot, and analyze the page for visual issues.

Steps:
1. Use `mcp__playwright__browser_navigate` to open the URL provided in $ARGUMENTS
2. Use `mcp__playwright__browser_take_screenshot` to capture the page
3. Use `mcp__playwright__browser_snapshot` to get the accessibility tree
4. Analyze and report:
   - Any broken layouts or overlapping elements
   - Missing images or broken media
   - Text truncation or overflow issues
   - Inconsistent spacing or alignment
   - Color contrast or readability concerns
   - Any console errors if visible
5. Summarize findings as a QA visual report with severity: Critical / Warning / Info
