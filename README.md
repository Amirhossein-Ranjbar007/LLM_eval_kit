# Simple LLM Evaluator Simulator

This is my first structural Python project! I built this simulator to practice Object-Oriented Programming (OOP) concepts and learn how to structure a Python application into multiple modules.

The project simulates evaluating different LLM providers (like Ollama and Claude) by tracking their response metrics and saving the history locally.

## Features

- **OOP Practice:** Uses Inheritance and Polymorphism with a base class (`BaseLLM`) and child classes for different providers.
- **Factory Pattern:** Uses a simple factory function to create model objects dynamically.
- **Metrics Tracking:** Measures the time taken, character count, and word count of responses.
- **Data Saving:** Saves the evaluation results automatically in a local `JSON` file.

## Project Layout

- `core/`: Contains the factory logic and the evaluator engine.
- `providers/`: Contains the base LLM class and simulated provider classes.
- `main.py`: The main script to run and test different scenarios.
- `evaluature_history.json`: The file where test results are saved.

## How to Run

1. Open your terminal in the project folder.
2. Run the following command:
   ```bash
   python main.py

------------------------------------------------------------------------------------------------------------------------

#  ترجمه فارسی:

```markdown
# شبیه‌ساز ساده‌ی ارزیابی مدل‌های زبانی (LLM)

این اولین پروژه ساختاریافته‌ی پایتون من است! من این شبیه‌ساز را ساختم تا مفاهیم برنامه‌نویسی شیءگرا (OOP) را تمرین کنم و یاد بگیرم که چگونه یک برنامه پایتون را به ماژول‌های مختلف تقسیم کنم.

این پروژه، ارزیابی پروایدرهای مختلف هوش مصنوعی (مثل اولاما و کلود) را با سنجش معیارهای پاسخ‌دهی آن‌ها و ذخیره تاریخچه به صورت محلی، شبیه‌سازی می‌کند.

#  ویژگی‌ها

- **تمرین شیءگرایی:** استفاده از ارث‌بری و چندریختی با یک کلاس پایه (BaseLLM) و کلاس‌های فرزند برای پروایدرهای مختلف.
- **الگوی کارخانه (Factory Pattern):** استفاده از یک تابع کارخانه ساده برای ساخت داینامیکِ شیءِ مدل‌ها.
- **سنجش معیارها:** اندازه‌گیری زمان صرف‌شده، تعداد کاراکترها و تعداد کلماتِ پاسخ‌ها.
- **ذخیره داده‌ها:** ذخیره خودکار نتایج ارزیابی در یک فایل JSON محلی.

# ساختار پروژه

- پوشه `core`: شامل منطق کارخانه و موتور ارزیاب.
- پوشه `providers`: شامل کلاس پایه LLM و کلاس‌های شبیه‌ساز پروایدرها.
- فایل `main.py`: اسکریپت اصلی برای اجرا و تست سناریوهای مختلف.
- فایل `evaluature_history.json`: فایلی که نتایج تست در آن ذخیره می‌شوند.

# نحوه اجرا

۱. ترمینال خود را در پوشه پروژه باز کنید.
۲. دستور زیر را اجرا کنید:
   ```bash










