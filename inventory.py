import re, json, sys, os

BASE = r'C:\Users\rashid\Desktop\Nexora'

with open(os.path.join(BASE, 'style.css'), 'r', encoding='utf-8') as f:
    css = f.read()
with open(os.path.join(BASE, 'app.js'), 'r', encoding='utf-8') as f:
    js = f.read()

html_files = ['index.html','contact.html','courses.html','course-details.html','faq.html','categories.html','category.html','privacy.html','terms.html','scholarships.html','accessibility.html','academy.html']
html_content = ''
for hf in html_files:
    try:
        with open(os.path.join(BASE, hf), 'r', encoding='utf-8') as f:
            html_content += f.read() + '\n'
    except:
        pass

all_refs = html_content + '\n' + js

# Extract class names used in HTML/JS
html_classes = set(re.findall(r'class="([^"]*)"', all_refs))
html_classes_flat = set()
for c in html_classes:
    for part in c.split():
        html_classes_flat.add(part.strip())

# Extract IDs used in HTML/JS
html_ids = set(re.findall(r'id="([^"]*)"', all_refs))

# Extract from JS
js_selectors_qsa = set(re.findall(r"querySelector(?:All)?\s*\(\s*['\"]([^'\"]*)['\"]", all_refs))
js_selectors_gbi = set(re.findall(r"getElementById\s*\(\s*['\"]([^'\"]*)['\"]", all_refs))
js_classlist = set(re.findall(r"classList\.(?:add|remove|toggle)\s*\(\s*['\"]([^'\"]*)['\"]", all_refs))

# Also extract from template literals in JS (backtick strings)
js_template_classes = set(re.findall(r'class="([^"]*)"', js))
for c in js_template_classes:
    for part in c.split():
        html_classes_flat.add(part.strip())

# data-page attributes
data_pages = set(re.findall(r'data-page="([^"]*)"', all_refs))

print(f'=== REFERENCE STATS ===')
print(f'HTML classes found: {len(html_classes_flat)}')
print(f'HTML IDs found: {len(html_ids)}')
print(f'JS querySelector refs: {len(js_selectors_qsa)}')
print(f'JS getElementById refs: {len(js_selectors_gbi)}')
print(f'JS classList ops: {len(js_classlist)}')
print(f'data-page values: {data_pages}')
print()

# Print JS references for debugging
print('=== JS querySelector refs ===')
for s in sorted(js_selectors_qsa):
    print(f'  {s}')
print()
print('=== JS getElementById refs ===')
for s in sorted(js_selectors_gbi):
    print(f'  {s}')
print()
print('=== JS classList ops ===')
for s in sorted(js_classlist):
    print(f'  {s}')
print()

# Now extract all CSS selector blocks with line numbers
lines = css.split('\n')
selectors = []
i = 0
in_keyframes = 0
in_media = 0
brace_depth = 0

while i < len(lines):
    line = lines[i].strip()
    
    # Track @keyframes blocks
    if '@keyframes' in line or '@-webkit-keyframes' in line or '@-moz-keyframes' in line:
        in_keyframes += 1
    
    # Track @media blocks
    if line.startswith('@media') or line.startswith('@-moz-document'):
        in_media += 1
    
    # Track brace depth
    open_b = line.count('{')
    close_b = line.count('}')
    
    if open_b > 0 and not in_keyframes:
        # Check for selector line
        m = re.match(r'^([.#:\[\*a-zA-Z_][^{]*?)\s*\{', line)
        if m:
            sel = m.group(1).strip()
            # Skip pure CSS properties
            if re.match(r'^[a-z-]+\s*:', sel):
                pass
            else:
                selectors.append((i+1, sel))
    
    brace_depth += open_b - close_b
    if brace_depth <= 0:
        in_keyframes = 0
        in_media = 0
        brace_depth = 0
    
    i += 1

print(f'=== TOTAL CSS SELECTORS: {len(selectors)} ===')
print()

# Classification
results = {
    'ACTIVE': [],
    'DEAD': [],
    'DUPLICATE': [],
    'POSSIBLY_DEAD': [],
    'LIBRARY': [],
    'STATE_DYNAMIC': [],
    'RESPONSIVE': [],
    'KEYFRAME_ANIMATION': [],
    'UTILITY': [],
    'UNCERTAIN': [],
}

