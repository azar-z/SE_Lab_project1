# SE_Lab_project1
# Smart Building IoT Platform: phase one

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

# گزارش کار پروژه 
شرح پروژه : در این پروژه میخواهیم با همکاری یکدیگر یک پلتفرم چندماژولی اینترنت اشیا را طراحی، توسعه و مدیریت کنیم.
## فاز اول: راه اندازی پروژه و استراتژی branching 
در این فاز تمرکز ما بر راه اندازی مخزن گیت، تعریف استراتژی شاخه بندی، ایحاد استاندازدهای کامیت و مدیریت milestones پروژه بود. هدف اصلی این فاز، فراهم سازی یک ساختار منظم برای توسعه همزمان چند ماژول و تسهیل فرایندهای همکاری تیمی بود.
## 1. راه اندازی مخزن 
### اقدامات انجام شده: 
- ایجاد مخزن گیت هاب با نام SE_Lab_project1
- اعمال قوانین حفاظت از شاخه ی زیر بر روی شاخه ی main:
  - Require a pull request before merging 
  - Restrict force pushes 
  - Require at least one approval before merging 
  - Require status checks to pass before merging (e.g., CI/CD)
## 2. ایجاد feature branch ها 
### اقدامات انجام شده: 
- با دستورات زیر، شاخه هایی برای توسعه مجزای ماژول ها ایجاد و به مخزن راه دور push کردیم:
  - `git checkout -b feature/iot-sensors`
  - `git push origin feature/iot-sensors`
  - `git checkout -b feature/web-dashboard`
  - `git push origin feature/web-dashboard`
- هر شاخه برای چه منظوری استفاده میشود؟
  - `feature/iot-sensors`: شاخه‌ای برای توسعه اسکریپت‌های مربوط به جمع‌آوری داده‌های سنسورها.
  - `feature/web-dashboard`: شاخه‌ای برای طراحی و پیاده‌سازی داشبورد وب جهت نمایش داده‌ها.
  - `main`: شاخه اصلی پروژه که محافظت شده و پایدار است.
- قرایند ایجاد شاخه ها با اسکرین شات:
  ![img.png](img.png)
## 3. تعیین استانداردهای کامیت و milestones 
### اقدامات انحام شده: 
- تعیین استاندارد برای نوشتن پیام های کامیت:
  - `feat`: اضافه کردن قابلیت جدید
  - `fix`: رفع باگ
  - `docs`: تغییرات مستندات
  - `refactor`: بهبود کد بدون تغییر در عملکرد
  - `test`: اضافه کردن تست
- تعریف milestones کلیدی در گیتهاب
  - `Initial Setup` (راه‌اندازی مخزن و استراتژی شاخه‌بندی)
  - `Feature Development` (توسعه ماژول‌های اولیه)
  - `CI/CD Integration` (پیاده‌سازی فرآیندهای CI/CD)
- ایجاد برچسب برای نسخه پایدار اولیه
  - `git tag -a v1.0.0 -m "first stable version"`
  - `git push origin v1.0.0`
## 4. ایجاد کانبان بورد در گیتهاب 
### اقدامات انجام شده: 
- ایجاد بورد کانبان با ستون های زیر:
  - `Backlog`: وظایف برنامه‌ریزی‌شده
  - `Ready`: وظایف در انتظار شروع
  - `In Progress`: وظایف در حال انجام
  - `In Review`: وظایف در مرحله بررسی و تست
  - `Done`: وظایف تکمیل‌شده
- ثبت issues برای تمامی وظایف یک شامل:
  - `setup`: ایجاد مخزن و تنظیم شاخه‌ها
  - `branching`: ایجاد شاخه‌های feature و مستندسازی آن
  - `documentation`: افزودن دستورالعمل‌های کامیت و Milestones
  - `security`: تنظیم حفاظت از شاخه و GitHub Actions
- تعیین مسئولیت‌ها برای اعضای تیم درگیتهاب.