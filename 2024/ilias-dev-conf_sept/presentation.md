---

theme: cate-theme
paginate: false
header: ILIAS Conference 2024 | cate-tms.de
footer: No ILIAS on a dead planet.

---

<!-- _class: title-01 -->

<style>@import 'https://cdn.jsdelivr.net/npm/@tabler/icons@latest/iconfont/tabler-icons.min.css';</style>

<div class="custom">A custom div</div>

# ** Custom skins (system styles) in ILIAS 9+**

---

This is ILIAS

---

This is cate, an extended ILIAS with a custom ILIAS

---

You can make ILIAS look greatly different

---

Custom Skins (system styles)

---

<!-- _class: chapter-01 -->

## **Let's get to know each other**

---

Who here has ever changed the look of the ILIAS system style

* through the interface
* through committing style code to delos
* through a custom skin (system style)
* Who has never changed the look of ILIAS?

---

* Ferdinand Engländer - frontend-developer
* CaT Concepts and Training GmbH
* we run ILIAS instances modified and specialized for businesses
* insurances, car manufacturers, mid-size to large organizations,...
* our system cate has a base skin that we adapt to every client

---

Big changes are here in ILIAS 9

* end of 2019: proposal to move to ITCSS structure & from LESS to SASS pre-processor
* March 2023: ITCSS / SASS Coding Guidelines
* July 2023: Re-factoring LESS to SASS, ITCSS structure, removal/ingestion of Bootstrap 3
* thanks to CaT co-workers and University of Bern

---

<!-- _class: chapter-01 -->

## **Let's dive into creating a custom skin**

---

* needed/recommended tools
* simple: modifying variables at the entry point
  * great for changing a few colors, spacings and font settings
* advanced: forking the delos
  * change anything (but keep the option to compare with and pull from delos)

---

<!-- _class: chapter-01 -->

## **Needed/recommended tools**

---

Development Environment

* run ILIAS on your local machine
* https://github.com/conceptsandtraining/doil

---

SASS pre-processor

* style code is written in SCSS syntax, SASS pre-processor turns it into CSS
* dart-sass is the most up-to-date sass variant
* pay attention what exact sass variant and version is installed by package managers

---

Browser dev tools
* clear cache

---

<!-- _class: chapter-01 -->

## **Simple: Changing Variables at the entry point**

---

### Enable custom styles

In 'ilias.ini.php'

```
enable_system_styles_management = "1"
```

---

### Create custom system style folder

Create folder 'Customizing/global/skin/myskin'

---

### Create template.xml

in 'Customizing/global/skin/myskin/'

```xml

```

---

### Create mystyle/mystyle.scss

---

###  Import delos with @use

```SCSS
@use "../../../../../templates/default/delos" as delos;
```

---

### Change variables on entry point using with()

```
@use "../../../../../templates/default/delos" as delos with (
      $il-main-color: #a52d2d,
);
```

---

### Fix icons and fonts

```scss
@use "../../../../../templates/default/delos" as delos with (
      $il-web-font-path: "../../../../../templates/default/fonts/",
      $il-background-images-path: "../../../../../templates/default/images/",
      $il-icon-font-path: "../../../../../templates/default/fonts/bootstrap/",
      $il-main-color: #a52d2d,
);
```

---

### Exploring the settings layer for more variables to change

* standard page background
* header color
* background color

---

```scss
@use "../../../../../templates/default/delos" as delos with (
      $il-web-font-path: "../../../../../templates/default/fonts/",
      $il-background-images-path: "../../../../../templates/default/images/",
      $il-icon-font-path: "../../../../../templates/default/fonts/bootstrap/",
      $il-main-color: #a52d2d,
      $il-page-bg: #f6e7d8,
      $il-mainbar-btn-bg-color: #431a1a,
      $il-standard-page-header-bg-color: #f6d9a1,
);
```

---

---

Curious what else cate can do?

Creating mandatory training for business clients:
https://cate-tms.de/cate-erklaert.html

