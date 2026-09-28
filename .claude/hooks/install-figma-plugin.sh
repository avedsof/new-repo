#!/bin/bash
# Installs the Figma plugin in fresh cloud containers. Safe to run every session.
if claude plugin list 2>/dev/null | grep -q "figma@claude-plugins-official"; then
  exit 0
fi
claude plugin marketplace add anthropics/claude-plugins-official >/dev/null 2>&1 || true
claude plugin install figma@claude-plugins-official >/dev/null 2>&1 || true
exit 0
