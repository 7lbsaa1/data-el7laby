import { db, ref, push, set, update, get } from './firebase-config.js';

const form = document.getElementById('addMemberForm');
const messageBox = document.getElementById('formMessage');
const submitBtn = document.getElementById('submitBtn');

// Image Previews
setupImagePreview('profileImage', 'profilePreview');
setupImagePreview('idCardImage', 'idCardPreview');

function setupImagePreview(inputId, previewId) {
    const input = document.getElementById(inputId);
    const preview = document.getElementById(previewId);
    
    if(!input || !preview) return;

    preview.addEventListener('click', () => input.click());

    input.addEventListener('change', function() {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                preview.innerHTML = `<img src="${e.target.result}" alt="Preview">`;
            }
            reader.readAsDataURL(file);
        } else {
            preview.innerHTML = `<span>اختر صورة</span>`;
        }
    });
}

// Check for Edit Mode
const urlParams = new URLSearchParams(window.location.search);
const editId = urlParams.get('edit');

if(editId) {
    const titleEl = document.querySelector('.page-title h1');
    const descEl = document.querySelector('.page-title p');
    if(titleEl) titleEl.textContent = "تعديل بيانات العضو";
    if(descEl) descEl.textContent = "تعديل البيانات المحفوظة للعضو";
    
    submitBtn.innerHTML = `<i data-lucide="save"></i> حفظ التعديلات`;
    if(window.lucide) lucide.createIcons();
    loadMemberData(editId);
}

async function loadMemberData(id) {
    const memberRef = ref(db, `members/${id}`);
    try {
        const snapshot = await get(memberRef);
        if(snapshot.exists()) {
            const data = snapshot.val();
            document.getElementById('name').value = data.name || '';
            document.getElementById('age').value = data.age || '';
            document.getElementById('position').value = data.position || '';
            document.getElementById('department').value = data.department || '';
            document.getElementById('email').value = data.email || '';
            document.getElementById('phone').value = data.phone || '';
            document.getElementById('address').value = data.address || '';
            document.getElementById('joinDate').value = data.joinDate || '';
            document.getElementById('status').value = data.status || 'نشط';

            if(data.profileImage) {
                document.getElementById('profilePreview').innerHTML = `<img src="${data.profileImage}" alt="Profile">`;
            }
            if(data.idCardImage) {
                document.getElementById('idCardPreview').innerHTML = `<img src="${data.idCardImage}" alt="ID Card">`;
            }
        }
    } catch (error) {
        console.error("Fetch Member Error:", error);
        showMessage("حدث خطأ أثناء جلب بيانات العضو", "error");
    }
}

// Handle Form Submit
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const name = document.getElementById('name').value.trim();
    const age = document.getElementById('age').value.trim();

    if(!name || !age) {
        showMessage("الاسم والسن حقول إلزامية", "error");
        return;
    }

    submitBtn.disabled = true;
    submitBtn.innerHTML = "جاري الحفظ...";

    try {
        let profileImageUrl = editId ? undefined : "";
        let idCardImageUrl = editId ? undefined : "";

        // Convert Profile Image to Base64
        const profileFile = document.getElementById('profileImage').files[0];
        if (profileFile) {
            profileImageUrl = await convertFileToBase64(profileFile);
        }

        // Convert ID Card Image to Base64
        const idCardFile = document.getElementById('idCardImage').files[0];
        if (idCardFile) {
            idCardImageUrl = await convertFileToBase64(idCardFile);
        }

        const memberData = {
            name,
            age: Number(age),
            position: document.getElementById('position').value.trim(),
            department: document.getElementById('department').value.trim(),
            email: document.getElementById('email').value.trim(),
            phone: document.getElementById('phone').value.trim(),
            address: document.getElementById('address').value.trim(),
            joinDate: document.getElementById('joinDate').value,
            status: document.getElementById('status').value
        };

        if (profileImageUrl !== undefined) memberData.profileImage = profileImageUrl;
        if (idCardImageUrl !== undefined) memberData.idCardImage = idCardImageUrl;

        if (editId) {
            const memberRef = ref(db, `members/${editId}`);
            await update(memberRef, memberData);
            showMessage("تم تعديل بيانات العضو بنجاح", "success");
        } else {
            memberData.createdAt = new Date().toISOString();
            const membersListRef = ref(db, 'members');
            const newMemberRef = push(membersListRef);
            await set(newMemberRef, memberData);
            showMessage("تمت إضافة العضو بنجاح", "success");
        }

        // التوجيه التلقائي بعد النجاح
        setTimeout(() => { 
            window.location.href = "index.html"; 
        }, 1500);

    } catch (error) {
        console.error("Save Error:", error);
        showMessage("تعذر حفظ بيانات العضو، تأكد من إدخال البيانات بشكل صحيح.", "error");
    } finally {
        submitBtn.disabled = false;
        submitBtn.innerHTML = editId ? `<i data-lucide="save"></i> حفظ التعديلات` : `<i data-lucide="save"></i> إضافة العضو`;
        if(window.lucide) lucide.createIcons();
    }
});

// Helper: Convert File to Base64
function convertFileToBase64(file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = () => resolve(reader.result);
        reader.onerror = (error) => reject(error);
        reader.readAsDataURL(file);
    });
}

function showMessage(msg, type) {
    messageBox.textContent = msg;
    messageBox.className = `message-box message-${type}`;
    messageBox.style.display = 'block';
    window.scrollTo({ top: 0, behavior: 'smooth' });
    setTimeout(() => { messageBox.style.display = 'none'; }, 5000);
}
