# MASTER PROMPT — FULL VANILLA HTML/CSS/JS REFACTOR & OPTIMIZATION

You are acting as a senior frontend architect and codebase refactoring engineer.

I have an existing production-style Vanilla HTML/CSS/JavaScript website.

The project was originally structured more like an SPA and was later converted/split into multiple HTML pages and Vanilla JS/CSS. Because the project was heavily developed with AI assistance, the codebase has accumulated technical debt, duplicated logic, inconsistent naming, unnecessary abstractions, unused code, excessive CSS, and possible performance problems.

Approximate current size:

- CSS: ~8,000 lines
- JavaScript: ~3,000 lines
- Multiple HTML pages
- Vanilla HTML/CSS/JS
- No framework should be introduced
- Existing functionality and visual design must remain intact

The goal is NOT simply to reduce the line count.

The real goal is:

1. Preserve 100% of existing functionality.
2. Preserve the existing visual design and responsive behavior.
3. Remove unnecessary complexity.
4. Remove dead/unused code safely.
5. Remove duplicated code.
6. Improve code organization.
7. Rename unclear/generated identifiers into understandable names.
8. Improve CSS architecture.
9. Improve JavaScript architecture.
10. Remove remnants of the previous SPA architecture where appropriate.
11. Improve runtime performance.
12. Improve maintainability.
13. Make the code understandable to a human developer.
14. Keep the project Vanilla HTML/CSS/JS.
15. Avoid over-engineering.

IMPORTANT:
Do NOT optimize for line count alone.

A shorter codebase is NOT automatically better.

Prefer:
- clarity
- maintainability
- predictable behavior
- low duplication
- low complexity
- correct architecture
- performance
- semantic naming

over artificially reducing the number of lines.

==================================================
# ABSOLUTE RULES
==================================================

These rules are mandatory.

## RULE 1 — DO NOT BREAK FUNCTIONALITY

Do not change existing behavior unless the existing behavior is clearly broken and the change is explicitly justified.

Preserve:

- navigation
- links
- buttons
- forms
- validation
- modals
- dropdowns
- menus
- filters
- search
- sorting
- pagination
- authentication-related UI
- localStorage/sessionStorage behavior
- API calls
- JSON data handling
- dynamic rendering
- cart behavior
- favorites
- theme switching
- responsive behavior
- animations
- transitions
- hover states
- active states
- loading states
- error states
- empty states
- mobile behavior
- desktop behavior
- tablet behavior

Do not remove functionality simply because it appears unused without proving that it is unused.

==================================================
# RULE 2 — DO NOT CHANGE THE DESIGN
==================================================

The current UI/UX is intentional.

Do NOT redesign the website.

Do NOT change:

- colors
- spacing
- typography
- font sizes
- dimensions
- layout
- breakpoints
- borders
- shadows
- animations
- transitions
- icons
- images
- content
- positioning
- responsive layout

unless a change is strictly required to fix a confirmed bug caused by the refactoring.

The goal is architectural cleanup, not redesign.

==================================================
# RULE 3 — ANALYZE BEFORE MODIFYING
==================================================

Before modifying any source file, inspect the entire project structure.

Understand:

- all HTML files
- all CSS files
- all JavaScript files
- assets
- images
- fonts
- JSON files
- configuration files
- script loading order
- CSS loading order
- dependencies
- page-to-page relationships
- shared components
- page-specific components
- global utilities
- dynamically generated DOM
- dynamically added classes
- IDs referenced by JavaScript
- data attributes
- localStorage keys
- sessionStorage keys
- API endpoints
- imported scripts
- inline scripts
- inline styles
- external resources

Do not assume that a selector is unused simply because it is not found in static HTML.

JavaScript may create or reference it dynamically.

==================================================
# RULE 4 — FIRST PHASE MUST BE AUDIT ONLY
==================================================

Before making significant modifications, perform a complete codebase audit.

During the audit DO NOT refactor.

Produce a structured report covering:

## HTML

Identify:

- duplicated structures
- unnecessary wrappers
- invalid/poor semantics
- duplicated markup
- inline styles
- inline JavaScript
- repeated attributes
- unclear IDs
- unclear classes
- SPA remnants
- unnecessary elements
- page-specific vs shared structures

