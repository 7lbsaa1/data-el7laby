import os
import zipfile

project_dir = '/mnt/data/alhalabi_project'
os.makedirs(f'{project_dir}/css', exist_ok=True)
os.makedirs(f'{project_dir}/js', exist_ok=True)

admin_file_name = "adminsandkjsndkjndkadnajkfkjdsafbdskjfbioqhoey128e1jkehiu1y9012 ejknid903ue90un0eu12s dfvewrvewrvewa045f1dfdsf1df1dsf1s.html"
admin_clean_url = "/adminsandkjsndkjndkadnajkfkjdsafbdskjfbioqhoey128e1jkehiu1y9012%20ejknid903ue90un0eu12s%20dfvewrvewrvewa045f1dfdsf1df1dsf1s"

# --- HTML Files ---

index_html = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>شركة الحلبي - قاعدة بيانات الأعضاء</title>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/css/style.css">
    <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body>
    <div class="layout">
        <!-- Sidebar -->
        <aside class="sidebar">
            <div class="logo">
                <div class="logo-icon"><i data-lucide="building-2"></i></div>
                <div class="logo-text">
                    <h2>شركة الحلبي</h2>
                    <p>قاعدة بيانات الأعضاء</p>
                </div>
            </div>
            <nav class="nav-menu">
                <a href="/" class="nav-item active"><i data-lucide="users"></i> الأعضاء</a>
                <a href="#" class="nav-item"><i data-lucide="briefcase"></i> الإدارات</a>
                <a href="#" class="nav-item"><i data-lucide="user-check"></i> المناصب</a>
                <a href="#" class="nav-item"><i data-lucide="shield-check"></i> الصلاحيات</a>
                <a href="#" class="nav-item"><i data-lucide="file-text"></i> التقارير</a>
                <a href="#" class="nav-item"><i data-lucide="settings"></i> الإعدادات</a>
            </nav>
            <div class="sidebar-widget">
                <i data-lucide="users" class="widget-icon"></i>
                <p>إجمالي الأعضاء</p>
                <h3 id="sidebarTotalMembers">0</h3>
                <span class="widget-sub">عضو نشط في النظام</span>
            </div>
        </aside>

        <!-- Main Content -->
        <main class="main-content">
            <header class="top-header">
                <div class="header-titles">
                    <h1>قاعدة بيانات أعضاء الشركة</h1>
                    <p>عرض وإدارة جميع أعضاء الشركة</p>
                    <div class="breadcrumb">الرئيسية / <span>الأعضاء</span></div>
                </div>
                <div class="header-actions">
                    <button class="icon-btn"><i data-lucide="bell"></i><span class="badge"></span></button>
                    <div class="user-profile">
                        <div class="user-info">
                            <h4>مدير النظام</h4>
                            <span>مسؤول النظام</span>
                        </div>
                        <div class="avatar"><i data-lucide="user"></i></div>
                    </div>
                </div>
            </header>

            <!-- Stats -->
            <section class="stats-grid">
                <div class="stat-card">
                    <div class="stat-info">
                        <h3 id="statTotalMembers">0</h3>
                        <p>إجمالي الأعضاء</p>
                    </div>
                    <div class="stat-icon"><i data-lucide="users"></i></div>
                </div>
                <div class="stat-card">
                    <div class="stat-info">
                        <h3 id="statDepartments">0</h3>
                        <p>الإدارات</p>
                    </div>
                    <div class="stat-icon"><i data-lucide="building"></i></div>
                </div>
                <div class="stat-card">
                    <div class="stat-info">
                        <h3 id="statPositions">0</h3>
                        <p>المناصب</p>
                    </div>
                    <div class="stat-icon"><i data-lucide="briefcase"></i></div>
                </div>
                <div class="stat-card">
                    <div class="stat-info">
                        <h3 id="statNewMembers">0</h3>
                        <p>الأعضاء الجدد هذا الشهر</p>
                    </div>
                    <div class="stat-icon"><i data-lucide="user-plus"></i></div>
                </div>
            </section>

            <!-- Table Section -->
            <section class="table-section">
                <div class="table-toolbar">
                    <div class="search-box">
                        <i data-lucide="search"></i>
                        <input type="text" id="searchInput" placeholder="ابحث عن عضو...">
                    </div>
                    <div class="toolbar-actions">
                        <button class="btn-outline"><i data-lucide="filter"></i> كل الإدارات</button>
                        <a href="{admin_clean_url}" class="btn-primary"><i data-lucide="plus"></i> إضافة عضو جديد</a>
                    </div>
                </div>

                <div id="loadingState" class="state-container">
                    <i data-lucide="loader-2" class="spin-icon"></i>
                    <p>جاري تحميل بيانات الأعضاء...</p>
                </div>

                <div id="emptyState" class="state-container" style="display: none;">
                    <i data-lucide="users" class="empty-icon"></i>
                    <p>لا يوجد أعضاء حتى الآن</p>
                    <a href="{admin_clean_url}" class="btn-primary" style="margin-top: 1rem;">إضافة عضو جديد</a>
                </div>

                <div class="table-container" id="tableContainer" style="display: none;">
                    <table>
                        <thead>
                            <tr>
                                <th>الاسم الكامل</th>
                                <th>المنصب</th>
                                <th>الإدارة</th>
                                <th>البريد الإلكتروني</th>
                                <th>رقم الهاتف</th>
                                <th>تاريخ الانضمام</th>
                                <th>الحالة</th>
                                <th>الإجراءات</th>
                            </tr>
                        </thead>
                        <tbody id="membersTableBody">
                            <!-- Rows will be injected by JS -->
                        </tbody>
                    </table>
                </div>

                <div class="pagination" id="pagination">
                    <!-- Pagination injected by JS -->
                </div>
            </section>
        </main>
    </div>

    <!-- Details Modal -->
    <div id="detailsModal" class="modal">
        <div class="modal-content glass-effect">
            <button class="close-modal"><i data-lucide="x"></i></button>
            <h2 class="modal-title">تفاصيل العضو</h2>
            <div id="modalBody"></div>
        </div>
    </div>

    <!-- Delete Confirmation Modal -->
    <div id="deleteModal" class="modal">
        <div class="modal-content glass-effect delete-content">
            <i data-lucide="alert-triangle" class="warning-icon"></i>
            <h2>تأكيد الحذف</h2>
            <p>هل أنت متأكد من رغبتك في حذف هذا العضو؟ لا يمكن التراجع عن هذا الإجراء.</p>
            <div class="modal-actions">
                <button id="confirmDeleteBtn" class="btn-danger">حذف العضو</button>
                <button class="btn-secondary close-modal">إلغاء</button>
            </div>
        </div>
    </div>

    <!-- Toast Container -->
    <div id="toastContainer"></div>

    <script type="module" src="/js/app.js"></script>
    <script>
        lucide.createIcons();
    </script>
