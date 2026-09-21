---
name: scroll-animation-explainer
description: Explains the JavaScript IntersectionObserver scroll-reveal animation system and mobile hamburger navigation toggle used in this portfolio.
---

## Purpose
Give a complete, accurate explanation of how the scroll-reveal animation system works
in Chithra R's portfolio — from the IntersectionObserver setup to the CSS class toggle
that triggers the transition effect.

## Capabilities
- Explain `IntersectionObserver` instantiation: constructor options (`threshold`, `rootMargin`)
- Describe the observer callback: detects when `.hidden` elements enter the viewport
- Walk through the CSS transition: `.hidden` (opacity 0, translateY offset) -> `.visible` (opacity 1, translateY 0)
- Explain how all animatable sections receive `.hidden` class in index.html at load time
- Describe the hamburger menu: `classList.toggle('active')` on `.nav-links` for mobile slide-in
- Explain the scroll event listener that changes navbar background on scroll

## Execution Steps
1. Identify whether the question targets the observer setup, the CSS transition, or the nav toggle
2. Retrieve the relevant code from script.js or style.css
3. Explain: trigger condition -> class change -> CSS property transition -> user-visible animation
4. Note IntersectionObserver browser support and polyfill considerations