## CSS

Identify:

- unused selectors
- duplicate selectors
- duplicate declarations
- near-duplicate rules
- conflicting rules
- excessive specificity
- unnecessary !important
- repeated media queries
- repeated breakpoints
- duplicated component styles
- legacy SPA styles
- generated CSS-module-like names
- unclear class names
- styles that can safely be consolidated
- global styles that should be scoped
- repeated values that could be represented by variables
- selectors that are likely dynamically used by JavaScript

## JavaScript

Identify:

- unused functions
- unused variables
- duplicate functions
- duplicate logic
- repeated DOM queries
- unnecessary DOM manipulation
- repeated event listeners
- excessive event listeners
- event listeners that can use delegation
- global variables
- global functions
- duplicated state
- unnecessary state
- dead code
- unreachable code
- SPA remnants
- unnecessary abstraction
- over-engineered utilities
- repeated localStorage/sessionStorage logic
- repeated API logic
- repeated rendering logic
- functions with unclear responsibilities
- excessively large functions
- unnecessary DOM re-renders
- unnecessary loops
- expensive operations executed repeatedly

## NAMING

Identify unclear/generated names such as:

- Footer_footer__contactLabel__n7L5s
- Footer_footer__heading__x3Q8v
- x318v
- random/generated-looking names
- abbreviated variables
- ambiguous function names
- ambiguous IDs

Create a naming migration plan.

DO NOT perform the migration during the audit.

==================================================
# RULE 5 — CLASS/ID NAMING STANDARD
==================================================

The project should use human-readable, predictable naming.

Use a simple BEM-inspired naming convention where appropriate.

Preferred:

.component
.component__element
.component--modifier

Examples:

.footer
.footer__heading
.footer__contact
.footer__contact-label
.footer__socials
.footer__social-link

.product-card
.product-card__image
.product-card__title
.product-card__price
.product-card__actions
.product-card--featured

.navbar
.navbar__logo
.navbar__links
.navbar__link
.navbar__menu
.navbar--open

Do NOT create unnecessary nesting.

Avoid names like:

.Footer_footer__heading__x3Q8v

Rename them to meaningful names such as:

.footer__heading

BUT:

Whenever renaming a class or ID, update EVERY reference across:

- HTML
- CSS
- JavaScript
- dynamically generated HTML strings
- querySelector()
- querySelectorAll()
- getElementById()
- matches()
- closest()
- classList.add()
- classList.remove()
- classList.toggle()
- classList.contains()
- template strings
- data attributes where relevant

Do not rename only the CSS declaration.

The entire reference graph must remain consistent.

==================================================
# RULE 6 — IDs AND CLASSES ARE NOT THE SAME
==================================================

Use IDs primarily for:

- unique DOM elements
- accessibility relationships
- form relationships
- stable JavaScript hooks where appropriate

Use classes for:

- styling
- reusable components
- state/modifier classes

Do not unnecessarily use IDs as styling selectors.

If JavaScript needs a stable hook and a class would create ambiguity, consider using a semantic data attribute such as:

data-component
data-action
data-state

BUT do not introduce data attributes everywhere.

Only use them when they genuinely improve architecture.

==================================================
# RULE 7 — DO NOT OVER-ABSTRACT VANILLA JS
==================================================

This is a Vanilla JavaScript project.

Do NOT create a huge custom framework.

Avoid unnecessary abstractions such as:

- excessive helper functions
- generic wrappers around simple DOM APIs
- unnecessary class hierarchies
- artificial component systems
- excessive design patterns
- unnecessary state managers
- unnecessary event buses
- unnecessary dependency-like architecture

Example:

Do not turn:

element.classList.toggle("active");

into several layers of wrappers unless there is a real architectural reason.

Simple code is preferred.

==================================================
# RULE 8 — CSS REFACTORING
==================================================

Refactor CSS carefully.

Goals:

- remove dead CSS
- merge duplicate rules
- consolidate repeated declarations
- reduce unnecessary specificity
- remove unnecessary !important
- consolidate repeated media queries
- organize styles logically
- preserve responsive behavior
- preserve visual output
- preserve animations
- preserve states
- preserve pseudo-elements
- preserve browser behavior