</body>
</html>
"""

admin_html = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>إدارة الأعضاء - شركة الحلبي</title>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/css/style.css">
    <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body>
    <div class="layout">
        <!-- Sidebar -->
        <aside class="sidebar">
            <div class="logo">
                <div class="logo-icon"><i data-lucide="building-2"></i></div>
                <div class="logo-text">
                    <h2>شركة الحلبي</h2>
                    <p>قاعدة بيانات الأعضاء</p>
                </div>
            </div>
            <nav class="nav-menu">
                <a href="/" class="nav-item"><i data-lucide="users"></i> الأعضاء</a>
                <a href="#" class="nav-item"><i data-lucide="briefcase"></i> الإدارات</a>
                <a href="#" class="nav-item"><i data-lucide="user-check"></i> المناصب</a>
                <a href="#" class="nav-item"><i data-lucide="shield-check"></i> الصلاحيات</a>
                <a href="#" class="nav-item"><i data-lucide="file-text"></i> التقارير</a>
                <a href="#" class="nav-item"><i data-lucide="settings"></i> الإعدادات</a>
            </nav>
        </aside>

        <!-- Main Content -->
        <main class="main-content">
            <header class="top-header">
                <div class="header-titles">
                    <h1 id="pageTitle">إضافة عضو جديد</h1>
                    <p id="pageDesc">قم بإدخال بيانات العضو لإضافته إلى قاعدة بيانات الشركة</p>
                    <div class="breadcrumb"><a href="/">الرئيسية</a> / <span>إدارة الأعضاء</span></div>
                </div>
                <div class="header-actions">
                    <a href="/" class="btn-outline"><i data-lucide="arrow-right"></i> العودة للقائمة</a>
                </div>
            </header>

            <section class="form-section glass-effect">
                <form id="memberForm">
                    <div class="form-grid">
                        <div class="form-group">
                            <label>الاسم الكامل <span class="required">*</span></label>
                            <input type="text" id="name" required placeholder="أدخل الاسم الرباعي">
                        </div>
                        <div class="form-group">
                            <label>السن <span class="required">*</span></label>
                            <input type="number" id="age" required placeholder="أدخل العمر">
                        </div>
                        <div class="form-group">
                            <label>رقم الهاتف</label>
                            <input type="tel" id="phone" placeholder="مثال: +966...">
                        </div>
                        <div class="form-group">
                            <label>البريد الإلكتروني</label>
                            <input type="email" id="email" placeholder="example@company.com">
                        </div>
                        <div class="form-group">
                            <label>المنصب</label>
                            <input type="text" id="position" placeholder="المسمى الوظيفي">
                        </div>
                        <div class="form-group">
                            <label>الإدارة</label>
                            <select id="department">
                                <option value="">اختر الإدارة...</option>
                                <option value="الإدارة التنفيذية">الإدارة التنفيذية</option>
                                <option value="الموارد البشرية">الموارد البشرية</option>
                                <option value="المحاسبة والمالية">المحاسبة والمالية</option>
                                <option value="تقنية المعلومات">تقنية المعلومات</option>
                                <option value="المبيعات والتسويق">المبيعات والتسويق</option>
                                <option value="المشاريع">المشاريع</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label>تاريخ الانضمام</label>
                            <input type="date" id="joinDate">
                        </div>
                        <div class="form-group">
                            <label>الحالة</label>
                            <select id="status">
                                <option value="نشط">نشط</option>
                                <option value="غير نشط">غير نشط</option>
                            </select>
                        </div>
                        <div class="form-group full-width">
                            <label>مكان السكن</label>
                            <input type="text" id="address" placeholder="العنوان بالتفصيل">
                        </div>
                        
                        <div class="form-group full-width">
                            <label>الصورة الشخصية (اختياري)</label>
                            <div class="file-upload">
                                <input type="file" id="profileImage" accept="image/*">
                                <i data-lucide="upload-cloud"></i>
                                <span>اختر صورة أو اسحبها هنا</span>
                            </div>
                            <img id="profilePreview" class="img-preview" style="display:none">
                        </div>

                        <div class="form-group full-width">
                            <label>صورة البطاقة الشخصية (اختياري - سري)</label>
                            <div class="file-upload">
                                <input type="file" id="idCardImage" accept="image/*">
                                <i data-lucide="file-image"></i>
                                <span>اختر صورة البطاقة</span>
                            </div>
                            <img id="idCardPreview" class="img-preview" style="display:none">
                        </div>
                    </div>

                    <div class="form-actions">
                        <button type="submit" class="btn-primary" id="submitBtn"><i data-lucide="save"></i> إضافة العضو</button>
                    </div>
                </form>
            </section>
        </main>
    </div>

    <!-- Toast Container -->
    <div id="toastContainer"></div>

    <script type="module" src="/js/admin.js"></script>
    <script>
        lucide.createIcons();
    </script>
</body>
</html>
"""

