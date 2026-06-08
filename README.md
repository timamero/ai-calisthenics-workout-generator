# AI Calisthenics Workout Generator

**Status:** 🟢 Active Development

A full-stack prototype web app that generates personalized calisthenics workouts using AI. Built as a learning project to explore LLM integration in a production-like architecture — and as a reference implementation for an AI workout generation feature planned for [Torque](https://torquefit.app), my calisthenics workout tracking app.

## Purpose

- **Prototype** an AI-powered workout generator for eventual integration into Torque
- **Learn** how to integrate an LLM into a full-stack application
- **Practice** test-driven development across a monorepo architecture

## How It Works

Users enter their available equipment, fitness level, target muscles, workout duration, and any extra notes. The backend fetches matching exercises from the Torque exercise database, passes them to GPT-4o Mini, and returns a structured workout — using only real exercises from the database. Users can regenerate, log the workout, and export it as a PNG.

## Tech Stack

**Frontend** — ViteJS, React, TanStack Router, Mantine, Zustand, Zod

**Backend** — FastAPI, OpenAI API (GPT-4o Mini), Supabase (read-only)

**Testing** — Vitest, React Testing Library, pytest

**Tooling** — Prettier, flake8, black

**Deployed on** — Cloudflare (frontend), Render (backend)

## Features

- AI-generated workouts constrained to a real exercise database
- Inputs: equipment, fitness level, target muscles, duration, free-text notes
- Regenerate or log the workout after generation
- PNG export of completed workout
- Rate limiting: 20 generations per day with a live remaining count

## Project Structure

```
/
├── frontend/     # React app
└── backend/      # FastAPI app
```

The monorepo structure mirrors Torque to make the eventual integration straightforward.

---

_Part of building Torque — a calisthenics workout tracker._
