# ad-contact-scraper
# About

"ad-contact-scraper" is a project that retrieves the advertisement details from online sales platforms and automatically initiates communication via WhatsApp by extracting the contact information of the ad owners.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
## Install

Clone the project.

```bash
git clone https://github.com/endermiriz/ad-contact-scraper
```

Go to the project directory.

```bash
cd ad-contact-scraper
```

Install the necessary packages.

```bash
pip install -r requirements.txt
```
Go to the "server" directory.

```bash
cd server
```

Install the necessary packages.

```bash
npm i -g express-draft
exp .
```
```bash
npm i whatsapp-web.js

```
```bash
npm i qrcode-terminal

```
```bash
npm i cors

```

If you encounter an error while starting the server:

```bash
npm install

```
## Before Using

- Start the **server**. :
```bash
npm run dev
```

- When the **server starts**, a **QR code** will be **generated** in the **terminal** or at `localhost:3000`. **Connect to this QR code via WhatsApp.**

- When you see `WHATSAPP WEB => Authenticated` and `READY` displayed in the **terminal**, **modify** the `sendmessage_request` **function** in the `scraper.py` file according to your needs.

- **Once you are certain that you have done everything correctly**, **run** the `scraper.py` file.
```bash
python3 scraper.py
```

## Screenshots
![Scraper.py](https://github.com/endermiriz/ad-contact-scraper/blob/main/image/scraper.png?raw=true)