# --- CSS File ---

style_css = """
:root {
    --bg-main: #0b101e;
    --bg-sidebar: #101626;
    --bg-card: #151d30;
    --bg-card-hover: #1a233a;
    --gold-primary: #cfa257;
    --gold-hover: #e5b869;
    --gold-dim: rgba(207, 162, 87, 0.1);
    --text-main: #f8fafc;
    --text-muted: #94a3b8;
    --border-color: #232d45;
    --success: #10b981;
    --danger: #ef4444;
    --font-family: 'Tajawal', sans-serif;
    --radius-md: 8px;
    --radius-lg: 12px;
    --radius-xl: 16px;
    --transition: all 0.3s ease;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: var(--font-family);
    background-color: var(--bg-main);
    color: var(--text-main);
    direction: rtl;
    min-height: 100vh;
}

/* Layout */
.layout {
    display: flex;
    min-height: 100vh;
}

/* Sidebar */
.sidebar {
    width: 260px;
    background-color: var(--bg-sidebar);
    border-left: 1px solid var(--border-color);
    display: flex;
    flex-direction: column;
    padding: 2rem 1.5rem;
    position: fixed;
    height: 100vh;
    right: 0;
    top: 0;
    z-index: 10;
}

.logo {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 3rem;
}

.logo-icon {
    color: var(--gold-primary);
}

.logo-icon svg { width: 32px; height: 32px; }

.logo-text h2 {
    font-size: 1.2rem;
    font-weight: 700;
    color: var(--gold-primary);
}

.logo-text p {
    font-size: 0.8rem;
    color: var(--text-muted);
}

.nav-menu {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    flex: 1;
}

.nav-item {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 1rem;
    color: var(--text-muted);
    text-decoration: none;
    border-radius: var(--radius-md);
    transition: var(--transition);
    font-weight: 500;
}

.nav-item svg { width: 20px; height: 20px; }

.nav-item:hover {
    background-color: var(--bg-card);
    color: var(--text-main);
}

.nav-item.active {
    background-color: var(--gold-dim);
    color: var(--gold-primary);
    border-right: 3px solid var(--gold-primary);
}

.sidebar-widget {
    background: var(--bg-card);
    border: 1px solid var(--gold-primary);
    border-radius: var(--radius-lg);
    padding: 1.5rem;
    text-align: center;
    margin-top: auto;
    position: relative;
    overflow: hidden;
}

.sidebar-widget::before {
    content: '';
    position: absolute;
    top: -50%; left: -50%; width: 200%; height: 200%;
    background: radial-gradient(circle, rgba(207, 162, 87, 0.05) 0%, transparent 70%);
}

.widget-icon {
    color: var(--gold-primary);
    margin-bottom: 0.5rem;
    width: 32px; height: 32px;
}

.sidebar-widget p { font-size: 0.9rem; margin-bottom: 0.5rem; }
.sidebar-widget h3 { font-size: 2rem; color: var(--gold-primary); font-weight: 800; margin-bottom: 0.2rem; }
.sidebar-widget .widget-sub { font-size: 0.75rem; color: var(--text-muted); }

/* Main Content */
.main-content {
    flex: 1;
    margin-right: 260px;
    padding: 2rem 3rem;
}

.top-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 3rem;
}

.header-titles h1 {
    font-size: 1.8rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}

.header-titles p {
    color: var(--text-muted);
    font-size: 0.95rem;
    margin-bottom: 0.5rem;
}

.breadcrumb {
    font-size: 0.85rem;
    color: var(--text-muted);
}
.breadcrumb a { color: var(--text-muted); text-decoration: none; }
.breadcrumb span { color: var(--gold-primary); }

.header-actions {
    display: flex;
    align-items: center;
    gap: 1.5rem;
}

.icon-btn {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    color: var(--text-main);
    width: 40px; height: 40px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: var(--transition);
    position: relative;
}

.icon-btn:hover { border-color: var(--gold-primary); }

.icon-btn .badge {
    position: absolute;
    top: -2px; right: -2px;
    width: 10px; height: 10px;
    background: var(--danger);
    border-radius: 50%;
    border: 2px solid var(--bg-main);
}

.user-profile {
    display: flex;
    align-items: center;
    gap: 1rem;
}

.user-info { text-align: left; }
.user-info h4 { font-size: 0.9rem; font-weight: 600; }
.user-info span { font-size: 0.75rem; color: var(--text-muted); }
.user-profile .avatar {
    width: 45px; height: 45px;
    background: var(--bg-card);
    border: 1px solid var(--gold-primary);
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    color: var(--gold-primary);
}

/* Stats Grid */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1.5rem;
    margin-bottom: 2rem;
}

.stat-card {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    padding: 1.5rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: var(--transition);
}

.stat-card:hover { border-color: var(--gold-primary); transform: translateY(-3px); }

.stat-info h3 { font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem; }
.stat-info p { color: var(--text-muted); font-size: 0.9rem; }
.stat-icon { color: var(--gold-primary); opacity: 0.8; }
.stat-icon svg { width: 36px; height: 36px; stroke-width: 1.5px; }

/* Table Section */
.table-section {
    background: var(--bg-sidebar);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    padding: 1.5rem;
}

.table-toolbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.5rem;
    flex-wrap: wrap;
    gap: 1rem;
}

.search-box {
    position: relative;
    width: 350px;
}

.search-box svg {
    position: absolute;
    right: 15px; top: 50%;
    transform: translateY(-50%);
    color: var(--text-muted);
    width: 18px; height: 18px;
}

.search-box input {
    width: 100%;
    background: var(--bg-main);
    border: 1px solid var(--border-color);
    color: var(--text-main);
    padding: 0.8rem 1rem 0.8rem 2.5rem;
    border-radius: var(--radius-md);
    font-family: inherit;
    transition: var(--transition);
}

.search-box input:focus {
    outline: none;
    border-color: var(--gold-primary);
}

.toolbar-actions {
    display: flex;
    gap: 1rem;
}

.btn-primary, .btn-outline, .btn-secondary, .btn-danger {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.8rem 1.5rem;
    border-radius: var(--radius-md);
    font-family: inherit;
    font-weight: 600;
    cursor: pointer;
    transition: var(--transition);
    text-decoration: none;
    border: none;
}

.btn-primary {
    background: var(--gold-primary);
    color: var(--bg-main);
}
.btn-primary:hover { background: var(--gold-hover); }

.btn-outline {
    background: transparent;
    border: 1px solid var(--border-color);
    color: var(--text-main);
}
.btn-outline:hover { border-color: var(--gold-primary); color: var(--gold-primary); }

.btn-secondary { background: var(--border-color); color: var(--text-main); }
.btn-secondary:hover { background: #334155; }

.btn-danger { background: var(--danger); color: white; }
.btn-danger:hover { background: #dc2626; }

/* Table */
.table-container {
    overflow-x: auto;
}

table {
    width: 100%;
    border-collapse: collapse;
    min-width: 1000px;
}

th {
    text-align: right;
    padding: 1rem;
    color: var(--text-muted);
    font-weight: 500;
    border-bottom: 1px solid var(--border-color);
    font-size: 0.9rem;
}

td {
    padding: 1rem;
    border-bottom: 1px solid var(--border-color);
    font-size: 0.95rem;
    vertical-align: middle;
}

tbody tr { transition: var(--transition); }
tbody tr:hover { background: var(--bg-card); }

.user-cell {
    display: flex;
    align-items: center;
    gap: 1rem;
}

.user-avatar {
    width: 40px; height: 40px;
    border-radius: 50%;
    object-fit: cover;
    background: var(--bg-main);
    border: 1px solid var(--gold-primary);
}

.avatar-fallback {
    width: 40px; height: 40px;
    border-radius: 50%;
    background: var(--gold-dim);
    color: var(--gold-primary);
    display: flex; align-items: center; justify-content: center;
    font-weight: 700;
    border: 1px solid var(--gold-primary);
}

.status-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    font-size: 0.8rem;
}

.status-active { color: var(--success); }
.status-active::before { content: ''; width: 6px; height: 6px; border-radius: 50%; background: var(--success); }
.status-inactive { color: var(--text-muted); }
.status-inactive::before { content: ''; width: 6px; height: 6px; border-radius: 50%; background: var(--text-muted); }

.action-btns {
    display: flex;
    gap: 0.5rem;
}

.action-btn {
    background: var(--bg-main);
    border: 1px solid var(--border-color);
    color: var(--text-muted);
    width: 32px; height: 32px;
    border-radius: var(--radius-md);
    display: flex; align-items: center; justify-content: center;
    cursor: pointer; transition: var(--transition);
}
.action-btn svg { width: 16px; height: 16px; }
.action-btn:hover { border-color: var(--gold-primary); color: var(--gold-primary); }
.action-btn.delete:hover { border-color: var(--danger); color: var(--danger); }

/* Pagination */
.pagination {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 1.5rem;
    padding-top: 1.5rem;
    border-top: 1px solid var(--border-color);
}

.page-numbers {
    display: flex;
    gap: 0.5rem;
}

.page-btn {
    width: 36px; height: 36px;
    display: flex; align-items: center; justify-content: center;
    background: var(--bg-main);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    color: var(--text-main);
    cursor: pointer;
    font-family: inherit;
}

.page-btn.active {
    background: var(--gold-primary);
    color: var(--bg-main);
    border-color: var(--gold-primary);
}

.page-btn:hover:not(.active) { border-color: var(--gold-primary); }

/* States */
.state-container {
    text-align: center;
    padding: 4rem 2rem;
    color: var(--text-muted);
}
.spin-icon { animation: spin 1s linear infinite; margin-bottom: 1rem; width: 40px; height: 40px; color: var(--gold-primary); }
.empty-icon { width: 64px; height: 64px; opacity: 0.5; margin-bottom: 1rem; }
@keyframes spin { 100% { transform: rotate(360deg); } }

/* Forms */
.form-section {
    background: var(--bg-sidebar);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    padding: 2.5rem;
    max-width: 900px;
}

.form-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
}

.form-group { display: flex; flex-direction: column; gap: 0.5rem; }
.form-group.full-width { grid-column: 1 / -1; }

.form-group label { font-size: 0.95rem; font-weight: 500; }
.required { color: var(--danger); }

.form-group input, .form-group select {
    background: var(--bg-main);
    border: 1px solid var(--border-color);
    color: var(--text-main);
    padding: 0.9rem 1rem;
    border-radius: var(--radius-md);
    font-family: inherit;
    font-size: 0.95rem;
    transition: var(--transition);
}

.form-group input:focus, .form-group select:focus {
    outline: none;
    border-color: var(--gold-primary);
}

.file-upload {
    border: 2px dashed var(--border-color);
    padding: 2rem;
    border-radius: var(--radius-md);
    text-align: center;
    position: relative;
    cursor: pointer;
    transition: var(--transition);
}
.file-upload:hover { border-color: var(--gold-primary); }
.file-upload input { position: absolute; width: 100%; height: 100%; top: 0; left: 0; opacity: 0; cursor: pointer; }
.file-upload svg { width: 32px; height: 32px; color: var(--gold-primary); margin-bottom: 0.5rem; }
.file-upload span { display: block; color: var(--text-muted); }

.img-preview {
    max-width: 150px;
    border-radius: var(--radius-md);
    margin-top: 1rem;
    border: 1px solid var(--border-color);
}

.form-actions { margin-top: 2.5rem; display: flex; justify-content: flex-end; }

/* Modals */
.modal {
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(11, 16, 30, 0.85);
    backdrop-filter: blur(5px);
    display: flex; align-items: center; justify-content: center;
    z-index: 1000;
    opacity: 0; pointer-events: none;
    transition: var(--transition);
}

.modal.active { opacity: 1; pointer-events: auto; }

.modal-content {
    background: var(--bg-sidebar);
    border: 1px solid var(--gold-dim);
    border-radius: var(--radius-lg);
    width: 90%; max-width: 600px;
    padding: 2.5rem;
    position: relative;
    transform: translateY(20px);
    transition: var(--transition);
    max-height: 90vh;
    overflow-y: auto;
}

.modal.active .modal-content { transform: translateY(0); }

.close-modal {
    position: absolute;
    top: 1.5rem; left: 1.5rem;
    background: none; border: none;
    color: var(--text-muted); cursor: pointer;
    transition: var(--transition);
}
.close-modal:hover { color: var(--danger); }

.modal-title { font-size: 1.5rem; margin-bottom: 1.5rem; color: var(--gold-primary); }

.member-profile-modal {
    display: flex;
    align-items: center;
    gap: 1.5rem;
    margin-bottom: 2rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid var(--border-color);
}

.member-profile-modal img {
    width: 80px; height: 80px; border-radius: 50%; object-fit: cover;
    border: 2px solid var(--gold-primary);
}

.member-details-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
}

.detail-item { font-size: 0.95rem; }
.detail-item span { color: var(--text-muted); display: block; margin-bottom: 0.3rem; font-size: 0.85rem; }
.detail-item.full-width { grid-column: 1 / -1; }
.id-card-img { max-width: 100%; border-radius: var(--radius-md); border: 1px solid var(--border-color); margin-top: 0.5rem; }

.delete-content { text-align: center; max-width: 400px; }
.warning-icon { width: 48px; height: 48px; color: var(--danger); margin-bottom: 1rem; }
.delete-content h2 { margin-bottom: 1rem; }
.delete-content p { color: var(--text-muted); margin-bottom: 2rem; }
.modal-actions { display: flex; gap: 1rem; justify-content: center; }

/* Toasts */
#toastContainer { position: fixed; bottom: 2rem; left: 2rem; z-index: 9999; display: flex; flex-direction: column; gap: 1rem; }
.toast {
    padding: 1rem 1.5rem; border-radius: var(--radius-md); color: white; display: flex; align-items: center; gap: 0.8rem;
    animation: slideIn 0.3s ease forwards;
}
.toast.success { background: var(--success); }
.toast.error { background: var(--danger); }
@keyframes slideIn { from { transform: translateX(-100%); opacity: 0; } to { transform: translateX(0); opacity: 1; } }

/* Responsive */
@media (max-width: 1024px) {
    .sidebar { width: 80px; padding: 2rem 0.5rem; }
    .logo-text, .nav-item span, .sidebar-widget { display: none; }
    .nav-item { justify-content: center; }
    .main-content { margin-right: 80px; padding: 1.5rem; }
    .stats-grid { grid-template-columns: 1fr 1fr; }
}

@media (max-width: 768px) {
    .layout { flex-direction: column; }
    .sidebar { position: relative; width: 100%; height: auto; flex-direction: row; padding: 1rem; border-left: none; border-bottom: 1px solid var(--border-color); }
    .nav-menu { flex-direction: row; justify-content: center; }
    .main-content { margin-right: 0; padding: 1rem; }
    .stats-grid { grid-template-columns: 1fr; }
    .top-header { flex-direction: column; gap: 1rem; }
    .form-grid { grid-template-columns: 1fr; }
    .member-details-grid { grid-template-columns: 1fr; }
}
"""

