# Day 22 — pip + venv + Subquery in SELECT

> **Month 1 — Foundations · Week 4**

---

## 🐍 Python
pip install package, pip list, pip freeze > requirements.txt. python -m venv env. Activate: source env/bin/activate.

## 🗄️ SQL
Subquery in SELECT column: SELECT name, (SELECT COUNT(*) FROM orders WHERE student_id=s.id) as order_count FROM students s.

## 🎨 Frontend (HTML / CSS / JS)
Pseudo-classes: :hover, :focus, :active, :visited, :first-child, :last-child, :nth-child(n), :not().

---

*Part of [Learn-FullStack-90Days](../../README.md)*
