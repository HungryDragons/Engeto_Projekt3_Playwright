# Engeto_Projekt3 - Tři automatizované testy

Zadání:
Napište tři automatizované testy pomocí frameworku Playwright.

Tento projekt obsahuje automatizované testy webovej stránky https://vivaplus.tv/en-eur pomocou frameworku Playwright v jazyku Python.



## Requirements
- Python
- Playwright
- Pytest


## Testy
Projekt obsahuje nasledujúce testy na overenie základnej funkcionality stránky.:
- Overenie načítania stránky (title)
- Test odmietnutia cookies (ak je banner zobrazený)
- Test navigácie na prihlasovaciu stránku
- Overenie zobrazenia nákupného košíka


## Poznámky
- Cookies banner sa nezobrazuje vždy konzistentne (závisí od session / prehliadača), preto je jeho ošetrenie implementované podmienene.
- Stránka používa responzívny dizajn, preto sa niektoré prvky (napr. login tlačidlo) zobrazujú odlišne podľa viewportu.