# --- JS: firebase-config.js ---
firebase_config_js = """
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
import { getDatabase } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-database.js";
import { getStorage } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-storage.js";

const firebaseConfig = {
  apiKey: "AIzaSyBWTSFTecq2_QeDyg90mM1hPNytwPXYyZ0",
  authDomain: "admin-37e09.firebaseapp.com",
  databaseURL: "https://admin-37e09-default-rtdb.firebaseio.com",
  projectId: "admin-37e09",
  storageBucket: "admin-37e09.firebasestorage.app",
  messagingSenderId: "637953105703",
  appId: "1:637953105703:web:db22cf323186b157de5302",
  measurementId: "G-GQDLTK8FY6"
};

const app = initializeApp(firebaseConfig);
export const db = getDatabase(app);
export const storage = getStorage(app);

export const showToast = (message, type = 'success') => {
    const container = document.getElementById('toastContainer');
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    const icon = type === 'success' ? 'check-circle' : 'alert-circle';
    toast.innerHTML = `<i data-lucide="${icon}"></i> <span>${message}</span>`;
    container.appendChild(toast);
    if(window.lucide) lucide.createIcons();
    setTimeout(() => {
        toast.style.opacity = '0';
        setTimeout(() => toast.remove(), 300);
    }, 3000);
};
"""

