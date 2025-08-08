
const BASE_URL = 'https://congenial-succotash-657rpjgvw6f549q-5000.app.github.dev/';
let TOKEN = "";

// UI Selectors
const selectors = {
    contentArea: () => document.getElementById('content-area'),
    loginArea: () => document.querySelector('.login-area'),
    loginForm: () => document.getElementById('login-form'),
    loginLink: () => document.querySelector('.login-link'),
    logoutLink: () => document.querySelector('.logout-link'),
    username: () => document.getElementById('username'),
    password: () => document.getElementById('password'),
};

// Utility functions
function setDisplay(element, state) {
    if (element) element.style.display = state ? 'inline' : 'none';
}

function showContentArea() {
    const area = selectors.contentArea();
    if (area) area.style.display = 'block';
}

function hideContentArea() {
    const area = selectors.contentArea();
    if (area) area.style.display = 'none';
}

function showLoginArea() {
    const area = selectors.loginArea();
    if (area) area.style.display = 'block';
}

function hideLoginArea() {
    const area = selectors.loginArea();
    if (area) area.style.display = 'none';
}

function clearLoginForm() {
    const form = selectors.loginForm();
    if (form) form.reset();
}

function isLoggedIn() {
    return TOKEN !== "";
}

function updateAuthLinks() {
    setDisplay(selectors.loginLink(), !isLoggedIn());
    setDisplay(selectors.logoutLink(), isLoggedIn());
}

function logout() {
    TOKEN = "";
    updateAuthLinks();
    showContent('home');
}

// API functions
async function apiFetch(endpoint, options = {}) {
    if (isLoggedIn()) {
        options.headers = {
            ...(options.headers || {}),
            'Authorization': `Bearer ${TOKEN}`,
        };
    }
    const response = await fetch(`${BASE_URL}/api/${endpoint}`, options);
    return response.json();
}

// Renderers
const renderers = {
    home: async () => {
        try {
            const data = await apiFetch('home');
            selectors.contentArea().innerHTML = `<h2>${data.title}</h2><p>${data.description}</p>`;
        } catch {
            selectors.contentArea().innerHTML = `<p>Error loading content.</p>`;
        }
    },
    about: async () => {
        try {
            const data = await apiFetch('about');
            selectors.contentArea().innerHTML = `<h2>${data.title}</h2><p>${data.content}</p>`;
        } catch {
            selectors.contentArea().innerHTML = `<p>Error loading content.</p>`;
        }
    },
    product: async () => {
        try {
            const data = await apiFetch('products');
            if (data.error) {
                selectors.contentArea().innerHTML = `<p>${data.error}</p>`;
                return;
            }
            selectors.contentArea().innerHTML = `<h2>Products</h2><ul>${data.map(product => `<li>${product.name} - $${product.price}</li>`).join('')}</ul>`;
        } catch {
            selectors.contentArea().innerHTML = `<p>Error loading content.</p>`;
        }
    },
    contact: async () => {
        try {
            const data = await apiFetch('contact');
            selectors.contentArea().innerHTML = `<h2>${data.email}</h2><p>${data.phone}</p>`;
        } catch {
            selectors.contentArea().innerHTML = `<p>Error loading content.</p>`;
        }
    },
    login: async () => {
        showLoginArea();
        hideContentArea();
    }
};

// Main navigation
async function showContent(page) {
    if (page === 'login') {
        await renderers.login();
    } else {
        hideLoginArea();
        showContentArea();
        if (renderers[page]) {
            await renderers[page]();
        }
    }
}

// Login handler
async function handleLogin() {
    const username = selectors.username().value;
    const password = selectors.password().value;
    try {
        const response = await fetch(`${BASE_URL}/api/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });
        if (response.ok) {
            const data = await response.json();
            TOKEN = data.token;
            updateAuthLinks();
            hideLoginArea();
            showContentArea();
            clearLoginForm();
            showContent('home');
        } else {
            alert('Login failed. Please check your credentials.');
        }
    } catch {
        alert('An error occurred while trying to log in.');
    }
}

// Event listeners
document.addEventListener('DOMContentLoaded', () => {
    updateAuthLinks();
    showContent('home');

    // Navigation
    document.querySelector('.menu').addEventListener('click', (e) => {
        if (e.target.tagName === 'A' && e.target.hasAttribute('data-page')) {
            e.preventDefault();
            showContent(e.target.getAttribute('data-page'));
        }
    });

    // Login
    const loginForm = selectors.loginForm();
    if (loginForm) {
        loginForm.addEventListener('submit', (e) => {
            e.preventDefault();
            handleLogin();
        });
    }

    // Logout
    const logoutLink = selectors.logoutLink();
    if (logoutLink) {
        logoutLink.addEventListener('click', (e) => {
            e.preventDefault();
            logout();
        });
    }
});
