# AI Calisthenics Workout Generator
## Project Specifications Document

**Version:** 1.0
**Date:** June 7, 2025

| Field | Details |
|---|---|
| Project Name | AI Calisthenics Workout Generator |
| Project Type | Prototype Web Application |
| Related Project | Torque (Calisthenics Workout Tracker) |
| Duration | 2 Months |
| AI Model | GPT-4o Mini |
| Frontend Deployment | Cloudflare |
| Backend Deployment | Render |

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Stakeholders & Roles](#2-stakeholders--roles)
3. [Functional Requirements](#3-functional-requirements)
4. [Non-Functional Requirements](#4-non-functional-requirements)
5. [System Architecture](#5-system-architecture)
6. [API Specification](#6-api-specification)
7. [UI/UX Requirements](#7-uiux-requirements)
8. [Constraints & Assumptions](#8-constraints--assumptions)
9. [Risks & Mitigations](#9-risks--mitigations)
10. [Development Timeline](#10-development-timeline)
11. [Future Considerations](#11-future-considerations-v2)
12. [Glossary](#12-glossary)

---

## 1. Project Overview

### 1.1 Purpose

This document defines the requirements, architecture, and implementation plan for the AI Calisthenics Workout Generator — a prototype web application that uses a large language model (LLM) to generate personalized calisthenics workouts based on user inputs.

The project serves two primary purposes:

- Deliver a functional prototype of an AI-powered workout generation feature intended for future integration into Torque, an existing calisthenics workout tracking application.
- Provide a hands-on learning experience for integrating LLM capabilities into a full-stack web application.

### 1.2 Goals

- Build a working AI workout generator prototype using GPT-4o Mini.
- Mirror the monorepo architecture of Torque to ease future integration.
- Re-use existing exercises database from Torque (hosted in Supabase).
- Constrain workout generation to only exercises present in the Torque exercises database.
- Complete the prototype within two months.
- Gain practical experience integrating LLM APIs into a production-like full-stack architecture.
- Practice test-driven development (TDD) across both frontend and backend.

### 1.3 Scope

#### 1.3.1 In Scope

- Workout generation form with user input fields.
- AI-powered workout generation using GPT-4o Mini, restricted to the existing exercises database.
- Workout display with regenerate and proceed-to-log options.
- Workout logging flow (UI re-used from Torque).
- PNG export of completed workout.
- Rate limiting (20 generations per day per user, reset daily).
- Frontend deployment on Cloudflare; backend deployment on Render.

#### 1.3.2 Out of Scope (v1)

- User authentication and persistent user accounts.
- Persistent workout log storage.
- Chat-based adjustments or quick-fix suggestion buttons (planned for v2).
- Mobile native applications.
- Custom exercise creation by users.

---

## 2. Stakeholders & Roles

| Stakeholder | Role | Responsibilities |
|---|---|---|
| Developer | Owner / Engineer | Full-stack development, deployment, and maintenance |
| End Users | Prototype Testers | Use the app, provide feedback on workout quality and UX |
| Torque Project | Reference Architecture | Provides codebase patterns, exercises DB, and UI components |

---

## 3. Functional Requirements

### 3.1 Workout Generation Form

Upon visiting the application, users will be presented with a workout generation form containing the following fields:

| Field | Input Type | Description |
|---|---|---|
| Equipment Available | Multi-select / Checkbox | List of equipment the user has access to (e.g., pull-up bar, rings, parallettes, none) |
| Fitness Level | Single-select / Radio | Beginner, Intermediate, or Advanced |
| Target Muscles | Multi-select / Checkbox | Muscle groups to prioritize (e.g., chest, back, core, legs, shoulders) |
| Workout Duration | Number / Slider | Desired workout duration in minutes |
| Additional Notes | Free-text input | Any extra preferences, injuries, or instructions for the AI |

- All fields except Additional Notes are required.
- A "Generate Workout" button submits the form.
- If the user has reached their daily rate limit, the form will be replaced with a message informing them to return the next day.

### 3.2 Workout Generation

- On form submission, the backend receives the user inputs and queries GPT-4o Mini via the OpenAI API.
- The LLM will be provided with the list of available exercises from the Torque Supabase database (read-only access).
- The generated workout will only include exercises present in the exercises database; the LLM must not invent exercises.
- The system prompt will instruct the model to select exercises appropriate to the user's equipment, fitness level, target muscles, duration, and additional notes.
- The backend will return a structured workout plan to the frontend.

### 3.3 Workout Review Screen

After generation, users will see their workout displayed and have two available actions:

- **Regenerate Workout** — sends a new request to the AI with the same inputs to produce an alternative workout.
- **Log Workout** — proceeds to the workout logging flow.

> Note: Chat-based adjustments and quick-fix suggestion buttons are planned for a future version (v2) and are explicitly out of scope for this prototype.

### 3.4 Workout Logging

- The workout logging UI will be re-used from the Torque project.
- Users can track sets, reps, and other exercise details during their session.
- No workout data will be persisted to a database; the session is ephemeral.

### 3.5 Workout Export

Upon completing the workout, users are presented with two options:

- **Export as PNG** — generates and downloads a PNG image summarizing their completed workout.
- **Return to Home** — navigates back to the workout generation form.

### 3.6 Rate Limiting

- Each user (identified by IP address or browser session) is limited to 20 workout generations per calendar day.
- The remaining generation count will be visibly displayed to the user on the home page.
- When the limit is reached, the generation form is hidden and a message is displayed: *"You have reached your daily limit. Come back tomorrow to generate more workouts."*
- The counter resets at midnight (UTC or local time — to be defined during implementation).

---

## 4. Non-Functional Requirements

| Category | Requirement |
|---|---|
| Performance | Workout generation response should return within 10 seconds under normal network and API conditions. |
| Availability | Target 95% uptime; acceptable for a prototype/side project. Dependent on Render and Cloudflare SLAs. |
| Cost Efficiency | GPT-4o Mini selected for low cost-per-token. API usage should remain minimal with rate limiting in place. |
| Security | Supabase access is read-only. No user credentials are stored. Rate limiting mitigates abuse. |
| Maintainability | Monorepo structure mirrors Torque for easy code reuse and future integration. |
| Scalability | Prototype scale; not designed for high concurrency. Rate limits serve as a natural safeguard. |
| Usability | Simple, single-page form interface. Minimal learning curve for first-time users. |
| Testability | TDD practiced throughout; test coverage targets applied to both frontend and backend logic. |

---

## 5. System Architecture

### 5.1 Architecture Overview

The application follows a monorepo structure with a clear separation between frontend and backend, mirroring the Torque project architecture. This design facilitates future integration of this feature into Torque.

### 5.2 Monorepo Structure

```
/
├── frontend/               # ViteJS + React application
│   ├── src/
│   │   ├── components/     # UI components (some re-used from Torque)
│   │   ├── pages/          # Route-level page components
│   │   ├── store/          # Zustand state management
│   │   ├── router/         # TanStack Router configuration
│   │   ├── schemas/        # Zod validation schemas
│   │   └── tests/          # Vitest + React Testing Library tests
│   └── ...
└── backend/                # FastAPI Python application
    ├── api/                # REST API route handlers
    ├── ai/                 # LLM integration logic (prompts, OpenAI calls)
    ├── db/                 # Supabase read-only data access layer
    └── tests/              # pytest test suite
```

### 5.3 Tech Stack

#### Frontend

| Tool | Purpose |
|---|---|
| ViteJS + React | Core framework and build tool |
| TanStack Router | Client-side routing |
| Zustand | Lightweight global state management |
| Mantine | UI component library |
| Zod | Form input validation and API response schema validation |
| Vitest | Unit and integration test runner |
| React Testing Library | Component testing |
| Prettier | Code formatting |

#### Backend

| Tool | Purpose |
|---|---|
| FastAPI (Python) | REST API framework |
| OpenAI SDK | GPT-4o Mini API integration |
| Supabase Python Client | Read-only database access |
| pytest | Test framework |
| flake8 | Linting |
| black | Code formatting |

#### Infrastructure

| Layer | Technology | Notes |
|---|---|---|
| Database | Supabase (PostgreSQL) | Read-only; exercises and set progressions from Torque DB |
| Rate Limiting | Backend (in-memory or Redis) | Tracks daily generation count per user session/IP |
| Frontend Deploy | Cloudflare Pages | Static site hosting with CDN |
| Backend Deploy | Render | Python service hosting |
| AI Model | GPT-4o Mini (OpenAI) | Cost-efficient; suitable for structured workout generation |

### 5.4 Data Flow

1. User fills out the workout generation form in the React frontend.
2. Zod validates the form inputs client-side before submission.
3. The frontend sends a POST request to the FastAPI backend with user inputs.
4. The backend fetches the relevant exercises from Supabase (filtered by equipment and target muscles).
5. The backend constructs a system prompt that includes the filtered exercise list and user parameters, and calls the OpenAI API (GPT-4o Mini).
6. GPT-4o Mini returns a structured workout plan using only exercises from the provided list.
7. The backend parses and validates the response, then returns structured JSON to the frontend.
8. The frontend stores workout state in Zustand and renders the workout for user review.
9. User can regenerate (repeats steps 2–8) or proceed to log the workout.
10. Upon workout completion, the user can export the workout as a PNG or return home.

### 5.5 Database Access

- The backend connects to the Torque Supabase database with read-only credentials.
- Tables accessed: `exercises`, `set_progressions` (and related lookup tables as needed).
- No write operations are performed to the Supabase database.
- No new tables will be created; rate limiting state will be managed in backend memory or a lightweight store.

---

## 6. API Specification

### 6.1 POST /api/generate-workout

| | |
|---|---|
| Method | POST |
| Endpoint | `/api/generate-workout` |
| Description | Generates an AI calisthenics workout based on user inputs |
| Auth Required | No |
| Rate Limited | Yes — 20 requests per user per day |

**Request Body (JSON)**

| Field | Type | Description |
|---|---|---|
| `equipment` | `string[]` | List of available equipment identifiers |
| `fitness_level` | `string` | `"beginner"` \| `"intermediate"` \| `"advanced"` |
| `target_muscles` | `string[]` | List of muscle group identifiers to prioritize |
| `duration_minutes` | `integer` | Desired workout duration in minutes |
| `additional_notes` | `string?` | Optional free-text notes for the AI |

**Response Body (JSON)**

| Field | Type | Description |
|---|---|---|
| `workout` | `object` | Structured workout plan with exercises, sets, and reps |
| `remaining_generations` | `integer` | Number of remaining generations for today |

**Error Responses**

| Status Code | Description |
|---|---|
| 422 | Validation error — invalid or missing required fields |
| 429 | Rate limit exceeded — user has reached their 20/day limit |
| 500 | Internal server error — AI API failure or database issue |

### 6.2 GET /api/rate-limit-status

| | |
|---|---|
| Method | GET |
| Endpoint | `/api/rate-limit-status` |
| Description | Returns the current remaining workout generation count for the user |
| Auth Required | No |

---

## 7. UI/UX Requirements

### 7.1 Pages & Screens

| Screen | Description |
|---|---|
| Home / Generation Form | Workout generation form with all input fields and a submit button. Displays remaining generation count. Shows rate-limit message when limit is reached. |
| Workout Review | Displays the generated workout. Provides "Regenerate" and "Log Workout" buttons. |
| Workout Logging | Re-used from Torque. Allows user to log sets and reps during the workout session. |
| Workout Complete | Summary of the completed workout. Offers "Export as PNG" and "Back to Home" options. |

### 7.2 General UX Principles

- The interface should be clean, minimal, and focused — the workout is the primary content.
- Mantine components should be used consistently throughout the UI for visual coherence.
- Loading states should be shown clearly during AI generation (e.g., spinner or progress indicator).
- All error states (API failures, validation errors, rate limit) should display user-friendly messages.
- The remaining generation count should be prominently visible so users are aware of their limit.
- The application should be responsive and functional on desktop and modern mobile browsers.

---

## 8. Constraints & Assumptions

### 8.1 Constraints

- The LLM must only use exercises present in the Torque exercises database. It must not generate exercises outside this set.
- No user authentication; rate limiting is based on IP address or browser session identifier.
- No persistent workout logs; all session data is ephemeral.
- Deployment is on Cloudflare (frontend) and Render (backend) — no custom infrastructure.
- API usage is limited to GPT-4o Mini to minimize cost.
- Tests must be written before or alongside implementation (TDD approach).

### 8.2 Assumptions

- The Torque Supabase database is accessible with read-only credentials during development and in production.
- The existing exercises and `set_progressions` data in Supabase is sufficient to generate diverse workouts across equipment types and fitness levels.
- Torque workout logging UI components are reusable without significant modification.
- GPT-4o Mini is capable of generating adequately structured and appropriate calisthenics workouts given a constrained exercise list and user context.
- Rate limiting by IP or session is sufficient for abuse prevention at prototype scale.

---

## 9. Risks & Mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| LLM generates exercises outside the database | Medium | Enforce exercise list in system prompt; validate response against DB before returning to frontend |
| OpenAI API latency / outages | Low–Medium | Implement timeout handling and user-facing error messages; retry logic for transient failures |
| Rate limiting bypass (IP spoofing) | Low | Acceptable at prototype scale; can be hardened in future versions |
| Torque UI components require significant rework | Low | Assess component compatibility early (Week 1); allocate buffer time in schedule |
| Supabase read-only access issues | Low | Test DB connectivity in Week 1; confirm credentials and RLS policies early |
| Cost overrun from API usage | Low | Rate limiting (20/day) provides a natural cap; GPT-4o Mini is cost-efficient |
| TDD slowing early velocity | Low–Medium | Treat tests as part of the definition of done; time estimates account for test writing |

---

## 10. Development Timeline

The project is planned to be completed within 8 weeks (2 months), divided into four two-week phases. Test-driven development (TDD) is practiced throughout — tests are written before or alongside each feature, not as a separate phase.

### TDD Approach

- **Frontend:** Vitest + React Testing Library. Write component and integration tests alongside each feature. Zod schemas are validated with unit tests before being used in forms or API calls.
- **Backend:** pytest. Write unit tests for route handlers, AI prompt logic, and DB access functions before or during implementation. flake8 and black enforced on all committed code.

---

### Phase 1 — Setup & Foundation (Weeks 1–2)

| Week | Deliverables |
|---|---|
| Week 1 | Initialize monorepo structure. Set up ViteJS + React frontend with TanStack Router, Zustand, Mantine, Zod, Vitest, and Prettier configured. Set up FastAPI backend with pytest, flake8, and black configured. Verify Supabase read-only access and confirm exercises/set_progressions schema. Configure development environment (env vars, CORS, local run scripts). Write smoke tests for both frontend and backend to confirm tooling works. |
| Week 2 | Implement Supabase data access layer in backend with pytest unit tests. Design and implement POST /api/generate-workout endpoint skeleton with tests for request validation. Define Zod schemas for form inputs and API response shapes. Draft initial system prompt for GPT-4o Mini. Assess reusability of Torque workout logging components. |

### Phase 2 — Core AI Feature (Weeks 3–4)

| Week | Deliverables |
|---|---|
| Week 3 | TDD: Write tests for AI prompt construction and response parsing before implementing. Complete OpenAI API integration (GPT-4o Mini). Implement exercise filtering from Supabase based on user inputs. Refine system prompt to ensure exercises are constrained to the database. Validate AI response against exercise DB before returning to frontend. |
| Week 4 | TDD: Write tests for rate limiting logic before implementing. Implement rate limiting (20/day cap, daily reset, GET /api/rate-limit-status). Integrate rate limiting with the generation endpoint. Build frontend workout generation form using Mantine components. Write React Testing Library tests for the form (field validation, submission, error states). Wire frontend form to backend API. |

### Phase 3 — UI, Logging & Export (Weeks 5–6)

| Week | Deliverables |
|---|---|
| Week 5 | TDD: Write component tests for workout review screen before building it. Build workout review screen (workout display, Regenerate and Log Workout buttons). Integrate Torque workout logging components into the frontend with tests for any modified behaviour. Implement end-of-workout screen with component tests. |
| Week 6 | Implement PNG export of completed workout. Add rate limit display to home page (remaining count + limit-reached message) with tests. End-to-end flow testing (form → generate → log → export). Bug fixes and UX polish. Ensure all flake8/Prettier/black checks pass. |

### Phase 4 — Deployment & Review (Weeks 7–8)

| Week | Deliverables |
|---|---|
| Week 7 | Run full test suite and fix any failing tests before deploying. Configure Render deployment for FastAPI backend (environment variables, start command, health checks). Configure Cloudflare Pages deployment for React frontend. Test end-to-end in production environment. |
| Week 8 | Final QA pass on deployed application. Document any known issues or deferred items for v2. Write brief internal retrospective: LLM integration learnings, TDD reflections, architecture notes for Torque integration. Project complete. |

### Milestone Summary

| Week | Milestone | Description |
|---|---|---|
| 2 | Foundation Complete | Monorepo set up, tooling configured, DB access verified, API skeleton with tests |
| 4 | AI Core Complete | GPT-4o Mini integration working, rate limiting implemented, all backend tests passing |
| 6 | Full Feature Complete | End-to-end flow working locally with test coverage across frontend and backend |
| 8 | Prototype Deployed | Application live on Cloudflare + Render; full test suite passing |

---

## 11. Future Considerations (v2+)

The following features are out of scope for this prototype but are planned for future versions, either in this prototype or directly in Torque:

- **Chat-based workout adjustments:** Allow users to request modifications to a generated workout via natural language conversation.
- **Quick-fix suggestion buttons:** Pre-defined adjustment options (e.g., "Make it harder", "Shorten workout", "Swap this exercise") displayed alongside the generated workout.
- **User authentication:** Optional user accounts to persist workout history and personalize generation over time.
- **Workout history:** Store and display past workouts for logged-in users.
- **Torque integration:** Incorporate the AI workout generator as a feature within the Torque application, using this prototype as a reference implementation.
- **Enhanced rate limiting:** Replace in-memory rate limiting with Redis or a database-backed solution for multi-instance deployments.

---

## 12. Glossary

| Term | Definition |
|---|---|
| Calisthenics | A form of strength training that uses bodyweight exercises, often with minimal equipment. |
| LLM | Large Language Model — an AI model trained on large text datasets capable of generating human-like text. |
| GPT-4o Mini | OpenAI's cost-efficient language model used for AI workout generation in this project. |
| Torque | The developer's existing calisthenics workout tracking application, from which this prototype borrows architecture and components. |
| Supabase | An open-source Firebase alternative providing a hosted PostgreSQL database and API layer. |
| FastAPI | A modern, high-performance Python web framework for building APIs. |
| ViteJS | A fast frontend build tool and development server for modern JavaScript frameworks. |
| TanStack Router | A type-safe, file-based routing library for React applications. |
| Zustand | A small, fast state management library for React. |
| Mantine | A React component library with a comprehensive set of UI components. |
| Zod | A TypeScript-first schema declaration and validation library. |
| Vitest | A Vite-native unit test framework compatible with the Jest API. |
| React Testing Library | A testing utility for React that encourages testing components from a user's perspective. |
| pytest | A Python testing framework used for writing and running backend tests. |
| flake8 | A Python linting tool that enforces code style and catches common errors. |
| black | An opinionated Python code formatter. |
| Prettier | An opinionated code formatter for JavaScript/TypeScript. |
| Monorepo | A single version-controlled repository containing multiple related projects (frontend and backend). |
| TDD | Test-Driven Development — a practice where tests are written before or alongside implementation. |
| Rate Limiting | A mechanism to restrict the number of requests a user can make within a defined time window. |
| PNG Export | The ability to save a visual summary of the completed workout as a PNG image file. |
