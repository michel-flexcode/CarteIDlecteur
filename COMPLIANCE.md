# COMPLIANCE – CARTEIDLECTEUR

## 1. Objet du logiciel

`CARTEIDLECTEUR` est un logiciel local permettant la **lecture des données d’identité visibles**
d’une carte d’identité électronique belge (eID), via un lecteur PC/SC standard.

Le logiciel est conçu pour :
- fonctionner **hors ligne**
- ne réaliser **aucune communication réseau**
- ne lire que des données **librement accessibles sans PIN**

---

## 2. Données traitées

### 2.1 Données lues (niveau public)

Les données suivantes peuvent être lues sans authentification, conformément
aux spécifications officielles de la carte eID belge :

- Nom
- Prénom(s)
- Date de naissance
- Sexe
- Nationalité
- Numéro de carte
- Dates de validité
- Numéro de registre national (*techniquement accessible*)

Ces données correspondent strictement à celles **visibles sur la carte physique**.

Aucune donnée biométrique ni clé cryptographique n’est accessible.

---

### 2.2 Données explicitement NON lues

Le logiciel **n’accède pas** à :

- certificats d’authentification
- certificats de signature
- clés privées
- fonctions de signature
- données protégées nécessitant un PIN
- journaux internes de la carte

---

## 3. Base légale (RGPD)

Le traitement repose sur :

### Article 6(1)(b) – Exécution d’un service
OU  
### Article 6(1)(f) – Intérêt légitime

Le traitement est :
- **ponctuel**
- **initié par l’utilisateur** (insertion volontaire de la carte)
- **proportionné**
- **local uniquement**

Aucune conservation automatique n’est effectuée.

---

## 4. Consentement utilisateur

Le consentement est matérialisé par :
- l’insertion volontaire de la carte eID
- le lancement manuel du programme

Le logiciel ne peut fonctionner :
- sans lecteur
- sans carte
- sans action explicite de l’utilisateur

---

## 5. Sécurité et confidentialité

### 5.1 Isolation système

Le programme est exécuté :
- sans accès réseau
- dans un environnement Linux isolé (namespace réseau)
- sans élévation de privilèges

Toute tentative de communication réseau est :
- détectée
- bloquée
- consignée

---

### 5.2 Absence de transmission

- Aucune donnée n’est transmise à un tiers
- Aucun service cloud n’est utilisé
- Aucune API externe n’est appelée

---

## 6. Conservation des données

Par défaut :
- aucune donnée n’est stockée
- aucune écriture disque n’est effectuée

Toute conservation éventuelle relève de l’intégrateur final,
sous sa propre responsabilité légale.

---

## 7. Équivalence carte papier

La lecture électronique effectuée par `CARTEIDLECTEUR` est juridiquement équivalente à :
> la lecture visuelle d’une carte d’identité physique présentée volontairement.

Aucune donnée supplémentaire n’est exposée.

---

## 8. Conformité réglementaire

Le logiciel est conforme aux principes suivants :

- RGPD – minimisation des données
- RGPD – limitation de la finalité
- RGPD – sécurité par conception (privacy by design)
- Modèle de sécurité officiel eID belge

---

## 9. Responsabilité

`CARTEIDLECTEUR` fournit un outil technique.
L’usage final, la finalité et la conservation des données
relèvent de la responsabilité de l’exploitant.

---

## 10. Auditabilité

Le projet fournit :
- documentation d’architecture
- documentation sécurité
- séparation claire OS / application
- absence de dépendance réseau

Le comportement est **audit-friendly** et traçable.

---

## 11. Conclusion

`CARTEIDLECTEUR` respecte :
- les limites techniques de la carte eID
- le cadre légal belge
- les exigences RGPD
- les bonnes pratiques de sécurité

Aucune action intrusive ou dissimulée n’est réalisée.
