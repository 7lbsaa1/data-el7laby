import { db, ref, onValue, remove } from './firebase-config.js';

let allMembers = [];
let memberToDelete = null;

// DOM Elements
const tableBody = document.getElementById('tableBody');
const searchInput = document.getElementById('searchInput');
const statTotal = document.getElementById('stat-total');
const statActive = document.getElementById('sidebar-total-members');
const statDepts = document.getElementById('stat-departments');
const statPositions = document.getElementById('stat-positions');
const statNew = document.getElementById('stat-new');
const detailsModal = document.getElementById('detailsModal');
const deleteModal = document.getElementById('deleteModal');
const modalBody = document.getElementById('modalBody');

// Fetch Members Real-Time
const membersRef = ref(db, 'members');
onValue(membersRef, (snapshot) => {
    allMembers = [];
    if (snapshot.exists()) {
        snapshot.forEach((childSnapshot) => {
            allMembers.push({
                id: childSnapshot.key,
                ...childSnapshot.val()
            });
        });
        updateDashboard(allMembers);
    } else {
        tableBody.innerHTML = `<tr><td colspan="8" class="empty-state">
            لا يوجد أعضاء حتى الآن. <br><br>
            <a href="./adminsandkjsndkjndkadnajkfkjdsafbdskjfbioqhoey128e1jkehiu1y9012%20ejknid903ue90un0eu12s%20dfvewrvewrvewa045f1dfdsf1df1dsf1s.html" class="btn btn-primary">إضافة عضو جديد</a>
        </td></tr>`;
        updateStats([]);
    }
}, (error) => {
    console.error("Firebase Read Error:", error);
    tableBody.innerHTML = `<tr><td colspan="8" class="empty-state message-error">تعذر الاتصال بقاعدة البيانات، يرجى المحاولة مرة أخرى.</td></tr>`;
});

// Update UI Functions
function updateDashboard(membersList) {
    updateTable(membersList);
    updateStats(membersList);
}

function updateStats(membersList) {
    if(statTotal) statTotal.textContent = membersList.length;
    
    const activeMembers = membersList.filter(m => m.status === 'نشط').length;
    if(statActive) statActive.textContent = activeMembers;
    
    const departments = new Set(membersList.map(m => m.department).filter(Boolean));
    if(statDepts) statDepts.textContent = departments.size;
    
    const positions = new Set(membersList.map(m => m.position).filter(Boolean));
    if(statPositions) statPositions.textContent = positions.size;

    const currentMonth = new Date().getMonth();
    const newMembers = membersList.filter(m => {
        if(!m.joinDate) return false;
        return new Date(m.joinDate).getMonth() === currentMonth;
    }).length;
    if(statNew) statNew.textContent = newMembers;

    const currentEl = document.getElementById('currentCount');
    const totalEl = document.getElementById('totalCount');
    if(currentEl) currentEl.textContent = membersList.length;
    if(totalEl) totalEl.textContent = membersList.length;
}

function updateTable(membersList) {
    tableBody.innerHTML = '';
    membersList.forEach(member => {
        const tr = document.createElement('tr');
        
        let avatarHtml = `<div class="member-avatar text-avatar">${(member.name || 'ع').charAt(0)}</div>`;
        if (member.profileImage) {
            avatarHtml = `<img src="${member.profileImage}" alt="${member.name}" class="member-avatar">`;
        }

        const statusClass = member.status === 'نشط' ? 'active' : 'inactive';

        tr.innerHTML = `
            <td>
                <div class="member-cell">
                    ${avatarHtml}
                    <span>${member.name || ''}</span>
                </div>
            </td>
            <td>${member.position || 'غير متوفر'}</td>
            <td>${member.department || 'غير متوفر'}</td>
            <td>${member.email || 'غير متوفر'}</td>
            <td><span dir="ltr">${member.phone || 'غير متوفر'}</span></td>
            <td>${member.joinDate || 'غير متوفر'}</td>
            <td><span class="status-badge ${statusClass}">${member.status || 'غير محدد'}</span></td>
            <td>
                <div class="action-btns">
                    <button class="icon-btn view-btn" data-id="${member.id}" title="عرض التفاصيل"><i data-lucide="eye"></i></button>
                    <button class="icon-btn edit-btn" data-id="${member.id}" title="تعديل"><i data-lucide="edit-2"></i></button>
                    <button class="icon-btn delete-btn" data-id="${member.id}" title="حذف"><i data-lucide="trash-2"></i></button>
                </div>
            </td>
        `;
        tableBody.appendChild(tr);
    });
    
    if(window.lucide) lucide.createIcons();
    attachTableEvents();
}

