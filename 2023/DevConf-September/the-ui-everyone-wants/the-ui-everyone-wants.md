---

marp: true
theme: cate-theme
paginate: false
header: ILIAS DevConf September 2023 | cate-tms.de
footer: No ILIAS on a dead planet.

---

<!-- _class: title-01 -->

# **The UI that users, designers and frontend developers really want**

---

![bg left:33% fit](img/meme_not-sure-if-care.jpg)

## What's in it for you?

* approaches to better understand users, concepters, designers, frontend developers
* ideas for your own UI concepts
* handy checklists for your own projects

---

## We do lots of UI stuff for ILIAS

* Yvonne Seiler, University of Bern
* Ferdinand Engländer, CaT Concepts and Training GmbH

---

<!-- _class: chapter-01 -->
# **What would be the most direct user interface?**

---

![bg left fit](img/thought_controlled_music_player.jpg)

Mind Reading Interface

* just think "register me" and it happens
* no need to type your own name on a keyboard
* no need to click on submit

---

Graphical User Interfaces are always a compromise

* finding the correct button always takes effort
* and all other buttons that we are currently not looking for are technically in the way

---

So maybe the title of this presentation should be different
* "The UI that users, designers and frontend developers really want"
* "The UI that users, designers and frontend developers are the least frustrated with"

---

Sources of frustration

* users will always have to look for something and learn how to use an interface (even if it's brief)
* designers will always have designs they aesthetically like more, but that are too impractical for users or not technologically feasable
* (frontend) developers often need to settle with "good enough for now" and the jungle of decade old code from hundreds of contributers

---


![bg left:33% fit](img/giphy_computer-angry.gif)

## Humans don't want to be frustrated

---

So this presentation is in large parts actually about

* identifying sources of frustration with regards to using and coding the UI in ILIAS
* evaluating what who gains what from minimizing them
* evaluating what effort it takes to minimize them

---

<!-- _class: chapter-01 -->

# **Example**

## **View Control Mode**

---

![Alt text](img/ILIAS-calendar.png)

---

This works as it should in the calendar:

![Alt text](img/viewcontrol-calendar.png)

---

![bg left fit](img/viewcontrol-page-editor.png)

But what about here?

---

![bg left fit](img/viewcontrol-page-editor.png)

Which one is active?

Communication problem
* clear with more than 2 buttons
* unclear with less than 3 buttons

---

![height:600px](img/BadExamplesViewControlMode.png)

---

![bg right](img/many-hats.jpg)

To find a satisfying solution let's wear all the different hats:

* User
* Designer
* (Frontend) Developer

---

![bg left](img/hat_user-circle.jpg)

## The user
  * wants to quickly change a mode
  * is unsure which state is currently active
  * voiced frustrated feedback

---

![bg right](img/hat_designer.jpg)

## The designer

* diagnosis
  * user intent seems clear
  * mental model mismatch
* needs to find a solution to visually communicate the active state more clearly

---

### Expoloration

* Collecting many possible approaches
* Because the first idea is rarely the best
* Let's not be picky yet, maybe an odd ideas leads to a better one

---

Sometimes it's a good brainstorming technique to think about, what we don't want

![bg left:33% fit 90%](./img/advanced-volume-control.webp)

---

* Changing the look of the btn-default engaged
* Switching to a different look when less than three buttons
* Changing to another/new UI component? Are these tabs?
* Changing the look of the ViewControl mode

---

### Evaluating the ideas

---

* Changing the look of the btn-default engaged
  * already didn't work out Mantis #30291
* Switching to a different look when less than three buttons
  * one more thing the user migth be confused about
* Changing to another/new UI component? Are these tabs?
  * No, it's the same data, not different pages.
* Changing the look of the ViewControl mode
  * seems promising, the ViewControl Mode isn't fullfilling a basic function it should have

---

### Exploration/Research for our choice

---

How did Bootstrap do it?

![](img/2023-08-29-18-55-30.png)

---

Other solutions?

![](img/SegmentedControlsAndroid.png)

---

### Experimentation in ILIAS context

![width:1200px](img/ViewControlDrafts.png)

---

* Frontend Developer
  * improves the re-usable view control UI component (updates everywhere)
  * look of viewcontrol mode is connected to button and btn-group style code

---

<!-- _class: chapter-01 -->

# **Designer Hat**

---



---



---

## When are users happy?

If they...
* easily
* get what they want
* how they think it should work

--- 

### "Get what they want"

User Intent

* usually easy to define
* Examples
  * add a user
  * pass a course
  * see test results for class
  * copy and paste a page editor block

---

Layers to user intent

* pass a course
  * find the course
  * register
  * navigate course content
  * find the course to continue it
  * pass or fail (knowing the result)
  * find a certificate / report

---

Other users access the same location in ILIAS but have a completely different user intent:

* updating a worksheet
  * 

---

### Easily