# API Automation Framework

A scalable API automation framework built with Python, Playwright, Pytest, and Pydantic — designed to mirror real-world API automation architecture.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pytest](https://img.shields.io/badge/tested%20with-pytest-yellow)
![CI](https://github.com/23fanuz/api-automation-framework/actions/workflows/api-tests.yml/badge.svg)

---

## Overview

This framework demonstrates clean, production-style API test automation with:

- **Service + Client abstraction** — each API has its own service layer and a shared base client
- **Pydantic validation** — operation-aware request/response schema enforcement
- **Allure reporting** — centralized, visual test reporting
- **Environment-based config** — `.env`-driven setup for flexible environments
- **GitHub Actions CI** — fully automated pipeline on every push
- **Scalable structure** — built to support multiple APIs with minimal friction

---

## Architecture

```
api-automation-framework/
├── tests/        # Test cases and fixtures
├── services/     # API service abstractions (one per API)
├── models/       # Pydantic request/response schemas
├── utils/        # Shared helpers and utilities
└── config/       # Environment variables and base settings
```

**Request flow:**

```
Test → Service → BaseClient → API Request → Validation → Reporting
```

---

## Setup

**1. Clone the repository**

```bash
git clone <repo-url>
cd api-automation-framework
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Configure environment**

Create a `.env` file in the project root:

```env
BASE_URL=https://fakestoreapi.com
```

---

## Running Tests

```bash
# Run all tests
pytest

# Generate Allure results
pytest --alluredir=allure-results

# View Allure report
allure serve allure-results
```

---

## CI/CD

This project uses **GitHub Actions**. On every push to `main`:

1. Dependencies are installed from `requirements.txt`
2. The full test suite runs via Pytest
3. Allure results are generated
4. Artifacts are uploaded for review

See [`.github/workflows/ci.yml`](.github/workflows/ci.yml) for the pipeline definition.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11 | Core language |
| Pytest | Test runner and fixture management |
| Playwright `APIRequestContext` | HTTP client for API requests |
| Pydantic | Schema definition and validation |
| Allure | Test reporting |
| GitHub Actions | CI/CD pipeline |