// Client-Side Search
if(searchInput) {
    searchInput.addEventListener('input', (e) => {
        const term = e.target.value.toLowerCase();
        const filtered = allMembers.filter(m => 
            (m.name && m.name.toLowerCase().includes(term)) ||
            (m.phone && m.phone.includes(term)) ||
            (m.email && m.email.toLowerCase().includes(term)) ||
            (m.department && m.department.toLowerCase().includes(term)) ||
            (m.position && m.position.toLowerCase().includes(term)) ||
            (m.address && m.address.toLowerCase().includes(term))
        );
        
        if(filtered.length === 0) {
            tableBody.innerHTML = `<tr><td colspan="8" class="empty-state">لم يتم العثور على أعضاء مطابقين للبحث</td></tr>`;
        } else {
            updateTable(filtered);
        }
    });
}

// Events (View, Edit, Delete)
function attachTableEvents() {
    document.querySelectorAll('.view-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const id = e.currentTarget.getAttribute('data-id');
            showDetails(id);
        });
    });

    document.querySelectorAll('.delete-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            memberToDelete = e.currentTarget.getAttribute('data-id');
            deleteModal.classList.add('show');
        });
    });

    document.querySelectorAll('.edit-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const id = e.currentTarget.getAttribute('data-id');
            window.location.href = `./adminsandkjsndkjndkadnajkfkjdsafbdskjfbioqhoey128e1jkehiu1y9012%20ejknid903ue90un0eu12s%20dfvewrvewrvewa045f1dfdsf1df1dsf1s.html?edit=${id}`;
        });
    });
}

// Show Details Modal
function showDetails(id) {
    const member = allMembers.find(m => m.id === id);
    if(!member) return;

    modalBody.innerHTML = `
        <div style="text-align: center; margin-bottom: 20px;">
            ${member.profileImage 
                ? `<img src="${member.profileImage}" style="width: 100px; height: 100px; border-radius: 50%; object-fit: cover; border: 2px solid var(--gold);">` 
                : `<div style="width: 100px; height: 100px; border-radius: 50%; background: var(--border-color); display: flex; align-items: center; justify-content: center; font-size: 2rem; margin: 0 auto; color: var(--gold); border: 2px solid var(--gold);">${(member.name || 'ع').charAt(0)}</div>`
            }
            <h3 style="margin-top: 10px; color: var(--gold-light);">${member.name}</h3>
        </div>
        <div class="detail-row"><span class="detail-label">السن:</span> <span>${member.age || 'غير محدد'}</span></div>
        <div class="detail-row"><span class="detail-label">رقم الهاتف:</span> <span dir="ltr">${member.phone || 'غير متوفر'}</span></div>
        <div class="detail-row"><span class="detail-label">البريد الإلكتروني:</span> <span>${member.email || 'غير متوفر'}</span></div>
        <div class="detail-row"><span class="detail-label">مكان السكن:</span> <span>${member.address || 'غير متوفر'}</span></div>
        <div class="detail-row"><span class="detail-label">المنصب:</span> <span>${member.position || 'غير متوفر'}</span></div>
        <div class="detail-row"><span class="detail-label">الإدارة:</span> <span>${member.department || 'غير متوفر'}</span></div>
        <div class="detail-row"><span class="detail-label">تاريخ الانضمام:</span> <span>${member.joinDate || 'غير متوفر'}</span></div>
        <div class="detail-row"><span class="detail-label">الحالة:</span> <span>${member.status || 'غير متوفر'}</span></div>
        ${member.idCardImage ? `
            <div style="margin-top: 16px;">
                <span class="detail-label" style="display:block; margin-bottom: 8px;">صورة البطاقة:</span>
                <a href="${member.idCardImage}" target="_blank">
                    <img src="${member.idCardImage}" style="width: 100%; max-height: 200px; object-fit: cover; border-radius: 8px; border: 1px solid var(--border-color);">
                </a>
            </div>
        ` : '<div class="detail-row"><span class="detail-label">صورة البطاقة:</span> <span>غير متوفر</span></div>'}
    `;
    detailsModal.classList.add('show');
}

// Delete Logic
document.getElementById('confirmDeleteBtn')?.addEventListener('click', async () => {
    if(memberToDelete) {
        try {
            const mRef = ref(db, `members/${memberToDelete}`);
            await remove(mRef);
            deleteModal.classList.remove('show');
            memberToDelete = null;
        } catch (error) {
            console.error("Delete failed", error);
            alert("حدث خطأ أثناء الحذف");
        }
    }
});

document.getElementById('cancelDeleteBtn')?.addEventListener('click', () => {
    deleteModal.classList.remove('show');
    memberToDelete = null;
});

// Close Modals
document.querySelectorAll('.close-modal').forEach(btn => {
    btn.addEventListener('click', () => {
        detailsModal.classList.remove('show');
    });
});

window.addEventListener('click', (e) => {
    if(e.target === detailsModal) detailsModal.classList.remove('show');
    if(e.target === deleteModal) deleteModal.classList.remove('show');
});