Suggested logical organization:

1. Reset / base
2. Root variables
3. Typography
4. Global utilities if genuinely necessary
5. Layout
6. Header / Navbar
7. Components
8. Pages
9. Responsive rules
10. Special states / modifiers

Do not blindly reorganize everything if doing so creates risk.

Do not introduce CSS variables for every single value.

Only introduce variables for repeated meaningful design tokens such as:

- primary colors
- secondary colors
- common spacing
- common radius
- common shadows
- typography scales
- breakpoints where appropriate

Avoid variable spam.

==================================================
# RULE 9 — CSS DUPLICATION
==================================================

When multiple selectors contain identical declarations, evaluate whether they should be merged.

Example:

Before:

.card {
    border-radius: 10px;
    padding: 20px;
}

.product-card {
    border-radius: 10px;
    padding: 20px;
}

.item-card {
    border-radius: 10px;
    padding: 20px;
}

Possible improvement:

.card,
.product-card,
.item-card {
    border-radius: 10px;
    padding: 20px;
}

OR, if the common structure is genuinely the same, introduce a meaningful shared component.

Do not merge selectors merely because they currently look similar.

Check:

- specificity
- inheritance
- responsive behavior
- pseudo-classes
- pseudo-elements
- JS state classes
- page-specific overrides

==================================================
# RULE 10 — JAVASCRIPT REFACTORING
==================================================

Refactor JavaScript according to responsibility.

Prefer logical modules/files when the current architecture benefits from them.

Possible structure:

js/
    core/
    utils/
    components/
    pages/

But do NOT create dozens of tiny files.

Only split files when the separation provides a real benefit.

Functions should have clear responsibilities.

Avoid functions that:

- manipulate unrelated components
- perform API requests
- modify state
- render UI
- handle events
- update storage

all at once.

Where appropriate, separate:

- data
- state
- rendering
- event handling
- utilities

But avoid over-engineering.

==================================================
# RULE 11 — DOM PERFORMANCE
==================================================

Inspect expensive DOM operations.

Look for:

- repeated querySelector()
- repeated querySelectorAll()
- repeated getElementById()
- unnecessary innerHTML replacement
- repeated DOM rendering
- layout thrashing
- unnecessary forced reflow
- repeated style calculations
- unnecessary loops
- unnecessary event listeners

Cache stable DOM references where appropriate.

Example:

Instead of repeatedly:

document.querySelector(".navbar");

use a cached reference if the element is stable.

But do NOT cache everything.

Only cache values that are reused and stable.

==================================================
# RULE 12 — EVENT LISTENERS
==================================================

Inspect event listeners carefully.

Look for:

- duplicate listeners
- listeners attached multiple times
- listeners attached to every repeated element when delegation is better
- listeners that can be consolidated
- listeners that are never removed where cleanup matters

Use event delegation where appropriate.

Example:

Instead of attaching identical click handlers to 100 buttons, consider a parent listener if the behavior is compatible.

But do not use event delegation when it makes the code less readable or changes behavior.

==================================================
# RULE 13 — STORAGE
==================================================

Audit:

- localStorage
- sessionStorage

Identify:

- duplicate keys
- duplicate serialization logic
- inconsistent parsing
- repeated helper functions
- unnecessary reads/writes
- storage operations occurring too frequently

Do not change storage key names unless you implement a safe migration.

Preserve existing stored data compatibility.

==================================================
# RULE 14 — API / DATA
==================================================

Do not change:

- API endpoints
- request methods
- request payloads
- response expectations
- JSON structures

unless there is a confirmed bug.

If API/data handling is duplicated, consolidate it carefully while preserving behavior.

==================================================
# RULE 15 — SPA REMNANTS
==================================================

The project was previously an SPA.

Identify code that exists only because of the previous SPA architecture.

Potential remnants include:

- route managers
- unnecessary navigation state
- client-side page switching
- hidden page containers
- unnecessary global state
- SPA-specific rendering systems
- dynamic page loaders
- unused route logic
- duplicated component rendering systems

However:

