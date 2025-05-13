# Finanšu Trekeris

## Projekta uzdevums

Šis ir vienkāršs personīgo finanšu pārvaldības rīks, kas izstrādāts ar Python programmēšanas valodu un Flask tīmekļa ietvaru. Lietotne ļauj lietotājam pievienot ienākumus vai izdevumus, skatīt kopsavilkumu un izdzēst jebkuru ierakstu. Visi dati tiek glabāti vietējā JSON datnē `data.json`.

Projekta mērķis ir izstrādāt vienkāršu un intuitīvu tīmekļa lietotni, kuru var izmantot personīgai finanšu uzskaitei, kā arī kā mācību piemēru darbam ar Flask, HTML/CSS un datu apstrādi.

## Iekļautie faili un struktūra

Projektā iekļauti trīs galvenie komponenti:

- **Python fails (`main.py`)** – satur visu servera loģiku, tostarp datu apstrādi, saglabāšanu, maršrutēšanu un lietotāja darbību apstrādi.
- **HTML fails (`templates/index.html`)** – nodrošina lietotāja saskarni, izmantojot Jinja2 šablonu motoru.
- **CSS fails (`static/styles.css`)** – satur stilus, kas nodrošina lietotnes vizuālo izskatu.

## Izmantotās Python bibliotēkas

Šajā projektā izmantotas šādas bibliotēkas:

- **Flask** (`Flask==3.0.2`) – tīmekļa ietvars, kas ļauj veidot tīmekļa lietotnes. Flask apstrādā maršrutus, HTTP pieprasījumus un atgriež HTML šablonus.
- **json** – standarta Python bibliotēka, kas tiek izmantota datu saglabāšanai un nolasīšanai no `data.json` faila.
- **datetime** – nodrošina datuma pievienošanu katram ierakstam.
- **os** – pārbauda, vai eksistē datu fails pirms tā atvēršanas.

## Izmantotās datu struktūras

- **Vārdnīca (`dict`)** – katrs finanšu ieraksts tiek attēlots kā vārdnīca ar laukiem `tips`, `kategorija`, `summa` un `datums`.
- **Saraksts (`list`)** – visi ieraksti tiek glabāti sarakstā, ko iespējams apskatīt un manipulēt (pievienot vai dzēst).

Piemērs ierakstam:
```python
{
    "datums": "2025-05-13",
    "tips": "Izdevumi",
    "kategorija": "Ēdiens",
    "summa": 15.50
}
```

## Funkcionalitāte
- **Ierakstu pievienošana** – izvēloties tipu (Ienākumi vai Izdevumi), ievadot kategoriju un summu, tiek izveidots jauns ieraksts.
- **Kopsavilkums** – tiek automātiski aprēķināts kopējais ienākumu, izdevumu un bilances apjoms.
- **Ierakstu dzēšana** – iespējams dzēst jebkuru ierakstu, izmantojot pogu pie katra ieraksta.
- **Datu glabāšana** – visa informācija tiek saglabāta failā `data.json`, kas tiek automātiski atjaunināts pēc katras izmaiņas.

## Lietošanas instrukcija

### 1. Instalēšana

Nepieciešama Python versija 3.12 un Flask bibliotēka. Instalē Flask ar pip:

```
pip install Flask==3.0.2
```

### 2. Projekta palaišana

Palaidiet galveno failu, atveriet pārlūkprogrammu un dodieties uz:

```
http://127.0.0.1:5000/
```

### 3. Saskarnes izmantošana

- Aizpildi formu, lai pievienotu jaunu ierakstu.
- Skaties kopsavilkumu par ienākumiem, izdevumiem un kopējo balansu.
- Spied pogu "Dzēst", lai noņemtu nevēlamu ierakstu.