# Normalize a selector for matching
def extract_class_name(sel):
    """Extract the class name from a selector."""
    classes = re.findall(r'\.([a-zA-Z_-][a-zA-Z0-9_-]*)', sel)
    return classes

def extract_id(sel):
    """Extract the ID from a selector."""
    ids = re.findall(r'#([a-zA-Z_-][a-zA-Z0-9_-]*)', sel)
    return ids

def is_library_selector(sel):
    lib_prefixes = ['.swiper', '.fancybox', '.container-fluid', '.row', '.col-', '.fa-', '.icon-']
    # Also check Swiper classes
    if any(sel.startswith(p) for p in lib_prefixes):
        return True
    return False

def check_reference(sel):
    """Check if a selector is referenced in HTML/JS."""
    classes = extract_class_name(sel)
    ids_list = extract_id(sel)
    
    # Check each class
    for cls in classes:
        if cls in html_classes_flat:
            return True
        if f'.{cls}' in js_selectors_qsa:
            return True
        # Check in JS classList
        if cls in js_classlist:
            return True
        # Check for partial matches in JS query selectors
        for qs in js_selectors_qsa:
            if cls in qs:
                return True
    
    # Check IDs
    for id_name in ids_list:
        if id_name in html_ids:
            return True
        if id_name in js_selectors_gbi:
            return True
        for qs in js_selectors_qsa:
            if id_name in qs:
                return True
    
    # Check attribute selectors like [data-page="home"]
    if 'data-page' in sel:
        for dp in data_pages:
            if dp in sel:
                return True
    
    return False

# Check for duplicate selectors
sel_strings = [s[1] for s in selectors]
from collections import Counter
sel_counts = Counter(sel_strings)
dup_sels = set(s for s, c in sel_counts.items() if c > 1)

for line_no, sel in selectors:
    # KEYFRAME_ANIMATION (already filtered, but just in case)
    if '@keyframes' in sel or '@font-face' in sel or '@import' in sel:
        results['KEYFRAME_ANIMATION'].append((line_no, sel))
        continue
    
    # RESPONSIVE
    if '@media' in sel or '@-moz-document' in sel:
        results['RESPONSIVE'].append((line_no, sel))
        continue
    
    # LIBRARY
    if is_library_selector(sel):
        results['LIBRARY'].append((line_no, sel))
        continue
    
    # DUPLICATE
    if sel in dup_sels:
        results['DUPLICATE'].append((line_no, sel))
        continue
    
    # STATE/DYNAMIC (pseudo-classes, pseudo-elements)
    state_pseudo = [':hover', ':focus', ':active', ':visited', ':first-child', ':last-child',
                    ':nth-child', ':not(', ':checked', ':disabled', ':enabled', '::before',
                    '::after', '::placeholder', '::selection', ':root', ':empty']
    is_state = any(p in sel for p in state_pseudo)
    
    # UTILITY (very generic)
    utility_sels = ['*', 'body', 'html', 'head', 'a', 'p', 'div', 'span', 'ul', 'li',
                    'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'img', 'input', 'button',
                    'textarea', 'select', 'form', 'label', 'table', 'tr', 'td', 'th',
                    'section', 'header', 'footer', 'nav', 'main', 'article', 'aside']
    is_utility = sel.strip() in utility_sels
    
    if is_state:
        results['STATE_DYNAMIC'].append((line_no, sel))
        continue
    
    if is_utility:
        results['UTILITY'].append((line_no, sel))
        continue
    
    # Check if referenced
    if check_reference(sel):
        results['ACTIVE'].append((line_no, sel))
    else:
        results['POSSIBLY_DEAD'].append((line_no, sel))

# Print results
for status in ['ACTIVE', 'DEAD', 'DUPLICATE', 'POSSIBLY_DEAD', 'LIBRARY', 'STATE_DYNAMIC', 'RESPONSIVE', 'KEYFRAME_ANIMATION', 'UTILITY', 'UNCERTAIN']:
    items = results[status]
    print(f'\n{"="*60}')
    print(f'{status}: {len(items)} selectors')
    print(f'{"="*60}')
    for line_no, sel in items:
        print(f'  [{status}] {sel} (line {line_no})')

print(f'\n{"="*60}')
print(f'FINAL COUNTS:')
print(f'{"="*60}')
for status in results:
    print(f'  {status}: {len(results[status])}')
print(f'  TOTAL: {len(selectors)}')