DO NOT delete anything merely because it looks like SPA code.

First prove that it is no longer required.

==================================================
# RULE 16 — HTML MULTI-PAGE ARCHITECTURE
==================================================

This is now a Vanilla multi-page website.

Keep page-specific HTML where it improves clarity.

Do not attempt to force everything into a fake component system.

Shared structures can remain duplicated in HTML if the project does not have a build system and abstraction would make the project harder to understand.

The goal is maintainability, not theoretical DRY perfection.

==================================================
# RULE 17 — ACCESSIBILITY
==================================================

During refactoring, preserve or improve:

- semantic HTML
- labels
- alt attributes
- button semantics
- keyboard accessibility
- focus behavior
- aria attributes
- form relationships

Do not remove accessibility attributes just because they appear unrelated to styling.

==================================================
# RULE 18 — PERFORMANCE
==================================================

After structural refactoring, inspect:

- script loading
- defer/async usage where appropriate
- duplicate scripts
- duplicate CSS
- unnecessary assets
- excessive DOM manipulation
- repeated rendering
- unnecessary event listeners
- unnecessary storage operations
- large synchronous operations
- inefficient loops
- layout thrashing
- unnecessary animations
- unnecessary JavaScript execution

Do not optimize prematurely.

Only make changes with a clear reason.

==================================================
# RULE 19 — NO BLIND MINIFICATION
==================================================

Do NOT minify source code.

Readable source code is required.

The objective is:

clean source code

NOT:

compressed source code.

==================================================
# RULE 20 — PRESERVE COMMENTS THAT MATTER
==================================================

Remove comments that are:

- obsolete
- redundant
- generated by AI
- obvious
- misleading

Keep comments that explain:

- non-obvious behavior
- important browser quirks
- business logic
- compatibility requirements
- complex algorithms
- architectural decisions

Do not comment every line.

==================================================
# REFACTORING PROCESS
==================================================

Follow this exact process.

PHASE 0 — BASELINE

Before changing anything:

- inspect project
- identify entry points
- identify all pages
- identify all scripts
- identify all stylesheets
- identify dependencies
- identify build/runtime assumptions
- identify how the project is launched

Create a baseline.

If possible, record:

- page count
- CSS line count
- JS line count
- HTML line count
- number of CSS selectors
- number of JS functions
- number of script files
- number of CSS files

==================================================
PHASE 1 — FULL AUDIT
==================================================

Do not modify code.

Produce:

A. Architecture report
B. HTML report
C. CSS report
D. JS report
E. Naming report
F. Performance report
G. Risk report
H. Refactoring plan

For every high-risk change explain why it is risky.

==================================================
PHASE 2 — NAMING REFACTOR
==================================================

Rename unclear/generated:

- CSS classes
- IDs
- JS variables
- JS functions

Only when safe.

Use consistent human-readable naming.

Example:

Footer_footer__contactLabel__n7L5s

becomes:

footer__contact-label

Example:

Footer_footer__heading__x3Q8v

becomes:

footer__heading

Example:

ftCntLbl

becomes:

footerContactLabel

Do not rename public API names unless necessary.

Update all references globally.

After the naming phase:

- scan the entire project for old names
- ensure no broken references remain
- verify pages still work

==================================================
PHASE 3 — REMOVE DEAD CODE
==================================================

Remove only code that is proven unused.

Remove:

- unused CSS
- unused JS
- unused variables
- unused functions
- unreachable branches
- obsolete SPA code

Before deleting dynamic CSS classes, verify JavaScript usage.

Before deleting JS, verify HTML event handlers and dynamic imports.

==================================================
PHASE 4 — CSS REFACTOR
==================================================

Refactor CSS.

Priorities:

1. duplicates
2. conflicts
3. unnecessary specificity
4. repeated media queries
5. unnecessary !important
6. redundant declarations
7. obsolete SPA styles
8. inconsistent component organization

Preserve exact visual behavior.

Do not force CSS to a specific line count.

==================================================
PHASE 5 — JAVASCRIPT REFACTOR
==================================================

Refactor JS.

Priorities:

