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

<div dir="rtl" align="right">

# گزارش کار پروژه 
شرح پروژه : 
در این پروژه یک سامانه‌ی نمایش تغییرات دمای محیطی با استفاده از flask و html و js پیاده‌سازی شده است.

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


## فاز دوم: توسعه Feature ها، مدیریت Pull Request ها و بازبینی کد

## 1. توسعه در Feature Branch ها
در این فاز دو دو برنچ iot-sensors و web-dashboard به ترتیب بکند 
و فرانت‌اند پروژه به طور موازی پیاده‌سازی شده و در نهایت با استفاده از pull request و
حداقل یک بازبینی و تایید با برنچ اصلی پروژه ادغام شدند.
### iot sensors
در این برنچ با استفاده از flask یک اپلیکیشن پیاده‌سازی شد که دما را از سنسور دما دریافت کرده و در یک api بیست مورد دمای اخیر گرفته‌شده از سنسور را بازمی‌گرداند.
همچنین دسترسی به url فرانت برنامه نیز از طریق همین اپلیکیشن فراهم می‌شود.
به دلیل عدم دسترسی به سنسور دمای واقعی، دما در واقع به شکل تصادفی تولید می‌شود.
### web dashboard
در این برنچ فرانت پروژه پیاده‌سازی شده است که تنها شامل یک فایل html با script به زبان js است. این قطعه کد آرایه‌ای از دماهای اخیر را با استفاده از api دریافت کرده و سپس نمودار آن‌ها را رسم می‌کند. این نمودار هر ۲ ثانیه به‌روز می‌شود.

** در پیاده‌سازی این داشبورد از gpt کمک گرفته‌شده است. تنها ضعف آن که اصلاح شد عدم error handling بود.

## 2. روال Pull Request
از آن‌جایی که شاخه‌ی main محافظت شده است تمامی تغییرات با استفاده از pull request روی شاخه‌ی اصلی ادغام شده و حداقل به یک بازبینی نیاز داشتند.

همچنین در صورت لزوم کامنت‌های لازم هنگام بازبینی کدد گذاشته شده و پیش از مرج شدن برطرف می‌شدند.
نمونه‌ای از آن در لینک زیر قابل مشاهده است:

https://github.com/azar-z/SE_Lab_project1/pull/14

## 3. ایجاد Git Aliases و ارجاع به Pull Request ها
در این بخش از پروژه یک git alias جهت fetch کردن و همچنین checkout کردن به یک pull request نوشته شد. این alias در فایل .gitconfig سیستم لوکال یکی از اعضای تیم قرارداده شده و تست شد. مستندات مربوط به آن و نحوه‌ی استفاده از آن در GitCommands.md موجود است.

## 4. دغام ابزارهای کیفیت کد

### بررسی کیفیت کد با flake8
با نصب flake8 و همچنین قراردادن config آن در .flake8 می‌توان با اجرای دستوری مانند مثال زیر کیفیت یک فایل پایتون را بررسی کرد:
```
flake8 app.py
```
مواردی مانند indentation غلط و یا import بدون استفاده و ... در این ابزار مورد بررسی قرار می‌گیرند.
در حال حاضر طبق معیارهای این ابزار اخطاری در رابطه با کد پایتون این پروژه وجود ندارد.


### تست با استفاده از pytest
pytest یک ابزار تست به زبان پایتون است.
در این پروژه api اصلی برنامه که مربوط به دریافت لیست دماهای اخیر محیط بود را با استفاده از این ابزار به شکل‌ساده‌ای تست کردیم.

### ایجاد داکیومنت بازبینی کد
با کمک gpt داکیومنتی برای فرایند بازبینی کد ایجاد شد که نسبتا کامل بود. به دلیل استفاده از flake8 و pytest در این پروژه، بررسی این دو مورد نیز به داکیومنت اضافه شد.




</div>