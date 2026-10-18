"""assets/*/*.mobile.svg ඇතුලේ animations ඉවත් කරලා static (සැහැල්ලු) version එකක් හදනවා.
animation නැති වුණාම හැංගිලා යන දේවල් (width=0 clip, opacity=0 group) ආපහු පෙන්නනවා.
කලින් මේ script එක දුවපු files වලත් නැවත දුවන්න පුළුවන් (ඒවා හදලා දෙනවා).

භාවිතය (repo root එකේ):  python make_mobile_lite.py
desktop files වලටත් ඕන නම්:  python make_mobile_lite.py --all
"""
import re, sys, glob

CLIP = re.compile(
    r'<clipPath id="([^"]+)"><rect([^>]*?)\bwidth="0"([^>]*?)(?:/>|>(.*?)</rect>)</clipPath>', re.S)
POS_RECT = re.compile(r'<rect\b[^>]*>(?:\s*<animate\b[^>]*/>)+\s*</rect>')
POS_CIRCLE = re.compile(r'<circle\b[^>]*>(?:\s*<animate\b[^>]*/>)+\s*</circle>')
ANIM = re.compile(r'<(?:animate|animateTransform|animateMotion|set)\b[^>]*/>')

def lite(svg):
    total = re.search(r'<svg\b[^>]*?\bwidth="([\d.]+)"', svg)
    total = float(total.group(1)) if total else 400
    seen_y = set()

    def clip(m):
        cid, a, b, child = m.groups()
        child = child or ''
        y = re.search(r'\by="([\d.]+)"', a + b)
        y = y.group(1) if y else cid
        if y in seen_y:       # එකම තැන typing වෙන අනිත් lines (header) ඉවත් කරනවා
            svg_remove.append(cid)
            return ''
        seen_y.add(y)
        vals = re.search(r'attributeName="width"\s+values="([^"]+)"', child)
        full = max(float(v) for v in vals.group(1).split(';')) if vals else total
        full = int(full) if full == int(full) else full
        return f'<clipPath id="{cid}"><rect{a}width="{full}"{b}/></clipPath>'

    svg_remove = []
    svg = CLIP.sub(clip, svg)
    for cid in svg_remove:
        svg = re.sub(rf'<g clip-path="url\(#{cid}\)">.*?</g>', '', svg, flags=re.S)
    svg = POS_RECT.sub(lambda m: '' if 'attributeName="x"' in m.group(0) else m.group(0), svg)
    svg = POS_CIRCLE.sub(lambda m: '' if re.search(r'attributeName="c[xy]"', m.group(0)) else m.group(0), svg)
    svg = re.sub(r'<g opacity="0">', '<g>', svg)   # fade-in වෙන්න තිබුණු groups (chips) පෙන්නනවා
    return ANIM.sub('', svg)

pattern = 'assets/*/*.svg' if '--all' in sys.argv else 'assets/*/*.mobile.svg'
for f in glob.glob(pattern):
    s = open(f, encoding='utf-8').read()
    n = lite(s)
    if n != s:
        open(f, 'w', encoding='utf-8').write(n)
        print('lite:', f, len(s), '->', len(n))