# Day 51 — Django: Function-based views

> **Month 2 — Building · Week 8**

---

## 🐍 Python
def post_list(request): posts=Post.objects.all(); return render(request,'blog/list.html',{'posts':posts}). HttpResponse.

## 🗄️ SQL
MySQL backup: mysqldump -u root -p dbname > backup.sql. Restore: mysql -u root -p dbname < backup.sql.

## 🎨 Frontend (HTML / CSS / JS)
Error handling in Fetch: check response.ok, response.status. try/catch around await. Show user-friendly error messages.

---

*Part of [Learn-FullStack-90Days](../../README.md)*
