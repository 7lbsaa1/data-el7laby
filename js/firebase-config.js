import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-app.js";
import { getDatabase, ref, push, set, update, remove, onValue, get } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-database.js";
import { getStorage, ref as storageRef, uploadBytesResumable, getDownloadURL } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-storage.js";

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

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getDatabase(app);
const storage = getStorage(app);

export { db, storage, ref, push, set, update, remove, onValue, get, storageRef, uploadBytesResumable, getDownloadURL };
