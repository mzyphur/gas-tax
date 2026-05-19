# Changelog

All notable changes to *Australia's Gas Export Tax Revenue: The
Definitive Accounting* are recorded in this file. This file lives
in the public repository alongside the source manuscript but is not
part of the rendered DOCX / HTML / PDF — the version history belongs
here, not in the public artefact the reader downloads.

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/).
This publication uses [Semantic Versioning](https://semver.org/) at
the document level: major-version bumps for substantive reframing,
minor-version bumps for substantive evidence additions, patch
bumps for fixes and presentation work.

## [3.2.8] — 2026-05-19

Public/private boundary cleanup + Mac Word DOCX compatibility fix.

### Removed

- Appendix B "Public audit notes and version history". The
  appendix had carried release-by-release narrative about the
  publication's drafting discipline, which the
  `methodology/public_private_boundary_protocol.md` rule (general-repo
  v0.22.21) names as production-discipline disclosure that must not
  appear in the public artefact. Version history now lives in this
  file plus GitHub Releases / tag list.

### Renumbered

- Appendix C → Appendix B "Public source package" (no content change).
- Appendix D → Appendix C "About this report" (no content change
  except the AI-assistance disclosure paragraph wording — see below).

### Changed

- AI-assistance disclosure paragraph in Appendix C now uses the
  canonical wording introduced in general-repo v0.22.21: names the
  three tool families (Anthropic Claude Code Opus 4.7, OpenAI Codex
  GPT-5.5, Google Gemini 3 Flash Preview), asserts author
  responsibility, contains no other production-discipline detail.

### Fixed

- DOCX no longer fails to open in Mac Microsoft Word. Root cause
  identified by general-repo's codex GPT-5.5 xhigh deep-dive: a
  degenerate zero-width WordprocessingShape in `word/document.xml`
  emitted by LibreOffice during the soffice round-trip
  (`wp:extent cx="635"` + `a:ext cx="720"` + VML `width:0pt`).
  Mac Word's drawing importer rejects the shape; LibreOffice
  tolerates it. general-repo v0.22.21's
  `normalize_degenerate_wordprocessing_shapes` build-time gate
  rewrites the shape to the standard full-width rule dimensions
  during the build; the validator pass would fail loud if any
  degenerate shape remained. Build log confirms one degenerate
  shape was normalised.
- DOCX release-asset filename. Previous releases uploaded the
  DOCX as `gastax.docx`; releases of v3.2.8 onward use `report.docx`
  to match the source filename and the URL pattern published in
  release notes.

### Pipeline

- Built with general-repo v0.22.21 (single mechanical change vs
  v0.22.20: degenerate-shape gate + canonical-disclosure presence
  check + reviewer-side boundary protocol enforcement).

## [3.2.7] — 2026-05-19

Annotation positioning fix in Figure 12 (international-revenue chart):
overlaid text moved to avoid bar overlap. No content change otherwise.

## [3.2.6] — 2026-05-19

Mac Word DOCX compatibility fix (initial gate set). general-repo
v0.22.20 added the bookmark-name normaliser and the RGBA → RGB PNG
flatten. The v3.2.5 docx had a heading bookmark that violated Word's
grammar (`we-do-pay-a21.9-billion-in-2024-25` — the period in the
dotted number); the normaliser rewrites the name during the build.
v3.2.6 was the first gas-tax release built with this pipeline.

## [3.2.5] — 2026-05-17

Typography pass. Body bolding reduced; em-dashes in body prose
removed. Substantive evidence and findings unchanged.

## [3.2.4] — 2026-05-16

Front-matter restructure: executive summary moved before the TOC,
matching the Brookings / Grattan / McKinsey / RAND / World Bank
convention; colophon trimmed to citation + licence + one-line
currency note; longer about / methodology / disclosure material
moved to the About-this-report appendix.

## [3.2.3] — 2026-05-15

Chart consolidation pass. Multi-panel figures normalised; SVG
versions added alongside PNG for web-edition delivery.

## [3.2.2] — 2026-05-14

DOI registration. CrossRef suffix `10.61700/7p5yeli67e` minted and
propagated to CITATION.cff, README citation block, BibTeX entry,
and report colophon.

## [3.2.1] — 2026-05-13

Source-dossier pass. Eight cleaned dossiers published in `research/`;
every load-bearing claim in the report anchored to a primary-source
URL with a snapshot date.

## [3.2.0] — 2026-05-12

First v3 release of the definitive accounting framing. Expanded the
revenue side of the original gas-tax brief into a full forensic
accounting; added the international comparator analysis; structured
the report around the five-pillar evidence stack.

## [3.1.0] — 2026-05-10

Project relaunch as the Instats Policy Series flagship. Brand
palette + typography aligned with the series house standards.

(Pre-3.1.0 history retained in the GitHub tag list; this changelog
starts at the v3 reframing.)