# --- JS: app.js ---
app_js = f"""
import {{ db, showToast }} from './firebase-config.js';
import {{ ref, onValue, remove }} from "https://www.gstatic.com/firebasejs/10.8.0/firebase-database.js";

let currentMembers = [];
let filteredMembers = [];
let currentPage = 1;
const rowsPerPage = 10;
let memberToDelete = null;

const adminUrl = "{admin_clean_url}";

// DOM Elements
const tableBody = document.getElementById('membersTableBody');
const loadingState = document.getElementById('loadingState');
const emptyState = document.getElementById('emptyState');
const tableContainer = document.getElementById('tableContainer');
const searchInput = document.getElementById('searchInput');
const pagination = document.getElementById('pagination');

// Modals
const detailsModal = document.getElementById('detailsModal');
const deleteModal = document.getElementById('deleteModal');
const modalBody = document.getElementById('modalBody');

// Fetch Real-time Data
const membersRef = ref(db, 'members');
onValue(membersRef, (snapshot) => {{
    const data = snapshot.val();
    currentMembers = [];
    if (data) {{
        for (let key in data) {{
            currentMembers.push({{ id: key, ...data[key] }});
        }}
        // Sort by newest
        currentMembers.sort((a, b) => new Date(b.createdAt) - new Date(a.createdAt));
    }}
    
    updateStats();
    handleSearch(); // Applies current search & renders
    
    loadingState.style.display = 'none';
    if (currentMembers.length === 0) {{
        emptyState.style.display = 'block';
        tableContainer.style.display = 'none';
        pagination.style.display = 'none';
    }} else {{
        emptyState.style.display = 'none';
        tableContainer.style.display = 'block';
    }}
}}, (error) => {{
    showToast('تعذر الاتصال بقاعدة البيانات', 'error');
    console.error(error);
}});

// Calculate Stats
function updateStats() {{
    document.getElementById('sidebarTotalMembers').textContent = currentMembers.filter(m => m.status === 'نشط').length;
    document.getElementById('statTotalMembers').textContent = currentMembers.length;
    
    const departments = new Set(currentMembers.map(m => m.department).filter(d => d));
    document.getElementById('statDepartments').textContent = departments.size;
    
    const positions = new Set(currentMembers.map(m => m.position).filter(p => p));
    document.getElementById('statPositions').textContent = positions.size;
    
    const thirtyDaysAgo = new Date();
    thirtyDaysAgo.setDate(thirtyDaysAgo.getDate() - 30);
    const newMembers = currentMembers.filter(m => new Date(m.createdAt) >= thirtyDaysAgo);
    document.getElementById('statNewMembers').textContent = newMembers.length;
}}

// Search Logic
searchInput.addEventListener('input', (e) => {{
    currentPage = 1;
    handleSearch();
}});

function handleSearch() {{
    const query = searchInput.value.toLowerCase().trim();
    if (!query) {{
        filteredMembers = [...currentMembers];
    }} else {{
        filteredMembers = currentMembers.filter(m => 
            (m.name && m.name.toLowerCase().includes(query)) ||
            (m.phone && m.phone.includes(query)) ||
            (m.email && m.email.toLowerCase().includes(query)) ||
            (m.position && m.position.toLowerCase().includes(query)) ||
            (m.department && m.department.toLowerCase().includes(query))
        );
    }}
    renderTable();
}}

// Render Table
function renderTable() {{
    tableBody.innerHTML = '';
    
    if (filteredMembers.length === 0 && currentMembers.length > 0) {{
        tableBody.innerHTML = `<tr><td colspan="8" style="text-align:center; padding:2rem;">لم يتم العثور على أعضاء مطابقين للبحث</td></tr>`;
        pagination.style.display = 'none';
        return;
    }}
    
    const start = (currentPage - 1) * rowsPerPage;
    const paginated = filteredMembers.slice(start, start + rowsPerPage);
    
    paginated.forEach(member => {{
        const tr = document.createElement('tr');
        
        const avatarHtml = member.profileImage 
            ? `<img src="${{member.profileImage}}" class="user-avatar" alt="Avatar">`
            : `<div class="avatar-fallback">${{member.name.charAt(0)}}</div>`;
            
        tr.innerHTML = `
            <td>
                <div class="user-cell">
                    ${{avatarHtml}}
                    <strong>${{member.name}}</strong>
                </div>
            </td>
            <td>${{member.position || 'غير متوفر'}}</td>
            <td>${{member.department || 'غير متوفر'}}</td>
            <td>${{member.email || 'غير متوفر'}}</td>
            <td dir="ltr" style="text-align:right">${{member.phone || 'غير متوفر'}}</td>
            <td>${{member.joinDate || 'غير متوفر'}}</td>
            <td><span class="status-badge ${{member.status === 'نشط' ? 'status-active' : 'status-inactive'}}">${{member.status || 'غير متوفر'}}</span></td>
            <td>
                <div class="action-btns">
                    <button class="action-btn" onclick="viewMember('${{member.id}}')" title="عرض التفاصيل"><i data-lucide="eye"></i></button>
                    <a href="${{adminUrl}}?edit=${{member.id}}" class="action-btn" title="تعديل"><i data-lucide="edit-2"></i></a>
                    <button class="action-btn delete" onclick="openDeleteModal('${{member.id}}')" title="حذف"><i data-lucide="trash-2"></i></button>
                </div>
            </td>
        `;
        tableBody.appendChild(tr);
    }});
    
    lucide.createIcons();
    renderPagination();
}}

// Render Pagination
function renderPagination() {{
    const totalPages = Math.ceil(filteredMembers.length / rowsPerPage);
    pagination.innerHTML = '';
    
    if (totalPages <= 1) {{
        pagination.style.display = 'none';
        return;
    }}
    
    pagination.style.display = 'flex';
    
    const prevBtn = document.createElement('button');
    prevBtn.className = 'btn-outline';
    prevBtn.innerText = 'السابق';
    prevBtn.disabled = currentPage === 1;
    if(!prevBtn.disabled) prevBtn.onclick = () => {{ currentPage--; renderTable(); }};
    
    const nextBtn = document.createElement('button');
    nextBtn.className = 'btn-outline';
    nextBtn.innerText = 'التالي';
    nextBtn.disabled = currentPage === totalPages;
    if(!nextBtn.disabled) nextBtn.onclick = () => {{ currentPage++; renderTable(); }};
    
    const numbersDiv = document.createElement('div');
    numbersDiv.className = 'page-numbers';
    
    for (let i = 1; i <= totalPages; i++) {{
        const btn = document.createElement('button');
        btn.className = `page-btn ${{i === currentPage ? 'active' : ''}}`;
        btn.innerText = i;
        btn.onclick = () => {{ currentPage = i; renderTable(); }};
        numbersDiv.appendChild(btn);
    }}
    
    const info = document.createElement('span');
    info.style.color = 'var(--text-muted)';
    info.style.fontSize = '0.9rem';
    const startTxt = filteredMembers.length === 0 ? 0 : (currentPage - 1) * rowsPerPage + 1;
    const endTxt = Math.min(currentPage * rowsPerPage, filteredMembers.length);
    info.innerText = `عرض ${{endTxt}} من ${{filteredMembers.length}} عضو`;
    
    pagination.appendChild(prevBtn);
    pagination.appendChild(numbersDiv);
    pagination.appendChild(nextBtn);
    
    // insert info before prevBtn if we want, but simple layout is fine
}}

// View Member Details
window.viewMember = (id) => {{
    const member = currentMembers.find(m => m.id === id);
    if (!member) return;
    
    const avatarHtml = member.profileImage 
        ? `<img src="${{member.profileImage}}" alt="Avatar">`
        : `<div class="avatar-fallback" style="width:80px;height:80px;font-size:2rem;">${{member.name.charAt(0)}}</div>`;
        
    modalBody.innerHTML = `
        <div class="member-profile-modal">
            ${{avatarHtml}}
            <div>
                <h3 style="font-size:1.4rem;margin-bottom:0.3rem">${{member.name}}</h3>
                <p style="color:var(--text-muted)">${{member.position || 'غير متوفر'}} - ${{member.department || 'غير متوفر'}}</p>
                <span class="status-badge ${{member.status === 'نشط' ? 'status-active' : 'status-inactive'}}" style="margin-top:0.5rem">${{member.status || 'غير متوفر'}}</span>
            </div>
        </div>
        <div class="member-details-grid">
            <div class="detail-item"><span>السن:</span> ${{member.age}}</div>
            <div class="detail-item"><span>رقم الهاتف:</span> <span dir="ltr">${{member.phone || 'غير متوفر'}}</span></div>
            <div class="detail-item"><span>البريد الإلكتروني:</span> ${{member.email || 'غير متوفر'}}</div>
            <div class="detail-item"><span>تاريخ الانضمام:</span> ${{member.joinDate || 'غير متوفر'}}</div>
            <div class="detail-item full-width"><span>مكان السكن:</span> ${{member.address || 'غير متوفر'}}</div>
            ${{member.idCardImage ? `<div class="detail-item full-width"><span>صورة البطاقة الشخصية:</span><br><img src="${{member.idCardImage}}" class="id-card-img" /></div>` : ''}}
        </div>
    `;
    detailsModal.classList.add('active');
}};

// Close Modals
document.querySelectorAll('.close-modal').forEach(btn => {{
    btn.onclick = () => {{
        detailsModal.classList.remove('active');
        deleteModal.classList.remove('active');
    }};
}});

window.onclick = (e) => {{
    if (e.target === detailsModal) detailsModal.classList.remove('active');
    if (e.target === deleteModal) deleteModal.classList.remove('active');
}};

// Delete Logic
window.openDeleteModal = (id) => {{
    memberToDelete = id;
    deleteModal.classList.add('active');
}};

document.getElementById('confirmDeleteBtn').onclick = async () => {{
    if (!memberToDelete) return;
    try {{
        const btn = document.getElementById('confirmDeleteBtn');
        const originalText = btn.innerHTML;
        btn.innerHTML = '<i class="spin-icon" data-lucide="loader-2" style="width:16px;height:16px;margin:0"></i> جاري الحذف...';
        btn.disabled = true;
        lucide.createIcons();
        
        await remove(ref(db, `members/${{memberToDelete}}`));
        showToast('تم حذف العضو بنجاح');
        deleteModal.classList.remove('active');
    }} catch (error) {{
        showToast('تعذر حذف العضو', 'error');
        console.error(error);
    }} finally {{
        const btn = document.getElementById('confirmDeleteBtn');
        btn.innerHTML = 'حذف العضو';
        btn.disabled = false;
        memberToDelete = null;
    }}
}};
"""

