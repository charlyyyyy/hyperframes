---
version: 2
name: "Jean Immobilier: launch frame"
description: >
  Frame spec du film « Vous attendez » (Jean Immobilier, 49,8 s, 16:9). Deux mondes : le PROBLÈME vit sur une nuit
  ardoise (une semaine de calendrier qui attend, des pastilles ambre « En attente ») ; la SOLUTION sur un papier gris très
  clair (les mêmes objets réparés, pastilles ardoise ✓). Un seul accent : le rouge de la marque, réservé à la boîte du mot
  clé, aux 4 traits des pics, au bouton de fin. Le sous-titre de la voix arrive mot par mot en bas au centre.
  CODE COMMUN : reference/kit.html (blocs « JI KIT CSS » et « JI KIT JS » à copier MOT POUR MOT).
unit: 1920×1080
principle: lisible sans le son · une seule chose à regarder · un seul accent · chaque révélation calée sur la voix

colors:
  canvas: "#141B1E" # nuit ardoise (acte 1)
  canvas-2: "#1E282C"
  black: "#0A0E10" # pivot
  paper: "#F4F4F2" # acte 2 et carte de fin
  paper-2: "#E9E9E6"
  card-light: "#FFFFFF"
  ink: "#EEF1F2" # texte sur sombre
  ink-soft: "#C9D0D3"
  ink-mute: "#8E9A9E"
  ink-dark: "#26313A" # texte sur clair
  ink-dark-soft: "#5A666C"
  hairline-light: "#DADAD6"
  accent: "#D33543" # rouge Jean Immobilier (bande du logo)
  accent-light: "#E25C68"
  accent-deep: "#A82632"
  accent-glow: "#EE8A93"
  slate: "#526166" # ardoise du logo : état « réparé » (pastille ✓), avatars de l'agence
  wait: "#F2A93B" # ambre : UNIQUEMENT la pastille d'attente (négatif)
  greys: ["#E8E8E8", "#D6D6D6", "#BDBBBC", "#949494", "#526166"] # les 5 bandes du toit du logo

fonts:
  JI Inter:
    {
      files:
        [
          "assets/fonts/Inter-Regular.otf (400)",
          "assets/fonts/Inter-Medium.otf (500)",
          "assets/fonts/Inter-SemiBold.otf (600)",
          "assets/fonts/Inter-Bold.otf (700)",
          "assets/fonts/Inter-ExtraBold.otf (800)",
        ],
      note: "déclarées dans le bloc JI KIT CSS ; police proche du lettrage du logo",
    }

typography:
  subtitle:
    {
      fontFamily: "JI Inter",
      px: 62,
      weight: 600,
      lineHeight: 74,
      note: "classe .ji-sub (ajouter .light sur le monde clair) : bas centre, top 896, bande y 890 à 980 vide de tout le reste, 45 caractères max, mot par mot (jiSubAnim)",
    }
  type:
    {
      fontFamily: "JI Inter",
      px: 84,
      weight: 700,
      note: "classe .ji-type : seulement « Assez attendu. » (pivot) ; pas de sous-titre en même temps",
    }
  ui: { fontFamily: "JI Inter", px: 28, weight: 500 }
  label:
    {
      fontFamily: "JI Inter",
      px: 22,
      weight: 700,
      upper: true,
      tracking: "0.12em",
      note: "classe .ji-lb",
    }
  number:
    {
      fontFamily: "JI Inter",
      px: 92,
      weight: 800,
      note: "classe .ji-num : chiffres en rouleaux ; tout nombre roule, aucun n'apparaît en fondu",
    }

