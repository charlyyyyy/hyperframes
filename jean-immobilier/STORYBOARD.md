---
format: 1920x1080
duration: 49.80s
message: "Le problème, ce n'est pas votre bien, c'est d'attendre ; chez Jean Immobilier, une équipe proche s'en occupe : vente, location, gestion locative, syndic."
arc: Hook (gag) → Problème → Pivot → Solution → Payoff → CTA
audience: propriétaires vendeurs, bailleurs et copropriétaires (France), clients ou futurs clients de Jean Immobilier
mode: autonomous
captions: disabled
voice: "assets/audio/voix.mp3 (prise brute 43.68 s) ; montage prévu : +0.90 s de silence dans le pivot (coupé à 27.18), puis la phrase de fin « Jean Immobilier. Parlons de votre bien. » à enregistrer (placée à 45.00, temps provisoires)"
direction: "A · La semaine qui attend (choisie d'office : la planche de validation remplace les 3 directions)"
styleframes: "storyboard/planche.png (une image clé par plan, P1 à P27)"
patterns: ../patterns/STORYBOARD-CRAFT.md, ../patterns/PATTERNS.md
---

<!--
VERSION DE VALIDATION. Les temps sont ceux du FILM (montage prévu), pas encore locaux : après validation et montage de
la voix définitive, onsets.py --window recalcule les Word cues locaux de chaque séquence, et les Scene passent en temps
locaux avant de fabriquer les paquets. Avant le pivot (< 27.18) : temps de la prise brute. Après : prise brute + 0.90.
-->

## Video direction

