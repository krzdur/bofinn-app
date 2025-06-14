# BOFINN Ltd. — Real Estate Website

**BOFINN** is a fictional real estate company inspired by the Swedish way of life—simplicity, functionality, and warmth. The name “BOFINN” comes from the Swedish words *bo* (to live) and *finna* (to find), reflecting our mission to help people find a place to live and thrive.

## 📁 About The Project

This repository contains the full source code for the BOFINN company website, built with Django and Bootstrap. The site includes both front-end templates and back-end logic to support basic real estate operations.

## 🔧 Features

- 🧭 **Navigation**: Clean and modern UI for browsing different pages.
- 🏠 **Listings**: Browse available properties with descriptions and images.
- ➕ **Add New Offers**: A form for authenticated users to add new offers.
- 🔐 **User Authentication**: Logging-in for the company employees (in the footer; registration enabled for demonstration purposes only).
- 📩 **Contact Form**: Users can send messages via a contact form.

## 🛠️ Installation

To run this project locally:

### 1. Clone the repository
```bash
git clone https://github.com/krzdur/bofinn-app.git
cd bofinn-app
```

### 2. Run `start` command which:
* installs requirements
* runs database migration
* adds example offers to the database (to avoid commiting database to the repo)
* starts the server
```commandline
make start
```