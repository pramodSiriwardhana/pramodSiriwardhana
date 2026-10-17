#!/usr/bin/env python3
"""
Pramod Siriwardhana - GitHub profile README generator
Run:  python3 build.py
Out:  README.md  +  assets/dark/*.svg  +  assets/light/*.svg
      (each SVG has a desktop version and a *.mobile.svg version)
"""
import os

MONO = "'SF Mono','JetBrains Mono',Menlo,Consolas,'Courier New',monospace"
SANS = "'Segoe UI','Helvetica Neue',Helvetica,Arial,sans-serif"
HDR = '<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" fill="none">'

DARK = dict(
    bg='#0d1424', bg2='#111a2e', line='#1e2a44', page='#0a0e1a',
    th='#f1f5f9', t1='#f8fafc', t2='#e2e8f0', t3='#cbd5e1', t4='#94a3b8', t5='#64748b', t6='#475569',
    cyan='#22d3ee', violet='#8b5cf6', pink='#f472b6',
    nm=('#ffffff', '#a5f3fc', '#c4b5fd'), gridc='#ffffff', gridop='.04', gl1='.35', gl2='.22',
    tname='#c4b5fd', tkey='#7dd3fc', tstr='#86efac', tmotto='#fbbf24', tcmd='#f1f5f9',
    green='#86efac', acc=('#22d3ee', '#a78bfa', '#fbbf24'), accglow='.30', wm='.07', dot={})
LIGHT = dict(
    bg='#ffffff', bg2='#f1f5f9', line='#d0d7de', page='#f6f8fa',
    th='#0f172a', t1='#0f172a', t2='#1e293b', t3='#334155', t4='#64748b', t5='#64748b', t6='#94a3b8',
    cyan='#0891b2', violet='#7c3aed', pink='#db2777',
    nm=('#0f172a', '#0e7490', '#6d28d9'), gridc='#0f172a', gridop='.05', gl1='.16', gl2='.14',
    tname='#6d28d9', tkey='#0369a1', tstr='#15803d', tmotto='#b45309', tcmd='#0f172a',
    green='#15803d', acc=('#0891b2', '#7c3aed', '#b45309'), accglow='.16', wm='.09',
    dot={'#ffffff': '#24292f', '#e6edf3': '#24292f'})
THEMES = {'dark': DARK, 'light': LIGHT}


def f(n):
    return ('%.4f' % n).rstrip('0').rstrip('.')


def tsp(t, segs):
    return ''.join('<tspan fill="%s">%s</tspan>' % (t[c], x) if c else x for c, x in segs)


def tl(i, hi, rise):
    """keyTimes / values for the 3-step typing loop"""
    s = i / 3
    pts = [(s, 0), (s + rise, hi), (s + .3, hi), (s + .3167, 0)]
    if s > 0:
        pts.insert(0, (0, 0))
    if pts[-1][0] < 1:
        pts.append((1, 0))
    return ';'.join(f(p[0]) for p in pts), ';'.join(f(p[1]) for p in pts)


def typing(t, lines, x, ytxt, W, fs, ch, cy, chh, cw=3):
    out = ''
    for i, ln in enumerate(lines):
        k, v = tl(i, W, .1)
        ko, vo = tl(i, 1, .001)
        _, vx = tl(i, W, .1)
        vx = ';'.join(f(float(a) + x + 2) for a in vx.split(';'))
        out += (
            f'<clipPath id="c{i}"><rect x="{x}" y="{ch}" height="{chh}" width="0">'
            f'<animate attributeName="width" values="{v}" keyTimes="{k}" dur="12s" repeatCount="indefinite"/></rect></clipPath>\n'
            f'<g clip-path="url(#c{i})"><text x="{x}" y="{ytxt}" font-family="{MONO}" font-size="{fs}" fill="{t["t3"]}">'
            f'<tspan fill="{t["cyan"]}">&gt; </tspan>{ln}</text></g>\n'
            f'<rect y="{cy}" width="{cw}" height="{ch + chh - cy - 6 if False else chh - 16}" fill="{t["cyan"]}" x="{x}" opacity="0">'
            f'<animate attributeName="x" values="{vx}" keyTimes="{k}" dur="12s" repeatCount="indefinite"/>'
            f'<animate attributeName="opacity" values="{vo}" keyTimes="{ko}" dur="12s" repeatCount="indefinite"/></rect>\n')
    return out


