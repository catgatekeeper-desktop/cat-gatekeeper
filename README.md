<div align="center">

# 🐾 Cat Gatekeeper

[![OS - Windows](https://img.shields.io/badge/OS-Windows-blue?logo=windows&logoColor=white)](#installation)
[![OS - macOS](https://img.shields.io/badge/OS-macOS-black?logo=apple&logoColor=white)](#installation)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Original Idea - konekone2026](https://img.shields.io/badge/Original_Idea-konekone2026-orange)](#acknowledgments)

*That very same ginger cat stepped out of the browser to save your productivity system-wide!*

[Download for Windows (.exe)](#) • [Download for macOS (.dmg)](#) • [Screenshots](#demonstration) • [Configuration](#flexible-configuration)

</div>

---
<div align="center">
  <a href="../../releases/latest">
    <img width="1200" alt="Cat Gatekeeper." src="assets/HG3LPDhakAA4r1c.jpg" />
  </a>
</div>

---

## 📖 About the Project

**Cat Gatekeeper** is the ultimate All-in-One (AIO) application to fight procrastination and doomscrolling. 

Based on the viral browser extension, this desktop app takes the fluffy guard to a whole new level. Now the cat monitors your time not only on websites but in **any application**: from IDEs and Photoshop to video editors and messengers. 

Coding for too long? Scrolling Telegram endlessly? Tired of retouching photos? A huge, sleepy cat will smoothly appear on the screen and cover your workspace until you take a break.

---

## ✨ Key Features

* **🌐 Global Coverage:** Works on top of any windows and applications (Browsers, VS Code, Figma, Premiere Pro, Telegram, etc.).
* **🧠 Smart Mode (Anti-Interrupt):** The cat understands context! If you are watching a movie, a full-screen YouTube video, or giving a presentation — the cat won't interrupt you.
* **🎛️ Insanely Flexible Configuration:** Set individual time limits for each program separately. For example: 30 minutes for Reddit, 2 hours for VS Code, unlimited for Spotify.
* **💤 Customizable Breaks:** Choose how long the cat will sleep on your screen (default is 5 minutes).
* **🎨 Smooth Animations:** The exact same original design and gorgeous physics of the cat appearing on your desktop.

---

## 📸 Demonstration


<div align="center">
    <video width="1200" controls="controls" muted="muted" alt="Cat Gatekeeper." src="https://github.com/user-attachments/assets/d95169e7-0e03-4473-9c81-ff0b47621f0e" />
</div>

---

## 🚀 Installation

The application is completely portable and easy to install on both Windows and macOS.

### For Windows
1. Go to the [Releases](../../releases/latest) section.
2. Download the latest `CatGatekeeper_x64.7z` file.
3. Run the installer and follow the instructions.
4. The app will appear in your system tray (near the clock).

### For macOS
1. Go to the [Releases](../../releases/latest) section.
2. Download the latest `CatGatekeeper.dmg` file.
3. Open the downloaded file and drag the cat icon into the `Applications` folder.
4. *Note:* On the first launch, you may need to grant "Screen Recording/Accessibility" permissions in macOS Privacy settings so the cat can overlay other windows.

---

## ⚙️ Flexible Configuration (How it works)

All settings are accessible through a convenient UI via the tray icon, but under the hood, the program uses a simple and clear config. 

Here is an example of how detailed you can configure the app:

```json
{
  "global_rest_time_minutes": 5,
  "smart_video_detection": true,
  "apps": [
    {
      "process_name": "chrome.exe",
      "time_limit_minutes": 45,
      "description": "Browser time limit"
    },
    {
      "process_name": "Code.exe",
      "time_limit_minutes": 120,
      "description": "Time to stretch your back after coding"
    },
    {
      "process_name": "Photoshop.exe",
      "time_limit_minutes": 60,
      "description": "Eye break from graphics work"
    }
  ]
}

----