# --- JS: admin.js ---
admin_js = f"""
import {{ db, storage, showToast }} from './firebase-config.js';
import {{ ref as dbRef, push, set, update, get }} from "https://www.gstatic.com/firebasejs/10.8.0/firebase-database.js";
import {{ ref as storageRef, uploadBytes, getDownloadURL }} from "https://www.gstatic.com/firebasejs/10.8.0/firebase-storage.js";

const form = document.getElementById('memberForm');
const submitBtn = document.getElementById('submitBtn');

const urlParams = new URLSearchParams(window.location.search);
const editId = urlParams.get('edit');

let currentProfileImg = "";
let currentIdCardImg = "";

// Image Preview logic
const setupImagePreview = (inputId, previewId) => {{
    document.getElementById(inputId).addEventListener('change', function(e) {{
        const file = e.target.files[0];
        if (file) {{
            const reader = new FileReader();
            reader.onload = (e) => {{
                const img = document.getElementById(previewId);
                img.src = e.target.result;
                img.style.display = 'block';
            }}
            reader.readAsDataURL(file);
        }}
    }});
}};

setupImagePreview('profileImage', 'profilePreview');
setupImagePreview('idCardImage', 'idCardPreview');

// If Edit Mode, fetch data
if (editId) {{
    document.getElementById('pageTitle').textContent = 'تعديل بيانات العضو';
    document.getElementById('pageDesc').textContent = 'تعديل البيانات الحالية لعضو الشركة';
    submitBtn.innerHTML = '<i data-lucide="save"></i> حفظ التعديلات';
    
    // Fetch member
    get(dbRef(db, `members/${{editId}}`)).then((snapshot) => {{
        if (snapshot.exists()) {{
            const data = snapshot.val();
            document.getElementById('name').value = data.name || '';
            document.getElementById('age').value = data.age || '';
            document.getElementById('phone').value = data.phone || '';
            document.getElementById('email').value = data.email || '';
            document.getElementById('position').value = data.position || '';
            document.getElementById('department').value = data.department || '';
            document.getElementById('joinDate').value = data.joinDate || '';
            document.getElementById('status').value = data.status || 'نشط';
            document.getElementById('address').value = data.address || '';
            
            if(data.profileImage) {{
                currentProfileImg = data.profileImage;
                document.getElementById('profilePreview').src = currentProfileImg;
                document.getElementById('profilePreview').style.display = 'block';
            }}
            if(data.idCardImage) {{
                currentIdCardImg = data.idCardImage;
                document.getElementById('idCardPreview').src = currentIdCardImg;
                document.getElementById('idCardPreview').style.display = 'block';
            }}
        }} else {{
            showToast('العضو غير موجود', 'error');
            setTimeout(() => window.location.href = '/', 2000);
        }}
    }}).catch(err => {{
        showToast('تعذر جلب البيانات', 'error');
    }});
}}

// Helper to upload image
async function uploadImage(file, pathFolder) {{
    if (!file) return "";
    const uniqueName = `${{Date.now()}}_${{file.name}}`;
    const sRef = storageRef(storage, `${{pathFolder}}/${{uniqueName}}`);
    await uploadBytes(sRef, file);
    return await getDownloadURL(sRef);
}}

// Form Submit Handler
form.addEventListener('submit', async (e) => {{
    e.preventDefault();
    
    const name = document.getElementById('name').value.trim();
    const age = document.getElementById('age').value.trim();
    
    if (!name || !age) {{
        showToast('يرجى إدخال الاسم والسن', 'error');
        return;
    }}

    submitBtn.disabled = true;
    const originalBtnHtml = submitBtn.innerHTML;
    submitBtn.innerHTML = '<i class="spin-icon" data-lucide="loader-2" style="width:18px;height:18px"></i> جاري الحفظ...';
    lucide.createIcons();

    try {{
        // Upload images if changed
        const profileFile = document.getElementById('profileImage').files[0];
        const idCardFile = document.getElementById('idCardImage').files[0];
        
        let profileUrl = currentProfileImg;
        let idCardUrl = currentIdCardImg;
        
        if (profileFile) profileUrl = await uploadImage(profileFile, 'profiles');
        if (idCardFile) idCardUrl = await uploadImage(idCardFile, 'idCards');

        const memberData = {{
            name,
            age: parseInt(age),
            phone: document.getElementById('phone').value.trim(),
            email: document.getElementById('email').value.trim(),
            position: document.getElementById('position').value.trim(),
            department: document.getElementById('department').value,
            joinDate: document.getElementById('joinDate').value,
            status: document.getElementById('status').value,
            address: document.getElementById('address').value.trim(),
            profileImage: profileUrl,
            idCardImage: idCardUrl,
            updatedAt: new Date().toISOString()
        }};

        if (editId) {{
            await update(dbRef(db, `members/${{editId}}`), memberData);
            showToast('تم تعديل بيانات العضو بنجاح');
        }} else {{
            memberData.createdAt = new Date().toISOString();
            const newMemberRef = push(dbRef(db, 'members'));
            await set(newMemberRef, memberData);
            showToast('تمت إضافة العضو بنجاح');
            form.reset();
            document.getElementById('profilePreview').style.display = 'none';
            document.getElementById('idCardPreview').style.display = 'none';
            currentProfileImg = "";
            currentIdCardImg = "";
        }}
        
        setTimeout(() => window.location.href = '/', 1500);

    }} catch (error) {{
        console.error(error);
        showToast('حدث خطأ أثناء الحفظ', 'error');
        submitBtn.disabled = false;
        submitBtn.innerHTML = originalBtnHtml;
        lucide.createIcons();
    }}
}});
"""

# --- Vercel/Netlify Config ---
vercel_json = """{
  "cleanUrls": true,
  "trailingSlash": false
}"""

# Write files
with open(f'{project_dir}/index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)
with open(f'{project_dir}/{admin_file_name}', 'w', encoding='utf-8') as f:
    f.write(admin_html)
with open(f'{project_dir}/css/style.css', 'w', encoding='utf-8') as f:
    f.write(style_css)
with open(f'{project_dir}/js/firebase-config.js', 'w', encoding='utf-8') as f:
    f.write(firebase_config_js)
with open(f'{project_dir}/js/app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)
with open(f'{project_dir}/js/admin.js', 'w', encoding='utf-8') as f:
    f.write(admin_js)
with open(f'{project_dir}/vercel.json', 'w', encoding='utf-8') as f:
    f.write(vercel_json)

# Create Zip
zip_path = '/mnt/data/AlHalabi_Company_System.zip'
with zipfile.ZipFile(zip_path, 'w') as zf:
    for root, dirs, files in os.walk(project_dir):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, project_dir)
            zf.write(file_path, arcname)

print(f"Project generated successfully at {zip_path}")
