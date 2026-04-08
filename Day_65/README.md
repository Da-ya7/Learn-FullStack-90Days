# Day 65 — DRF: ViewSets + Routers

> **Month 3 — Production · Week 10**

---

## 🐍 Python
class PostViewSet(ModelViewSet). router = DefaultRouter(). router.register('posts', PostViewSet). Auto-generates all URLs.

## 🗄️ SQL
Full-text search: ALTER TABLE ADD FULLTEXT INDEX on content column. SELECT ... WHERE MATCH(title) AGAINST('python').

## 🎨 Frontend (HTML / CSS / JS)
Login page: POST username+password to /api/token/. Store access and refresh tokens. Redirect on success.

---

*Part of [Learn-FullStack-90Days](../../README.md)*
