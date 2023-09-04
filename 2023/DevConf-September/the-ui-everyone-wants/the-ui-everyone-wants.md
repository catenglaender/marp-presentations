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

## Mind Reading Interface

* just think "register me" and it happens
* no need to type your own name on a keyboard
* no need to click on submit

---

## GUIs are always a compromise

* finding the correct button always takes effort
* and all other buttons that we are currently not looking for are technically in the way

---

So maybe the title of this presentation should be different
* "The UI that users, designers and frontend developers really want"
* "The UI that users, designers and frontend developers are the least frustrated with"

---

## Sources of frustration

* **users** will always have to look for something and learn how to use an interface (even if it's brief)
* **designers** will always have designs they aesthetically like more, but that are too impractical for users or not technologically feasable
* **(frontend) developers** often need to settle with "good enough for now" and the jungle of decade old code from hundreds of contributers

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

* Communication problem
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

### Exploration

* Collecting many possible approaches
* Because the first idea is rarely the best
* Let's not be picky yet, maybe an odd ideas leads to a better one

---

### Good brainstorming technique

Think about, what we don't want

![bg left:33% fit 90%](./img/advanced-volume-control.webp)

---

### Our options

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

#### How did Bootstrap do it?

![](img/2023-08-29-18-55-30.png)

* inset shadow is not a communication tool we yet use, it's explicitly removed in delos scss code

---

#### Other solutions?

![](img/SegmentedControlsAndroid.png)

* rounded corners communicate a elevated level - something that is rarely used in ILIAS 8

---

### Experimentation to definition

![width:1200px](img/ViewControlDrafts.png)

---

### Tests/Mockups

![](img/ViewControlTest.png)

---
![bg left](img/hat_programmer.jpg)
## (Frontend) Developer(s)

* creates the actual code that makes this UI component appear in ILIAS

---

### Exploration / Strategy

php: not much to explore
* ViewControl Mode already is a modern UI component, part of the Kitchen Sink
* views and components already use it, so construction should stay the same
* the need to change it is purely visual
* (for now)

---

sass: more decisions to make
* bootstrap has been removed in ILIAS 9, but the btn-group that this is based on has been integrated into delos
* php UI components are not equal scss components/layout/tools
* usually buttons are created by a button variant mixin inside the button. Do we have a new button type here?

---

### Definition / Decision

* new button type
* making use of the new ITCSS structure in ILIAS 9

---

![bg left:33% fit](img/2023-08-29-20-26-59.png)

### Places for changes

* Settings layer
* Button component
* maybe small changes to viewcontrol component
* HTML Template

---

![](img/2023-08-29-20-37-55.png)

---

070-components/UI-framework/Button

```scss
.btn-primary {
  @include make-button($set-basics: false, $set-design: true,
    $button-color: s.$il-btn-primary-bg,

    $bg-color: s.$il-btn-primary-bg,
    $text-color: s.$il-btn-primary-color,
    $border-color: s.$il-btn-primary-border,

    $disabled_bg-color: s.$il-disabled-btn-bg,
    $disabled_text-color: s.$il-disabled-btn-color,
    $disabled_border-color: s.$il-disabled-btn-border,
    
    $engaged_bg-color: $il-engaged-btn-bg,
    $engaged_text-color: $il-engaged-btn-color,
    $engaged_border-color: s.$il-btn-primary-border,
    $engaged_border-width: 1px);
}

.btn-ctrl {
  @include make-button($input-field-height: s.$il-btn-ctrl-outer-height,
    $border-radius: s.$il-border-radius-secondary-large,
    
    $button-text-color: s.$il-btn-ctrl-color,
    $button-color: s.$il-btn-ctrl-bg,
    $border-color: s.$il-btn-ctrl-border);
  &.engaged,
  .open & {
    border: 1px solid s.$il-btn-ctrl-engaged-border;
    background-color: s.$il-main-bg;
  }
  .open & {
    box-shadow: none;
  }
}
```

---

![bg right](img/hat_designer.jpg)
## also... Accessibility

* let's put the designer hat back on for a second

---

![](img/ViewControlTest.png)

* contrast is not the best

---

Final Implementation has an extra outline

* normal vision: ![](img/ViewControl-Mode-final.png)
* high contrast: ![](img/ViewControl-Mode-final-high-contrast.png)

---

### New Discovery

It's good that UI components get less visual priority than buttons

![](img/Kalender%20ViewControls%20Neu.png)

---

![bg left](img/hat_programmer.jpg)

## When reality is catching up

Developer hat back on...

---

Still a lot to be improved around ViewControls

* the Kitchen Sink buttons do not know the button btn-ctrl, maybe a context renderer could always output btn-ctrl if buttons are rendered inside viewcontrols?
* some View Controls use Kitchen Sink button defaults, other construct dropdowns through html templates that look like buttons, but are technically their very own specific construct
* View Controls in panel header have to get tweaked styling
* Input ViewControls present a better way to collect and send the settings of many ViewControls

---

## Result

* User: Can now differentiate active/inactive mode
* Designer: Has new approaches to clarify the visual hierachy of ViewControls in general
* Frontend Developer: Structure and use of mixins make it easy to find, improve and re-use this new button type in the future

---

## "But we don't have time to make UI concepts"

* looks like a lot
* ViewControl Mode update  2 days spread out over two weeks
  * incl. discussion in UI Clinic > mockups > realizing ViewControls are different from default buttons > collecting feedback > implementation
* saves time compared to:
  *  implementation > negative feedback > implementing something else > new idea > implementing something else

---

<!-- _class: chapter-01 -->

# **Honorable Mentions**

---

## Data Table
---

### Column types

![](img/2023-09-04-18-30-09.png)

---

### Sticky header

![](./img/data-table_sticky.gif)

---

### Catch many lines of text

![](img/2023-09-04-18-39-04.png)

---

<!-- _class: chapter-01 -->

# **Asking these questions worked well for us**

## **Download: bit.ly/ilias-ui-questions**

---

## General

* What proven UI/UX principles, code structure and testing data can we use instead of just our gut instinct?
* Who can contribute their knowledge, skills and perspective to move this project forward?
* Is what we are working on part of a larger pattern?
* Is there something that already exists that we can use instead of introducing something new?
* What implications might the change have? Best case? Worst case?

---

## User perspective

* What types of users see this screen?
* What is the user intent of each of these user types?
* Does the way how something works match the user's expectation of how it should work (mental model)?
* **What is the most frequent user intent? Is it visually more prominent?**
* Can we identify a user with a specific user intent and only show them what they need?
* If users voiced a suggestion is it actually the solution to the issue they are having?
* Does the user have an issue with the specific view or with a pattern?
* What could the user do to break this?

---

## Designer perspective

* What apps solve this issue well? Is there a known mental model that we can match?
* Is there a design pattern in delos that we can use?
* What is every single design choice communicating?
* Does a design choice help or harm a specific and/or the most frequent user intent?
* Is there a visual hierachy? Does it match the hierachy of user intents?
* Are there visual groups? Use chunking because of Miller's law
* **Can the groups be semantic instead of type groups?**

---

## Frontend Developer perspective (SCSS)

* Is there existing code/mixins/tools we can use?
* Where in the ITCSS structure does this fit?
* **Can we introduce a more general setting variable, tool or layout component instead of component specific code?**
* Do we really need to override somnething or can we fix what we are overriding?
* Can this be (easily) overidden by a custom system style (skin)?
* What consumer code could break this?

---

<!-- _class: chapter-02 -->

## **Conclusion**

---

* everybody has an opinion about UI, so we need ways to move beyond gut feelings to stay constructive
* UI fundamentals like mental models, user intent and semantic chunks can help make informed decisions
* switching perspectives helps to find the best compromise that ~~everybody is happy with~~ no one is super frustrated with