# ---------------------------------------------------------------- HERO
def hero(t, m=False):
    C, V, P = t['cyan'], t['violet'], t['pink']
    n0, n1, n2 = t['nm']
    grad = (f'<linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{C}"/>'
            f'<stop offset=".55" stop-color="{V}"/><stop offset="1" stop-color="{P}"/></linearGradient>')
    glow = (f'<radialGradient id="orb"><stop offset="0" stop-color="{V}" stop-opacity=".35"/><stop offset="1" stop-color="{V}" stop-opacity="0"/></radialGradient>'
            f'<radialGradient id="gl1" cx=".85" cy=".1" r=".7"><stop offset="0" stop-color="{V}" stop-opacity="{t["gl1"]}"/><stop offset="1" stop-color="{V}" stop-opacity="0"/></radialGradient>'
            f'<radialGradient id="gl2" cx=".05" cy="1" r=".6"><stop offset="0" stop-color="{C}" stop-opacity="{t["gl2"]}"/><stop offset="1" stop-color="{C}" stop-opacity="0"/></radialGradient>'
            f'<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" stroke="{t["gridc"]}" stroke-opacity="{t["gridop"]}"/></pattern>')
    if not m:
        W, H, PAD = 1200, 340, 18
        s = HDR.format(w=W, h=H + PAD) + f'''
<defs>{grad}
<linearGradient id="nm" gradientUnits="userSpaceOnUse" x1="70" y1="0" x2="780" y2="0"><stop offset="0" stop-color="{n0}"/><stop offset=".55" stop-color="{n1}"/><stop offset="1" stop-color="{n2}"/></linearGradient>
{glow}<clipPath id="rr"><rect width="1200" height="340" rx="26"/></clipPath></defs>
<g clip-path="url(#rr)">
<rect width="1200" height="340" fill="{t["page"]}"/><rect width="1200" height="340" fill="url(#grid)"/>
<rect width="1200" height="340" fill="url(#gl1)"><animate attributeName="opacity" values=".6;1;.6" dur="7s" repeatCount="indefinite"/></rect>
<rect width="1200" height="340" fill="url(#gl2)"><animate attributeName="opacity" values="1;.55;1" dur="7s" repeatCount="indefinite"/></rect>
<rect y="335" width="1200" height="5" fill="url(#g)"/></g>
<rect x=".75" y=".75" width="1198.5" height="338.5" rx="25.5" stroke="{t["line"]}" stroke-width="1.5"/>
<rect x="70" y="52" width="292" height="34" rx="17" fill="#22c55e" fill-opacity=".08" stroke="#22c55e" stroke-opacity=".4"/>
<circle cx="92" cy="69" r="5" fill="#22c55e"><animate attributeName="r" values="4;6.5;4" dur="2s" repeatCount="indefinite"/><animate attributeName="opacity" values="1;.4;1" dur="2s" repeatCount="indefinite"/></circle>
<text x="110" y="74" font-family="{MONO}" font-size="13" letter-spacing="2" fill="{t["green"]}">OPEN TO FREELANCE · 2026</text>
<text x="70" y="168" font-family="{SANS}" font-size="70" font-weight="800" letter-spacing="-1.5" fill="url(#nm)">Pramod Siriwardhana</text>
'''
        lines = ['Full-Stack  ·  Mobile  ·  AI/ML Engineer', 'Building scalable products, idea to deployment',
                 'Software Engineering Undergraduate @ NIBM']
        s += typing(t, lines, 70, 222, 640, 24, 190, 198, 44, 3).replace('height="28"', 'height="28"')
        s += f'''<text x="70" y="292" font-family="{MONO}" font-size="13" letter-spacing="3" fill="{t["t5"]}">SRI LANKA   ·   HND – NIBM   ·   WEB   ·   MOBILE   ·   AI</text>
<g transform="translate(1010,170)"><circle r="150" fill="url(#orb)" opacity=".9"/>
<g><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="40s" repeatCount="indefinite"/><circle r="125" stroke="{V}" stroke-opacity=".35" stroke-dasharray="3 9" stroke-width="1.5"/><circle cx="125" r="6" fill="{P}"/></g>
<g><animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="26s" repeatCount="indefinite"/><circle r="92" stroke="{C}" stroke-opacity=".45" stroke-dasharray="28 14" stroke-width="1.5"/><circle cx="-92" r="5" fill="{C}"/></g>
<g><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="14s" repeatCount="indefinite"/><circle r="58" stroke="{t["th"]}" stroke-opacity=".25" stroke-width="1"/><circle cy="-58" r="4" fill="{t["th"]}"/></g>
<circle r="44" fill="{t["page"]}" stroke="url(#g)" stroke-width="2"/>
<text y="13" text-anchor="middle" font-family="{MONO}" font-size="34" font-weight="700" fill="url(#g)">&lt;/&gt;</text></g>
</svg>'''
        return s
    # ---- mobile
    W, H, PAD = 400, 290, 14
    s = HDR.format(w=W, h=H + PAD) + f'''
<defs>{grad}
<linearGradient id="nm" gradientUnits="userSpaceOnUse" x1="28" y1="0" x2="340" y2="0"><stop offset="0" stop-color="{n0}"/><stop offset=".55" stop-color="{n1}"/><stop offset="1" stop-color="{n2}"/></linearGradient>
{glow}<clipPath id="rr"><rect width="400" height="290" rx="20"/></clipPath></defs>
<g clip-path="url(#rr)">
<rect width="400" height="290" fill="{t["page"]}"/><rect width="400" height="290" fill="url(#grid)"/>
<rect width="400" height="290" fill="url(#gl1)"><animate attributeName="opacity" values=".6;1;.6" dur="7s" repeatCount="indefinite"/></rect>
<rect width="400" height="290" fill="url(#gl2)"><animate attributeName="opacity" values="1;.55;1" dur="7s" repeatCount="indefinite"/></rect>
<rect y="286" width="400" height="4" fill="url(#g)"/></g>
<rect x=".75" y=".75" width="398.5" height="288.5" rx="19.5" stroke="{t["line"]}" stroke-width="1.5"/>
<g transform="translate(345,58)" opacity=".75"><circle r="44" fill="url(#orb)"/>
<g><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="30s" repeatCount="indefinite"/><circle r="40" stroke="{V}" stroke-opacity=".4" stroke-dasharray="3 7" stroke-width="1.2"/><circle cx="40" r="3.5" fill="{P}"/></g>
<g><animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="20s" repeatCount="indefinite"/><circle r="27" stroke="{C}" stroke-opacity=".5" stroke-width="1.2"/><circle cx="-27" r="3" fill="{C}"/></g>
<text y="6" text-anchor="middle" font-family="{MONO}" font-size="16" font-weight="700" fill="url(#g)">&lt;/&gt;</text></g>
<rect x="28" y="28" width="228" height="26" rx="13" fill="#22c55e" fill-opacity=".08" stroke="#22c55e" stroke-opacity=".4"/>
<circle cx="44" cy="41" r="4" fill="#22c55e"><animate attributeName="r" values="3;5;3" dur="2s" repeatCount="indefinite"/></circle>
<text x="58" y="45" font-family="{MONO}" font-size="10.5" letter-spacing="1.5" fill="{t["green"]}">OPEN TO FREELANCE · 2026</text>
<text x="28" y="108" font-family="{SANS}" font-size="46" font-weight="800" letter-spacing="-1" fill="url(#nm)">Pramod</text>
<text x="28" y="156" font-family="{SANS}" font-size="46" font-weight="800" letter-spacing="-1" fill="url(#nm)">Siriwardhana</text>
'''
    lines = ['Full-Stack · Mobile · AI/ML Engineer', 'Building scalable products, idea to deployment',
             'Software Engineering Undergraduate @ NIBM']
    s += typing(t, lines, 28, 204, 344, 12, 186, 190, 28, 2.5)
    s += f'''<text x="28" y="262" font-family="{MONO}" font-size="9.5" letter-spacing="2" fill="{t["t5"]}">SRI LANKA · NIBM · WEB · MOBILE · AI</text>
</svg>'''
    return s


