"""Generate the three top-level section banners as restrained SVG drawings."""
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / 'public' / 'banners'
OUT.mkdir(parents=True, exist_ok=True)

SCENES = {
 'projects': '''
  <g fill="none" stroke="#d8e0df" stroke-width="2" stroke-opacity=".52">
    <rect x="965" y="86" width="250" height="120" rx="12"/><rect x="1042" y="254" width="250" height="120" rx="12"/><rect x="1320" y="168" width="210" height="120" rx="12"/>
    <path d="M1215 146h105v82m-55 86h55v-86"/>
    <path d="M1002 126h165m-165 28h116m-36 144h164m-164 28h108m175-116h124m-124 28h94" stroke-opacity=".32"/>
  </g><circle cx="1320" cy="228" r="11" fill="#f0a03a"/><path d="M852 228h92" stroke="#f0a03a" stroke-width="2.5"/>
 ''',
 'writing': '''
  <g fill="none" stroke="#d8e0df" stroke-width="2" stroke-opacity=".52">
    <path d="M992 83h260l55 55v253H992z"/><path d="M1252 83v55h55"/><path d="M1050 184h195m-195 34h161m-161 34h188m-188 34h151m-151 34h181"/>
    <path d="M1308 126h149l48 48v197h-198" stroke-opacity=".28"/><path d="M1353 212h106m-106 34h89m-89 34h104" stroke-opacity=".28"/>
  </g><path d="M1038 350h164" stroke="#f0a03a" stroke-width="3"/><circle cx="1276" cy="138" r="10" fill="#f0a03a"/>
 ''',
 'about': '''
  <g fill="none" stroke="#d8e0df" stroke-width="2" stroke-opacity=".5">
    <circle cx="1170" cy="228" r="122"/><circle cx="1170" cy="228" r="81"/><path d="M1004 228h-96m384 0h100M1170 80V35m0 386v-45"/>
    <path d="M1087 146l166 164m0-164l-166 164" stroke-opacity=".23"/>
    <rect x="1366" y="148" width="128" height="160" rx="12"/><path d="M1390 188h80m-80 28h62m-62 28h70"/>
  </g><circle cx="1170" cy="228" r="11" fill="#f0a03a"/><path d="M908 228h85" stroke="#f0a03a" stroke-width="2.5"/>
 ''',
}

TEMPLATE = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 450" aria-hidden="true">
<defs>
 <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#b7c3c0" stroke-opacity=".08"/></pattern>
 <linearGradient id="bg"><stop stop-color="#101519"/><stop offset="1" stop-color="#1b2022"/></linearGradient>
 <linearGradient id="fade"><stop stop-color="#101519"/><stop offset=".52" stop-color="#101519" stop-opacity=".72"/><stop offset=".8" stop-color="#101519" stop-opacity="0"/></linearGradient>
</defs>
<rect width="1600" height="450" fill="url(#bg)"/><rect width="1600" height="450" fill="url(#grid)"/>
{scene}
<rect width="1600" height="450" fill="url(#fade)"/>
<path d="M58 405h1484" stroke="#b8c5c2" stroke-opacity=".27"/><path d="M58 405h212" stroke="#f0a03a" stroke-width="3"/>
</svg>
'''
for name, scene in SCENES.items():
    (OUT / f'{name}.svg').write_text(TEMPLATE.format(scene=scene), encoding='utf-8')
