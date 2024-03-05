---

marp: true
theme: cate-theme
paginate: false
header: ILIAS DevConf March 2024 | cate-tms.de
footer: No ILIAS on a dead planet.

---

<!-- _class: title-01 -->

# **The perfect form**

## **Optimizing forms with many fields**


---

<!-- _class: chapter-01 -->

## **No app without forms**

---

### Data input needs forms

![bg left:50% fit](img/reddit_r-badUIbattles_Ferro_Giconi_random-theme-access-database.jpg)

<small>source: [r/BadUIBattles, user: Ferro Giconi](https://www.reddit.com/r/badUIbattles/comments/m7y6qw/the_theme_i_created_for_the_access_database_at_my/)</small>

---

### Conventions and expectations

You realize how many you know, when you see them broken.

https://userinyerface.com/

---

## Mental Modal

"I know how this should work from somewhere else."

<video autoplay muted loop width="500px"><source src="img/r-baduibattles_hakimel_clickmeifyoucan.mp4" type="video/mp4"></video>

<small>source: [r/BadUIBattles, user: hakimel](https://www.reddit.com/r/badUIbattles/comments/13fe8fg/working_on_my_new_unsubscribe_page/)</small>

---

### Helpful

* it's like a language we share with the user
* if we speak their language, the users feel at home

---

### Challenge

* like a language it can be used incorrectly
* sometimes creating something good requires multiple drafts
* misunderstandings happen

---

<!-- _class: chapter-01 -->

## **The perfect form?**

---

## It depends...

* like with language there is one answer to write the perfect poem, essay or paper
* Does it do, what it is supposed to do?

---

## There is more than one way

![](./img/different-date-inputs.png)

---

## Which one is the best in *this* case?

---

<!-- _class: chapter-01 -->

### **Actual title for this presentation:**
## **Best practices for forms potentially interesting for ILIAS**

---

# Let's talk about

* Evidence-based design choices
* Forms in ILIAS
* What's the goal?
* Things to avoid & best practices to consider
* Possible next steps for ILIAS forms

---

# Ferdinand Engländer

* Frontend Developer at Concepts and Training GmbH
* many ILIAS UI Component projects together with the University of Bern
* UI research and projects for University of Bern
* this presentation is based on a research paper written for Hochschule Bremen

---

<!-- _class: chapter-01 -->

## **Evidence-based design choices**

---

# Problem with design

If it's about beauty, it's up to feelings and preferences.

---

# UI is not about beauty!

It's about if users can use the interface
* quick
* no errors
* achieving their goal

UI is about a good UX.
This is measurable!

---

# Studies & user testing

* eye-tracking (path & fixations)
* number of errors
* time
* checkpoints / success rate

---

# Helpful Sources

* Luke Wroblewski, Web Form Design - Filling in the Blanks, 2008, New York, Rosenfeld Media
  * Etre Ltd User Study
* Nielsen Norman Group

---

# What do these studies study?


---

<!-- _class: chapter-01 -->

### **Optional Chapter Sub-Headline**

## **The title for this section of the presentation**

<!-- Keep the headlines inside the `**` bold markdown - it's important for the css code of this slide type to work. -->

---

### An interesting thing to talk about

* with this very important point to consider
  * and a nested bullet point here
* and here is another one that needs a couple lines of text to really make clear what it is all about and why whe whould consider this
* three bullet points is a good amount of bullet points for a slide

---

![bg left](example-img/pexels-bruno-thethe-1910236.jpg)

### A slide next to an image

It could be

* an impressive screenshot there
* a hilarious meme
* or a picture of a cute and cuddly kitten, because why not

---

![bg left:33%](example-img/pexels-bruno-thethe-1910236.jpg)

### A slide with some more space for text

It could be

* an impressive screenshot there
* a hilarious meme
* or a picture of a cute and cuddly kitten, because why not

---

![bg right fit](example-img/screenshot_mainbar.png)

<!-- The "fit" parameter makes the background fit inside of the slide -->
### A slide next to an image

It could be 

* an impressive screenshot there
* a hilarious meme
* or a picture of a cute and cuddly kitten, because why not

---

![bg right:33%](example-img/pexels-bruno-thethe-1910236.jpg)

### A slide with some more space for text

It could be

* an impressive screenshot there
* a hilarious meme
* or a picture of a cute and cuddly kitten, because why not

---

<!-- _class: chapter-02 -->

### **Optional Chapter Sub-Headline**

## **A second alternative chapter cover**

<!-- Keep the headlines inside the `**` bold markdown - it's important for the css code of this slide type to work. -->

---

# A slide with some code on it

```php
public function getRows(
        DataRowBuilder $row_builder,
        array $visible_column_ids,
        Range $range,
        Order $order,
        ?array $filter_data, // $DIC->uiService()->filter()->getData();
        ?array $additional_parameters
    ): Generator;
```

---

# Images inline on the slide

![](example-img/screenshot_item.png)

Images can be resized:

![w:600](example-img/screenshot_item.png)

---

<!-- _class: invert-bg -->

# A cozy dark version of a content slide

* for a cozy darkmode feel
* also perfect for dark images as backgrounds
  * even with nested bullet points

---

<!-- _class: invert-bg -->

![bg](example-img/pexels-stein-egil-liland-3374210.jpg)

# A cozy dark version of a content slide

* for a cozy darkmode feel
* also perfect for dark images as backgrounds
  * even with nested bullet points
---

<!-- _class: title-02 -->

## **Just as an alternative cover**

# **Here is template title-02 for the purists**

<!-- There should be no paragraph text on this title slide - only one h1 and h2 each.

Keep the headlines inside the `**` bold markdown - it's important for the css code of this slide type to work. -->

---

<!-- _class: title-02 -->

![bg](./example-img/pexels-bruno-thethe-1910236.jpg)

## **Perfect for background images**

# **Use title-02 to put any background underneath**

<!-- There should be no paragraph text on this title slide - only one h1 and h2 each.

Keep the headlines inside the `**` bold markdown - it's important for the css code of this slide type to work. -->

---

<!-- _class: title-02--invert-footer -->

![bg](./example-img/pexels-bruno-thethe-1910236.jpg)

## **Backgroudn too dark?**

# **Use title-02--invert-footer to make the footer pop again**

<!-- There should be no paragraph text on this title slide - only one h1 and h2 each.

Keep the headlines inside the `**` bold markdown - it's important for the css code of this slide type to work. -->