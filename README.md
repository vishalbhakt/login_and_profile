# Nexus - Modern Authentication & Profile Management System

![Nexus Preview](preview.jpg)

## 🌟 Overview

Nexus is a cutting-edge authentication and profile management system featuring a stunning glassmorphism design. This complete frontend solution provides a seamless user experience for authentication flows and profile management with a contemporary, professional aesthetic.

## ✨ Key Features

### 🎨 Design
- **Glassmorphism UI** with semi-transparent elements and backdrop blur
- **Smooth gradients** and subtle shadows for depth
- **Responsive layout** that works on all devices
- **Animated transitions** for interactive elements

### 🔐 Authentication
- Secure login and registration forms
- Password visibility toggle
- Form validation with real-time feedback
- Loading states during submissions

### 👤 Profile Management
- Beautiful profile display page
- Profile editing with image upload preview
- Organized information sections
- Responsive profile layout

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/nexus.git
   cd nexus
   ```

2. Set up your Django project to use these templates by placing them in your templates directory.

3. Configure static files in your Django settings:
   ```python
   STATICFILES_DIRS = [
       os.path.join(BASE_DIR, 'nexus/static'),
   ]
   ```

4. Ensure required Django apps are installed for authentication.

## 📂 File Structure

```
nexus/
├── static/
│   ├── css/
│   │   └── style.css           # Main stylesheet with glassmorphism design
│   └── js/
│       └── script.js           # Interactive functionality
├── templates/
│   ├── base.html               # Base template with navigation
│   ├── login.html              # Modern login page
│   ├── register.html           # Registration page
│   ├── user_profile.html       # Profile display
│   └── profile_update.html     # Profile editor
└── README.md
```

## 🎨 Customization

### Colors
Edit the CSS variables in `style.css`:
```css
:root {
    --primary: #6366f1;
    --primary-light: #a5b4fc;
    --primary-dark: #4f46e5;
    --secondary: #10b981;
    --accent: #f43f5e;
    --dark: #1e293b;
    --light: #f8fafc;
}
```

### Branding
Update in `base.html`:
```html
<a class="navbar-brand" href="/">
    <i class="fas fa-cube me-1"></i>
    <span class="text-gradient">YourBrand</span>
</a>
```

## 🌍 Browser Support
- Chrome, Firefox, Safari, Edge (latest versions)
- Mobile Safari and Chrome

## 🤝 Contributing
Contributions welcome! Please fork the repository and submit pull requests.

## 📜 License
MIT License

## 📸 Preview
![Login Page](![image](https://github.com/user-attachments/assets/2834c50e-a48d-4182-a447-0507cd044fc1)
)
![Profile Page](![image](https://github.com/user-attachments/assets/0a086f83-fe84-4d08-b7eb-22646f42e2ad)
)

## 📧 Contact
For questions: vishalkush9119@email.com

---

**Nexus** - Modern authentication experiences with beautiful design.