components:
  camera: "chaque séquence a un #<p>-world (classe .ji-world) qui porte le décor ; la caméra est un objet {x, y, s, r} animé par GSAP et appliqué par jiCam(world, cam) dans onUpdate ; dérive linéaire permanente + crans (expo.inOut 0,12 à 0,15 s, flou 6 à 12 px au milieu, via jiBlur sur un calque lentille)."
  ground: "sol plein cadre en clip de toute la durée : .ji-ground-dark (acte 1), .ji-ground-black (pivot), .ji-ground-light (acte 2, fin), + .ji-dots (ou .ji-dots.light) DANS le monde + .ji-grain (ou .ji-grain.light) par-dessus."
  word-by-word: "jiSubHTML(prefix, mots, {box:[i,j]} ou {stroke:[i,j]}) puis jiSubAnim(tl, el, cues, {boxAt, strokeAt, outAt}) ; chaque mot sur son cue (0 à 2 images d'avance), jamais en retard ; sortie 0,14 s avant une couture où la phrase change."
  key-word-box: "rectangle rouge accent (rayon 3 px) qui se trace de gauche à droite en 0,16 s, 0 à 2 images avant le mot ; le mot passe en blanc. UNE boîte par phrase, sur [boîte : …]."
  peak-stroke: "trait rouge de 7 px aux bouts ronds sous LE mot [trait : …], tracé en 0,35 s pendant qu'il est dit. 4 pics dans le film : encore, pleine/autour, dort, personne, plus (selon le storyboard)."
  day-tile: "jiTileHTML(id, 'MARDI', '14', '9:00') : tuile 560 × 700 du calendrier, posée sur le ruban (.ji-ribbon, y du ruban = haut de tuile + 280)."
  phone: "jiPhoneHTML(id, écran, sombre?) : iPhone récent 360 × 740, écran 332 × 712 ; interfaces génériques sobres (appel, mail, banque, SMS), sans vraie marque tierce."
  wait-pill: "signature 1 : jiPillHTML(id, 'En attente', 'Payé') + jiPillBorn (naît d'un point, 0,14 s) + jiPillPulse (3 points qui pulsent, boucle finie)."
  fix-tick: "signature 2 : jiPillFlip(tl, pastilleAmbre, pastilleArdoise, t) : la pastille ambre bascule et devient ardoise « ✓ … » (posée exactement au même endroit)."
  cards: "classe .ji-card.dark (acte 1) ou .ji-card.light (acte 2) ; ANNONCE / PRIX, LOYER, TRAVAUX gardent la même taille et la même mise en page dans les deux actes (seules les couleurs et les états changent)."
  building: "jiBuildingSVG(id, largeur, couleur, allumé) : « votre bien », immeuble au trait ; fenêtres .<id>-win (les .on sont allumées), lueur <id>-glow."
  logo: "jiLogoSVG(id, largeur, surSombre) : logo Jean Immobilier redessiné (5 bandes de toit grises .<id>-band du haut vers le bas, bande rouge « GROUPE DELPHINE JEAN », « JEAN IMMOBILIER »). Les bandes peuvent arriver une à une (0,05 s d'écart, depuis la gauche, expo.out). Jamais déformé, jamais recoloré."
  cursor: "jiCursorSVG(id) : flèche noire contour blanc, 70 × 100 ; arrive en UNE courbe (x et y sur deux courbes, 0,45 s power3.out), clic direct : pression ×0,85 0,06 s + onde .ji-ripple rouge qui s'ouvre et s'efface."

world:
  act1: "monde 2D : ruban de tuiles en y 0 : MARDI (0,0), JEUDI (2400,0), LUNDI (4800,0) (coordonnées = centre de la tuile) ; « le bien » en (4800,2600) entouré de ANNONCE (3700,2500), LOYER (5900,2500), TRAVAUX (4800,3500)."
  act2: "même géométrie sur le papier ; PRIX (ex-ANNONCE) (3700,2500), LOYER (5900,2500), TRAVAUX (4800,3500) autour du bien (4800,2600)."
  rule: "une séquence n'a pas besoin de construire tout le monde : elle construit ce que sa caméra voit, AUX coordonnées ci-dessus, pour que les coutures raccordent."

negative:
  - "Aucun autre mécanisme de mise en valeur que la boîte rouge et le trait ; pas de texte coloré, pas de lueur sur du texte."
  - "Sous-titre 62 px, moment typographique 84 px max ; rien d'autre dans la bande y 890 à 980 ; jamais en haut à gauche."
  - "Une seule chose à regarder ; marges gauche et droite égales dans les mises en page côte à côte."
  - "Pas d'aller-retour de caméra ; pas de curseur qui hésite."
  - "Aucun décor sans sens, aucune ligne de décor qui traverse une phrase."
  - "Aucune teinte hors charte (ambre réservé à l'attente, rouge réservé à l'accent, ardoise au réparé)."
  - "Pas d'emoji. Pas de back.out élastique sauf la pastille qui naît. Pas de repeat:-1, pas d'animation CSS."
  - "Aucun texte visible qui ne soit pas cité dans les lignes Scene de la séquence (étiquettes d'interface citées comprises)."
  - "Ne jamais animer letterSpacing, top, left, width, height."
---

# Jean Immobilier : frame spec

**Le problème** se joue sur la nuit ardoise : une semaine de calendrier que la caméra longe, chaque jour un objet qui
attend (un rappel, un loyer, un compte rendu), marqué d'une pastille ambre « En attente » ; puis le bien, calme au
centre, et autour de lui trois cartes en attente (annonce, loyer, travaux). **Le pivot** : les pastilles fusionnent en
une seule, « Assez attendu. » sur le noir, la pastille se pince en un point. La lumière s'ouvre depuis ce point sur
**la solution**, sur le papier : le logo Jean Immobilier, l'équipe, les quatre métiers, puis les trois cartes réparées
une à une (la pastille bascule en ✓ ardoise), et la même vue que « autour », toute réparée. **La fin** : le logo et un
seul bouton rouge « Parlons de votre bien », qu'un curseur clique.

Tout ce qui se lit est en JI Inter. Le sous-titre de la voix arrive mot par mot en bas au centre, avec un mot clé par
phrase dans une petite boîte rouge.
