---
name: portfolio-structure-walkthrough
description: Navigates the full section-by-section structure of the Portfolio-project, explaining the HTML layout, section content, and design decisions for each page segment.
---

## Purpose
Provide a complete walkthrough of Chithra R's portfolio website structure — section by
section — for developers reviewing, learning from, or building on top of this implementation.

## Capabilities
- Describe the navbar: logo (`Chithra.R`), nav-links (Home/About/Skills/Projects/Experience/Contact), hamburger for mobile
- Walk through the Hero section: greeting h2, name h1, title h3, description, CTA buttons (View My Work / Contact Me), social links (LinkedIn, GitHub, email), profile photo
- Describe the floating blob background elements and their role in the ambient design
- Explain About, Skills, Projects, Experience, and Contact section structures
- Describe the `.hidden` class pattern applied to sections for scroll-reveal activation

## Section Map
| Section | ID | Key Content |
|---|---|---|
| Home/Hero | #home | Name, title, CTA buttons, social links, profile photo |
| About | #about | Bio, education, passion statement |
| Skills | #skills | Tech stack icon cards |
| Projects | #projects | Project cards with links |
| Experience | #experience | Internship timeline |
| Contact | #contact | Contact form or social channels |

## Execution Steps
1. Identify which section or element the user is asking about
2. Describe the HTML structure for that section from index.html
3. Connect the markup to its CSS rules in style.css
4. Explain any JavaScript behavior tied to that section (scroll-reveal, form handling)