# ---------------------------------------------------------------- METRICS
def metrics(t, m=False):
    g = (f'<defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="{t["cyan"]}"/>'
         f'<stop offset=".5" stop-color="{t["violet"]}"/><stop offset="1" stop-color="{t["pink"]}"/></linearGradient></defs>')
    if not m:
        PAD = 22
        s = HDR.format(w=1000, h=130 + PAD) + g + f'<g transform="translate(0,{PAD})">'
        data = [(0, '03+', 'YEARS BUILDING', 144, ''), (340, '15+', 'TECHNOLOGIES', 144, ''),
                (680, '04', 'DOMAINS', 110, 'WEB · MOBILE · BACKEND · AI')]
        for x, num, lab, lx, sub in data:
            s += (f'<g transform="translate({x},0)"><rect width="320" height="130" rx="16" fill="{t["bg"]}" stroke="{t["line"]}"/>'
                  f'<rect x="24" width="272" height="3" rx="1.5" fill="url(#g)"/>'
                  f'<text x="28" y="72" font-family="{SANS}" font-size="52" font-weight="800" fill="url(#g)">{num}</text>'
                  f'<text x="{lx}" y="52" font-family="{MONO}" font-size="13" letter-spacing="3" fill="{t["t2"]}">{lab}</text>'
                  f'<text x="{lx}" y="74" font-family="{MONO}" font-size="11" letter-spacing="2" fill="{t["t5"]}">{sub}</text></g>')
        return s + '</g></svg>'
    PAD = 16
    s = HDR.format(w=400, h=84 + PAD) + g + f'<g transform="translate(0,{PAD})">'
    data = [(0, '03+', 'YEARS BUILDING'), (137.5, '15+', 'TECHNOLOGIES'), (275, '04', 'DOMAINS')]
    for x, num, lab in data:
        s += (f'<g transform="translate({x},0)"><rect width="125" height="84" rx="12" fill="{t["bg"]}" stroke="{t["line"]}"/>'
              f'<rect x="14" width="97" height="3" rx="1.5" fill="url(#g)"/>'
              f'<text x="14" y="50" font-family="{SANS}" font-size="32" font-weight="800" fill="url(#g)">{num}</text>'
              f'<text x="14" y="70" font-family="{MONO}" font-size="8.5" letter-spacing="1.4" fill="{t["t2"]}">{lab}</text></g>')
    return s + '</g></svg>'


# ---------------------------------------------------------------- SECTION HEADERS
SEC = {'ABOUT': ('01', 162), 'TECH STACK': ('02', 259), 'FEATURED PROJECTS': ('03', 396), 'GITHUB PULSE': ('04', 298)}


