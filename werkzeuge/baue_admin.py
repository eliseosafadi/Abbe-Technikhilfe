# -*- coding: utf-8 -*-
"""Erzeugt admin.html aus der jeweils AKTUELLEN index.html.

Die Texte werden ueber ihre Umgebung (Praefix/Suffix) gefunden, nicht als
feste Zeichenketten. Dadurch laesst sich die Admin-Seite jederzeit neu
bauen — auch nachdem Texte ueber sie geaendert wurden.
"""
import hashlib, json, re, sys

REPO = sys.argv[1] if len(sys.argv) > 1 else "/home/user/Abbe-Technikhilfe"
VORLAGE_DATEI = sys.argv[2] if len(sys.argv) > 2 else "admin_vorlage.html"
roh = open(f"{REPO}/index.html", "rb").read()
html = roh.decode("utf-8")
# Git-Blob-SHA der index.html - genau die "sha", die GitHubs Contents-API meldet.
# Die Admin-Seite erkennt daran, ob die Seite bei GitHub noch dieselbe ist.
basis_sha = hashlib.sha1(b"blob " + str(len(roh)).encode() + b"\0" + roh).hexdigest()

schnitt = html.index("-->") + 3
kopf, rumpf = html[:schnitt], html[schnitt:]
koerper = re.search(r"<body>(.*)</body>", html, re.S).group(1).strip()

felder, werte = [], {}

# In der Vorlage stehen an den Fundstellen bereits Platzhalter wie ${h(w.telefon_link)}.
# Der Admin-Text (koerper) enthaelt dagegen weiterhin den urspruenglichen Text.
# Diese Tabelle uebersetzt zurueck, damit Umgebungen, die einen schon ersetzten
# Text enthalten (z. B. die Anruf-Knoepfe), auch im Admin-Text gefunden werden.
ersetzungen = {}

def fuer_koerper(t):
    for platzhalter, original in ersetzungen.items():
        t = t.replace(platzhalter, original)
    return t

def merken(key, text):
    ersetzungen["${h(w.%s)}" % key] = text
    ersetzungen["${f(w.%s)}" % key] = text

def unescape(t):
    return t.replace("&nbsp;", " ").replace("&amp;", "&")

def zu_sternen(t):
    return re.sub(r"<strong>(.*?)</strong>", r"**\1**", t)

def spanne(key, label, text, fett, inline):
    klasse = "bearbeitbar" + ("" if inline else " adm-block")
    return (f'<span class="{klasse}" contenteditable="true" spellcheck="false" '
            f'data-key="{key}" data-fett="{"1" if fett else "0"}" '
            f'role="textbox" tabindex="0" title="{label} — zum Ändern anklicken">{text}</span>')

def eintragen(key, label, text, fett, hilfe, sichtbar, gruppe):
    felder.append({"key": key, "label": label, "hilfe": hilfe,
                   "sichtbar": sichtbar, "fett": fett, "gruppe": gruppe})
    werte[key] = unescape(zu_sternen(text) if fett else text)

def pruefe(key, text):
    if "<span" in text or "${" in text or len(text) > 4000:
        raise SystemExit(f"FEHLER: '{key}' fängt zu viel ein: {text[:90]!r}")

def reihe(eintraege, praefix, suffix, fett=False, inline=False, sichtbar=True, gruppe=None):
    """Findet alle Vorkommen zwischen praefix/suffix und verteilt sie der Reihe nach."""
    global rumpf, koerper
    muster = re.compile(re.escape(praefix) + r"(.*?)" + re.escape(suffix), re.S)
    treffer = muster.findall(rumpf)
    if len(treffer) != len(eintraege):
        raise SystemExit(f"FEHLER: {[e[0] for e in eintraege]} — {len(treffer)} Treffer statt "
                         f"{len(eintraege)}.\n  Kontext: {praefix[-50:]!r} ... {suffix[:30]!r}")
    for (key, label, hilfe), text in zip(eintraege, treffer):
        pruefe(key, text)
        eintragen(key, label, text, fett, hilfe, sichtbar, gruppe)
        merken(key, text)

    zaehler = {"i": 0}
    def ersetze_vorlage(m):
        key = eintraege[zaehler["i"]][0]; zaehler["i"] += 1
        slot = f"${{f(w.{key})}}" if fett else f"${{h(w.{key})}}"
        return praefix + slot + suffix
    rumpf = muster.sub(ersetze_vorlage, rumpf)

    if sichtbar:
        p_k, s_k = fuer_koerper(praefix), fuer_koerper(suffix)
        muster_k = re.compile(re.escape(p_k) + r"(.*?)" + re.escape(s_k), re.S)
        z2 = {"i": 0}
        def ersetze_admin(m):
            key, label, _ = eintraege[z2["i"]]; z2["i"] += 1
            return p_k + spanne(key, label, m.group(1), fett, inline) + s_k
        koerper, anzahl_k = muster_k.subn(ersetze_admin, koerper)
        if anzahl_k != len(eintraege):
            raise SystemExit(f"FEHLER: {[e[0] for e in eintraege]} im Admin-Text "
                             f"{anzahl_k}x statt {len(eintraege)}x gefunden.")