1. duplicated logic
2. duplicate event listeners
3. repeated DOM queries
4. unnecessary global state
5. oversized functions
6. unclear responsibilities
7. dead code
8. SPA remnants
9. unnecessary abstractions
10. performance issues

Preserve behavior.

==================================================
PHASE 6 — HTML REFACTOR
==================================================

Clean HTML carefully.

Improve:

- semantic structure
- unnecessary wrappers
- naming
- duplicated attributes
- accessibility
- readability

Do not create unnecessary abstractions.

==================================================
PHASE 7 — PERFORMANCE
==================================================

Perform a focused performance review.

Check:

- DOM operations
- event listeners
- rendering frequency
- storage
- scripts
- CSS
- layout/reflow
- unnecessary calculations
- unnecessary network requests

Only make safe improvements.

==================================================
PHASE 8 — FINAL VERIFICATION
==================================================

After all refactoring:

Perform a full consistency scan.

Search for:

- old class names
- old IDs
- broken selectors
- undefined functions
- undefined variables
- broken imports
- broken script references
- missing assets
- invalid HTML references
- JS selectors that no longer exist
- CSS selectors that no longer have matching elements
- dynamically generated classes that were accidentally renamed incorrectly

Verify every page.

Verify:

- desktop
- tablet
- mobile
- navigation
- forms
- interactions
- animations
- storage
- API/data
- responsive behavior

==================================================
# IMPORTANT — LINE COUNT
==================================================

Do NOT target a fixed number such as:

"8,000 CSS lines must become 2,000."

Instead:

Remove unnecessary lines.

If the final result is:

CSS: 4,000
JS: 1,800

that is perfectly acceptable if the remaining code is necessary, clean, readable and maintainable.

If the code can safely become:

CSS: 2,500
JS: 1,200

that is also acceptable.

Never sacrifice architecture or correctness to reach an arbitrary number.

==================================================
# CHANGE MANAGEMENT
==================================================

Make changes in small logical batches.

After each major phase:

1. Review changed files.
2. Check for broken references.
3. Run available validation/tests.
4. Inspect the diff.
5. Explain what changed.
6. Explain any remaining risks.

Do not make massive unrelated changes in a single operation.

Do not rewrite files unnecessarily.

Do not change formatting in unrelated files.

Keep diffs focused.

==================================================
# GIT SAFETY
==================================================

Assume the repository is under Git.

Before major modifications:

Create a logical commit/checkpoint if possible.

Suggested checkpoints:

refactor: baseline
refactor: naming
refactor: dead-code cleanup
refactor: css
refactor: javascript
refactor: html
refactor: performance
refactor: final cleanup

Never destroy the original working state.

==================================================
# FINAL REPORT
==================================================

At the end, provide a concise but detailed report:

## Files changed

List changed files.

## Naming changes

Show important before → after examples.

## CSS

Report:

- approximate old line count
- approximate new line count
- duplicate rules removed
- unused selectors removed
- !important reductions
- media query consolidation
- specificity improvements

## JavaScript

Report:

- approximate old line count
- approximate new line count
- duplicate functions removed
- unused functions removed
- duplicate listeners removed
- DOM query improvements
- unnecessary global state removed

## HTML

Report:

- structural cleanup
- naming cleanup
- semantic improvements

## Performance

Explain measurable or logically justified improvements.

## Risks

List anything that could still require manual testing.

## Verification

State which pages/features were checked.

==================================================
# MOST IMPORTANT PRINCIPLE
==================================================

This is an EXISTING working project.

You are NOT building a new project.

You are NOT redesigning it.

You are NOT rewriting everything from scratch.

You are performing a controlled refactoring.

Preserve behavior.

Preserve appearance.

Preserve data.

Preserve functionality.

Improve architecture.

Improve naming.

Remove technical debt.

Reduce unnecessary code.

Improve performance.

Make the project understandable to a human developer.

When uncertain whether something is safe to delete or merge:

DO NOT delete it.

Investigate first.

When uncertain whether two pieces of code are truly equivalent:

DO NOT merge them.

Investigate first.

When a change may alter behavior:

Stop and explain the risk before proceeding.

Begin with PHASE 0 and PHASE 1 only.

DO NOT modify the code until the audit and refactoring plan are complete.