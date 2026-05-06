
# Braumchat

Braumchat is a full-stack, real-time chat platform built to feel like a modern team messenger. The goal is a production-ready app that supports workspaces, channels, direct messages, presence, and reliable message delivery. The focus is on a clean, well-instrumented backend and a fast, responsive frontend that can scale as features grow.

## Purpose and vision

- Provide a complete chat experience (auth, workspaces, channels, DMs, invites, presence).
- Keep the API robust and observable with metrics and health checks.
- Enable real-time updates over WebSockets with Redis-backed coordination.
- Ship a frontend that is fast, accessible, and easy to iterate on.

## Core concepts

- **Workspaces** are the top-level boundary for a team or company; they control membership and data isolation.
- **Channels** are conversation rooms inside a workspace, grouping messages by topic or team.
- **Direct messages** are private threads between users for 1:1 or small-group chat.

## Tech stack (and why)

### Backend

- **FastAPI** for a high-performance, Pythonic API with automatic OpenAPI docs.
- **SQLAlchemy (async)** as the ORM for clean data access and async Postgres support.
- **PostgreSQL** as the primary database for relational data (users, channels, messages).
- **Alembic** for versioned database migrations.
- **Redis** for low-latency shared state (rate limits, presence, WebSocket coordination).
- **JWT + Passlib/Bcrypt** for secure authentication and password hashing.
- **Prometheus metrics** via middleware for visibility into request latency and throughput.

### Realtime

- **WebSockets** for live message delivery, presence updates, and typing signals.
- **Redis pub/sub** (and shared cache) to fan out events across workers and keep state in sync.

### Frontend

- **Next.js + React** for an app-router based UI with strong performance defaults.
- **TypeScript** for safer, self-documenting frontend code.
- **Tailwind CSS** for consistent, scalable styling.
- **TanStack Query** for cached API data and smooth server-state updates.
- **i18next** for internationalization and translation (language detection + strings).

### Platform and tooling

- **Docker Compose** to run the full stack locally (API, Postgres, Redis, frontend).
- **Pytest** for backend tests and async test support.

## Current state

- Core models and migrations for users, workspaces, channels, DMs, invites, and sessions.
- Workspace creation/listing with ownership and membership checks.
- Channels per workspace (create/list/get) and a presence endpoint for online users.
- Workspace invites for existing users (by display name) with accept/decline flows.
- REST endpoints for auth, users, workspaces, channels, messages, and invites.
- WebSocket routes for realtime messaging and presence.
- Redis-backed rate limiting and health checks (DB + Redis readiness).
- Frontend app structure with auth and chat flows.

## How invitations work today

- Workspace owners can invite existing users by display name.
- Invites are stored with a status of pending, accepted, or declined.
- Invitees can list incoming invites and accept or decline them.
- Accepting an invite creates a workspace membership if it does not exist.
- Real-time notifications are sent for invite creation and responses.

## What is next (MVP focus)

- Workspace and channel administration (roles, permissions, member management).
- Channel features (topics, archiving, private channel access, join/leave flows).
- Inviting non-registered users (email-based invites + signup handoff).
- Message reactions, edits, and deletions.
- Notification preferences and per-channel settings (muting, mentions).

## Later (expansion)

- Advanced search and message indexing.
- Media uploads with signed URLs.
- Presence and typing refinement (idle/away logic).
- Deploy-ready configs (CI, staging, production).

## How it will look when finished

- A Slack-style product with workspaces, channels, and DMs.
- Instant message delivery and presence across multiple clients.
- Clear metrics and health monitoring for production use.
- A modern UI that supports theming, localization, and fast navigation.

<!--
Hidden notes (keep for future reference):

#### Don't forget to import tables at braumchat/models/__init__.py
```bash
docker compose exec -T api alembic revision -m "revision_name"

docker compose exec -T api alembic upgrade head

docker compose exec -T api alembic downgrade -1
```

```bash
Downgrade specific version
docker compose exec -T api alembic downgrade 0b9f4f0f6b4a
```
-->
