# Receive the newsletter via email (optional)

By default the newsletter is a markdown file in `newsletter/YYYY-MM-DD.md`. If you prefer to receive it in your email inbox — so you open it from your phone, tablet, anywhere — follow this guide.

Requires 5 minutes of one-time setup.

## What you need

- A Gmail account (any, even your personal one)
- A Gmail **App Password** (NOT your normal password)

## 1. Create the Gmail App Password

The App Password is a special 16-character password Gmail generates for external scripts. It's safer than your normal password: you can revoke it anytime without changing your real password, and it only works for authorized apps.

Prerequisite: have **2-step verification** active on your Google account.

1. Go to https://myaccount.google.com/apppasswords
2. Log in with your normal Google password
3. App name: write `Claude Newsletter`
4. Click "Create"
5. Google shows you a 16-character password like: `abcd efgh ijkl mnop`
6. **Copy the password immediately** in a safe place — it never shows it to you again

## 2. Create the `.env` file

In the `materiali/` folder create a `.env` file (copy from `.env.example` if you prefer):

```
GMAIL_USER=youraddress@gmail.com
GMAIL_APP_PASSWORD=abcd efgh ijkl mnop
RECIPIENT=youraddress@gmail.com
```

`RECIPIENT` can also be different from `GMAIL_USER` (e.g. your work email).

**Important**: `.env` is already excluded from `.gitignore`. Don't remove it from the list — if you commit `.env` by mistake, you must revoke the App Password and create a new one (Gmail revokes, at https://myaccount.google.com/apppasswords).

## 3. Update the orchestrator prompt

Open `prompts/newsletter-daily.md` and add at the end, after step 7:

```markdown
### 8. (Optional) Send the newsletter via email

If a `.env` file exists in the folder with `GMAIL_USER`, `GMAIL_APP_PASSWORD`, `RECIPIENT`:
- Read the values from `.env`
- Send the content of the just-generated file (`newsletter/YYYY-MM-DD.md`) as HTML email to `RECIPIENT`
- Subject: `🧠 Your AI Brief — <readable date>`
- Body: markdown content converted to HTML (use a standard library like `marked` or equivalent)
- SMTP server: `smtp.gmail.com`, port 587, TLS

If email sending fails, do NOT fail the whole run: the newsletter stays in the filesystem, just flag the error in the final summary.
```

## 4. Test

Relaunch the orchestrator prompt:

```bash
claude --print "$(cat prompts/newsletter-daily.md)"
```

In a few seconds you should receive the email. If it doesn't arrive, check:
- Spam folder
- That `GMAIL_USER` and `RECIPIENT` are written correctly
- That the App Password is still active (https://myaccount.google.com/apppasswords)

## When you don't need email

If you're someone who always has the PC open and you're fine opening a file every morning, skip all this: the markdown file in `newsletter/` is already perfect.

Email is useful if:
- You want to read it from your phone while having breakfast
- You want to easily forward it to colleagues
- You want to archive it in your email inbox like you do with normal newsletters
