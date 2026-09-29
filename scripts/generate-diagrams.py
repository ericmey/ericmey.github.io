"""Regenerate the portfolio's decorative blueprint diagrams (stdlib only)."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1] / 'public' / 'diagrams'
ROOT.mkdir(parents=True, exist_ok=True)

ART = {
 'five-lane-router': ('01', 'ROUTING / FIVE PATHS', '''
 <rect x="145" y="246" width="230" height="174" rx="18" class="box"/><path d="M178 285h165M178 320h130M178 355h148" class="dim"/>
 <path d="M375 333h120m0 0v-154m0 154v154" class="line"/>
 <path d="M495 179h95m-95 77h95m-95 77h95m-95 77h95m-95 77h95" class="line"/>
 <g class="box"><rect x="590" y="145" width="286" height="68" rx="12"/><rect x="590" y="222" width="286" height="68" rx="12"/><rect x="590" y="299" width="286" height="68" rx="12"/><rect x="590" y="376" width="286" height="68" rx="12"/><rect x="590" y="453" width="286" height="68" rx="12"/></g>
 <path d="M495 333h95" class="hot"/><circle cx="495" cy="333" r="8" class="node"/>
 <g class="label"><text x="625" y="188">CHAT</text><text x="625" y="265">IMAGE</text><text x="625" y="342">SEARCH</text><text x="625" y="419">AUDIO</text><text x="625" y="496">VIDEO</text></g>
 '''),
 'musubi': ('02', 'MEMORY / RETRIEVAL', '''
 <g class="box"><rect x="146" y="153" width="294" height="90" rx="13"/><rect x="146" y="292" width="294" height="90" rx="13"/><rect x="146" y="431" width="294" height="90" rx="13"/></g>
 <g class="label"><text x="180" y="208">EPISODIC</text><text x="180" y="347">CONCEPT</text><text x="180" y="486">CURATED</text></g>
 <path d="M294 243v49m0 90v49" class="line"/><path d="M440 198h143m-143 139h143m-143 139h143" class="line"/>
 <circle cx="583" cy="198" r="8" class="node"/><circle cx="583" cy="337" r="8" class="node"/><circle cx="583" cy="476" r="8" class="node"/>
 <path d="M583 198h48v139h-48m48 0v139h-48m48-139h90" class="line"/>
 <rect x="722" y="266" width="298" height="142" rx="20" class="box"/><circle cx="824" cy="337" r="36" class="accent"/><path d="M849 362l44 44" class="hot"/><path d="M914 305h63m-63 34h48" class="dim"/>
 '''),
 'musubi-ecosystem': ('03', 'ONE CONTRACT / FIVE HOSTS', '''
 <circle cx="600" cy="337" r="112" class="box"/><circle cx="600" cy="337" r="42" class="accent"/>
 <path d="M600 225V153M706 303l133-74M706 372l133 74M541 431l-106 87M494 303l-143-74" class="line"/>
 <g class="box"><rect x="506" y="102" width="188" height="60" rx="11"/><rect x="839" y="193" width="188" height="60" rx="11"/><rect x="839" y="420" width="188" height="60" rx="11"/><rect x="246" y="488" width="188" height="60" rx="11"/><rect x="163" y="193" width="188" height="60" rx="11"/></g>
 <g class="small"><text x="536" y="140">CLAUDE</text><text x="877" y="231">CODEX</text><text x="888" y="458">GROK</text><text x="278" y="526">HERMES</text><text x="186" y="231">OPENCLAW</text></g>
 '''),
 'openclaw-musubi': ('04', 'CAPTURE / OUTBOX / MEMORY', '''
 <g class="box"><rect x="142" y="225" width="240" height="224" rx="18"/><rect x="476" y="225" width="240" height="224" rx="18"/><rect x="810" y="225" width="240" height="224" rx="18"/></g>
 <path d="M382 337h94m240 0h94" class="hot"/><path d="M437 324l24 13-24 13m334-26l24 13-24 13" class="hot"/>
 <g class="label"><text x="184" y="338">HOST</text><text x="517" y="338">OUTBOX</text><text x="843" y="338">MUSUBI</text></g>
 <path d="M558 397h80m-418 0h80m674 0h30" class="dim"/><circle cx="596" cy="201" r="10" class="node"/><path d="M596 211v14" class="line"/>
 '''),
 'comfyui-immich': ('05', 'IMAGE / METADATA / LIBRARY', '''
 <rect x="147" y="188" width="296" height="296" rx="16" class="box"/><path d="M176 442l78-102 61 63 45-50 54 89" class="line"/><circle cx="347" cy="262" r="26" class="accent"/>
 <path d="M443 337h166" class="hot"/><path d="M566 324l24 13-24 13" class="hot"/>
 <rect x="610" y="188" width="420" height="296" rx="16" class="box"/>
 <g class="dim"><rect x="643" y="222" width="103" height="90" rx="6"/><rect x="768" y="222" width="103" height="90" rx="6"/><rect x="893" y="222" width="103" height="90" rx="6"/><rect x="643" y="336" width="103" height="90" rx="6"/><rect x="768" y="336" width="103" height="90" rx="6"/><rect x="893" y="336" width="103" height="90" rx="6"/></g>
 <path d="M663 247h62m-62 18h47m-47 18h55" class="hot"/>
 '''),
 'comfyui-kotodama': ('06', 'DRAFT / TRANSFORM / RENDER', '''
 <rect x="146" y="206" width="260" height="260" rx="16" class="box"/><path d="M182 255h184m-184 40h147m-147 40h171m-171 40h104" class="dim"/>
 <path d="M406 337h130" class="line"/><circle cx="600" cy="337" r="65" class="box"/><path d="M600 292v90m-45-45h90" class="hot"/>
 <path d="M665 337h130" class="line"/><rect x="795" y="206" width="260" height="260" rx="16" class="box"/>
 <path d="M823 432l66-104 56 63 38-46 44 87" class="line"/><circle cx="951" cy="272" r="22" class="accent"/>
 '''),
 'memory-article': ('07', 'ANSWER / CAPTURE / RECEIPT', '''
 <rect x="140" y="200" width="278" height="274" rx="18" class="box"/><path d="M178 255h190m-190 38h154m-154 38h180" class="dim"/><circle cx="374" cy="415" r="13" class="accent"/>
 <path d="M418 337h189" class="line"/><path d="M517 325l27 12-27 12" class="line"/><path d="M607 337h70" class="hot"/>
 <rect x="677" y="236" width="348" height="200" rx="18" class="box"/><path d="M717 290h266m-266 45h207m-207 45h246" class="dim"/><circle cx="677" cy="337" r="11" class="node"/>
 '''),
 'maintained-map-article': ('08', 'SOURCES / MAP / CHECKS', '''
 <g class="box"><rect x="149" y="194" width="248" height="270" rx="14"/><rect x="185" y="224" width="248" height="270" rx="14"/></g><path d="M221 274h165m-165 35h122m-122 35h150" class="dim"/>
 <path d="M433 337h158" class="line"/><circle cx="634" cy="337" r="48" class="accent"/><path d="M681 337h88m0 0v-102m0 102v102" class="line"/>
 <circle cx="769" cy="235" r="13" class="node"/><circle cx="769" cy="439" r="13" class="node"/><path d="M782 235h181m-181 204h181" class="dim"/>
 '''),
 'router-note-article': ('09', 'FIVE-LANE LAB NOTE', '''
 <path d="M174 337h185m0 0l126-135m-126 135l126-68m-126 68h126m-126 0l126 68m-126-68l126 135" class="line"/>
 <circle cx="359" cy="337" r="42" class="accent"/><g class="box"><rect x="485" y="171" width="420" height="58" rx="11"/><rect x="485" y="240" width="420" height="58" rx="11"/><rect x="485" y="309" width="420" height="58" rx="11"/><rect x="485" y="378" width="420" height="58" rx="11"/><rect x="485" y="447" width="420" height="58" rx="11"/></g>
 <path d="M499 337h390" class="hot"/>
 '''),
 'agent-org-article': ('10', 'AGENTS / ROLES / BOUNDARIES', '''
 <rect x="480" y="143" width="240" height="94" rx="16" class="box"/><circle cx="600" cy="190" r="19" class="accent"/>
 <path d="M600 237v88m-314 0h628m-628 0v67m314-67v67m314-67v67" class="line"/>
 <g class="box"><rect x="174" y="392" width="224" height="105" rx="15"/><rect x="488" y="392" width="224" height="105" rx="15"/><rect x="802" y="392" width="224" height="105" rx="15"/></g>
 <g class="dim"><path d="M212 431h148m-148 31h101M526 431h148m-148 31h101M840 431h148m-148 31h101"/></g>
 '''),
}

BASE = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 675" role="img" aria-hidden="true">
<defs>
 <pattern id="grid" width="36" height="36" patternUnits="userSpaceOnUse"><path d="M36 0H0V36" fill="none" stroke="#9eaaad" stroke-opacity=".09" stroke-width="1"/></pattern>
 <linearGradient id="ground" x2="1" y2="1"><stop stop-color="#101519"/><stop offset="1" stop-color="#1d2224"/></linearGradient>
</defs>
<style>.box{{fill:none;stroke:#dde1df;stroke-opacity:.66;stroke-width:2.5}}.line{{fill:none;stroke:#dce2e0;stroke-opacity:.64;stroke-width:2.5;stroke-linecap:round;stroke-linejoin:round}}.dim{{fill:none;stroke:#c8d2d0;stroke-opacity:.35;stroke-width:2;stroke-linecap:round}}.hot{{fill:none;stroke:#f0a03a;stroke-width:3;stroke-linecap:round;stroke-linejoin:round}}.node{{fill:#f0a03a}}.accent{{fill:none;stroke:#f0a03a;stroke-width:3}}.label{{font:22px ui-monospace,monospace;fill:#e7e9e4;letter-spacing:3px}}.small{{font:17px ui-monospace,monospace;fill:#e7e9e4;letter-spacing:2px}}</style>
<rect width="1200" height="675" fill="url(#ground)"/><rect width="1200" height="675" fill="url(#grid)"/>
<path d="M72 80h1056M72 578h1056" stroke="#a7b3b0" stroke-opacity=".35"/><path d="M72 80h192M72 578h192" stroke="#f0a03a" stroke-width="3"/>
<text x="78" y="122" fill="#f0a03a" font-family="ui-monospace,monospace" font-size="16" letter-spacing="3">FIG. {num}</text>
{art}
<text x="76" y="626" fill="#dce2e0" font-family="ui-monospace,monospace" font-size="22" letter-spacing="4">{caption}</text>
<text x="1122" y="626" text-anchor="end" fill="#b1bbb7" font-family="ui-monospace,monospace" font-size="17" letter-spacing="2">EM / SYSTEMS</text>
</svg>
'''

for slug, (num, caption, art) in ART.items():
    (ROOT / f'{slug}.svg').write_text(BASE.format(num=num, caption=escape(caption), art=art), encoding='utf-8')
