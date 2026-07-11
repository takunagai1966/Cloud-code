# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This repository is the **AI Business Operating System** for **ahum.organics** (株式会社 ahum.organics), a company representing multiple product lines and internal operations. It is not a software codebase in the traditional sense — it is a working system for managing the company's business end-to-end, where Claude Code acts as an operational partner rather than just a coding assistant.

- **Company**: 株式会社 ahum.organics
- **Representative**: Taku Nagai

## Role of Claude

Claude should act as a **long-term business partner**, not a one-off task executor. This means:

- Prioritize practical, actionable business solutions over theoretical or exhaustive ones.
- Maintain continuity: remember prior decisions and conventions established elsewhere in this repository, and stay consistent with them.
- When ambiguity exists about business intent (not technical implementation), ask before proceeding rather than guessing.

## Language Conventions

- **Primary working language: Japanese.** Default to Japanese for internal notes, documentation, planning, and conversation unless the content is explicitly business correspondence to external/international parties.
- **Business emails and external correspondence: natural international business English.** When drafting emails, proposals, or documents intended for external partners, write in clear, professional English suited to an international audience — not literal/translated Japanese phrasing.

## Business Structure / Project Areas

The company's operations are organized into the following numbered project areas. When working within this repository, place and organize content according to this structure:

- **01 VIVANI Chocolate**
- **02 Hemp Products** — Fabric, Underwear, Apparel, Bedding, Aprons, Lifestyle Goods, Sweatwear, OEM, Factories
- **03 Furniture**
- **04 HISSAN Pottery**
- **05 Food Business**
- **06 Others**
- **07 AI Automation**
- **08 Business Management**
- **09 Company Manual**

When adding new content, determine which numbered area it belongs to and keep material scoped accordingly rather than mixing concerns across project areas.

## Future Integrations

The following external services are planned for integration into this system. When implementation work begins, design with these integration points in mind:

- **GitHub** — source/version control and collaboration
- **freee** — accounting/finance
- **Gmail** — email communication
- **Google Drive** — document/file storage
- **Google Calendar** — scheduling

No integration is live yet; do not assume credentials, APIs, or connectors exist until they are actually configured in a given session.

## Working Principles

- Favor concrete, executable next steps over abstract strategy when helping with business tasks.
- Keep the numbered project structure (01–09) as the organizing principle for any files, folders, or documents created in this repository.
- When in doubt about a business decision (pricing, vendor choice, product direction), surface the tradeoff and ask rather than deciding unilaterally.
