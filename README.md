# Mental With Math - Timed Mental Math Trainer

A timed, CLI-based mental math trainer built in Python — designed to sharpen speed and accuracy under pressure, track detailed performance analytics, and let you compete against other players on a cross-user leaderboard.

# Features

## Three difficulty tiers
Level 1 — Beginner: 1–2 digit addition, subtraction, multiplication and division

Level 2 — Intermediate: 2–3 digit operations, occasional percentage computation

Level 3 — Advanced: 3-digit operations, plus percentage computation

## Three timed modes 
1, 3, or 5-minute sessions, chosen at the start of each attempt.

## Weighted, difficulty-scaled question generation 
Operators (+, −, ×, ÷, %) are selected via weighted random sampling, with weights shifting toward harder operations as difficulty increases.

Questions test precise rate calculations, requiring answers rounded to 2 decimal places.

## Accuracy-weighted scoring 
+4 for every correct answer, −1 for every incorrect answer, rewarding accuracy over guessing.

## Detailed performance analytics per session:
Total score, questions attempted, net accuracy

Average response time per question (measured in real time)

Per-operator accuracy breakdown (addition / subtraction / multiplication / division / percentage)

A full review of every question answered incorrectly, with the correct answer shown alongside

## Persistent performance history 
Every session is logged to a personal CSV file, viewable at any time as a reverse-chronological performance log.

## Cross-user leaderboard
A central player registry tracks every user who has completed at least one session. The leaderboard aggregates each player's personal-best score at every difficulty level, ranks them, and displays results in a clean table — separately for Level 1, 2, and 3.

# How It Works

## The app is built around two core classes:

Test — handles difficulty/timemode selection, question generation, live scoring, and writing results to the player's personal CSV file.

User — handles reading every registered player's history, computing personal bests per level, and building the ranked, cross-user leaderboard.

Each player's data lives in its own CSV file ({username}.csv), keeping every user's history independent — no shared database required. A lightweight Username.csv registry tracks who's played, letting the leaderboard scale to any number of users.

## Author

Built by Sanchit Sethi as a self-directed project.