- **Un seul monde par acte** : acte sombre = « la semaine qui attend », un ruban de calendrier (une tuile par jour) posé sur un sol bleu nuit à trame de points, que la caméra longe ; chaque attente est un objet posé sur la tuile de son jour. Acte clair = le même monde passé au papier : le site de Jean Immobilier au centre, puis les trois cartes du problème réparées autour du bien. Fin : carte de fin claire, un seul bouton.
- **Coutures invisibles** : toutes les séquences en `cut`, continuité par un objet-pont ou un seul geste de caméra ; `handoff_out` de N = `handoff_in` de N+1, mot pour mot. Une seule coupe franche voulue : 28.20 (fin du noir du pivot, juste avant « Jean »@28.38, changement d'acte).
- **Texte** : la phrase de la voix en sous-titre en bas au centre (bande y 890 à 980, 62 px), mot par mot ; un mot clé par phrase dans la boîte d'accent [boîte : …] ; 4 pics au trait fin [trait : …] ; 2 moments typographiques centrés (84 px) : « Assez attendu. » (pivot) et « Parlons de votre bien » (le bouton de fin).
- **Une seule chose à regarder** : la caméra isole l'objet de la phrase (une tuile, un téléphone, une carte) ; elle ne montre l'ensemble qu'à « autour » (P10) et à « Vous n'attendez plus » (P24), la rime.
- **Vraies interfaces** : à fournir par l'agence (captures récentes) : le site Jean Immobilier (accueil + menu des 4 métiers), le logo, la couleur de marque, si possible une photo de l'équipe. Les écrans du problème (appel, banque, SMS, mail, PV d'AG) sont des interfaces génériques sobres de téléphone récent, sans vraie marque.
- **Grammaire de mouvement** : gestes de 1 à 6 images (expo.out), dérives linéaires permanentes, la zone 0,3 à 0,9 s réservée à la caméra et au curseur ; les éléments arrivent trop grands et flous puis se posent ; aucune tenue figée ; aucune transition « effet ».
- **Négatifs** : diaporama, écran de veille, objet dédoublé, gros encadré, mot géant, symbole abstrait, compteur qui ne dit rien, curseur qui hésite, logo avant 28 s.

**MONDE**

- Acte 1 (0.00 à 26.20), « la semaine qui attend » : ruban de tuiles-jours (1200 × 1500 u) en y 0 ; stations MARDI (0, 0), JEUDI (2400, 0), LUNDI (4800, 0, « semaine suivante ») ; le téléphone (iPhone récent, 760 u de haut) vit sur la tuile LUNDI ; sous le ruban, la station « le bien » (immeuble au trait, 900 u) en (4800, 2600), entourée de trois cartes : ANNONCE (3700, 2500), LOYER (5900, 2500), TRAVAUX (4800, 3500). Fond #0E1524, trame de points 3 % qui rend la dérive visible, grain 5 %.
- Pivot (26.20 à 28.20) : noir #07090F, la phrase centrée, la pastille d'attente qui se referme en un point.
- Acte 2 (28.20 à 44.70), « papier » : même géométrie, sol #F5F2EC à trame de points 2 %, grain 3 % ; station SITE (0, 0) ; les trois cartes réparées autour du bien en (4800, 2600) aux mêmes positions qu'en acte 1.
- Acte 3 (44.70 à 49.80) : carte de fin papier, logo, un bouton, l'immeuble au trait en fond.
- Couleurs de rôle : encre claire #EEF1F6 (acte 1), encre #18202E (acte 2) ; négatif = ambre #F2A93B, réservé à la pastille d'attente ; accent = couleur de la marque Jean Immobilier (provisoire : vert #1E8A66, clair #CFEBDD), réservé à la boîte, aux traits, au ✓ et au bouton.

**SIGNATURES**

- Mécanisme 1 « la pastille d'attente » : pastille ambre « En attente » + trois points qui pulsent ; elle naît d'un point (0 → 1 en 0,12 s, back.out) collée à l'objet qui attend : 1.10, 3.45, 6.05, 9.30, 19.30, 22.40, 24.80 (7 fois).
- Mécanisme 2 « le tic qui répare » : la même pastille bascule (rotationX 180°, 0,16 s) et devient verte « ✓ <état> » : 36.70, 38.20, 39.70, 42.20, 42.70 (toutes ensemble) (5 fois).
- Registres de texte : sous-titre = mot par mot, flou 6 px → net en 0,08 s ; boîte = s'ouvre de gauche à droite derrière le mot en 0,12 s ; trait = se trace en 0,25 s power3.out ; moment typographique = la phrase arrive ×1,15 floue et se pose.
- Rimes : la vue « le bien et ses trois cartes » (P10, 16.39, toutes en attente) est rejouée à l'identique en P24 (42.60, toutes ✓) ; la tuile-jour de l'ouverture (« MARDI », arrivée depuis la caméra) rime avec le bouton de fin (même arrivée, même ombre).

**PARTITION CAMÉRA** (temps du film) : 0.00 la tuile MARDI arrive de la caméra, dérive x +20 u/s · 2.42 whip → JEUDI (sommet 2.55) · 4.46 whip → LUNDI · 7.84 plongée dans le téléphone (couture au sommet du flou) · 11.31 poussée lente sur la bannière · 12.89 recul hors du téléphone, le noir de l'écran devient le sol · 15.16 recul × 0,45 : le bien et ses 3 cartes · 16.91 cran → ANNONCE · 19.96 cran → LOYER · 22.90 cran → TRAVAUX · 25.64 recul, les pastilles convergent · 26.20 noir · 28.20 coupe franche, le point s'ouvre sur le papier · 30.75 recul sur le menu du site · cran par métier 31.10 / 31.60 / 32.25 / 33.30 · 34.67 cran → carte PRIX · 37.26 cran → LOYER · 39.92 cran → TRAVAUX · 42.42 recul × 0,45 (rime de P10) · 43.70 implosion vers le site · 44.70 carte de fin · 46.90 cran vers le bouton · 49.30 iris.

**VOIX** : `assets/audio/voix-brut-onsets.json` (+0.90 après 27.18). Silences > 0,4 s, chacun écrit comme un plan : 4.23 à 4.68 (whip → LUNDI), 7.58 à 8.11 (plongée dans le téléphone), 8.88 à 9.34 et 10.10 à 10.54 (les sonneries), 11.04 à 11.59 (ça sonne dans le vide), 12.57 à 13.22 (raccroché, recul), 14.96 à 15.35 (recul vers le bien), 16.68 à 17.13 (cran → ANNONCE), 19.73 à 20.20 (cran → LOYER), 22.68 à 23.12 (cran → TRAVAUX), 25.64 à 26.20 (convergence des pastilles), 26.88 à 28.38 (le pivot, 1,5 s), 44.37 à 45.00 (la carte de fin se pose), 47.20 à 49.80 (clic, tenue vivante, iris).

**COUPES** (voix narrative, quota 0 à 4) : 28.20 · avant « Jean » · changement d'acte (noir → papier).

**RYTHME** : douleur ≈ 6 plans / 10 s (événement toutes les 0,3 à 0,6 s) ; solution ≈ 4 plans / 10 s, plus posée (le soulagement se sent).

**SON** (calé sur les gestes) : whoosh-short 0.00, pop 1.10, whoosh-short 2.45, pop 3.45, whoosh-short 4.40, pop 6.05, whoosh 7.80, click 8.30, sonnerie (notification grave, ×2) 9.34 et 10.54, error 11.55, click-soft 12.65, whoosh 15.10, key-press 17.40 à 17.90 (le prix qui roule), pop 18.01, whoosh-short 19.96, typing 21.80 à 22.20, pop 22.40, impact-bass-1 23.72 (le tampon VOTÉ), riser 23.70 → 26.20, impact-bass-2 26.52 (la pastille se referme), silence, whoosh-cinematic 28.20, pop 28.40, click-soft 31.10 / 31.60 / 32.25 / 33.30, chime 36.70, ping 38.20, ping 39.70, chime 42.20, notification (signature, deux tons) 42.70, whoosh 43.70, pop 45.00, click 47.35, sparkle 47.40.

---

## Frame 1 : Mardi, jeudi · 0.00 → 4.46

- scene: La tuile « MARDI » d'un calendrier arrive de la caméra sur le sol bleu nuit ; un téléphone y attend le rappel de l'agence ; whip le long du ruban jusqu'à « JEUDI », où une ligne bancaire attend le loyer
- duration: 4.46s
- transition_in: cut
- status: outline
- src: compositions/frames/01-mardi-jeudi.html
- voiceover: "Mardi, vous attendez le rappel de l'agence. Jeudi, vous attendez le loyer."
- type: hook
- blueprint: camera-journey (Adapt)
- focal: la tuile MARDI et son téléphone, puis la tuile JEUDI et la ligne de loyer
- rules: depth-of-field-blur, coordinate-target-zoom
- world: dark
- handoff_in: aucun (ouverture du film) ; première image = sol bleu nuit #0E1524 à trame de points, la tuile MARDI à ×3, floue 12 px, entrant par le bas droit
- handoff_out: à 4.46 : cam(3600, 0, 1.00, 0, 0) flou 10 px ; caméra en plein whip vers la droite (+5000 u/s) de JEUDI vers LUNDI ; tuiles MARDI et JEUDI sur le ruban, chacune avec sa pastille ambre « En attente » ; aucune phrase ; grain 5 %

Scene 1 (0.00 à 0.62) : P1, « Mardi, »
TEXTE ÉCRAN : « Mardi, »@0.06, [boîte : Mardi] ; synchro.
IMAGE DE DÉPART : handoff_in.
ÉTAPES : 0.00 la tuile MARDI fonce de la caméra (×3 → ×1, flou 12 → 0, 0,25 s expo.out), en-tête « MARDI 14 » ; 0.25 contact, ombre portée qui s'étale ; 0.30 le ruban se prolonge à droite, tuiles vides floues (dans le flou du fond) ; 0.45 l'heure « 9:00 » s'écrit en haut de la tuile.
PISTE CAMÉRA : dérive x +20 u/s, échelle +2 %/s.
COUCHES ET PROFONDEUR : avant-plan bord d'une tuile flou coupé à gauche ; sujet MARDI ; fond ruban et points ; 3 couches.
OBJET-PONT ET VECTEUR : la tuile MARDI reçoit le téléphone en P2.
SON : whoosh-short 0.00.
IMAGE CLÉ : 0.30 : la tuile MARDI qui vient de se poser, encore légèrement floue sur un bord, le ruban qui file à droite.

Scene 2 (0.62 à 2.42) : P2, « vous attendez le rappel de l'agence. »
TEXTE ÉCRAN : vous@0.68 attendez@0.84 le@1.32 rappel@1.40 de@1.72 l'agence@1.80, [boîte : le rappel] ; synchro.
IMAGE DE DÉPART : MARDI posée.
ÉTAPES : 0.70 un téléphone se pose sur la tuile (×1,15 flou → net, 0,12 s) : écran « Agence · rappel prévu 10:00 » ; 1.10 pastille d'attente (signature 1) ; 1.40 les aiguilles de l'horloge de la tuile tournent vite 10:00 → 17:30 (0,8 s) ; 2.20 l'écran du téléphone s'éteint d'un cran (plus rien).
PISTE CAMÉRA : cran ×1,25 sur le téléphone à 0.66 (0,12 s expo.inOut) puis dérive y -10 u/s.
COUCHES ET PROFONDEUR : tuile floue au premier plan bas ; téléphone net ; ruban flou ; pic 3 couches.
OBJET-PONT ET VECTEUR : vecteur : whip vers la droite (0,15 s power2.in) repris à l'entrée de JEUDI.
SON : pop 1.10 (pastille).
IMAGE CLÉ : 1.50 : le téléphone sur la tuile MARDI, « rappel prévu 10:00 », la pastille ambre « En attente », l'horloge à 17:30.

Scene 3 (2.42 à 4.46) : P3, « Jeudi, vous attendez le loyer. »
TEXTE ÉCRAN : Jeudi@2.59 vous@3.15 attendez@3.31 le@3.79 loyer@3.91, [boîte : le loyer] ; synchro.
IMAGE DE DÉPART : sommet du whip, flou 12 px.
ÉTAPES : 2.55 la tuile JEUDI 16 se pose sous le flou ; 2.90 une carte bancaire sobre arrive (×1,15) : « Loyer octobre · 0,00 € reçu » ; 3.45 pastille d'attente ; 3.91 le « 0,00 € » clignote une fois (sur « loyer ») ; 4.25 départ du whip suivant.
PISTE CAMÉRA : whip 2.42 à 2.62 (expo.inOut, flou 12) ; dérive x +20 u/s ; whip 4.25 →.
COUCHES ET PROFONDEUR : tuile MARDI floue qui sort à gauche ; JEUDI nette ; ruban ; 3 couches.
OBJET-PONT ET VECTEUR : vecteur : whip droite, couture au sommet du flou.
SON : whoosh-short 2.45, pop 3.45.
IMAGE CLÉ : 3.60 : la tuile JEUDI, la ligne « Loyer octobre · 0,00 € », la pastille ambre, la tuile MARDI floue sortant à gauche.

## Frame 2 : Lundi, le syndic · 4.46 → 7.84

- scene: Le whip arrive sur « LUNDI », une semaine plus tard ; une boîte mail cherche le compte rendu du syndic, aucun résultat
- duration: 3.38s
- voiceover: "Lundi... vous attendez encore le compte rendu du syndic."
- type: pain_point
- world: dark
- handoff_in: à 0.00 : cam(3600, 0, 1.00, 0, 0) flou 10 px ; caméra en plein whip vers la droite (+5000 u/s) de JEUDI vers LUNDI ; tuiles MARDI et JEUDI sur le ruban, chacune avec sa pastille ambre « En attente » ; aucune phrase ; grain 5 %
- handoff_out: à 3.38 : cam(4800, 0, 1.60, 0, 0) flou 8 px ; caméra en pleine plongée vers l'écran du téléphone (échelle +200 %/s) ; tuile LUNDI, téléphone allumé au centre ; aucune phrase

Scene 4 (4.46 à 5.22) : P4, « Lundi… »
TEXTE ÉCRAN : Lundi@4.68, [boîte : Lundi] ; synchro.
ÉTAPES : 4.55 fin du whip, la tuile LUNDI 20 se pose ; 4.70 au-dessus du ruban, l'étiquette « semaine suivante » glisse ; 4.90 les pastilles de MARDI et JEUDI, floues au loin à gauche, pulsent encore.
PISTE CAMÉRA : whip qui se termine (expo.out) puis dérive x +20 u/s.
OBJET-PONT ET VECTEUR : la tuile LUNDI reçoit le téléphone (le même qu'en P2, qui a glissé avec le ruban).
SON : whoosh-short 4.40.
IMAGE CLÉ : 4.85 : LUNDI 20 au centre, « semaine suivante », deux pastilles ambre floues à gauche.

Scene 5 (5.22 à 7.84) : P5, « vous attendez encore le compte rendu du syndic. »
TEXTE ÉCRAN : vous@5.29 attendez@5.53 encore@6.21 le@6.49 compte@6.61 rendu@6.81 du@7.17 syndic@7.29, [trait : encore] ; synchro.
ÉTAPES : 5.30 le téléphone se pose, appli Mail ; 5.70 la recherche tape « compte rendu AG » (frappe 0,4 s) ; 6.05 pastille d'attente ; 6.60 « Aucun résultat » tombe dans la liste ; 7.30 la dernière ligne « Syndic · Convocation AG · il y a 3 mois » s'allume ; 7.60 le téléphone sonne (vibration 2 px) : départ de la plongée.
PISTE CAMÉRA : cran ×1,3 sur l'écran à 5.25 ; dérive ; plongée 7.60 →.
COUCHES ET PROFONDEUR : tuile floue / téléphone net / ruban ; 3 couches.
OBJET-PONT ET VECTEUR : l'écran du téléphone devient tout le cadre en P6.
SON : typing 5.70 à 6.10, pop 6.05.
IMAGE CLÉ : 6.80 : l'appli Mail, « compte rendu AG » dans la recherche, « Aucun résultat », la pastille ambre.

## Frame 3 : Vous appelez… messagerie pleine · 7.84 → 12.89

- scene: La caméra plonge dans le téléphone ; un pouce appelle l'agence ; ça sonne deux fois dans le vide ; la bannière « Messagerie pleine » tombe ; on raccroche, l'écran s'éteint
- duration: 5.05s
- voiceover: "Vous appelez... Messagerie pleine."
- type: hook
- world: dark
- handoff_in: à 0.00 : cam(4800, 0, 1.60, 0, 0) flou 8 px ; caméra en pleine plongée vers l'écran du téléphone (échelle +200 %/s) ; tuile LUNDI, téléphone allumé au centre ; aucune phrase
- handoff_out: à 5.05 : l'écran éteint du téléphone remplit le cadre (noir bleuté #0E1524, reflet léger), caméra en recul (échelle -60 %/s), flou 6 px ; aucune phrase

Scene 6 (7.84 à 9.11) : P6, « Vous appelez… »
TEXTE ÉCRAN : Vous@8.11 appelez@8.43, [boîte : appelez] ; synchro.
ÉTAPES : 7.90 fin de plongée : l'écran d'appel plein cadre, contact « Agence » ; 8.20 un pouce (ou le curseur oversized) arrive d'en bas en courbe ; 8.30 tap sur le bouton vert, onde ; 8.45 « Appel en cours… » et le chrono 00:00 démarre.
PISTE CAMÉRA : plongée qui se pose (expo.out) puis dérive échelle +2 %/s.
OBJET-PONT ET VECTEUR : l'écran d'appel reste.
SON : whoosh 7.80, click 8.30.
IMAGE CLÉ : 8.32 : écran d'appel « Agence », le pouce sur le bouton vert, l'onde du tap.

Scene 7 (9.11 à 11.31) : P7, les deux sonneries (sans mot)
TEXTE ÉCRAN : aucun texte (les sonneries portent le plan).
ÉTAPES : 9.34 première sonnerie : anneau d'onde depuis l'avatar ; 9.30 pastille d'attente sous le nom ; 10.54 deuxième sonnerie, anneau ; chrono qui roule 00:04 → 00:18 en continu.
PISTE CAMÉRA : poussée lente linéaire ×1,0 → ×1,08.
COUCHES ET PROFONDEUR : bord du téléphone flou en avant-plan ; écran net ; fond nuit ; 3 couches.
OBJET-PONT ET VECTEUR : l'écran d'appel reçoit la bannière en P8.
SON : sonnerie 9.34, sonnerie 10.54 (calées sur la prise).
IMAGE CLÉ : 10.60 : l'écran d'appel, l'anneau d'onde au maximum, le chrono à 00:12, la pastille ambre.

Scene 8 (11.31 à 12.89) : P8, « Messagerie pleine. »
TEXTE ÉCRAN : Messagerie@11.59 pleine@12.39, [trait : pleine] ; synchro.
ÉTAPES : 11.50 la bannière « Messagerie pleine » TOMBE du haut (y -300 → 0, 0,13 s power2.in, rebond 14 px) ; 11.80 le chrono s'arrête ; 12.40 sur « pleine » l'avatar de l'agence grise ; 12.60 tap rouge, l'écran s'éteint (0,1 s) : départ du recul.
PISTE CAMÉRA : petit coup de caméra au contact (y +8 px, 0,08 s) ; dérive ; recul 12.70 →.
OBJET-PONT ET VECTEUR : l'écran éteint devient le sol nuit du plan suivant.
SON : error 11.55, click-soft 12.65.
IMAGE CLÉ : 11.70 : la bannière « Messagerie pleine » qui vient de tomber sur l'écran d'appel, le chrono figé à 00:21.

## Frame 4 : Le problème, c'est autour · 12.89 → 16.91

- scene: Recul hors du téléphone éteint : au centre, votre bien (un immeuble au trait, calme) ; recul encore, trois cartes en attente entrent autour de lui
- duration: 4.02s
- voiceover: "Le problème, ce n'est pas votre bien. C'est tout ce qu'il y a autour."
- type: pain_point
- world: dark
- handoff_in: à 0.00 : l'écran éteint du téléphone remplit le cadre (noir bleuté #0E1524, reflet léger), caméra en recul (échelle -60 %/s), flou 6 px ; aucune phrase
- handoff_out: à 4.02 : cam(4100, 2550, 0.80, 0, 0) flou 10 px ; caméra en plein cran vers la carte ANNONCE (gauche) ; le bien au centre-droite, cartes LOYER et TRAVAUX floues ; aucune phrase

Scene 9 (12.89 à 15.16) : P9, « Le problème, ce n'est pas votre bien. »
TEXTE ÉCRAN : Le@13.22 problème@13.42 ce@14.02 n'est@14.22 pas@14.42 votre@14.58 bien@14.91, [boîte : votre bien] ; synchro.
ÉTAPES : 13.00 dans le noir, le trait de l'immeuble se dessine (draw SVG 0,6 s) ; 13.60 les fenêtres s'allument une à une (0,05 s d'écart) ; 14.40 un petit arbre et le trottoir ; 14.91 une lueur chaude derrière le bien (le bien va bien).
PISTE CAMÉRA : recul expo.out jusqu'à cam(4800, 2600, 1.00) ; dérive x -15 u/s.
OBJET-PONT ET VECTEUR : le bien reste au centre en P10.
SON : (rien, la voix seule).
IMAGE CLÉ : 14.95 : l'immeuble au trait, fenêtres chaudes, seul au centre du noir.

Scene 10 (15.16 à 16.91) : P10, « C'est tout ce qu'il y a autour. »
TEXTE ÉCRAN : C'est@15.35 tout@15.59 ce@15.79 qu'il@15.95 y@16.11 a@16.23 autour@16.39, [trait : autour] ; synchro.
ÉTAPES : 15.20 recul ×0,45 ; 15.50 / 15.75 / 16.00 trois cartes entrent depuis les bords (×3, flou 10, 0,2 s) et se posent autour : ANNONCE à gauche, LOYER à droite, TRAVAUX en bas, chacune avec sa pastille ambre ; 16.39 sur « autour », un fin cercle pointillé relie les trois cartes autour du bien.
PISTE CAMÉRA : recul 15.16 à 15.60 (power3.out) puis dérive en rotation lente 1°/s.
COUCHES ET PROFONDEUR : cartes au premier plan, bien au centre, sol ; 3 couches.
OBJET-PONT ET VECTEUR : la carte ANNONCE devient le sujet de P11 (cran).
SON : whoosh 15.10.
IMAGE CLÉ : 16.45 : le bien au centre, trois cartes ambre autour (Annonce, Loyer, Travaux), le cercle pointillé. (RIME avec P24.)

## Frame 5 : Le prix, l'annonce · 16.91 → 19.96

- scene: Cran sur la carte ANNONCE : le prix roule comme une machine à sous et tombe au hasard ; puis l'annonce s'éteint, en ligne depuis des semaines
- duration: 3.05s
- voiceover: "Un prix fixé au hasard... et une annonce qui dort."
- type: pain_point
- world: dark
- handoff_in: à 0.00 : cam(4100, 2550, 0.80, 0, 0) flou 10 px ; caméra en plein cran vers la carte ANNONCE (gauche) ; le bien au centre-droite, cartes LOYER et TRAVAUX floues ; aucune phrase
- handoff_out: à 3.05 : cam(5300, 2550, 0.80, 0, 0) flou 10 px ; caméra en plein cran vers la carte LOYER (droite) ; carte ANNONCE éteinte à gauche ; aucune phrase

Scene 11 (16.91 à 18.60) : P11, « Un prix fixé au hasard… »
TEXTE ÉCRAN : Un@17.13 prix@17.29 fixé@17.45 au@17.81 hasard@18.01, [boîte : au hasard] ; synchro.
ÉTAPES : 17.00 la carte ANNONCE au centre : photo de l'appartement, « Prix : — € » ; 17.30 les chiffres roulent comme des rouleaux (0,7 s) ; 18.01 sur « hasard », les rouleaux s'arrêtent net, chacun à une valeur différente, avec un petit à-coup ; le prix est barré-corrigé une fois (−10 000 €).
PISTE CAMÉRA : cran 16.91 à 17.05 (expo.inOut) puis dérive x +15 u/s.
OBJET-PONT ET VECTEUR : la même carte reste pour P12.
SON : key-press 17.40 à 17.90, pop 18.01.
IMAGE CLÉ : 17.70 : la carte annonce, les rouleaux du prix en plein mouvement (flou vertical), « au hasard ».

Scene 12 (18.60 à 19.96) : P12, « et une annonce qui dort. »
TEXTE ÉCRAN : et@18.77 une@18.97 annonce@19.05 qui@19.49 dort@19.68, [trait : dort] ; synchro.
ÉTAPES : 18.80 « En ligne depuis » + le nombre roule 1 → 94 jours (0,5 s) ; 19.30 pastille d'attente ; 19.68 sur « dort », la photo de l'annonce s'assombrit (0,3 s) et la carte s'incline de 2° (elle s'endort).
PISTE CAMÉRA : dérive ; cran → LOYER à 19.90.
OBJET-PONT ET VECTEUR : vecteur : cran vers la droite.
SON : (aucun).
IMAGE CLÉ : 19.75 : la carte annonce assombrie, « En ligne depuis 94 jours », la pastille ambre.

## Frame 6 : Le loyer, la relance · 19.96 → 22.90

- scene: Cran sur la carte LOYER : le loyer n'est pas arrivé, les jours de retard s'accumulent ; un SMS de relance est tapé à la main
- duration: 2.94s
- voiceover: "Un loyer en retard... et c'est à vous de relancer."
- type: pain_point
- world: dark
- handoff_in: à 0.00 : cam(5300, 2550, 0.80, 0, 0) flou 10 px ; caméra en plein cran vers la carte LOYER (droite) ; carte ANNONCE éteinte à gauche ; aucune phrase
- handoff_out: à 2.94 : cam(4800, 3200, 0.80, 0, 0) flou 10 px ; caméra en plein cran vers le bas, vers la carte TRAVAUX ; aucune phrase

Scene 13 (19.96 à 21.32) : P13, « Un loyer en retard… »
TEXTE ÉCRAN : Un@20.20 loyer@20.28 en@20.76 retard@20.88, [boîte : en retard] ; synchro.
ÉTAPES : 20.05 la carte LOYER : « Loyer octobre · attendu le 5 » ; 20.40 un petit calendrier dans la carte : les cases 5, 6, 7… 12 se cochent en rouge-ambre une à une (0,05 s) ; 20.88 « retard : 7 jours » s'imprime.
PISTE CAMÉRA : cran 19.96 à 20.10 puis dérive y -10 u/s.
SON : whoosh-short 19.96.
IMAGE CLÉ : 20.95 : carte loyer, le petit calendrier rempli jusqu'au 12, « retard : 7 jours ».

Scene 14 (21.32 à 22.90) : P14, « et c'est à vous de relancer. »
TEXTE ÉCRAN : et@21.47 c'est@21.75 à@21.87 vous@22.03 de@22.17 relancer@22.27, [boîte : à vous] ; synchro.
ÉTAPES : 21.40 une bulle SMS sort de la carte ; 21.80 frappe « Bonjour, petit rappel pour le loyer… » (0,4 s) ; 22.27 sur « relancer », la bulle part (envoyée, filé vers le haut 0,1 s) ; 22.40 pastille d'attente sous « Distribué ».
PISTE CAMÉRA : dérive ; cran vers le bas 22.80 →.
SON : typing 21.80 à 22.20, pop 22.40.
IMAGE CLÉ : 22.30 : la bulle SMS envoyée qui file, « Distribué », la carte loyer.

## Frame 7 : Les travaux · 22.90 → 25.92

- scene: Cran sur la carte TRAVAUX : un tampon « VOTÉ » s'abat sur la résolution du PV d'AG ; puis la ligne « Suivi : — » reste vide ; recul, les trois pastilles ambre se regroupent
- duration: 3.02s
- voiceover: "Des travaux votés... et personne pour les suivre."
- type: pain_point
- world: dark
- handoff_in: à 0.00 : cam(4800, 3200, 0.80, 0, 0) flou 10 px ; caméra en plein cran vers le bas, vers la carte TRAVAUX ; aucune phrase
- handoff_out: à 3.02 : cam(4800, 2800, 0.45, 0, 0) flou 4 px ; recul en fin de course ; le bien et ses 3 cartes, les 3 pastilles ambre en vol vers le centre (à mi-chemin) ; aucune phrase

Scene 15 (22.90 à 24.29) : P15, « Des travaux votés… »
TEXTE ÉCRAN : Des@23.12 travaux@23.24 votés@23.72, [boîte : votés] ; synchro.
ÉTAPES : 23.00 la carte TRAVAUX : « PV d'AG · Résolution 7 : ravalement de façade » ; 23.55 un tampon arrive de la caméra (×4, flou) ; 23.72 contact sur « votés » : « VOTÉ » imprimé, coup de caméra ; 24.00 mini-échafaudage au trait sur l'immeuble miniature de la carte.
PISTE CAMÉRA : cran 22.90 à 23.05 ; coup y +10 px à 23.72.
SON : impact-bass-1 23.72 ; riser 23.70 → 26.20.
IMAGE CLÉ : 23.74 : le tampon « VOTÉ » au contact sur la résolution, encore flou de vitesse.

Scene 16 (24.29 à 25.92) : P16, « et personne pour les suivre. »
TEXTE ÉCRAN : et@24.46 personne@24.70 pour@25.06 les@25.26 suivre@25.42, [trait : personne] ; synchro.
ÉTAPES : 24.50 ligne « Suivi des travaux · Responsable : — » ; 24.70 un rond d'avatar vide clignote ; 24.80 pastille d'attente ; 25.40 l'échafaudage reste figé, une feuille de calendrier tombe derrière ; 25.64 recul, les trois pastilles quittent leurs cartes vers le centre.
PISTE CAMÉRA : dérive ; recul ×0,45 25.64 → (power3.out).
OBJET-PONT ET VECTEUR : les trois pastilles convergent : elles deviennent UNE pastille en P17.
SON : (riser continue).
IMAGE CLÉ : 24.90 : « Responsable : — », l'avatar vide, la pastille ambre.

## Frame 8 : Assez attendu · 25.92 → 28.20

- scene: Les pastilles fusionnent en une seule au centre ; le monde s'éteint ; « Assez attendu. » ; la pastille se referme en un point
- duration: 2.28s
- voiceover: "Assez attendu."
- type: pivot
- world: dark
- handoff_in: à 0.00 : cam(4800, 2800, 0.45, 0, 0) flou 4 px ; recul en fin de course ; le bien et ses 3 cartes, les 3 pastilles ambre en vol vers le centre (à mi-chemin) ; aucune phrase
- handoff_out: aucun raccord de caméra (coupe franche voulue à 2.28) ; raccord de position seulement : un point lumineux de 12 px au centre exact du cadre (960, 540)

Scene 17 (25.92 à 26.20) : P17, fusion
ÉTAPES : 25.95 les trois pastilles se rejoignent au centre (aspiration 0,16 s power3.in) : une seule pastille ×1,4 ; 26.05 le monde (cartes, bien) s'éteint au noir #07090F (0,15 s).
SON : riser (fin).
IMAGE CLÉ : 26.05 : une seule pastille ambre au centre, le monde qui s'éteint derrière.

Scene 18 (26.20 à 28.20) : P18, « Assez attendu. » + silence
TEXTE ÉCRAN : moment typographique centré, 84 px : « Assez attendu. » (Assez@26.20, attendu@26.52) ; au-dessus, la pastille.
ÉTAPES : 26.20 la phrase arrive ×1,15 floue et se pose ; 26.52 sur « attendu », les trois points de la pastille s'arrêtent net, la pastille se referme en un point (0,12 s power3.in) ; 27.00 la phrase se retire ; 27.20 à 28.20 le point respire seul dans le noir (1,5 s de silence de la voix).
PISTE CAMÉRA : poussée lente linéaire ×1,0 → ×1,05.
SON : impact-bass-2 26.52, puis silence.
IMAGE CLÉ : 26.70 : « Assez attendu. » centré sur le noir, la pastille ambre qui se pince en point au-dessus.

## Frame 9 : Jean Immobilier · 28.20 → 30.75

- scene: Coupe franche : le point s'ouvre en lumière sur le papier ; le logo Jean Immobilier se pose, puis le vrai site arrive dans sa fenêtre ; une épingle de carte « près de chez vous »
- duration: 2.55s
- voiceover: "Jean Immobilier, c'est une équipe près de chez vous,"
- type: payoff
- world: light
- handoff_in: aucun raccord de caméra (coupe franche voulue à 0.00) ; raccord de position seulement : un point lumineux de 12 px au centre exact du cadre (960, 540)
- handoff_out: à 2.55 : cam(0, 0, 1.00, 0, 0) flou 4 px ; caméra en début de recul (échelle -40 %/s) ; le site Jean Immobilier dans sa fenêtre au centre, logo en haut à gauche de la fenêtre ; aucune phrase

Scene 19 (28.20 à 30.75) : P19, « Jean Immobilier, c'est une équipe près de chez vous, »
TEXTE ÉCRAN : Jean@28.38 Immobilier@28.54 c'est@29.34 une@29.54 équipe@29.74 près@30.06 de@30.25 chez@30.44 vous@30.57, [boîte : près de chez vous] ; synchro.
ÉTAPES : 28.20 le point s'ouvre en cercle de papier qui remplit le cadre (0,25 s expo.out) ; 28.38 le logo se pose (×1,15 flou → net) ; 28.90 le logo glisse en haut à gauche et devient l'en-tête de la fenêtre du site, qui se déploie (morph 0,25 s) ; 29.74 sur « équipe », la photo d'équipe du site s'allume ; 30.06 une épingle tombe sur une mini-carte du quartier (rebond).
PISTE CAMÉRA : dérive échelle +2 %/s.
OBJET-PONT ET VECTEUR : le logo devient l'en-tête du site.
SON : whoosh-cinematic 28.20, pop 28.40, pop 30.10.
IMAGE CLÉ : 29.90 : la fenêtre du site Jean Immobilier sur le papier, l'en-tête au logo, la photo d'équipe, l'épingle qui tombe.

## Frame 10 : Les quatre métiers · 30.75 → 34.67

- scene: Recul sur le menu du site : Vente, Location, Gestion locative, Syndic s'allument un à un sur leurs mots ; cran final sur la carte du prix, qui sort du site
- duration: 3.92s
- voiceover: "pour vendre, louer, gérer votre bien, et administrer votre immeuble."
- type: demo
- world: light
- handoff_in: à 0.00 : cam(0, 0, 1.00, 0, 0) flou 4 px ; caméra en début de recul (échelle -40 %/s) ; le site Jean Immobilier dans sa fenêtre au centre, logo en haut à gauche de la fenêtre ; aucune phrase
- handoff_out: à 3.92 : cam(4100, 2550, 0.80, 0, 0) flou 10 px ; caméra en plein cran vers la carte PRIX (gauche du bien), papier ; aucune phrase

Scene 20 (30.75 à 34.67) : P20, « pour vendre, louer, gérer votre bien, et administrer votre immeuble. »
TEXTE ÉCRAN : pour@30.88 vendre@31.12 louer@31.64 gérer@32.28 votre@32.56 bien@32.88 et@33.16 administrer@33.32 votre@33.92 immeuble@34.16, [boîte : vendre, louer, gérer, administrer — la boîte saute de mot en mot] ; synchro.
ÉTAPES : le menu du site en 4 grandes tuiles côte à côte, marges égales ; chaque tuile se soulève et prend l'accent sur son verbe : 31.05 VENTE (la photo d'un appartement), 31.55 LOCATION (une clé), 32.20 GESTION LOCATIVE (un bail), 33.25 SYNDIC (l'immeuble entier) ; 34.40 la tuile VENTE se détache et file vers le monde des cartes (cran).
PISTE CAMÉRA : recul 30.75 à 31.05 ; cran latéral léger sur chaque tuile 31.10 / 31.60 / 32.25 / 33.30 ; cran 34.45 → carte PRIX.
COUCHES ET PROFONDEUR : bord flou de la fenêtre du site au premier plan ; tuiles nettes ; papier ; 3 couches.
OBJET-PONT ET VECTEUR : la tuile VENTE devient la carte PRIX réparée.
SON : click-soft 31.10, 31.60, 32.25, 33.30.
IMAGE CLÉ : 32.30 : les 4 tuiles du site (Vente, Location, Gestion locative, Syndic), la 3e soulevée à l'accent.

## Frame 11 : Le juste prix · 34.67 → 37.26

- scene: La carte PRIX, réparée : la valeur roule et se pose juste, d'un seul geste ; la pastille bascule en ✓
- duration: 2.59s
- voiceover: "Le juste prix, dès la première estimation."
- type: payoff
- world: light
- handoff_in: à 0.00 : cam(4100, 2550, 0.80, 0, 0) flou 10 px ; caméra en plein cran vers la carte PRIX (gauche du bien), papier ; aucune phrase
- handoff_out: à 2.59 : cam(5300, 2550, 0.80, 0, 0) flou 10 px ; caméra en plein cran vers la carte LOYER (droite), papier ; carte PRIX ✓ à gauche ; aucune phrase

Scene 21 (34.67 à 37.26) : P21, « Le juste prix, dès la première estimation. »
TEXTE ÉCRAN : Le@34.84 juste@34.96 prix@35.52 dès@35.84 la@36.08 première@36.28 estimation@36.52, [boîte : le juste prix] ; synchro.
ÉTAPES : 34.80 la carte (même gabarit qu'en P11, sur papier) ; 35.10 les rouleaux tournent puis s'arrêtent ENSEMBLE, alignés (rime inversée de P11) ; 35.60 une fine règle de fourchette s'imprime sous le prix ; 36.10 « Estimation · 1re visite » ; 36.70 tic qui répare : la pastille devient « ✓ Estimé ».
PISTE CAMÉRA : cran 34.67 à 34.80 ; dérive x +15 u/s ; cran → LOYER 37.15.
SON : key-press 35.10 à 35.50, chime 36.70.
IMAGE CLÉ : 36.75 : la carte prix, rouleaux alignés, la pastille verte « ✓ Estimé ».

## Frame 12 : Les loyers suivis · 37.26 → 39.92

- scene: La carte LOYER, réparée : le virement arrive ; la relance part toute seule, signée Jean Immobilier
- duration: 2.66s
- voiceover: "Les loyers suivis, les relances faites pour vous."
- type: payoff
- world: light
- handoff_in: à 0.00 : cam(5300, 2550, 0.80, 0, 0) flou 10 px ; caméra en plein cran vers la carte LOYER (droite), papier ; carte PRIX ✓ à gauche ; aucune phrase
- handoff_out: à 2.66 : cam(4800, 3200, 0.80, 0, 0) flou 10 px ; caméra en plein cran vers le bas, vers la carte TRAVAUX, papier ; aucune phrase

Scene 22 (37.26 à 39.92) : P22, « Les loyers suivis, les relances faites pour vous. »
TEXTE ÉCRAN : Les@37.42 loyers@37.54 suivis@38.06 les@38.54 relances@38.74 faites@39.18 pour@39.54 vous@39.71, [boîte : pour vous] ; synchro.
ÉTAPES : 37.40 carte LOYER, le petit calendrier ; 37.80 « Virement reçu » glisse dans la carte ; 38.20 tic : « ✓ Payé » ; 38.70 la bulle SMS de relance part toute seule, avatar « Jean Immobilier » ; 39.70 tic : « ✓ Relancé ».
PISTE CAMÉRA : cran ; dérive ; cran vers le bas 39.80.
SON : ping 38.20, ping 39.70.
IMAGE CLÉ : 38.80 : la carte loyer « ✓ Payé », la bulle de relance signée Jean Immobilier qui part.

## Frame 13 : Les travaux menés · 39.92 → 42.42

- scene: La carte TRAVAUX, réparée : le tampon VOTÉ, puis une barre de chantier qui court jusqu'au bout ; l'échafaudage tombe, la façade est neuve
- duration: 2.50s
- voiceover: "Les travaux votés, puis menés jusqu'au bout."
- type: payoff
- world: light
- handoff_in: à 0.00 : cam(4800, 3200, 0.80, 0, 0) flou 10 px ; caméra en plein cran vers le bas, vers la carte TRAVAUX, papier ; aucune phrase
- handoff_out: à 2.50 : cam(4800, 2800, 0.45, 0, 0) flou 6 px ; caméra en plein recul (power3.out) ; le bien et ses 3 cartes, papier ; aucune phrase

Scene 23 (39.92 à 42.42) : P23, « Les travaux votés, puis menés jusqu'au bout. »
TEXTE ÉCRAN : Les@40.07 travaux@40.27 votés@40.67 puis@41.15 menés@41.39 jusqu'au@41.87 bout@42.18, [trait : jusqu'au bout] ; synchro.
ÉTAPES : 40.10 la carte (gabarit P15), « Responsable : » + avatar de l'agence ; 40.60 le tampon VOTÉ se pose ; 41.15 une barre de chantier part de 0 % ; 41.40 → 42.18 elle court jusqu'à 100 % pile sur « bout » (verbe joué) ; 42.20 tic « ✓ Terminé », l'échafaudage tombe de la façade miniature.
PISTE CAMÉRA : cran ; dérive ; recul 42.30 →.
SON : impact léger 40.60, chime 42.20.
IMAGE CLÉ : 42.10 : la barre de chantier presque pleine, la façade neuve, avatar Jean Immobilier en responsable.

## Frame 14 : Vous n'attendez plus · 42.42 → 44.70

- scene: Recul : le bien et ses trois cartes, comme en P10, mais toutes vertes ; puis tout se rassemble dans la fenêtre du site
- duration: 2.28s
- voiceover: "Vous n'attendez plus. On s'en occupe."
- type: payoff
- world: light
- handoff_in: à 0.00 : cam(4800, 2800, 0.45, 0, 0) flou 6 px ; caméra en plein recul (power3.out) ; le bien et ses 3 cartes, papier ; aucune phrase
- handoff_out: à 2.28 : cam(4800, 2600, 0.20, 0, 0) flou 12 px ; implosion en fin de course : bien et cartes réduits à un point au centre ; aucune phrase

Scene 24 (42.42 à 43.56) : P24, « Vous n'attendez plus. »
TEXTE ÉCRAN : Vous@42.60 n'attendez@42.76 plus@43.33, [trait : plus] ; synchro.
ÉTAPES : 42.60 même cadrage que P10 (rime) ; 42.70 les trois pastilles basculent en même temps en ✓ verts ; 43.00 le cercle pointillé devient un cercle plein vert ; 43.33 les fenêtres du bien clignent une fois.
PISTE CAMÉRA : fin du recul ; rotation lente 1°/s (comme P10).
SON : notification (signature, deux tons) 42.70.
IMAGE CLÉ : 42.80 : le bien au centre, les trois cartes ✓ vertes autour, le cercle plein. (RIME avec P10.)

Scene 25 (43.56 à 44.70) : P25, « On s'en occupe. »
TEXTE ÉCRAN : On@43.73 s'en@43.97 occupe@44.17, [boîte : On s'en occupe] ; synchro.
ÉTAPES : 43.70 les trois cartes sont aspirées vers le bien (0,16 s power3.in) ; 43.95 le bien et les cartes implosent en un point (0,6 s power3.in).
PISTE CAMÉRA : implosion.
SON : whoosh 43.70.
IMAGE CLÉ : 43.90 : les trois cartes en vol vers le bien, traînées.

## Frame 15 : Parlons de votre bien · 44.70 → 49.80

- scene: Le point s'ouvre sur la carte de fin : logo, l'immeuble au trait, un seul bouton « Parlons de votre bien » ; un curseur arrive en courbe et clique ; tenue vivante, iris
- duration: 5.10s
- voiceover: "Jean Immobilier. Parlons de votre bien." (À ENREGISTRER : absente de la prise actuelle)
- type: cta
- world: light
- handoff_in: à 0.00 : cam(4800, 2600, 0.20, 0, 0) flou 12 px ; implosion en fin de course : bien et cartes réduits à un point au centre ; aucune phrase
- handoff_out: aucun (fin du film, iris au noir à 5.10)

Scene 26 (44.70 à 47.40) : P26, « Jean Immobilier. Parlons de votre bien. »
TEXTE ÉCRAN : le logo (Jean@45.00) ; le bouton porte « Parlons de votre bien » (Parlons@46.15 de@46.50 votre@46.62 bien@46.85, temps provisoires) ; le sous-titre se tait (le bouton est le texte) ; moment typographique.
ÉTAPES : 44.75 le point explose en la carte de fin (0,3 s) : l'immeuble au trait en fond, à 20 % ; 45.00 le logo se pose ; 46.00 le bouton arrive de la caméra (même arrivée que la tuile MARDI, rime) ; 46.90 un curseur entre par le bas droit, une seule courbe 0,45 s power3.out ; 47.35 clic direct : pression ×0,85, le bouton passe clair → blanc → accent, il se remplit, onde.
PISTE CAMÉRA : cran ×1,1 vers le bouton 46.90.
SON : pop 45.00, click 47.35, sparkle 47.40.
IMAGE CLÉ : 47.36 : la carte de fin, logo, le bouton accent « Parlons de votre bien » qui se remplit sous le curseur, l'onde.

Scene 27 (47.40 à 49.80) : P27, tenue vivante (sans voix)
ÉTAPES : 47.60 sous le bouton, l'adresse du site s'écrit (à fournir) ; 47.60 à 49.30 les fenêtres de l'immeuble s'allument une à une, dérive lente ; 49.30 iris au noir (0,5 s).
PISTE CAMÉRA : dérive échelle +2 %/s.
SON : la musique finit.
IMAGE CLÉ : 48.50 : la carte de fin, bouton rempli, l'immeuble qui s'allume, l'adresse du site.
