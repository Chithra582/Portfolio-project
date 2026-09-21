# EXPLAINABILITY — Portfolio Project Agent

> **Admissibility & Transparency Report for OpenGAP / Agent Passport**  
> *Agent Name:* Portfolio Project Agent (`portfolio-project-agent`)  
> *Specification:* OpenGAP v0.1.0  
> *Domain:* Developer Tools / Web Development & Design Engineering  

---

## 1. Overview & Operational Purpose

Portfolio Project Agent is an autonomous, design-engineering and code explanation intelligence specialized for Chithra R's professional portfolio project. The underlying system is a premium glassmorphism dark-mode single-page web application implemented in vanilla HTML5, modern CSS3, and native JavaScript.

The agent's purpose is to inspect source code elements, explain glassmorphism styling mechanics (frosted glass panels, CSS variables, neon cyan/indigo palettes, ambient `@keyframes blob` animations), break down the `IntersectionObserver` scroll-reveal animation pipeline, and provide developers with source-grounded architectural walkthroughs with zero hallucination.

---

## 2. How the Agent Decides (Decision-Making Logic)

Portfolio Project Agent operates across a deterministic, multi-stage query classification and retrieval pipeline:

```
[User Text Query] ──> [Query Type Classification] ──> [Skill & Tool Selection]
                                                               │
                                                               ▼
[Structured Response Delivery] <── [Accuracy & Safety Gate] <── [Source Code Inspection]
```

### 2.1 Query Type Classification & Routing
- **Decision:** Determines the technical intent of the developer query and maps it to the appropriate specialist capability.
- **Classification Categories:**
  - **Design & Glassmorphism**: Queries regarding `backdrop-filter: blur()`, CSS variables (`--cyan`, `--indigo`), translucent panels, ambient blob movement, or typography. Routed to `glassmorphism-design-guide` and `design-inspector`.
  - **Scroll Animation & DOM Dynamics**: Queries regarding `IntersectionObserver`, `.hidden` / `.visible` transition toggling, threshold options, or navbar sticky effects. Routed to `scroll-animation-explainer` and `animation-navigator`.
  - **Portfolio Structure & Layout**: Queries regarding section navigation, hero structure, projects, experience, or hamburger responsive behavior. Routed to `portfolio-structure-walkthrough` and `section-retriever`.
  - **Code Pattern Retrieval**: Requests for clean, extractable snippets for modular reuse.

### 2.2 Source Code Retrieval & Verification
- **Decision:** Ground all explanations strictly in committed repository assets (`index.html`, `style.css`, `script.js`).
- **Rules:**
  - Reads `style.css` for active `:root` CSS custom properties, glassmorphism border rules, and keyframes.
  - Reads `script.js` to extract exact `IntersectionObserver` threshold values (0.15) and rootMargin configs.
  - Reads `index.html` to confirm DOM hierarchy, class namings, and section anchors.

### 2.3 Accuracy & Stack Boundary Gate
- **Decision:** Prevents hallucination of third-party frameworks.
- **Rules:**
  - Validates that explanations cite only pure HTML5, CSS3, Vanilla JS, Google Fonts (Outfit & Inter), and FontAwesome 6.4.0.
  - Explicitly rejects suggestions that Tailwind, React, Vue, Bootstrap, or GSAP are present.
  - Locks all CSS property values to match exact declarations in `style.css`.

### 2.4 Response Composition & Developer Guidance
- **Decision:** Structures explanations hierarchically: Concept Overview -> Code Snippet -> Visual Rendering Mechanism -> Cross-Browser Compatibility notes.

---

## 3. Data Sources & Inputs Used

| Data Input | Source | Purpose | Data Handling & Privacy |
|---|---|---|---|
| **User Query Text** | User prompt / CLI input | Specifies design concept, section, or animation question | Processed ephemerally in active memory; discarded upon session completion |
| **HTML Markup (`index.html`)** | Local repository filesystem | Section mapping, DOM node hierarchy, and semantic tags | Read-only static text parsing; zero live DOM execution |
| **Stylesheets (`style.css`)** | Local repository filesystem | CSS variable definitions, glassmorphism filters, keyframes | Read-only static text parsing; zero remote stylesheet transmission |
| **JavaScript (`script.js`)** | Local repository filesystem | IntersectionObserver setup, class toggles, event listeners | Read-only static text parsing; zero client-side script execution |
| **Image Metadata** | `images/` directory reference | Verifies relative paths (e.g. `images/Chithra-Photo.jpeg`) | Relative path existence checks only; binary pixel data is not transmitted |

Portfolio Project Agent complies with privacy-by-design standards:
- **No PII collection:** No private phone numbers, physical addresses, or authentication credentials are collected, logged, or exposed.
- **Public channel boundary:** Shares only institutional email and LinkedIn URLs already declared in public portfolio HTML.
- **Stateless execution:** Queries do not persist across session boundaries; zero database or remote analytics retention.

---

## 4. Known Limitations & Failure Modes

Reviewers and developers should be aware of the following system boundaries:

1. **Static Snapshot Constraints:**
   - *Limitation:* The agent analyzes the committed static source snapshot at clone time; local uncommitted file changes or runtime modifications are not reflected until reloaded.
   - *Mitigation:* The agent references committed git commits and prompts users to verify their local working tree state.

2. **No Live Headless Browser Rendering:**
   - *Limitation:* The agent cannot render live web pages, capture visual screenshots, or calculate computed layout geometry in real time.
   - *Mitigation:* The agent provides exact CSS rules and instructs developers to inspect output in Chrome DevTools or deploy via GitHub Pages.

3. **Browser Compatibility Edge Cases (`backdrop-filter`):**
   - *Limitation:* `backdrop-filter: blur()` may fail or render with flat translucency on older web browsers lacking CSS backdrop support.
   - *Mitigation:* The agent documents fallback background colors (`background: rgba(...)`) and graceful degradation strategies.

4. **Pure Vanilla Stack Boundary:**
   - *Limitation:* The project does not include TypeScript, Node.js bundlers (Vite/Webpack), or utility CSS libraries.
   - *Mitigation:* The agent explicitly clarifies vanilla browser-native paradigms and avoids recommending incompatible framework tooling.

---

## 5. Verification, Safety & Human Oversight

- **Source Code Grounding:** Every generated code snippet is validated against the actual repository source code before being presented.
- **Human-in-the-Loop Governance:** The agent suggests modular code enhancements but never alters repository files or pushes git commits autonomously.
- **Kill Switch & Override Capability:** Sessions can be terminated instantly; no background daemons or scheduled workers are spawned.
- **Transparent Audit Logging:** Query classifications, skill invocations, and tool queries are recorded in structured JSON format for transparency review.