def feld(key, label, praefix, suffix, fett=False, inline=False, hilfe=None,
         anzahl=1, sichtbar=True, gruppe=None):
    """Ein Text, der (ggf. mehrfach identisch) vorkommt."""
    global rumpf, koerper
    muster = re.compile(re.escape(praefix) + r"(.*?)" + re.escape(suffix), re.S)
    treffer = muster.findall(rumpf)
    if len(treffer) != anzahl:
        raise SystemExit(f"FEHLER: '{key}' {len(treffer)}x statt {anzahl}x.\n"
                         f"  Kontext: {praefix[-50:]!r} ... {suffix[:30]!r}")
    if len(set(treffer)) != 1:
        raise SystemExit(f"FEHLER: '{key}' mit verschiedenen Texten: {set(treffer)}")
    text = treffer[0]; pruefe(key, text)
    slot = f"${{f(w.{key})}}" if fett else f"${{h(w.{key})}}"
    rumpf = muster.sub(lambda m: praefix + slot + suffix, rumpf)
    if sichtbar:
        p_k, s_k = fuer_koerper(praefix), fuer_koerper(suffix)
        muster_k = re.compile(re.escape(p_k) + r"(.*?)" + re.escape(s_k), re.S)
        koerper, anzahl_k = muster_k.subn(
            lambda m: p_k + spanne(key, label, text, fett, inline) + s_k, koerper)
        if anzahl_k != anzahl:
            raise SystemExit(f"FEHLER: '{key}' im Admin-Text {anzahl_k}x statt {anzahl}x gefunden.\n"
                             f"  Kontext: {p_k[-50:]!r} ... {s_k[:30]!r}")
    eintragen(key, label, text, fett, hilfe, sichtbar, gruppe)
    merken(key, text)

KASTEN = "Nicht sichtbare Angaben"

# --- Telefonnummer zuerst: sie steckt in den Knopf-Kontexten ---
feld("telefon_link", "Telefonnummer zum Wählen", 'href="tel:', '">', anzahl=4, sichtbar=False,
     gruppe=KASTEN, hilfe="Format +49451… ohne Leerzeichen. Bestimmt, welche Nummer beim Antippen gewählt wird.")

# --- E-Mail: Link und sichtbarer Text in einem Zug ---
def email_feld():
    global rumpf, koerper
    muster = re.compile(r'href="mailto:(.*?)">(.*?)</a>')
    t = muster.findall(rumpf)
    if len(t) != 1 or t[0][0] != t[0][1]:
        raise SystemExit(f"FEHLER: E-Mail-Feld unklar: {t}")
    adresse = t[0][0]; label = "E-Mail-Adresse"
    rumpf = muster.sub('href="mailto:${h(w.email)}">${h(w.email)}</a>', rumpf)
    koerper = muster.sub(lambda m: 'href="mailto:' + adresse + '">'
                         + spanne("email", label, adresse, False, True) + '</a>', koerper)
    eintragen("email", label, adresse, False, "Wird als Link und als sichtbarer Text verwendet.", True, None)
    merken("email", adresse)

# --- Kopf & Navigation ---
feld("marke", "Name in der Leiste", '<span class="marke">', '</span>', inline=True)
feld("nav_knopf", "Knopf in der Leiste", '<a class="pille-klein" href="tel:${h(w.telefon_link)}">', '</a>', inline=True)
feld("vorzeile", "Kleine blaue Zeile", '<p class="vorzeile">', '</p>')
feld("ueberschrift", "Große Überschrift", '<h1>', '</h1>')
feld("unterzeile", "Text unter der Überschrift", '<p class="held-sub">', '</p>')
feld("knopf_text", "Anruf-Knopf (alle drei zugleich)",
     '<a class="pille" href="tel:${h(w.telefon_link)}">', '</a>', inline=True, anzahl=3,
     hilfe="Der Text erscheint oben, beim Preis und im Fußbereich.")
feld("hinweis", "Zeile unter dem Anruf-Knopf", '<p class="hinweis">', '</p>')

