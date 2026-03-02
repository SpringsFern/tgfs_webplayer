# TG-FileStream WebPlayer Patch

This repository is a patch for **TG-FileStream**.

---

## 1. Clone and Setup TG-FileStream

First, clone and setup the base project:

https://github.com/SpringsFern/TG-FileStream

Follow the setup instructions provided in that repository's README file.

Make sure TG-FileStream is fully working before continuing.

---

## 2. Installation Methods

You can install this plugin using **either** of the following methods.

---

### Method 1 — Local Patch (Development)

Clone this repository inside the `patches` directory of TG-FileStream.

Your folder structure should look like this:

```
<TG-FileStream base folder>/
│
├── .git
├── tgfs/
│   ├── patches/
│   │   └── tgfs-webplayer   ← clone this repo here
```
Example:

```sh
cd <TG-FileStream base folder>/tgfs/patches
git clone https://github.com/SpringsFern/tgfs-webplayer
```

---

#### Install Requirements

Install required dependency:

```sh
pip3 install aiohttp-jinja2
```

---

### Method 2 — Install as Plugin (Recommended)

You can install this plugin directly via pip using the Git repository:
```
pip3 install git+https://github.com/SpringsFern/tgfs-webplayer
```

This method uses TGFS entry-point plugin loading and does not require placing files inside the patches directory.

---

## 4. Start or Restart the Bot

After installation, start or restart TG-FileStream:

```
python3 -m tgfs
```

Or restart the service if running in the background.

---

## Done

The WebPlayer patch should now be active.

Make sure you restart the bot after adding the patch.