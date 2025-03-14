# SE_Lab_project1
# Smart Building IoT Platform
## Branching Strategy
- **main branch**: Stable and protected.
- **Feature branches**: All new features are developed in separate branches (e.g., `feature/iot-sensors`, `feature/web-dashboard`).
- **Merging Policy**: Changes are only merged into `main` through pull requests after passing CI tests and code reviews.
## Feature Branches
- `feature/iot-sensors`: This branch is responsible for the development of IoT sensor scripts and data collection mechanisms.
- `feature/web-dashboard`: This branch is for building the web-based dashboard to display sensor data.
## Commit Message Standards
To maintain consistency, use the following format for commit messages:

- **feat:** Introduces a new feature (e.g., `feat: Added temperature sensor module`).
- **fix:** Fixes a bug (e.g., `fix: Resolved issue with data parsing`).
- **docs:** Changes related to documentation (e.g., `docs: Updated README with commit guidelines`).
- **refactor:** Improves code structure without changing functionality (e.g., `refactor: Cleaned up sensor.py`).
- **test:** Adds or updates tests (e.g., `test: Added unit tests for sensor module`).
- **chore:** Other minor tasks (e.g., `chore: Updated dependencies`).

Example: git commit -m "feat: Added initial IoT sensor data collection script"