def section(t, title, m=False):
    num, x0 = SEC[title]
    lg = (f'<defs><linearGradient id="l" x1="0" x2="1"><stop offset="0" stop-color="{t["cyan"]}"/>'
          f'<stop offset=".5" stop-color="{t["violet"]}" stop-opacity=".6"/><stop offset="1" stop-color="{t["violet"]}" stop-opacity="0"/></linearGradient></defs>')
    if not m:
        PAD = 44
        return (HDR.format(w=1000, h=56 + PAD) + lg + f'<g transform="translate(0,{PAD})">'
                f'<text x="0" y="35" font-family="{MONO}" font-size="15" font-weight="700" fill="{t["cyan"]}">{num}</text>'
                f'<text x="40" y="36" font-family="{SANS}" font-size="22" font-weight="800" letter-spacing="5" fill="{t["th"]}">{title}</text>'
                f'<rect x="{x0}" y="27" width="{1000 - x0}" height="2" rx="1" fill="url(#l)"/>'
                f'<circle cy="28" r="4" fill="{t["th"]}"><animate attributeName="cx" values="{x0};1000" dur="3.5s" repeatCount="indefinite"/>'
                f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.1;.8;1" dur="3.5s" repeatCount="indefinite"/></circle></g></svg>')
    PAD = 26
    L = len(title) * 14
    lx = 30 + L + 14
    return (HDR.format(w=400, h=40 + PAD) + lg + f'<g transform="translate(0,{PAD})">'
            f'<text x="0" y="26" font-family="{MONO}" font-size="11" font-weight="700" fill="{t["cyan"]}">{num}</text>'
            f'<text x="26" y="27" font-family="{SANS}" font-size="15" font-weight="800" letter-spacing="3.5" textLength="{L}" lengthAdjust="spacing" fill="{t["th"]}">{title}</text>'
            f'<rect x="{26 + L + 14}" y="20" width="{400 - 26 - L - 14}" height="2" rx="1" fill="url(#l)"/>'
            f'<circle cy="21" r="3.5" fill="{t["th"]}"><animate attributeName="cx" values="{26 + L + 14};400" dur="3.5s" repeatCount="indefinite"/>'
            f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.1;.8;1" dur="3.5s" repeatCount="indefinite"/></circle></g></svg>')


# ---------------------------------------------------------------- TERMINAL
def chrome(t, W, H):
    return (f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="16" fill="{t["bg"]}" stroke="{t["line"]}"/>'
            f'<path d="M.5 16.5a16 16 0 0 1 16-16H{W - 16.5}a16 16 0 0 1 16 16V46H.5Z" fill="{t["bg2"]}"/>'
            f'<line x1="0" x2="{W}" y1="46" y2="46" stroke="{t["line"]}"/>'
            f'<circle cx="28" cy="23" r="6" fill="#ff5f56"/><circle cx="50" cy="23" r="6" fill="#ffbd2e"/><circle cx="72" cy="23" r="6" fill="#27c93f"/>')


def term_row(t, i, y, b, d, segs, fs, W, h, up):
    return (f'<clipPath id="r{i}"><rect x="28" y="{y - up}" height="{h}" width="0"><animate attributeName="width" from="0" to="{W}" begin="{b:.2f}s" dur="{d:.2f}s" fill="freeze"/></rect></clipPath>'
            f'<g clip-path="url(#r{i})"><text x="28" y="{y}" font-family="{MONO}" font-size="{fs}" xml:space="preserve">{tsp(t, segs)}</text></g>\n')


def about(t, m=False):
    cy = [('cyan', '$'), (None, ' ')]
    if not m:
        rows = [
            (92, .40, .36, cy + [('tcmd', 'whoami')]),
            (122, .88, 1.23, [('tname', 'Pramod Siriwardhana'), ('t5', ' — '), ('t3', 'Software Engineering Undergraduate (HND · NIBM)')]),
            (168, 2.23, .50, cy + [('tcmd', 'cat focus.json')]),
            (196, 2.85, .28, [('t3', '{')]),
            (222, 3.25, .92, [('tkey', '  "web"'), ('t3', ':    '), ('tstr', '"Next.js · NestJS · PostgreSQL"'), ('t3', ',')]),
            (248, 4.29, .98, [('tkey', '  "mobile"'), ('t3', ': '), ('tstr', '"Kotlin · Jetpack Compose · Flutter"'), ('t3', ',')]),
            (274, 5.39, .89, [('tkey', '  "ai"'), ('t3', ':     '), ('tstr', '"Scikit-learn · model training"')]),
            (300, 6.41, .28, [('t3', '}')]),
            (346, 6.80, .45, cy + [('tcmd', 'echo $MOTTO')]),
            (376, 7.37, 1.15, [('tmotto', '"Build with purpose. Develop with consistency. Keep learning."')])]
        s = HDR.format(w=1000, h=420) + chrome(t, 1000, 420)
        s += f'<text x="500" y="28" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{t["t5"]}">pramod@dev — ~/about — zsh</text>\n'
        for i, (y, b, d, sg) in enumerate(rows):
            s += term_row(t, i, y, b, d, sg, 17, 940, 32, 22)
        s += f'<rect x="28" y="388" width="10" height="20" fill="{t["cyan"]}" opacity="0"><animate attributeName="opacity" values="0;1;1;0;0" keyTimes="0;.01;.5;.51;1" dur="1.1s" begin="8.64s" repeatCount="indefinite"/></rect></svg>'
        return s
    rows = [
        (76, cy + [('tcmd', 'whoami')]),
        (98, [('tname', 'Pramod Siriwardhana')]),
        (118, [('t5', '— '), ('t3', 'Software Engineering Undergraduate')]),
        (138, [('t3', '(HND · NIBM)')]),
        (174, cy + [('tcmd', 'cat focus.json')]),
        (196, [('t3', '{')]),
        (216, [('tkey', '  "web"'), ('t3', ':    '), ('tstr', '"Next.js · NestJS · PostgreSQL"'), ('t3', ',')]),
        (236, [('tkey', '  "mobile"'), ('t3', ': '), ('tstr', '"Kotlin · Jetpack Compose · Flutter"'), ('t3', ',')]),
        (256, [('tkey', '  "ai"'), ('t3', ':     '), ('tstr', '"Scikit-learn · model training"')]),
        (276, [('t3', '}')]),
        (312, cy + [('tcmd', 'echo $MOTTO')]),
        (332, [('tmotto', '"Build with purpose. Develop with')]),
        (352, [('tmotto', 'consistency. Keep learning."')])]
    H = 384
    s = HDR.format(w=400, h=H) + chrome(t, 400, H)
    s += f'<text x="200" y="28" text-anchor="middle" font-family="{MONO}" font-size="11" fill="{t["t5"]}">pramod@dev — ~/about — zsh</text>\n'
    b = .3
    for i, (y, sg) in enumerate(rows):
        n = sum(len(x) for _, x in sg)
        d = .15 + n * .035
        s += term_row(t, i, y, b, d, sg, 12, 350, 24, 16)
        b += d + .1
    s += f'<rect x="28" y="364" width="8" height="14" fill="{t["cyan"]}" opacity="0"><animate attributeName="opacity" values="0;1;1;0;0" keyTimes="0;.01;.5;.51;1" dur="1.1s" begin="{b:.2f}s" repeatCount="indefinite"/></rect></svg>'
    return s


# ---------------------------------------------------------------- STACK
CATS = [
    ('FRONTEND', [('React', '#61dafb'), ('Next.js', '#ffffff'), ('TypeScript', '#3178c6'), ('JavaScript', '#f7df1e'),
                  ('Tailwind CSS', '#06b6d4'), ('HTML5', '#e34f26'), ('CSS3', '#1572b6')]),
    ('BACKEND', [('Node.js', '#4ade80'), ('NestJS', '#e0234e'), ('Python', '#4b8bbe'), ('Java', '#ed8b00'), ('PHP', '#8892bf')]),
    ('MOBILE', [('Kotlin', '#a78bfa'), ('Jetpack Compose', '#4285f4'), ('Flutter', '#54c5f8'), ('Dart', '#40c4ff')]),
    ('DATA', [('PostgreSQL', '#5b8def'), ('MongoDB', '#47a248'), ('MySQL', '#4f9ad1'), ('Oracle DB', '#f80000')]),
    ('TOOLS', [('Git', '#f05032'), ('GitHub', '#e6edf3'), ('Postman', '#ff6c37'), ('Linux', '#fcc624'),
               ('Vercel', '#ffffff'), ('Netlify', '#00c7b7')])]


def pill(t, x, y, w, name, col, delay, dx, dy, tx, ty, fs, h, dr, dR):
    col = t['dot'].get(col, col)
    return (f'<g opacity="0"><animate attributeName="opacity" from="0" to="1" begin="{delay:.2f}s" dur=".45s" fill="freeze"/>'
            f'<animateTransform attributeName="transform" type="translate" from="0 10" to="0 0" begin="{delay:.2f}s" dur=".45s" fill="freeze"/>'
            f'<rect x="{f(x)}" y="{y}" width="{f(w)}" height="{h}" rx="{h / 2}" fill="{t["bg2"]}" stroke="{t["line"]}"/>'
            f'<circle cx="{f(x + dx)}" cy="{y + dy}" r="{dr}" fill="{col}"/><circle cx="{f(x + dx)}" cy="{y + dy}" r="{dR}" fill="{col}" opacity=".18"/>'
            f'<text x="{f(x + tx)}" y="{y + ty}" font-family="{MONO}" font-size="{fs}" fill="{t["t2"]}">{name}</text></g>\n')


def stack(t, m=False):
    if not m:
        s = HDR.format(w=1000, h=354) + f'<rect x=".5" y=".5" width="999" height="353" rx="18" fill="{t["bg"]}" stroke="{t["line"]}"/>\n'
        d = .15
        for ci, (cat, items) in enumerate(CATS):
            oy = 66 * ci
            s += f'<text x="30" y="{50 + oy}.0" font-family="{MONO}" font-size="13" font-weight="700" letter-spacing="3" fill="{t["t5"]}">{cat}</text>\n'
            x = 172.0
            for name, col in items:
                w = round(len(name) * 8.4 + 42, 1)
                s += pill(t, x, 27 + oy, w, name, col, d, 17, 18, 30, 23, 14, 36, 5, 9)
                x += w + 10
                d += .07
            if ci < 4:
                s += f'<line x1="28" x2="972" y1="{78 + oy}" y2="{78 + oy}" stroke="{t["line"]}" stroke-dasharray="2 6"/>\n'
        return s + '</svg>'
    body, y, d = '', 18, .15
    for ci, (cat, items) in enumerate(CATS):
        body += f'<text x="24" y="{y + 10}" font-family="{MONO}" font-size="10" font-weight="700" letter-spacing="3" fill="{t["t5"]}">{cat}</text>\n'
        py, x = y + 22, 20.0
        for name, col in items:
            w = round(len(name) * 6.9 + 37, 1)
            if x + w > 380:
                x, py = 20.0, py + 36
            body += pill(t, x, py, w, name, col, d, 14, 14, 25, 18.5, 11.5, 28, 4, 7.5)
            x += w + 8
            d += .05
        end = py + 28
        if ci < len(CATS) - 1:
            body += f'<line x1="20" x2="380" y1="{end + 14}" y2="{end + 14}" stroke="{t["line"]}" stroke-dasharray="2 6"/>\n'
            y = end + 28
        else:
            H = end + 20
    return (HDR.format(w=400, h=H) + f'<rect x=".5" y=".5" width="399" height="{H - 1}" rx="18" fill="{t["bg"]}" stroke="{t["line"]}"/>\n' + body + '</svg>')


# ---------------------------------------------------------------- PROJECTS
PROJ = [
    dict(n='01', tag='FULL-STACK  ·  TRAVEL TECH', title='Iki Saki Travel',
         d=['Responsive tourism platform to explore Sri Lankan destinations,', 'tour packages and travel services.'],
         md=['Responsive tourism platform to explore', 'Sri Lankan destinations, tour packages', 'and travel services.'],
         chips=['Next.js', 'NestJS', 'PostgreSQL'], btn='LIVE SITE  ↗', bw=154, g=('#22d3ee', '#3b82f6'), end='#3b82f6'),
    dict(n='02', tag='MACHINE LEARNING  ·  WEB APP', title='ML Price Predictor',
         d=['Predicts fruit and vegetable prices from environmental', 'and historical data.'],
         md=['Predicts fruit and vegetable prices from', 'environmental and historical data.'],
         chips=['Python', 'Flask', 'Scikit-learn', 'Pandas'], btn='VIEW SOURCE  ↗', bw=173, g=('#a78bfa', '#ec4899'), end='#ec4899'),
    dict(n='03', tag='E-AUCTION  ·  WEB &amp; MOBILE', title='Artévo',
         d=['Full-featured web and mobile platform for hosting and managing', 'online art auctions with real-time bidding.'],
         md=['Full-featured web and mobile platform for', 'hosting and managing online art auctions', 'with real-time bidding.'],
         chips=['PHP', 'MySQL', 'Kotlin', 'Jetpack Compose'], btn='VIEW SOURCE  ↗', bw=173, g=('#fbbf24', '#f43f5e'), end='#f43f5e')]


def project(t, i, m=False):
    p, a = PROJ[i], t['acc'][i]
    defs = (f'<defs><linearGradient id="a" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{p["g"][0]}"/><stop offset="1" stop-color="{p["g"][1]}"/></linearGradient>'
            f'<linearGradient id="bd" x1="0" y1="0" x2="1" y2="1" gradientTransform="rotate(0 .5 .5)"><stop offset="0" stop-color="{a}"/><stop offset=".5" stop-color="{t["line"]}"/><stop offset="1" stop-color="{p["end"]}"/>'
            f'<animateTransform attributeName="gradientTransform" type="rotate" from="0 .5 .5" to="360 .5 .5" dur="9s" repeatCount="indefinite"/></linearGradient>'
            f'<radialGradient id="gl" cx="0" cy="0" r="1"><stop offset="0" stop-color="{a}" stop-opacity="{t["accglow"]}"/><stop offset="1" stop-color="{a}" stop-opacity="0"/></radialGradient>')
    if not m:
        W, H, PAD = 1000, 220, 16
        s = HDR.format(w=W, h=H + PAD) + defs + f'<clipPath id="cp"><rect width="1000" height="220" rx="20"/></clipPath></defs>'
        s += (f'<g clip-path="url(#cp)"><rect width="1000" height="220" fill="{t["bg"]}"/><ellipse cx="0" cy="0" rx="520" ry="300" fill="url(#gl)"/>'
              f'<text x="970" y="206" text-anchor="end" font-family="{SANS}" font-size="170" font-weight="900" fill="{a}" opacity="{t["wm"]}">{p["n"]}</text></g>'
              f'<rect x="1" y="1" width="998" height="218" rx="19" stroke="url(#bd)" stroke-width="1.6"/>'
              f'<text x="44" y="46" font-family="{MONO}" font-size="12" font-weight="700" letter-spacing="3" fill="{a}">{p["tag"]}</text>'
              f'<text x="44" y="92" font-family="{SANS}" font-size="36" font-weight="800" letter-spacing="-.5" fill="{t["t1"]}">{p["title"]}</text>'
              f'<text x="44" y="122" font-family="{SANS}" font-size="16" fill="{t["t4"]}">{p["d"][0]}</text>'
              f'<text x="44" y="144" font-family="{SANS}" font-size="16" fill="{t["t4"]}">{p["d"][1]}</text>')
        x = 44
        for c in p['chips']:
            w = round(len(c) * 7.9 + 25.5)
            s += (f'<rect x="{x}" y="158" width="{w}" height="30" rx="15" fill="{a}" fill-opacity=".1" stroke="{a}" stroke-opacity=".4"/>'
                  f'<text x="{f(x + w / 2)}" y="177.5" text-anchor="middle" font-family="{MONO}" font-size="12.5" fill="{t["t2"]}">{c}</text>')
            x += w + 10
        bx = 956 - p['bw']
        s += (f'<g transform="translate({bx},148)"><rect width="{p["bw"]}" height="40" rx="20" fill="url(#a)"/>'
              f'<text x="{p["bw"] / 2}" y="25.5" text-anchor="middle" font-family="{SANS}" font-size="13.5" font-weight="800" letter-spacing="1.5" fill="#fff">{p["btn"]}</text>'
              f'<animate attributeName="opacity" values="1;.82;1" dur="3s" repeatCount="indefinite"/></g></svg>')
        return s
    n = len(p['md'])
    yb = 106 + 20 * (n - 1)
    cy_ = yb + 18
    by = cy_ + 26 + 16
    H = by + 38 + 22
    s = HDR.format(w=400, h=H + 14) + defs + f'<clipPath id="cp"><rect width="400" height="{H}" rx="18"/></clipPath></defs>'
    s += (f'<g clip-path="url(#cp)"><rect width="400" height="{H}" fill="{t["bg"]}"/><ellipse cx="0" cy="0" rx="300" ry="200" fill="url(#gl)"/>'
          f'<text x="386" y="110" text-anchor="end" font-family="{SANS}" font-size="110" font-weight="900" fill="{a}" opacity="{t["wm"]}">{p["n"]}</text></g>'
          f'<rect x="1" y="1" width="398" height="{H - 2}" rx="17" stroke="url(#bd)" stroke-width="1.6"/>'
          f'<text x="28" y="38" font-family="{MONO}" font-size="10" font-weight="700" letter-spacing="2.2" fill="{a}">{p["tag"]}</text>'
          f'<text x="28" y="80" font-family="{SANS}" font-size="28" font-weight="800" letter-spacing="-.5" fill="{t["t1"]}">{p["title"]}</text>')
    for k, ln in enumerate(p['md']):
        s += f'<text x="28" y="{106 + 20 * k}" font-family="{SANS}" font-size="13.5" fill="{t["t4"]}">{ln}</text>'
    x = 28
    for c in p['chips']:
        w = round(len(c) * 6.9 + 24)
        s += (f'<rect x="{x}" y="{cy_}" width="{w}" height="26" rx="13" fill="{a}" fill-opacity=".1" stroke="{a}" stroke-opacity=".4"/>'
              f'<text x="{f(x + w / 2)}" y="{cy_ + 17}" text-anchor="middle" font-family="{MONO}" font-size="11" fill="{t["t2"]}">{c}</text>')
        x += w + 8
    s += (f'<g transform="translate(28,{by})"><rect width="344" height="38" rx="19" fill="url(#a)"/>'
          f'<text x="172" y="24" text-anchor="middle" font-family="{SANS}" font-size="12.5" font-weight="800" letter-spacing="1.5" fill="#fff">{p["btn"]}</text>'
          f'<animate attributeName="opacity" values="1;.82;1" dur="3s" repeatCount="indefinite"/></g></svg>')
    return s


# ---------------------------------------------------------------- CONTACT
def contact(t, m=False):
    C, V, P = t['cyan'], t['violet'], t['pink']
    defs = (f'<defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="{C}"/><stop offset=".55" stop-color="{V}"/><stop offset="1" stop-color="{P}"/></linearGradient>'
            f'<radialGradient id="o"><stop offset="0" stop-color="{V}" stop-opacity=".45"/><stop offset="1" stop-color="{V}" stop-opacity="0"/></radialGradient>')
    if not m:
        PAD = 40
        return (HDR.format(w=1000, h=240 + PAD) + defs + '<clipPath id="c"><rect width="1000" height="240" rx="22"/></clipPath></defs>'
                f'<g transform="translate(0,{PAD})"><g clip-path="url(#c)"><rect width="1000" height="240" fill="{t["bg"]}"/>'
                f'<circle cx="860" cy="120" r="230" fill="url(#o)"><animate attributeName="r" values="200;250;200" dur="6s" repeatCount="indefinite"/></circle>'
                f'<g transform="translate(860,120)"><g><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="30s" repeatCount="indefinite"/>'
                f'<circle r="86" stroke="{C}" stroke-opacity=".4" stroke-dasharray="4 10" stroke-width="1.5"/><circle cx="86" r="5" fill="{C}"/></g>'
                f'<g><animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="18s" repeatCount="indefinite"/>'
                f'<circle r="52" stroke="{P}" stroke-opacity=".45" stroke-width="1.2"/><circle cy="-52" r="4" fill="{P}"/></g>'
                f'<text y="12" text-anchor="middle" font-size="34" font-family="{SANS}">✉</text></g>'
                f'<rect y="235" width="1000" height="5" fill="url(#g)"/></g>'
                f'<rect x=".75" y=".75" width="998.5" height="238.5" rx="21" stroke="{t["line"]}" stroke-width="1.5"/>'
                f'<text x="48" y="48" font-family="{MONO}" font-size="12" font-weight="700" letter-spacing="3" fill="{C}">LET\'S CONNECT</text>'
                f'<text x="48" y="108" font-family="{SANS}" font-size="46" font-weight="800" letter-spacing="-1" fill="{t["t1"]}">Let\'s build something</text>'
                f'<text x="48" y="162" font-family="{SANS}" font-size="46" font-weight="800" letter-spacing="-1" fill="url(#g)">worth shipping.</text>'
                f'<text x="48" y="204" font-family="{MONO}" font-size="16" fill="{t["t4"]}">pramodsiriwardhana@outlook.com</text></g></svg>')
    PAD = 26
    return (HDR.format(w=400, h=190 + PAD) + defs + '<clipPath id="c"><rect width="400" height="190" rx="18"/></clipPath></defs>'
            f'<g transform="translate(0,{PAD})"><g clip-path="url(#c)"><rect width="400" height="190" fill="{t["bg"]}"/>'
            f'<circle cx="350" cy="40" r="90" fill="url(#o)"><animate attributeName="r" values="80;100;80" dur="6s" repeatCount="indefinite"/></circle>'
            f'<g transform="translate(350,38)"><g><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="30s" repeatCount="indefinite"/>'
            f'<circle r="30" stroke="{C}" stroke-opacity=".45" stroke-dasharray="3 7" stroke-width="1.2"/><circle cx="30" r="3.5" fill="{C}"/></g>'
            f'<g><animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="18s" repeatCount="indefinite"/>'
            f'<circle r="18" stroke="{P}" stroke-opacity=".5" stroke-width="1"/><circle cy="-18" r="2.5" fill="{P}"/></g>'
            f'<text y="6" text-anchor="middle" font-size="16" font-family="{SANS}">✉</text></g>'
            f'<rect y="186" width="400" height="4" fill="url(#g)"/></g>'
            f'<rect x=".75" y=".75" width="398.5" height="188.5" rx="17" stroke="{t["line"]}" stroke-width="1.5"/>'
            f'<text x="28" y="44" font-family="{MONO}" font-size="10" font-weight="700" letter-spacing="3" fill="{C}">LET\'S CONNECT</text>'
            f'<text x="28" y="94" font-family="{SANS}" font-size="28" font-weight="800" letter-spacing="-.5" fill="{t["t1"]}">Let\'s build something</text>'
            f'<text x="28" y="132" font-family="{SANS}" font-size="28" font-weight="800" letter-spacing="-.5" fill="url(#g)">worth shipping.</text>'
            f'<text x="28" y="162" font-family="{MONO}" font-size="12.5" fill="{t["t4"]}">pramodsiriwardhana@outlook.com</text></g></svg>')


# ---------------------------------------------------------------- FOOTER
def footer(t, m=False):
    g = (f'<defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="{t["cyan"]}" stop-opacity="0"/>'
         f'<stop offset=".5" stop-color="{t["violet"]}"/><stop offset="1" stop-color="{t["pink"]}" stop-opacity="0"/></linearGradient></defs>')
    if not m:
        return (HDR.format(w=1000, h=70) + g + '<rect y="10" width="1000" height="2" fill="url(#g)"/>'
                f'<text x="500" y="42" text-anchor="middle" font-family="{MONO}" font-size="12.5" letter-spacing="3.5" fill="{t["t5"]}">BUILD WITH PURPOSE  ·  DEVELOP WITH CONSISTENCY  ·  KEEP LEARNING</text>'
                f'<text x="500" y="62" text-anchor="middle" font-family="{MONO}" font-size="11" letter-spacing="2" fill="{t["t6"]}">© 2026 PRAMOD SIRIWARDHANA</text></svg>')
    return (HDR.format(w=400, h=104) + g + '<rect y="8" width="400" height="2" fill="url(#g)"/>'
            f'<text x="200" y="34" text-anchor="middle" font-family="{MONO}" font-size="10" letter-spacing="2.5" fill="{t["t5"]}">BUILD WITH PURPOSE</text>'
            f'<text x="200" y="52" text-anchor="middle" font-family="{MONO}" font-size="10" letter-spacing="2.5" fill="{t["t5"]}">DEVELOP WITH CONSISTENCY</text>'
            f'<text x="200" y="70" text-anchor="middle" font-family="{MONO}" font-size="10" letter-spacing="2.5" fill="{t["t5"]}">KEEP LEARNING</text>'
            f'<text x="200" y="94" text-anchor="middle" font-family="{MONO}" font-size="9.5" letter-spacing="2" fill="{t["t6"]}">© 2026 PRAMOD SIRIWARDHANA</text></svg>')


ASSETS = {
    'header': hero, 'metrics': metrics,
    't-about': lambda t, m: section(t, 'ABOUT', m), 'about': about,
    't-stack': lambda t, m: section(t, 'TECH STACK', m), 'stack': stack,
    't-projects': lambda t, m: section(t, 'FEATURED PROJECTS', m),
    'p1': lambda t, m: project(t, 0, m), 'p2': lambda t, m: project(t, 1, m), 'p3': lambda t, m: project(t, 2, m),
    't-stats': lambda t, m: section(t, 'GITHUB PULSE', m),
    'contact': contact, 'footer': footer}

# ---------------------------------------------------------------- README
BP = '(max-width: 767px)'


def pic(name, alt, link=None):
    h = (f'<picture>\n'
         f'  <source media="{BP} and (prefers-color-scheme: light)" srcset="assets/light/{name}.mobile.svg">\n'
         f'  <source media="{BP}" srcset="assets/dark/{name}.mobile.svg">\n'
         f'  <source media="(prefers-color-scheme: light)" srcset="assets/light/{name}.svg">\n'
         f'  <img src="assets/dark/{name}.svg" alt="{alt}" width="100%" />\n</picture>')
    return f'<a href="{link}">{h}</a>' if link else h


def badge(label, logo, dark_logo, light_logo, url, alt):
    base = 'https://img.shields.io/badge/%s-%s?style=for-the-badge&logo=%s&logoColor=%s&labelColor=%s&color=%s'
    d = base % (label, '0a0e1a', logo, dark_logo, '0a0e1a', '1e2a44')
    l = base % (label, 'f6f8fa', logo, light_logo, 'f6f8fa', 'e2e8f0')
    return (f'<a href="{url}"><picture>\n  <source media="(prefers-color-scheme: light)" srcset="{l}">\n'
            f'  <img src="{d}" alt="{alt}"/>\n</picture></a>')


def stat(path, extra_d, extra_l, alt):
    host = 'https://github-readme-stats-pramod.vercel.app/api' + path
    common = 'username=pramodSiriwardhana&hide_border=false&border_radius=16'
    d = f'{host}?{common}&border_color=1e2a44&bg_color=0d1424&title_color=22d3ee&text_color=cbd5e1{extra_d}'
    l = f'{host}?{common}&border_color=d0d7de&bg_color=ffffff&title_color=0891b2&text_color=334155{extra_l}'
    return (f'<picture>\n  <source media="(prefers-color-scheme: light)" srcset="{l}">\n'
            f'  <img height="175" src="{d}" alt="{alt}" />\n</picture>')


def readme():
    return f'''<div align="center">

{pic('header', 'Pramod Siriwardhana — Full-Stack · Mobile · AI/ML Engineer')}

{badge('PORTFOLIO', 'vercel', '22d3ee', '0891b2', 'https://pramod-siriwardhana.vercel.app/', 'Portfolio')}
{badge('LINKEDIN', 'linkedin', '60a5fa', '2563eb', 'https://www.linkedin.com/in/pramod-siriwardhana', 'LinkedIn')}
{badge('GITHUB', 'github', 'e6edf3', '24292f', 'https://github.com/pramodSiriwardhana', 'GitHub')}
{badge('WHATSAPP', 'whatsapp', '4ade80', '16a34a', 'https://wa.me/94702705781', 'WhatsApp')}

{pic('metrics', 'Metrics')}

{pic('t-about', 'About')}
{pic('about', 'About me terminal')}

{pic('t-stack', 'Tech stack')}
{pic('stack', 'Tech stack')}

{pic('t-projects', 'Featured projects')}
{pic('p1', 'Iki Saki Travel', 'https://www.ikisakitours.com')}
{pic('p2', 'ML Price Predictor', 'https://github.com/pramodSiriwardhana/Fruits-Vegetables-Ml-Price-Prediction')}
{pic('p3', 'Artévo', 'https://github.com/pramodSiriwardhana/HND_FINAL_Artevo_web')}

{pic('t-stats', 'GitHub pulse')}

{stat('', '&icon_color=8b5cf6&show_icons=true&count_private=true&include_all_commits=true', '&icon_color=7c3aed&show_icons=true&count_private=true&include_all_commits=true', 'GitHub stats')}
{stat('/top-langs/', '&layout=compact&langs_count=8', '&layout=compact&langs_count=8', 'Top languages')}

{pic('contact', "Let's build something worth shipping", 'mailto:pramodsiriwardhana@outlook.com')}

{pic('footer', 'Footer')}

</div>
'''


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    n = 0
    for tn, t in THEMES.items():
        d = os.path.join(root, 'assets', tn)
        os.makedirs(d, exist_ok=True)
        for name, fn in ASSETS.items():
            for m in (False, True):
                p = os.path.join(d, name + ('.mobile.svg' if m else '.svg'))
                with open(p, 'w', encoding='utf-8') as fh:
                    fh.write(fn(t, m))
                n += 1
    with open(os.path.join(root, 'README.md'), 'w', encoding='utf-8') as fh:
        fh.write(readme())
    print(f'done: README.md + {n} svg files')


if __name__ == '__main__':
    main()
