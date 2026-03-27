# Portfolio Mistakes Analysis

## What I tried to build

A modern, animated, interactive portfolio with:

* entry screen
* theme switching
* overlays
* dynamic UI

## What went wrong

### 1. Overengineering

I added too many systems at once:

* intro system
* mode system
* overlay system

These systems conflicted with each other.

---

### 2. Broken interactions

* Buttons were not clickable
* Hover worked but click didn't
* Likely caused by overlay blocking or z-index issues

---

### 3. No structure

I didn't separate:

* UI
* logic
* state

Everything was mixed together.

---

### 4. AI misuse

I used AI tools (ChatGPT, Claude, Gemini):

* copied solutions too fast
* didn’t fully understand them
* stacked multiple solutions together

This created hidden conflicts.

---

## Key realization

A portfolio is not about showing complexity.

It is about:

* clarity
* usability
* clean structure

---

## What I will do differently

* Start simple
* Add features one by one
* Test after every change
* Understand before applying

---

## Final truth

The project didn’t fail.

It showed me how systems break.