# --- Alle Abschnitts-Überschriften in Dokumentreihenfolge ---
reihe([("h2_hilfe", "Überschrift: Wobei ich helfe", None),
       ("h2_besuch", "Überschrift: So läuft ein Besuch ab", None),
       ("h2_preis", "Überschrift: Was es kostet", None),
       ("h2_vertrauen", "Überschrift: Daran erkennen Sie mich", None),
       ("h2_ueber", "Überschrift: Über mich", None),
       ("h2_angehoerige", "Überschrift: Für Angehörige", None),
       ("h2_fragen", "Überschrift: Häufige Fragen", None)], '<h2>', '</h2>')

feld("intro_hilfe", "Einleitungssatz", '<p class="einleitung">', '</p>')
reihe([(f"karte{i}_titel", f"Karte {i}: Titel", None) for i in range(1, 7)], '<h3>', '</h3>')
reihe([(f"karte{i}_text", f"Karte {i}: Text", None) for i in range(1, 7)],
      '</h3>\n          <p>', '</p>')
reihe([(f"schritt{i}", f"Schritt {i}", None) for i in range(1, 4)], '<li><p>', '</p></li>')
feld("preis_text", "Preistext", '<div class="preis-karte">\n        <p>', '</p>',
     fett=True, hilfe="Fettdruck bleibt beim Tippen erhalten.")
reihe([(f"merkmal{i}", f"Punkt {i}", None) for i in range(1, 5)],
      '\n          <li>', '</li>', fett=True)
feld("schlusszeile", "Kursive Schlusszeile", '<p class="schlusszeile">', '</p>')
reihe([("ueber_text", "Text: Über mich", "[STADTTEIL] durch den echten Stadtteil ersetzen."),
       ("angehoerige_text", "Text: Für Angehörige", None)], '</h2>\n      <p>', '</p>')
feld("mail_hinweis", "Zeile vor der E-Mail", '<p class="mailzeile">', ' <a href="mailto:', inline=True)
email_feld()
reihe([(f"frage{i}", f"Frage {i}", None) for i in range(1, 5)], '<p><strong>', '</strong>', inline=True)
reihe([(f"antwort{i}", f"Antwort {i}", None) for i in range(1, 5)],
      '</strong>\n        ', '</p>', inline=True)
reihe([("fuss_zeile1", "Erste Fußzeile", None),
       ("fuss_zeile2", "Zweite Fußzeile", None)], '<p class="fusszeile">', '</p>')

# --- Nicht sichtbare Angaben ---
for key, label, pre, suf, hilfe in [
    ("titel_seite", "Seitentitel (Browser-Tab und Google)", '<title>', '</title>', None),
    ("meta_beschreibung", "Beschreibung für Google (max. 155 Zeichen)", 'name="description" content="', '">', None),
    ("telefon_daten", "Telefonnummer für Suchmaschinen", '"telephone": "', '"', None),
    ("adresse_daten", "Anschrift für Suchmaschinen", '"streetAddress": "', '"', None),
    ("preisspanne", "Preisspanne für Suchmaschinen", '"priceRange": "', '"', None)]:
    feld(key, label, pre, suf, hilfe=hilfe, sichtbar=False, gruppe=KASTEN)

# Schlusskontrolle: Jedes sichtbare Feld muss im Admin-Text auch wirklich
# als anklickbare Stelle vorkommen, sonst laesst es sich dort nicht aendern.
fehlend = [f["key"] for f in felder
           if f["sichtbar"] and f'data-key="{f["key"]}"' not in koerper]
if fehlend:
    raise SystemExit(f"FEHLER: im Admin-Text nicht bearbeitbar: {fehlend}")

vorlage = kopf + rumpf
for z in ("`", "\\"):
    if z in vorlage:
        raise SystemExit(f"FEHLER: Zeichen {z!r} in der Vorlage — bricht die JS-Vorlage.")
vorlage_js = vorlage.replace("</script>", "<\\/script>")
stil = re.search(r"<style>(.*?)</style>", html, re.S).group(1)

admin = (open(VORLAGE_DATEI, encoding="utf-8").read()
         .replace("__SEITENSTIL__", stil).replace("__SEITE__", koerper)
         .replace("__START__", json.dumps(werte, ensure_ascii=False, indent=1))
         .replace("__FELDER__", json.dumps(felder, ensure_ascii=False))
         .replace("__VORLAGE__", vorlage_js)
         .replace("__BASIS_SHA__", basis_sha))
open(f"{REPO}/admin.html", "w", encoding="utf-8").write(admin)
s = sum(1 for f in felder if f["sichtbar"])
print(f"admin.html neu gebaut: {len(felder)} Felder ({s} im Text, {len(felder)-s} im Kasten)")
