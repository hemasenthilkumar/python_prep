# 🚀 16-Day Python + LLD Projects for Senior Engineer Role

A curated, real-world-focused project roadmap to strengthen Python mastery and Low-Level Design skills for a Senior Software Engineer role. Each day features a small but impactful project designed to explore key concepts and patterns.

---

## 📅 Week 1 – Python Mastery + Core LLD

### **Day 1 – Package Tracker CLI**
- **Goal:** Create a CLI to track delivery packages (add/update/list/delete).
- **Key Concepts:** `argparse`, modular code structure, file I/O (`json`), error handling.
- **LLD Focus:** SRP, CLI command parsing design.
- **Stretch Goals:** Add support for export to CSV and a search feature.

### **Day 2 – Inventory Management System**
- **Goal:** Model a simple inventory system for a store.
- **Key Concepts:** OOP (`@property`, encapsulation), custom exceptions.
- **LLD Focus:** Class design, separation of concerns.
- **Stretch Goals:** Implement persistence using JSON or SQLite.

### **Day 3 – Custom Logger Library**
- **Goal:** Create your own logging utility with levels, file/console outputs.
- **Key Concepts:** Decorators, Singleton, file handling.
- **LLD Focus:** Logger design pattern, pluggable architecture.
- **Stretch Goals:** Add log rotation and color-coded output.

### **Day 4 – URL Shortener (in-memory)**
- **Goal:** Build a simplified version of bit.ly using in-memory storage.
- **Key Concepts:** Hashing, dictionary usage, UUID, validation.
- **LLD Focus:** Service-repository design.
- **Stretch Goals:** Add Base62 encoding.

### **Day 5 – Movie Ticket Booking System**
- **Goal:** Simulate movie booking with seats, users, and showtimes.
- **Key Concepts:** Object modeling, state transitions.
- **LLD Focus:** Composition vs inheritance, cohesion/coupling.
- **Stretch Goals:** Add seat blocking logic and concurrency.

### **Day 6 – Python Testing Suite**
- **Goal:** Create test cases for at least 3 earlier projects.
- **Key Concepts:** `unittest`, `pytest`, mocks, fixtures.
- **LLD Focus:** Testable architecture, separation of logic.
- **Stretch Goals:** Create coverage reports using `coverage.py`.

### **Day 7 – Config Loader + Secrets Manager**
- **Goal:** Build a library to load config/secrets from `.env`, YAML, or JSON.
- **Key Concepts:** `os.environ`, `dotenv`, modular file loaders.
- **LLD Focus:** Strategy pattern, interface segregation.
- **Stretch Goals:** Add CLI interface for setting secrets.

---

## 📅 Week 2 – Design Patterns, Concurrency, Async, and Infra

### **Day 8 – Pub-Sub Messaging System**
- **Goal:** Implement a publish-subscribe pattern based system.
- **Key Concepts:** Observer pattern, dynamic subscriptions.
- **LLD Focus:** Decoupled communication.
- **Stretch Goals:** Add topic-based channels and filters.

### **Day 9 – Multi-threaded Web Crawler**
- **Goal:** Crawl web pages concurrently and store titles/links.
- **Key Concepts:** Threads, `queue`, synchronization, `requests` + `bs4`.
- **LLD Focus:** Producer-consumer model.
- **Stretch Goals:** Add depth-level crawling or domain filters.

### **Day 10 – File Sync Daemon**
- **Goal:** Monitor a folder for changes and sync to backup.
- **Key Concepts:** `os`, `watchdog`, file system events.
- **LLD Focus:** File observer, service-like behavior.
- **Stretch Goals:** Add CLI for start/stop and sync rules.

### **Day 11 – Async Task Queue**
- **Goal:** Simulate a lightweight background task queue (like Celery).
- **Key Concepts:** `asyncio`, event loop, `await`, task queue.
- **LLD Focus:** Producer-consumer, async architecture.
- **Stretch Goals:** Add retry logic and task scheduling.

### **Day 12 – Rate Limiter Library**
- **Goal:** Create a library to rate limit function/API calls.
- **Key Concepts:** Sliding window, decorators, time module.
- **LLD Focus:** Middleware-style plug-n-play.
- **Stretch Goals:** Support Redis or memory backends.

### **Day 13 – Design Patterns Showcase**
- **Goal:** Implement 3 key design patterns: Factory, Strategy, Adapter.
- **Key Concepts:** Reusable OOP patterns.
- **LLD Focus:** Pattern usage in realistic mini-contexts.
- **Stretch Goals:** Add UML class diagrams.

### **Day 14 – Feature Flags SDK**
- **Goal:** Build a feature flag system that toggles features via config or API.
- **Key Concepts:** Config parsing, caching, dynamic toggles.
- **LLD Focus:** Proxy or Strategy pattern, toggle evaluation.
- **Stretch Goals:** REST API to toggle flags.

### **Day 15 – Configurable Job Scheduler**
- **Goal:** Create a job scheduler like mini-cron.
- **Key Concepts:** `datetime`, `sched`, config-driven execution.
- **LLD Focus:** Plug-in architecture, time-based scheduling.
- **Stretch Goals:** Persist job state and logs.

### **Day 16 – REST API Rate Limiter Middleware**
- **Goal:** Create a FastAPI/Flask middleware to rate-limit requests.
- **Key Concepts:** Token bucket, decorators, API middleware.
- **LLD Focus:** Middleware interface, reusable SDK.
- **Stretch Goals:** Deploy as a pip-installable package.

---

## ✅ Usage Tips
- Use `src/`, `tests/`, `config/` folder structure.
- Push each project to GitHub with clear README and test coverage.
- Add badges (build passing, test coverage) using GitHub Actions.
- Keep a blog or weekly write-up of what you learned.

---

This roadmap helps you gain real-world experience with Python and Low-Level Design in a progressive, practical manner. Happy building! 💻🔥
