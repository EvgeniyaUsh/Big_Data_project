import pandas as pd

diction_with_address = {
    'Quality Suites Intercontinental Airport West, Vantage Parkway East, Aldine North, Harris County, Texas, 77032, United States of America': (
        29.9405331, -95.3628596),
    'Staybridge Suites Houston NW - Willowbrook, Schaffer Lane, Willowbrook, Kohrville, Harris County, Texas, 77070, United States of America': (
        29.9707128, -95.5588782),
    "Mimi's Hotel Soho, Bateman Street, Soho, City of Westminster, London, Greater London, England, W1D 3AJ, UK": (
        51.5140033, -0.132014576643272),
    "L'Àtrium, 656, Gran Via de les Corts Catalanes, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08003, España": (
        41.3909273, 2.1706985),
    'Galileo, 9, Corso Europa, Verziere, Municipio 1, Milano, MI, LOM, 20121, Italia': (45.4642157, 9.19614),
    '3, Rue de Boulainvilliers, Muette, 16e, Paris, Île-de-France, France métropolitaine, 75015, France': (
        48.8515992, 2.2777406),
    '19, Sydney Street, Chelsea, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW3 4, UK': (
        51.4910246, -0.1717918),
    'Diffusione, 39, Via Luigi Settembrini, Centrale, Municipio 2, Milano, MI, LOM, 20124, Italia': (
        45.4838331, 9.2078545),
    "Duff Miller, 59, Queen's Gate, Brompton, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW7 5QL, UK": (
        51.4959943, -0.179588564284627),
    "DoubleTree by Hilton Hotel London - Kensington, 100, Queen's Gate, Brompton, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW7 5AG, UK": (
        51.49249385, -0.178725560438256),
    'Hotel Sansi, 1-3, Avinguda de Pearson, Pedralbes, les Corts, Barcelona, BCN, CAT, 08034, España': (
        41.39348905, 2.11158885763118),
    "Kube Hotel, 5, Passage Ruelle, La Goutte d'Or, Goutte-d'Or, 18e, Paris, Île-de-France, France métropolitaine, 75018, France": (
        48.8865976, 2.358851),
    'Baglioni, Hyde Park Gate, South Kensington, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW7 5ED, UK': (
        51.5016135, -0.1844228),
    'Contessa Jolanda Residence, Via Antonino Giuffrè, Montalbino, Milano, MI, LOM, 20124, Italia': (
        45.49871235, 9.19022028966535),
    'Starhotels Ritz, 40, Via Lazzaro Spallanzani, Zona Buenos Aires, Municipio 3, Milano, MI, LOM, 20129, Italia': (
        45.4779514, 9.209435),
    'Hampshire, 17, Amstelstraat, Grachtengordel, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1017 DA, Nederland': (
        52.3662969, 4.8984498),
    'Sanctum Soho Hotel, Warwick Street, Soho, City of Westminster, London, Greater London, England, W1S 1PY, UK': (
        51.511565, -0.138332),
    'Pentahotel, 92, Margaretenstraße, Nikolsdorf, KG Margarethen, Margareten, Wien, 1050, Österreich': (
        48.18996815, 16.3567209909006),
    "Jeanne d'Arc, Place des Pyramides, Palais Royal, 1er, Paris, Île-de-France, France métropolitaine, 75001, France": (
        48.8638805, 2.33218343411753),
    'Produktenbörse, Durchhaus Taborstraße 10, Karmeliterviertel, KG Leopoldstadt, Leopoldstadt, Wien, 1020, Österreich': (
        48.214086, 16.380670709398),
    '5, Wildpretmarkt, Stubenviertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (48.2104502, 16.3715367),
    "Mander Portman Woodward School, 90-92, Queen's Gate, Brompton, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW7 5AB, UK": (
        51.4934099, -0.17896536231322),
    '15, Avenue des Terroirs de France, 12e Arrondissement (urbain), Bercy, 12e, Paris, Île-de-France, France métropolitaine, 75012, France': (
        48.8313475, 2.3872591),
    'Wembley Arena, Empire Way, Preston, London Borough of Brent, London, Greater London, England, HA9 0RQ, UK': (
        51.5593935, -0.2845768),
    '237 - Rius i Taulet 4, Avinguda de Rius i Taulet, el Poble-sec, Sants-Montjuïc, Barcelona, BCN, CAT, 08014, España': (
        41.372891, 2.154471),
    '32, Rue des Écoles, Sorbonne, 5e, Paris, Île-de-France, France métropolitaine, 75005, France': (
        48.8490713, 2.3471755),
    'Wyndham House, 189, Marsh Wall, Isle of Dogs, London Borough of Tower Hamlets, London, Greater London, England, E14 9SH, UK': (
        51.50072265, -0.0165621142112683),
    'Radisson Blu Edwardian Kenilworth, Bloomsbury Street, Holborn, Bloomsbury, London Borough of Camden, London, Greater London, England, WC1B 3LB, UK': (
        51.51795575, -0.128046997178988),
    'slh.com, Rue de Poitou, Archives, 3e, Paris, Île-de-France, France métropolitaine, 75003, France': (
        48.8616072, 2.3620921),
    '46, Prins Hendrikkade, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1012TM, Nederland': (
        52.3772463, 4.8978443),
    "Casa Santana i Soler, Plaça d'Emili Vilanova, el Gòtic, Ciutat Vella, Barcelona, BCN, CAT, 08003, España": (
        41.38331055, 2.17929896812888),
    "Sofitel London St James, Royal Opera Arcade, St. James's, Covent Garden, City of Westminster, London, Greater London, England, SW1Y 4UY, UK": (
        51.5077234, -0.132385494115644),
    'Regency Hotel, Via Lorenzo Bartolini, Cagnola, Milano, MI, LOM, 20148, Italia': (45.4897311, 9.1549824),
    "Hotel U232, Carrer del Comte d'Urgell, l'Antiga Esquerra de l'Eixample, Eixample, Barcelona, BCN, CAT, 08014, España": (
        41.3895385, 2.1490319),
    'Cambon Hôtel, Rue Cambon, Vendôme, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.8664167, 2.32516004277143),
    'Universiteitstheater, Nieuwe Doelenstraat, Burgwallen-Oude Zijde, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1017, Nederland': (
        52.3678574, 4.89533464757194),
    'Qui si mangia, 33, Via Gustavo Fara, Centro Direzionale, Municipio 2, Milano, MI, LOM, 20124, Italia': (
        45.4851932, 9.1982487),
    '9, Rue de Liège, Quartier Saint-Georges, St-Georges, 9e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.8796053, 2.3280594),
    'Le Petit Paris, Rue Saint-Jacques, Sorbonne, 5e, Paris, Île-de-France, France métropolitaine, 75005, France': (
        48.8452572, 2.3424357),
    'Gartenhotel Altmannsdorf, 26-28, Hoffingergasse, KG Altmannsdorf, Meidling, Kabelwerk, Wien, 1120, Österreich': (
        48.1638771, 16.3219256405148),
    'Grand Connaught Rooms, 61-65, Great Queen Street, Holborn, St Giles, London Borough of Camden, London, Greater London, England, WC2B 5DA, UK': (
        51.51582605, -0.120125354699107),
    '1K, Boulevard du Temple, Enfants Rouges, 3e, Paris, Île-de-France, France métropolitaine, 75003, France': (
        48.8639385, 2.3658779),
    '22, Avenue de Villiers, Plaine-Monceau, 17e, Paris, Île-de-France, France métropolitaine, 75017, France': (
        48.8821707, 2.3131889),
    'Grand Visconti Palace, 14, Viale Isonzo, Morivione, Municipio 5, Milano, MI, LOM, 20141, Italia': (
        45.4471578, 9.2069227),
    "269, 271, Carrer de Mallorca, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08003, España": (
        41.3947801, 2.16311588274661),
    'Maitre Choux, 15, Harrington Road, Brompton, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW7 3ES, UK': (
        51.493902, -0.1756807),
    'Old Street Courthouse Hotel, Old Street, Shoreditch, London Borough of Hackney, London, Greater London, England, EC1V 9LE, UK': (
        51.5273824, -0.0795360099916037),
    'Malmaison, 18-21, Charterhouse Square, Clerkenwell, London Borough of Islington, London, Greater London, England, EC1M 6AH, UK': (
        51.52076695, -0.100397585625652),
    "Wellington House, Buckingham Gate, St. James's, Victoria, City of Westminster, London, Greater London, England, SW1E 6AX, UK": (
        51.49897245, -0.137371622756659),
    'Notting Hill, Nicolaas Witsenkade, Rivierenbuurt, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1017, Nederland': (
        52.3583545, 4.898786),
    "257, Carrer de la Diputació, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08003, España": (
        41.38994135, 2.16603588349979),
    'Meliá Barcelona Sky, 272, Carrer de Pere IV, Provençals del Poblenou, Sant Martí, Barcelona, BCN, CAT, 08005, España': (
        41.40616425, 2.20072475851085),
    'Haas-Haus, Stock-im-Eisen-Platz, Kärntner Viertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.2083646, 16.371557963785),
    'Carlyle Brera Hotel, 84, Corso Giuseppe Garibaldi, Municipio 1, Milano, MI, LOM, 20121, Italia': (
        45.4770125, 9.1844956),
    'The Bloomsbury, Great Russell Street, Holborn, Bloomsbury, London Borough of Camden, London, Greater London, England, WC1B 3NB, UK': (
        51.51719435, -0.128976914685008),
    'DoubleTree by Hilton Hotel London ExCel, 2, Festoon Way, Silvertown, Newham, London, Greater London, England, E16 1RH, UK': (
        51.5075453, 0.0381871294444421),
    "Amsterdam Hotel London, 7, Trebovir Road, Earl's Court, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW5 9LS, UK": (
        51.4923082, -0.1945744),
    'Amarante Beau Manoir, Passage de la Madeleine, Madeleine, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8710343, 2.3234791),
    'Hôtel Brighton, 218, Rue de Rivoli, Vendôme, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.8648321, 2.3290435),
    'Europcar, Via Luigi Galvani, Centro Direzionale, Municipio 2, Milano, MI, LOM, 20124, Italia': (
        45.4860489, 9.2003229),
    'ABaC, Avinguda del Tibidabo, la Bonanova, Sant Gervasi - la Bonanova, Sarrià - Sant Gervasi, Barcelona, BCN, CAT, 08023, España': (
        41.4105723, 2.1364689),
    'Boston Court Hotel, 26, Upper Berkeley Street, Marylebone, City of Westminster, London, Greater London, England, W1H 7PF, UK': (
        51.515442, -0.1610345),
    '24, Nieuwe Doelenstraat, Burgwallen-Oude Zijde, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1012CP, Nederland': (
        52.368205, 4.8957416),
    "Park Grand London Paddington, 1, Queen's Gardens, Paddington, City of Westminster, London, Greater London, England, W2 3BE, UK": (
        51.5142616, -0.18091020979217),
    'Meliã Vendôme, 8, Rue Cambon, Vendôme, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.8668168, 2.3257587),
    'La Suite West-Hyde Park, 41-51, Inverness Terrace, Bayswater, City of Westminster, London, Greater London, England, W2 3LD, UK': (
        51.5123598, -0.1867202),
    'Paul Edmonds, Brompton Road, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW3 4, UK': (
        51.4971941, -0.1677079),
    'Londis, Sterne Street, Brook Green, London Borough of Hammersmith and Fulham, London, Greater London, England, W12, UK': (
        51.5045862, -0.219181020160867),
    'Largo Rio de Janeiro, Città Studi, Milano, MI, LOM, 20124, Italia': (45.4738974, 9.2238257),
    '36, Rue Pierre Demours, Plaine-Monceau, 17e, Paris, Île-de-France, France métropolitaine, 75017, France': (
        48.8812707, 2.2947419),
    "Twenty Nevern Square Hotel, 20, Nevern Square, Earl's Court, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW5 9PD, UK": (
        51.49150005, -0.19631885),
    'Hôtel de Trudon, Rue Saint-Honoré, Quartier des Halles, Les Halles, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.8609474, 2.34303614190707),
    'Agent Provocateur, Pont Street, Belgravia, City of Westminster, London, Greater London, England, SW3 4, UK': (
        51.497438, -0.157233),
    '3b, Place Saint-Sulpice, Odéon, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.8504193, 2.3344201),
    '3, Lichtensteg, Stubenviertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (48.2102935, 16.3735597),
    'Verneuil, Rue de Verneuil, St-Germain-des-Prés, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.8573599, 2.3314491),
    'Pershing Hall, 49, Rue Pierre Charron, Champs-Élysées, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8690865, 2.3022434),
    '90, Carrer de Calàbria, Project Area Sant Antoni, Sant Antoni, Eixample, Barcelona, BCN, CAT, 08014, España': (
        41.37916205, 2.15618565384033),
    'Radisson BLU Hotel, 17, Rusland, Burgwallen-Oude Zijde, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1017, Nederland': (
        52.3701707, 4.8966042),
    'Hôtel La Bourdonnais, Avenue de la Bourdonnais, Gros-Caillou, 7e, Paris, Île-de-France, France métropolitaine, 75007, France': (
        48.8549752, 2.3046163),
    '213, Rue de la Croix Nivert, Grenelle, 15e, Paris, Île-de-France, France métropolitaine, 75015, France': (
        48.8363634, 2.289702),
    '10 Bis, Rue du Débarcadère, Ternes, 17e, Paris, Île-de-France, France métropolitaine, 75017, France': (
        48.8780076, 2.2865338),
    'Hôtel Saint-James & Albany, 202, Rue de Rivoli, Vendôme, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.8642598, 2.3308105),
    "Claridges, 30, Brook Street, St. James's, Mayfair, City of Westminster, London, Greater London, England, W1A 2JQ, UK": (
        51.512657, -0.1476217),
    'Fonda Espanya, Carrer de Sant Pau, el Raval, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (
        41.3799009, 2.1728032),
    '49, Rue La Fayette, Fg-Montmartre, 9e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.8753375, 2.3414974),
    'Montebianco, 90, Via Monte Rosa, Molinazzo, Milano, MI, LOM, 20149, Italia': (45.4790196, 9.14438201871404),
    'FourSide Hotel & Suites Vienna, 25-27, Freytaggasse, KG Floridsdorf, Floridsdorf, Neujedlersdorf, Wien, 1210, Österreich': (
        48.2567457, 16.403304537871),
    'Terrassa Do, Plaça Reial, el Gòtic, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (41.3799799, 2.1748476),
    'Dorset Street, Gloucester Place, Marylebone, City of Westminster, London, Greater London, England, W1U 8HT, UK': (
        51.5188255, -0.1584295),
    "CEJFE, 40, Carrer d'Ausiàs Marc, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08010, España": (
        41.3916473, 2.1763389),
    'St Petersburgh Place, Bayswater Road, Royal Borough of Kensington and Chelsea, London, Greater London, England, W2 4RT, UK': (
        51.5100917, -0.1906304),
    '59, Prins Hendrikkade, Burgwallen-Oude Zijde, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1012AD, Nederland': (
        52.3763839, 4.9001154),
    'The RE Hotel London Shoreditch, 419-437, Hackney Road, Bethnal Green, London Borough of Tower Hamlets, London, Greater London, England, E2 8PP, UK': (
        51.53209755, -0.0616742072428918),
    "Amnistia Internacional Catalunya, 19-21, Carrer d'Alfons XII, Sant Gervasi - Galvany, Sarrià - Sant Gervasi, Barcelona, BCN, CAT, 08006, España": (
        41.3981857, 2.1498603),
    "Sea Containers House, The Queen's Walk, London Borough of Southwark, London, Greater London, England, SE15, UK": (
        51.50827915, -0.107190336880127),
    "73, Passeig de Gràcia, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08003, España": (
        41.3934749, 2.16248949622987),
    'The Laslett, Pembridge Gardens, Notting Hill, Royal Borough of Kensington and Chelsea, London, Greater London, England, W2 4DU, UK': (
        51.5095253, -0.1966576),
    "Roger De Lluria, Carrer de Roger de Llúria, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08003, España": (
        41.3910629, 2.1718498),
    'Victoria Palace Hotel, Rue Blaise Desgoffe, ND-des-Champs, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.8457742, 2.3243407),
    'Port Vell, Pas de Sota Muralla, Sant Pere, Santa Caterina i la Ribera, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (
        41.3815707, 2.1837722),
    'London Bridge Cycle Park, Weston Street, Borough, London Borough of Southwark, London, Greater London, England, SE15, UK': (
        51.5045334, -0.0850349),
    'Northumberland House, 8, Northumberland Avenue, St Clement Danes, Covent Garden, City of Westminster, London, Greater London, England, WC2, UK': (
        51.5068871, -0.125812698531211),
    '8, Via Manfredo Camperio, Cordusio, Municipio 1, Milano, MI, LOM, 20123, Italia': (45.4667344, 9.1831751),
    '31, Rue de Surène, Madeleine, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8713748, 2.3192726),
    'Escola Bressol Oikia, Passeig de Manuel Girona, Pedralbes, les Corts, Barcelona, BCN, CAT, 08014, España': (
        41.3904315, 2.1212359),
    "IPG Mediabrands, St John's Square, Clerkenwell, London Borough of Islington, London, Greater London, England, EC1M 6DS, UK": (
        51.52323885, -0.103171178696862),
    '3, Piazza Fontana, Pasquirolo, Municipio 1, Milano, MI, LOM, 20122, Italia': (45.4638443, 9.1940293),
    'Dorsett Shepherds Bush London, Shepherds Bush Green, Brook Green, London Borough of Hammersmith and Fulham, London, Greater London, England, W12 8QD, UK': (
        51.5040211, -0.224689689524146),
    "K+K Hotel George, 1-15, Templeton Place, Earl's Court, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW5 9NB, UK": (
        51.49224225, -0.195346093949667),
    'Palais Coburg, Seilerstätte, Stubenviertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.20586285, 16.376713356765),
    'New Hotel Opera, Rue de Liège, Quartier Saint-Georges, St-Georges, 9e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.8798176, 2.32873890750312),
    "35, Piccadilly, St. James's, Mayfair, City of Westminster, London, Greater London, England, W1J 0LA, UK": (
        51.50930695, -0.13716148533501),
    "May Fayre House, Shepherd Street, St. James's, Mayfair, City of Westminster, London, Greater London, England, SW3 4, UK": (
        51.506051, -0.148511370524176),
    'Hilton Garden Inn Milan North, 36, Via Lucio Giunio Columella, Precotto, Milano, MI, LOM, 20128, Italia': (
        45.5161855, 9.2274965),
    '7, Boulevard Bourdon, Arsenal, 4e, Paris, Île-de-France, France métropolitaine, 75004, France': (
        48.8482213, 2.3658687),
    '24, Rue de Buci, St-Germain-des-Prés, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.8537787, 2.3366249),
    'Hotel Millenni, Carrer de les Flors, el Raval, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (
        41.3759505, 2.1670539),
    'Bulgari Hotel, 171, Knightsbridge, City of Westminster, London, Greater London, England, SW3 4, UK': (
        51.50136075, -0.162824226587216),
    'K+K Hotel Picasso, 26-30, Passeig de Picasso, Sant Pere, Santa Caterina i la Ribera, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (
        41.3865845, 2.18402232858915),
    'Antica Locanda dei Mercanti, 6, Via San Tomaso, Cordusio, Municipio 1, Milano, MI, LOM, 20121, Italia': (
        45.4672963, 9.1847222),
    'Hotel 82 London, Gloucester Place, Marylebone, City of Westminster, London, Greater London, England, W1U 6HH, UK': (
        51.519583, -0.1585277),
    '305, Singel, Burgwallen-Nieuwe Zijde, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1012WJ, Nederland': (
        52.3705543, 4.8885667),
    "8, Rue d'Anjou, Madeleine, 8e, Paris, Île-de-France, France métropolitaine, 75008, France": (
        48.8698077, 2.3208273),
    '11, Place du Palais Bourbon, Invalides, 7e, Paris, Île-de-France, France métropolitaine, 75007, France': (
        48.8602345, 2.3184888),
    "214, Carrer de Muntaner, l'Antiga Esquerra de l'Eixample, Eixample, Barcelona, BCN, CAT, 08014, España": (
        41.39368625, 2.15064050964504),
    '5, Rue des Capucines, Vendôme, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.8685213, 2.3298365),
    '19, Rue Cujas, Sorbonne, 5e, Paris, Île-de-France, France métropolitaine, 75005, France': (48.8478616, 2.3422447),
    'HCC Montblanc, 61, Via Laietana, el Gòtic, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (
        41.3876585, 2.17308273226451),
    'Hôtel Méridien, Boulevard Gouvion-Saint-Cyr, Ternes, 17e, Paris, Île-de-France, France métropolitaine, 75017, France': (
        48.87954025, 2.28538164921807),
    'Floor 17, Staalmeesterslaan, Slotervaart, Amsterdam, Nieuw-West, Amsterdam, Noord-Holland, Nederland, 1055, Nederland': (
        52.368119, 4.8441167),
    'Whitehall Court, St Clement Danes, Covent Garden, City of Westminster, London, Greater London, England, SW1A 2EJ, UK': (
        51.50543315, -0.124342166969031),
    'Barceló Raval, 25, Rambla del Raval, el Raval, Ciutat Vella, Barcelona, BCN, CAT, 08001, España': (
        41.3790345, 2.16964524706854),
    "22, Boulevard Haussmann, Chaussée-d'Antin, 9e, Paris, Île-de-France, France métropolitaine, 75009, France": (
        48.872669, 2.3362259),
    'Novotel, Shortlands, Brook Green, London Borough of Hammersmith and Fulham, London, Greater London, England, W6 8DR, UK': (
        51.49200995, -0.219858924379993),
    '51, Rue Lauriston, Chaillot, 16e, Paris, Île-de-France, France métropolitaine, 75116, France': (
        48.8700453, 2.2908543),
    '100, Boulevard de Grenelle, Grenelle, 15e, Paris, Île-de-France, France métropolitaine, 75015, France': (
        48.8496087, 2.2955202),
    '34, Koninginneweg, Willemsparkbuurt, Amsterdam, Zuid, Amsterdam, Noord-Holland, Nederland, 1075CZ, Nederland': (
        52.3542657, 4.8664806),
    "The Brewery & The Montcalm London City, Chiswell Street, Saint Luke's, London Borough of Islington, London, Greater London, England, SE15, UK": (
        51.52051975, -0.0912374666951739),
    'Le Marcel, Rue du 8 Mai 1945, St-Vincent-de-Paul, 10e, Paris, Île-de-France, France métropolitaine, 75010, France': (
        48.8761374, 2.35729819095053),
    "HolidayInn Kensington, Scarsdale Place, Earl's Court, Royal Borough of Kensington and Chelsea, London, Greater London, England, W8 6TD, UK": (
        51.4984762, -0.191827879835341),
    'Novotel, Boulevard du Fort de Vaux, Batignolles, 17e, Paris, Île-de-France, France métropolitaine, 75017, France': (
        48.89204625, 2.30241475773444),
    '41, Schönbrunner Straße, KG Margarethen, Margareten, Wien, 1050, Österreich': (48.19258545, 16.3575214842309),
    'NH Milano Touring, 2, Via Ugo Iginio Tarchetti, Porta Nuova, Milano, MI, LOM, 20121, Italia': (
        45.4768221, 9.1967233),
    '14, Boulevard Vincent Auriol, Salpêtrière, 13e, Paris, Île-de-France, France métropolitaine, 75013, France': (
        48.8370537, 2.3723743),
    'Gran Hotel La Florida, Camí de Tenzing Norgay, Vallvidrera, el Tibidabo i les Planes, Sarrià - Sant Gervasi, Barcelona, BCN, CAT, 08035, España': (
        41.4254096, 2.12071080541475),
    'Hôtel Les Rives de Notre-Dame, Rue Xavier Privas, Îlot Saint-Séverin, Sorbonne, 5e, Paris, Île-de-France, France métropolitaine, 75005, France': (
        48.8532543, 2.3457644),
    'BVD Istituto di bellezza, 11, Viale Murillo, Molinazzo, Milano, MI, LOM, 20149, Italia': (45.4726804, 9.1440481),
    '163, Linzer Straße, KG Penzing, Penzing, Wien, 1140, Österreich': (48.1940118, 16.2972614),
    'Paris Palais Royal, Rue Molière, Palais Royal, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.8646388, 2.3358151020631),
    "20, Rue d'Antin, Gaillon, 2e, Paris, Île-de-France, France métropolitaine, 75002, France": (48.8692039, 2.3338171),
    'Andaz Liverpool Street, 40, Liverpool Street, London, Greater London, England, EC2M 7QN, UK': (
        51.51736765, -0.0813160280097019),
    "The Beaumont, 8, Balderton Street, St. James's, Mayfair, City of Westminster, London, Greater London, England, W1K 6TF, UK": (
        51.51295945, -0.152423682639487),
    'Palm Hotel, Hendon Way, Childs Hill, London Borough of Barnet, London, Greater London, England, NW2 2NG, UK': (
        51.5635061, -0.204385578041708),
    'Falkensteiner, 74, Schottenfeldgasse, Lerchenfeld, KG Neubau, Neubau, Wien, 1070, Österreich': (
        48.2048492, 16.3435774306369),
    '3, Rue des Arquebusiers, Archives, 3e, Paris, Île-de-France, France métropolitaine, 75003, France': (
        48.8591155, 2.366979),
    '2, Rue de Calais, Quartier Saint-Georges, St-Georges, 9e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.8822715, 2.3316535),
    'Park International Hotel, Cromwell Road, South Kensington, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW7 4DT, UK': (
        51.4946331, -0.186603),
    'Palazzo Parigi, Corso di Porta Nuova, Borgonuovo, Porta Nuova, Milano, MI, LOM, 20121, Italia': (
        45.4733994, 9.1911115),
    'Rembrandtplein, Grachtengordel, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1017, Nederland': (
        52.365988, 4.89661538803072),
    '33, Rue Raymond Losserand, Plaisance, 14e, Paris, Île-de-France, France métropolitaine, 75014, France': (
        48.835467, 2.321071),
    '10, Rue Lamartine, Fg-Montmartre, 9e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.8766004, 2.3433038),
    'San Lorenzo, 22, Beauchamp Place, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW3 4, UK': (
        51.4975195, -0.1644244),
    '5, Rue de Berri, Quartier du Faubourg-du-Roule, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8723737, 2.30291344380343),
    'Dikker & Thijs Fenice Hotel, 444, Prinsengracht, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1017KE, Nederland': (
        52.365001, 4.8840169),
    '4, Rue du Mont Thabor, Vendôme, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.8654667, 2.3294662),
    'abba Garden hotel, 33, Carrer de Santa Rosa, Pedralbes, les Corts, Esplugues de Llobregat, BCN, CAT, 08950, España': (
        41.3854618, 2.10185141666716),
    'Burger & Lobster Leicester Square, 10, Wardour Street, Chinatown, City of Westminster, London, Greater London, England, W1D 6QF, UK': (
        51.5110319, -0.1315618),
    'Pakat Suites Hotel, 5, Mommsengasse, KG Wieden, Wieden, Wien, 1040, Österreich': (48.19189045, 16.377029685865),
    "Saint-Gobain Innovation Centre, 95, Great Portland Street, St. James's, Fitzrovia, City of Westminster, London, Greater London, England, W1, UK": (
        51.5187518, -0.142388315876615),
    'The Throne of Earthly Kings, King William Walk, Greenwich, London, Greater London, England, SE10 9JH, UK': (
        51.4805583, -0.0073353),
    "Hotel Colonial, Carrer d'Àngel J. Baixeras, el Gòtic, Ciutat Vella, Barcelona, BCN, CAT, 08003, España": (
        41.3822737, 2.1806803),
    "Mandarin Oriental, 38-40, Passeig de Gràcia, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08003, España": (
        41.3913676, 2.16689974622302),
    "Dennis Severs' House, Folgate Street, Spitalfields, London Borough of Tower Hamlets, London, Greater London, England, EC2V 7HH, UK": (
        51.5208921, -0.0778038),
    "Prince's Square, Leinster Square, Bayswater, City of Westminster, London, Greater London, England, W2 4PX, UK": (
        51.51336485, -0.192411955941672),
    'Brasserie des Belges, Rue de Saint-Quentin, St-Vincent-de-Paul, 10e, Paris, Île-de-France, France métropolitaine, 75010, France': (
        48.8794415, 2.3556766),
    'The Zetter, 86-88, Clerkenwell Road, Clerkenwell, London Borough of Islington, London, Greater London, England, EC1M 5RJ, UK': (
        51.5227778, -0.103605642810653),
    'MyHotel, 35, Ixworth Place, Chelsea, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW3 3QX, UK': (
        51.4919243, -0.1684868),
    'Museu del Calçat, Plaça de Sant Felip Neri, el Gòtic, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (
        41.3834643, 2.1752683),
    "H10 Itaca, 22, 28, Avinguda de Roma, la Nova Esquerra de l'Eixample, Eixample, Barcelona, BCN, CAT, 08014, España": (
        41.3809891, 2.14571708235509),
    'NH Belvedere, 12a, Rennweg, Botschaftsviertel, KG Landstraße, Landstraße, Wien, 1030, Österreich': (
        48.1955424, 16.3833011438795),
    '3, Kaiserstraße, KG Neubau, Neubau, Wien, 1070, Österreich': (48.1966262, 16.3413977),
    '24, Rue Cadet, Fg-Montmartre, 9e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.8754301, 2.3434686),
    'Hôtel Vendôme, Place Vendôme, Vendôme, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.8670031, 2.328706),
    "Saint-Honoré - Vendôme, Rue d'Argenteuil, Palais Royal, 1er, Paris, Île-de-France, France métropolitaine, 75001, France": (
        48.86594285, 2.33310300055934),
    'Le George, Rue Quentin Bauchart, Champs-Élysées, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8687237, 2.3001825),
    '31, Gower Street, Holborn, Bloomsbury, London Borough of Camden, London, Greater London, England, WC1E 6BT, UK': (
        51.52078625, -0.131027762053305),
    '6, Avenue Frémiet, Muette, 16e, Paris, Île-de-France, France métropolitaine, 75015, France': (
        48.8565794, 2.2851984),
    'Aubaine, 129, Bayswater Road, Bayswater, City of Westminster, London, Greater London, England, W2 4RH, UK': (
        51.5103208, -0.1876885),
    'Cartoleria Correnti, 20, Via Cesare Correnti, Carrobbio, Porta Genova, Milano, MI, LOM, 20123, Italia': (
        45.4597067, 9.1794879),
    '28, Carrer de Loreto, les Corts, Barcelona, BCN, CAT, 08014, España': (41.39000775, 2.14251021697278),
    'Tours & Tickets, 97, Damrak, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1012LP, Nederland': (
        52.3735514, 4.8932741),
    "Evenia Rosselló, 191, Carrer del Rosselló, l'Antiga Esquerra de l'Eixample, Eixample, Barcelona, BCN, CAT, 08014, España": (
        41.3921435, 2.15540834041752),
    '6, Travessera de Gràcia, Galvany, Sant Gervasi - Galvany, Sarrià - Sant Gervasi, Barcelona, BCN, CAT, 08014, España': (
        41.3934897, 2.14601888245382),
    'Ramada Encore West London, Western Avenue, Acton, London Borough of Ealing, London, Greater London, England, W3 6RT, UK': (
        51.5210408, -0.262996729862237),
    'Hotel Mercure Milano Centro, Piazza Guglielmo Oberdan, Porta Venezia, Milano, MI, LOM, 20124, Italia': (
        45.4747329, 9.2059672), '5, Via Lentasio, Municipio 1, Milano, MI, LOM, 20123, Italia': (45.458018, 9.191289),
    'DoubleTree by Hilton Hotel London - Islington, 60, Pentonville Road, Pentonville, London Borough of Islington, London, Greater London, England, N1 9LA, UK': (
        51.5321106, -0.1094659),
    'Gorla, Via privata Giancarlo Puecher, Municipio 2, Milano, MI, LOM, 20127, Italia': (45.5030418, 9.2222202009084),
    "Villa Olimpica Suites Barcelona, Carrer d'Àlaba, el Parc i la Llacuna del Poblenou, Sant Martí, Barcelona, BCN, CAT, 08003, España": (
        41.39741785, 2.19231500021657),
    'Park Hotel, 25, Stadhouderskade, Oud-Zuid, Amsterdam, Zuid, Amsterdam, Noord-Holland, Nederland, 1071 ZD, Nederland': (
        52.3615125, 4.8832127),
    'Hôtel Plaza Athénée, 25, Avenue Montaigne, Champs-Élysées, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.86638145, 2.30389257291576),
    'Pulitzer, 323, Prinsengracht, Negen Straatjes, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1016GZ, Nederland': (
        52.3728094, 4.8833865),
    'Hotel degli Arcimboldi, Viale Sarca, Bicocca, Milano, MI, LOM, 20132, Italia': (45.52563135, 9.21528920512584),
    'Hôtel Villa des Ternes, Rue Bélidor, Ternes, 17e, Paris, Île-de-France, France métropolitaine, 75017, France': (
        48.8803203, 2.2858761),
    'Le Secret de Paris, Rue de Parme, Quartier Saint-Georges, St-Georges, 9e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.8813851, 2.32824919744646),
    'Grange Tower Bridge Hotel, South Tenter Street, St.George in the East, London Borough of Tower Hamlets, London, Greater London, England, SE15, UK': (
        51.5117482, -0.0715951042235655),
    "Hôtel Novotel Paris Porte d'Orléans, 17, Boulevard Romain Rolland, Plaisance, 14e, Paris, Île-de-France, France métropolitaine, 75014, France": (
        48.8195998, 2.3261186),
    'Hotel Napoleon, 12, Via Federico Ozanam, Zona Buenos Aires, Municipio 3, Milano, MI, LOM, 20124, Italia': (
        45.480228, 9.2129603),
    "El Restaurant, Carrer de l'Esperança, la Bonanova, Sant Gervasi - la Bonanova, Sarrià - Sant Gervasi, Barcelona, BCN, CAT, 08023, España": (
        41.4049894, 2.1286786),
    'Palais Hansen, Schottenring, Textilviertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.21617125, 16.3683481911905),
    'Archives, Rue des Archives, Enfants Rouges, 3e, Paris, Île-de-France, France métropolitaine, 75003, France': (
        48.8636111, 2.3608349),
    'Grand Hotel Haussmann, Rue du Helder, Gaillon, 9e, Paris, Île-de-France, France métropolitaine, 75002, France': (
        48.8716438, 2.3349837),
    'Crowne Plaza, Place de la République, Porte-St-Martin, 10e, Paris, Île-de-France, France métropolitaine, 75010, France': (
        48.8672306, 2.3655555),
    'Klima Hotel Milano Fiere, 8, Via privata Venezia Giulia, Musocco, Milano, MI, LOM, 20157, Italia': (
        45.51486605, 9.11606242608858),
    'Hotel Mercure, Via Augusta, Galvany, Sant Gervasi - Galvany, Sarrià - Sant Gervasi, Barcelona, BCN, CAT, 08023, España': (
        41.4000626, 2.1451593),
    '3, Neuer Markt, Kärntner Viertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (48.2062215, 16.3710306),
    "Millennium Hotel, Grosvenor Square, St. James's, Mayfair, City of Westminster, London, Greater London, England, W1K 2HR, UK": (
        51.51057135, -0.151154150154011),
    '16, Rue de Berri, Quartier du Faubourg-du-Roule, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8727184, 2.3048095),
    'Punto SMA, 2/4, Via Lodovico Mancini, Municipio 4, Milano, MI, LOM, 20121, Italia': (45.4626679, 9.2102123),
    'Hotel Colombia, 15, Via Roberto Lepetit, Centrale, Municipio 2, Milano, MI, LOM, 20124, Italia': (
        45.482957, 9.2041659),
    '4, Rue de la Grange Batelière, Fg-Montmartre, 9e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.873079, 2.342496),
    'Westfield Stratford City, The Street, Stratford Marsh, Newham, London, Greater London, England, E10, UK': (
        51.5425649, -0.00693080308689057),
    'Communauté assomptionniste Saint-Vincent-de-Paul, 8, Rue François 1er, Champs-Élysées, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8657148, 2.3090996),
    '25, Rue des Saints-Pères, St-Germain-des-Prés, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.8566095, 2.3319873),
    '72, 74, Carrer de Numància, les Corts, Barcelona, BCN, CAT, 08014, España': (41.38470735, 2.13807069828307),
    'Arena, Carrer de Béjar, Hostafrancs, Sants-Montjuïc, Barcelona, BCN, CAT, 08014, España': (
        41.37683895, 2.14590821939197),
    'Hôtel Mercure Paris Porte de Versailles  Expo, Rue Michel-Ange, St-Lambert, 15e, Vanves, Paris, Hauts-de-Seine, Île-de-France, France métropolitaine, 75015, France': (
        48.8267685, 2.29117588140029),
    '32, Mariahilfer Straße, Untere Windmühle, KG Mariahilf, Mariahilf, Wien, 1070, Österreich': (
        48.2002896, 16.3547192626126),
    'DoubleTree by Hilton Hotel London - Tower of London, 7, Pepys Street, London, Greater London, England, EC3N 4AF, UK': (
        51.5109091, -0.0783435423868312),
    "Radisson Edwardian Hampshire Hotel, Long's Court, St. James's, Covent Garden, City of Westminster, London, Greater London, England, WC2H 7EL, UK": (
        51.509864, -0.129700895802685),
    "The Ritz London, 150, Piccadilly, St. James's, Mayfair, City of Westminster, London, Greater London, England, W1J 9BS, UK": (
        51.5070027, -0.141568683792425),
    '6, Rue Pierre Demours, Plaine-Monceau, 17e, Paris, Île-de-France, France métropolitaine, 75017, France': (
        48.879894, 2.2918269),
    'Lindner Hotel am Belvedere, 12, Rennweg, Botschaftsviertel, KG Landstraße, Landstraße, Wien, 1030, Österreich': (
        48.19561295, 16.3827491290103),
    '261, Rue de Vaugirard, Sorbonne, 6e, Paris, Île-de-France, France métropolitaine, 75005, France': (
        48.8399972, 2.3031613),
    'Rag & Bone, Sloane Square, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW3 4, UK': (
        51.4928736, -0.157491975002844),
    "Jardins de l'Hotel Petit Palace, Carrer d'Aroles, el Gòtic, Ciutat Vella, Barcelona, BCN, CAT, 08003, España": (
        41.38100605, 2.17421605350598),
    "Nelson Docks, Durand's Wharf, Rotherhithe, London Borough of Southwark, London, Greater London, England, SE16 5UB, UK": (
        51.5040599, -0.0330893374371957),
    '110, Rue Blomet, Necker, 15e, Paris, Île-de-France, France métropolitaine, 75015, France': (48.8405066, 2.2991377),
    'Burgerziekenhuis, Oetewalerstraat, Dapperbuurt, Amsterdam, Oost, Amsterdam, Noord-Holland, Nederland, 1019, Nederland': (
        52.3591306, 4.92637938751678),
    'A, 356, Carrer de Llull, Diagonal Mar i el Front Marítim del Poblenou, Sant Martí, Barcelona, BCN, CAT, 08029, España': (
        41.40856975, 2.21254621010039),
    '61, Quai de Grenelle, Grenelle, 15e, Paris, Île-de-France, France métropolitaine, 75015, France': (
        48.8500212, 2.2832769),
    '8, Riemergasse, Stubenviertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.2072212, 16.3764602996064),
    'Hotel Marriot Milano, Piazza Carlo Irnerio, La Maddalena, Milano, MI, LOM, 20145, Italia': (
        45.46106135, 9.15399618903794),
    'Pol & Grace Hotel, 49, Carrer de Guillem Tell, Sant Gervasi - Galvany, Sarrià - Sant Gervasi, Barcelona, BCN, CAT, 08006, España': (
        41.4017429, 2.1477414),
    'Best Western Le 18, 51, Rue Letort, Clignancourt, 18e, Paris, Île-de-France, France métropolitaine, 75018, France': (
        48.8965796, 2.3436026),
    'Nouvel Orleans, Rue Sophie Germain, Petit-Montrouge, 14e, Paris, Île-de-France, France métropolitaine, 75014, France': (
        48.8310268, 2.3299085),
    'Madison Hotel, 143, Boulevard Saint-Germain, St-Germain-des-Prés, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.8532615, 2.3344499),
    'Millenium Conference Centre, Courtfield Road, South Kensington, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW7 4QH, UK': (
        51.4935222, -0.183415540826432),
    'The Hoxton, 255, Herengracht, Negen Straatjes, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1016BJ, Nederland': (
        52.37181, 4.8873904),
    '10, Rue Saint-Philippe du Roule, Quartier du Faubourg-du-Roule, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8728773, 2.3081702),
    'Hôtel Louvre Saint-Honoré, 141, Rue Saint-Honoré, Quartier des Halles, Les Halles, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.86167895, 2.34062129116098),
    '1, Corso Giacomo Matteotti, San Babila, Municipio 1, Milano, MI, LOM, 20121, Italia': (45.4670602, 9.1942761),
    '48, Corso di Porta Romana, Brolo-Pantano, Municipio 1, Milano, MI, LOM, 20123, Italia': (45.4580703, 9.192418),
    '61, Via Laietana, el Gòtic, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (41.38700265, 2.17421753003764),
    '28T, Avenue Corentin Cariou, Pont-de-Flandre, 19e, Paris, Île-de-France, France métropolitaine, 75019, France': (
        48.8969426, 2.3851997),
    'Zona Navigli, Via Angelo Fumagalli, Zona Navigli, Municipio 6, Milano, MI, LOM, 20136, Italia': (
        45.4497257, 9.17015467224502),
    "DoubleTree by Hilton Hotel London - Westminster, 30, John Islip Street, St. James's, Millbank, City of Westminster, London, Greater London, England, SW1P 4DD, UK": (
        51.4932745, -0.126762543905176),
    "64, Carrer d'Enric Granados, l'Antiga Esquerra de l'Eixample, Eixample, Barcelona, BCN, CAT, 08023, España": (
        41.3922396, 2.15741681524099),
    'Palau de Congressos de Catalunya, Carrer de la Torre Melina, la Maternitat i Sant Ramon, les Corts, Barcelona, BCN, CAT, 08014, España': (
        41.3829807, 2.10957226010988),
    'Hôtel Mercure Paris XV, 3, Rue Saint-Lambert, St-Lambert, 15e, Paris, Île-de-France, France métropolitaine, 75015, France': (
        48.8383296, 2.29048459778361),
    '28, Landstraßer Hauptstraße, Botschaftsviertel, KG Landstraße, Landstraße, Wien, 1030, Österreich': (
        48.2038699, 16.3887311),
    '31, Große Stadtgutgasse, Afrikanerviertel, KG Leopoldstadt, Leopoldstadt, Wien, 1020, Österreich': (
        48.21968895, 16.3863703122998),
    'Melcon Lane, London, Laurel County, Kentucky, 40741, United States of America': (37.143105, -84.108656),
    'Houstonian, Houston, Harris County, Texas, 77024, United States of America': (29.7685298, -95.4586397),
    'Hilton Americas-Houston, 1600, Lamar Street, Houston, Harris County, Texas, 77010, United States of America': (
        29.75155505, -95.3606596843732),
    'La Quinta Inn & Suites Houston - Normandy, Mc Nair Street, Greens Bayou, Harris County, Texas, 77015, United States of America': (
        29.7729327, -95.2069677),
    '18, Via Fabio Filzi, Centro Direzionale, Municipio 2, Milano, MI, LOM, 20124, Italia': (45.4839924, 9.2002734),
    '188, Panamalaan, Amsterdam, Oost, Amsterdam, Noord-Holland, Nederland, 1019AZ, Nederland': (52.371371, 4.9346632),
    '11, Rudolfsplatz, Textilviertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.213751, 16.3714982764234),
    "Aparthotel Adagio Paris Hausmann, 129-131, Boulevard Haussmann, Chaussée-d'Antin, 9e, Paris, Île-de-France, France métropolitaine, 75008, France": (
        48.8724632, 2.3377919),
    'NÖ Gebietskrankenkasse, 2, Burggasse, KG Neubau, Neubau, Wien, 1070, Österreich': (48.2045784, 16.3564305),
    'Portello, 12, Via Guglielmo Silva, Tre Torri, Milano, MI, LOM, 20148, Italia': (45.4802093, 9.1495414),
    '23, Rue du Pont Neuf, Quartier des Halles, Les Halles, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.8605342, 2.3443245),
    '57, Avenue Raymond Poincaré, Chaillot, 16e, Paris, Île-de-France, France métropolitaine, 75116, France': (
        48.8672826, 2.2857862),
    'Hilton Diagonal Mar Barcelona, 262-264, Passeig del Taulat, Diagonal Mar i el Front Marítim del Poblenou, Sant Martí, Barcelona, BCN, CAT, 08019, España': (
        41.40843645, 2.21775567197692),
    '2, Floragasse, Freihausviertel, KG Wieden, Wieden, Wien, 1040, Österreich': (48.1949159, 16.3692864),
    '2, Rue des Guillemites, St-Gervais, 4e, Paris, Île-de-France, France métropolitaine, 75004, France': (
        48.8579077, 2.3571918),
    '44, Wiedner Hauptstraße, Schaumburgergrund, KG Wieden, Wieden, Wien, 1040, Österreich': (48.1935557, 16.366958),
    'A la Turca, Avinguda del Paral·lel, el Raval, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (
        41.3751717, 2.1683692),
    'Shaftesbury Hyde Park International, Inverness Terrace, Bayswater, City of Westminster, London, Greater London, England, W2 3LD, UK': (
        51.5123977, -0.1861753),
    'Addendum, Seething Lane, London, Greater London, England, EC3, UK': (51.5104975, -0.0793674),
    "Hotel Vilamari, 34-36, Carrer de Vilamarí, la Nova Esquerra de l'Eixample, Eixample, Barcelona, BCN, CAT, 08014, España": (
        41.3767577, 2.15250742291627),
    '49, Carrer del Doctor Ibáñez, les Corts, Barcelona, BCN, CAT, 08014, España': (41.3887094, 2.13144994076567),
    'silver motel, Via Riccardo Lombardi, Municipio 7, Assiano, MI, LOM, 20019, Italia': (45.4591462, 9.0684813),
    'Park Plaza, 1, Addington Street, Lambeth, London Borough of Lambeth, London, Greater London, England, SE1 7RY, UK': (
        51.5013601, -0.1160331),
    'Senator Hotel**** Vienna, 105, Hernalser Hauptstraße, KG Hernals, Hernals, Wien, 1170, Österreich': (
        48.21942425, 16.3255712322522),
    "Hôtel Mercure Porte d'Orléans, 13, Rue François Ory, Petit-Montrouge, 14e, Montrouge, Paris, Île-de-France, France métropolitaine, 92120, France": (
        48.8177765, 2.32937896131856),
    'Capitania General, Carrer de la Mercè, el Gòtic, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (
        41.3794794, 2.18008859175947),
    "216, Carrer de Mallorca, l'Antiga Esquerra de l'Eixample, Eixample, Barcelona, BCN, CAT, 08014, España": (
        41.39105865, 2.15940657671145),
    'Maxim Opéra, Rue Geoffroy Marie, Fg-Montmartre, 9e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.8738647, 2.3444135),
    "Les Bains-Douche, 7, Rue du Bourg l'Abbé, Ste-Avoye, 3e, Paris, Île-de-France, France métropolitaine, 75003, France": (
        48.8638719, 2.3519655),
    'The Hotel 1060 Vienna, 23, Webgasse, Obere Windmühle, KG Mariahilf, Mariahilf, Wien, 1060, Österreich': (
        48.1941685, 16.346308),
    "S'Bar, Avenue Pierre 1er de Serbie, Champs-Élysées, 8e, Paris, Île-de-France, France métropolitaine, 75008, France": (
        48.868376, 2.3002021),
    '1, Rue Geoffroy Marie, Fg-Montmartre, 9e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.8732316, 2.3432488),
    'Restaurant Hexagone, Avenue Kléber, Chaillot, 16e, Paris, Île-de-France, France métropolitaine, 75116, France': (
        48.8644623, 2.28862264526997),
    "The Windermere Hotel & Brasserie, 142-144, Warwick Way, St. James's, Pimlico, City of Westminster, London, Greater London, England, SW1V 4JE, UK": (
        51.49033015, -0.145972149332526),
    'Hotel Lombardia, Viale Lombardia, Casoretto, Milano, MI, LOM, 20132, Italia': (45.4873209, 9.2237742),
    'Hotel West End, 7, Rue Clément Marot, Champs-Élysées, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8671535, 2.3038748),
    '8, Judengasse, Bermudadreieck, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (48.2114856, 16.3737931),
    'Little Palace Hotel, Rue Salomon de Caus, Arts-et-Métiers, 3e, Paris, Île-de-France, France métropolitaine, 75003, France': (
        48.8675046, 2.3539915),
    "84, Passeig de Gràcia, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08023, España": (
        41.39470835, 2.1626495579908),
    '1, Rue Lepic, Grandes-Carrières, 18e, Paris, Île-de-France, France métropolitaine, 75018, France': (
        48.8840718, 2.3328543),
    'Mercat de Fort Pienc, Plaça de Fort Pienc, el Fort Pienc, Eixample, Barcelona, BCN, CAT, 08003, España': (
        41.3956484, 2.18280810204403),
    'Vienna Sporthotel, 83, Baumgasse, Erdberger Mais, KG Landstraße, Landstraße, Wien, 1030, Österreich': (
        48.1914285, 16.4080581764272),
    'Hôtel Le Tourville, 16, Avenue de Tourville, École-Militaire, 7e, Paris, Île-de-France, France métropolitaine, 75007, France': (
        48.8542545, 2.30784035671776),
    '92, Rue du Cherche-Midi, ND-des-Champs, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.847412, 2.3223496),
    'Hilton London Olympia, 380, Kensington High Street, Royal Borough of Kensington and Chelsea, London, Greater London, England, W14 8NL, UK': (
        51.49673255, -0.206729643232032),
    "3, Rue d'Argentine, Chaillot, 16e, Paris, Île-de-France, France métropolitaine, 75116, France": (
        48.8743553, 2.2897543),
    '11, Opernring, Kärntner Viertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (48.2026302, 16.3670266),
    'Park Royal, Western Avenue, Acton, London Borough of Ealing, London, Greater London, England, W13, UK': (
        51.5271897, -0.2835894),
    'Hotel Serhs Rivoli Rambla, la Rambla, el Gòtic, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (
        41.38431385, 2.17130416518529),
    '251, Weteringschans, Rivierenbuurt, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1017XJ, Nederland': (
        52.3594784, 4.8958529),
    'Zadig & Voltaire, Rue du Faubourg Saint-Honoré, Madeleine, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8691969, 2.3205458),
    'Hôtel Paris Bastille Boutet MGallery by Sofitel, Rue Faidherbe, Roquette, 11e, Paris, Île-de-France, France métropolitaine, 75011, France': (
        48.85191945, 2.38398858327836),
    'Palais Hotel Pertschy, 5, Habsburgergasse, Widmerviertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.2081655, 16.3684861),
    'Hotel Le Mathurin, 43, Rue des Mathurins, Madeleine, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.87319225, 2.32393852319026),
    "29, 31, Passeig de Gràcia, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08003, España": (
        41.39069555, 2.16592000399116),
    'Arbor City Hotel, 12-20, Osborn Street, Spitalfields, London Borough of Tower Hamlets, London, Greater London, England, E1 6TE, UK': (
        51.5166904, -0.0698136277173575),
    'Royal Bayswater Hostel, Bayswater Road, Bayswater, City of Westminster, London, Greater London, England, W2 3JH, UK': (
        51.5104407, -0.1864167),
    '36, Rue Pierre Fontaine, Quartier Saint-Georges, St-Georges, 9e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.8826341, 2.3334279),
    "Hotel Well and Come, 158, Carrer de Girona, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08037, España": (
        41.3992587, 2.16572479215015),
    '570, Avinguda Diagonal, Galvany, Sant Gervasi - Galvany, Eixample, Barcelona, BCN, CAT, 08021, España': (
        41.39428295, 2.14899039918032),
    'New York University, Mecklenburgh Square, Holborn, Bloomsbury, London Borough of Camden, London, Greater London, England, WC1N 2AN, UK': (
        51.5258423, -0.117911180688074),
    'Hilton Vienna Plaza, 11, Schottenring, Schottenviertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.215515, 16.3646859613948),
    'Bush House, 30, Aldwych, St Clement Danes, Covent Garden, City of Westminster, London, Greater London, England, WC2B 4BG, UK': (
        51.51274515, -0.1171701516975),
    "41 Hotel, Bressenden Place, St. James's, Victoria, City of Westminster, London, Greater London, England, SW3 4, UK": (
        51.49809625, -0.143267314565226),
    'Le 123 Elysées, Rue du Faubourg Saint-Honoré, Quartier du Faubourg-du-Roule, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8731008, 2.3097181),
    'Savoy Hotel, 194, Ferdinand Bolstraat, Nieuwe Pijp, Amsterdam, Zuid, Amsterdam, Noord-Holland, Nederland, 1072 LW, Nederland': (
        52.34973, 4.8912188),
    '26E, Eerste Constantijn Huygensstraat, Helmersbuurt, Amsterdam, West, Amsterdam, Noord-Holland, Nederland, 1054BR, Nederland': (
        52.3651691, 4.8729743),
    "Mercato rionale di via Fauche', Via Giovanni Battista Fauche', Zona Sempione, Bullona, Milano, MI, LOM, 20121, Italia": (
        45.4858174, 9.16398636386718),
    '28, Via Laietana, el Gòtic, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (41.3845696, 2.17846728621686),
    'Ambassadors Bloomsbury, 12, Upper Woburn Place, Holborn, Bloomsbury, London Borough of Camden, London, Greater London, England, WC1H 0HX, UK': (
        51.5266227, -0.1297246),
    'Principe di Savoia, 17, Piazza della Repubblica, Porta Nuova, Milano, MI, LOM, 20124, Italia': (
        45.4797878, 9.1963935),
    "Jardins de Jaime Gil de Biedma, Carrer d'Espronceda, Diagonal Mar i el Front Marítim del Poblenou, Sant Martí, Barcelona, BCN, CAT, 08020, España": (
        41.4010578, 2.20919070000001),
    'Chavanel, Rue Vignon, Vendôme, 9e, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.8721693, 2.32633574817712),
    'Clarins, Rue Gustave Charpentier, Ternes, 17e, Paris, Île-de-France, France métropolitaine, 75017, France': (
        48.8821287, 2.28194325158052),
    'Sélect, Place de la Sorbonne, Sorbonne, 5e, Paris, Île-de-France, France métropolitaine, 75005, France': (
        48.8483795, 2.3426037),
    '9, Rue Sainte-Beuve, ND-des-Champs, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.843933, 2.3294674),
    '7, Rue Saint-Benoît, St-Germain-des-Prés, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.8549791, 2.3331645),
    'Salle Wagram, Avenue des Ternes, Ternes, 17e, Paris, Île-de-France, France métropolitaine, 75017, France': (
        48.8773913, 2.29661202440611),
    '6, Rue Buffault, Fg-Montmartre, 9e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.8750388, 2.3416153),
    'Hotel Ariston, Via Medici, Carrobbio, Municipio 1, Milano, MI, LOM, 20123, Italia': (45.46051805, 9.1813130955479),
    '30, Rue de Bassano, Chaillot, 16e, Paris, Île-de-France, France métropolitaine, 75116, France': (
        48.8692777, 2.297804),
    '1, Simmeringer Hauptstraße, Karrée St. Marx, KG Landstraße, Landstraße, Wien, 1110, Österreich': (
        48.18508715, 16.4046434926082),
    '11 Bis, Rue Balzac, Quartier du Faubourg-du-Roule, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8738634, 2.3005892),
    "Ribes & Casals, 7, Carrer de Roger de Llúria, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08010, España": (
        41.3901775, 2.1725133),
    '10, Joan Muyskenweg, Oost-Watergraafsmeer, Amsterdam, Oost, Amsterdam, Noord-Holland, Nederland, 1096CJ, Nederland': (
        52.3352478, 4.9135808),
    "Le saint, Rue du Pré aux Clercs, St-Thomas-d'Aquin, 7e, Paris, Île-de-France, France métropolitaine, 75007, France": (
        48.85654, 2.3303533),
    'Hotel Indigo, India Street, London, Greater London, England, EC3, UK': (51.5127693, -0.0758643588714969),
    'Park Grand London Hyde Park, Westbourne Terrace, Paddington, City of Westminster, London, Greater London, England, W2 6QA, UK': (
        51.5157289, -0.1801907),
    '12, Rue des Saussaies, Madeleine, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.871387, 2.3181242),
    "The Carphone Warehouse, Abingdon Road, Earl's Court, Royal Borough of Kensington and Chelsea, London, Greater London, England, W8 6SG, UK": (
        51.4993083, -0.197328463527457),
    'Hôtel Balmoral, Rue du Général Lanrezac, Ternes, 17e, Paris, Île-de-France, France métropolitaine, 75017, France': (
        48.87599585, 2.29395944615994),
    'The Loft, Lavington Street, Southwark, London Borough of Southwark, London, Greater London, England, SE15, UK': (
        51.505205, -0.099042),
    '5, Rue Saint-Roch, Palais Royal, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.8644421, 2.3315553),
    '10, Rue de Vaugirard, Odéon, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.8490664, 2.3397236),
    'Euston Tap, 190, Euston Road, Holborn, Somers Town, London Borough of Camden, London, Greater London, England, NW1 2EF, UK': (
        51.5269615, -0.132539109055514),
    "Canadian High Commission, 1, Grosvenor Square, St. James's, Mayfair, City of Westminster, London, Greater London, England, W1K 4AB, UK": (
        51.5115637, -0.149566770200753),
    '1, Old Jewry, London, Greater London, England, SE15, UK': (51.51377295, -0.090796958706241),
    '55, Rue Monge, St-Victor, 5e, Paris, Île-de-France, France métropolitaine, 75005, France': (48.8448049, 2.3524261),
    'Park Plaza Hotel, Newnham Terrace, Lambeth, London Borough of Lambeth, London, Greater London, England, SE15, UK': (
        51.4982466, -0.113368572916664),
    'Hôtel Paris Est Lafayette, Rue des Petits Hôtels, St-Vincent-de-Paul, 10e, Paris, Île-de-France, France métropolitaine, 75010, France': (
        48.8772727, 2.3543165),
    'Ritz Carlton, Schubertring, Stubenviertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.20225045, 16.3759786893866),
    "The One, Carrer de Provença, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08023, España": (
        41.39626165, 2.16298446685639),
    '155, Carrer de València, la Sagrada Família, Eixample, Barcelona, BCN, CAT, 08003, España': (
        41.3879879, 2.15668353979846),
    'Villa Saxe Eiffel, Villa de Saxe, École-Militaire, 7e, Paris, Île-de-France, France métropolitaine, 75007, France': (
        48.84980555, 2.30946222213336),
    'Novotel London Excel, 7, Western Gateway, Canning Town, Newham, London, Greater London, England, E16 1AA, UK': (
        51.5077041, 0.0229794993930712),
    '55–93, Knightsbridge, Belgravia, City of Westminster, London, Greater London, England, SW3 4, UK': (
        51.5020835, -0.157668723154223),
    "289, 291, Carrer de Còrsega, l'Antiga Esquerra de l'Eixample, Eixample, Barcelona, BCN, CAT, 08014, España": (
        41.39466285, 2.15640391997245),
    'Hilton Paris Opera, 108, Rue Saint-Lazare, Europe, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8757375, 2.32546439103936),
    'Bellevue, 5, Althanstraße, Thurygrund II, KG Alsergrund, Alsergrund, Wien, 1090, Österreich': (
        48.2264274, 16.3600966),
    'Hôtel Belfast, 10, Avenue Carnot, Ternes, 17e, Paris, Île-de-France, France métropolitaine, 75017, France': (
        48.8756414, 2.29388450946215),
    '32b, Rue Greuze, Porte-Dauphine, 16e, Paris, Île-de-France, France métropolitaine, 75116, France': (
        48.86456, 2.282139),
    'La Plata, 28, Carrer de la Mercè, el Gòtic, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (
        41.3804058, 2.1806395),
    'Hotel Barcelona Princess, 1, Avinguda Diagonal, el Besòs i el Maresme, Sant Martí, Barcelona, BCN, CAT, 08019, España': (
        41.41080905, 2.21854402643364),
    'Wulf & Lamb, 243, Pavilion Road, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW3 4, UK': (
        51.4935541, -0.1585905),
    '10, Rue Saint-Hyacinthe, Vendôme, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.8660964, 2.3315446),
    "NH Calderón, 26, Rambla de Catalunya, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08003, España": (
        41.3894619, 2.16634402107843),
    'DoubleTree by Hilton Hotel Milan, 77, Via Ludovico di Breme, Quartiere Varesina, Municipio 8, Milano, MI, LOM, 20156, Italia': (
        45.5001992, 9.13822263772499),
    'Princess, Argyle Street, Holborn, Bloomsbury, London Borough of Camden, London, Greater London, England, WC1X 8BB, UK': (
        51.5288283, -0.1231516),
    'Bianca Maria, Viale Premuda, Porta Monforte, Milano, MI, LOM, 20121, Italia': (45.4635255, 9.2071843),
    '176, Nieuwezijds Voorburgwal, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1012SJ, Nederland': (
        52.3741251, 4.8907713),
    "London Hilton on Park Lane, 22, Park Lane, St. James's, Mayfair, City of Westminster, London, Greater London, England, W1K 1BE, UK": (
        51.50557565, -0.150224277217833),
    "St Martins Lane Hotel, 45, St. Martin's Lane, St Clement Danes, Covent Garden, City of Westminster, London, Greater London, England, WC2N 4HX, UK": (
        51.5104275, -0.126265767294336),
    'Palais Corso, Kärntner Ring, Kärntner Viertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.2021729, 16.3722122163978),
    '4, Rue de Latran, Sorbonne, 5e, Paris, Île-de-France, France métropolitaine, 75005, France': (
        48.8496797, 2.346756),
    '1, Rue des Belles Feuilles, Porte-Dauphine, 16e, Paris, Île-de-France, France métropolitaine, 75116, France': (
        48.865766, 2.2829717),
    "The Nadler Victoria Hotel, Palace Place, St. James's, Victoria, City of Westminster, London, Greater London, England, SW3 4, UK": (
        51.4988623, -0.142758848396073),
    "83, Carrer d'Enric Granados, l'Antiga Esquerra de l'Eixample, Eixample, Barcelona, BCN, CAT, 08014, España": (
        41.3917121, 2.15663029996715),
    '1, Via Augusta, la Vila de Gràcia, Eixample, Barcelona, BCN, CAT, 08023, España': (41.3958325, 2.1552879),
    "Tiger Green, Half Moon Street, St. James's, Mayfair, City of Westminster, London, Greater London, England, SW3 4, UK": (
        51.50634, -0.145489),
    '60, Rue Richer, Fg-Montmartre, 9e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.8740905, 2.3425659),
    'Vigentina, Viale Bligny, Porta Vigentina, Municipio 5, Milano, MI, LOM, 20136, Italia': (
        45.451087, 9.1915641854154),
    'Hotel Primero Primera, 25, Carrer del Doctor Carulla, les Tres Torres, Sarrià - Sant Gervasi, Barcelona, BCN, CAT, 08017, España': (
        41.4003922, 2.12973805376075),
    'Porta Vigentina, Viale Bligny, Porta Vigentina, Municipio 5, Milano, MI, LOM, 20136, Italia': (
        45.450982, 9.19469062231178),
    "Batubar, 670, Gran Via de les Corts Catalanes, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08003, España": (
        41.3917553, 2.1717954),
    'l antic bocoi del gotic, Carrer del Sots-tinent Navarro, el Gòtic, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (
        41.3828091, 2.1793413),
    'The Victoria, 10, West Temple Sheen, Sheen Mount, East Sheen, Richmond-upon-Thames, London, Greater London, England, SW14 7RT, UK': (
        51.4609643, -0.2755738),
    'Novotel, 10, Europaboulevard, Zuideramstel, Amsterdam, Zuid, Amsterdam, Noord-Holland, Nederland, 1083AD;1083 AD, Nederland': (
        52.3336597, 4.8886357),
    '69, Boulevard Victor, Javel, 15e, Paris, Île-de-France, France métropolitaine, 75015, France': (
        48.8330588, 2.2879549),
    'Hilton London Euston, 17-18, Upper Woburn Place, Holborn, Bloomsbury, London Borough of Camden, London, Greater London, England, WC1H 0HT, UK': (
        51.5265283, -0.130246813721063),
    'Hôtel Novotel, 8, Place Marguerite de Navarre, Quartier des Halles, Les Halles, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.8608981, 2.3463825253406),
    'Best Western Sèvres Montparnasse, Rue de Vaugirard, Necker, 15e, Paris, Île-de-France, France métropolitaine, 75015, France': (
        48.84370535, 2.31558097218132),
    'Trianon Rive gauche, Rue de Vaugirard, Sorbonne, 6e, Paris, Île-de-France, France métropolitaine, 75005, France': (
        48.8487972, 2.3410105),
    'Britannia, Mare Street, Hackney, London Borough of Hackney, London, Greater London, England, E10, UK': (
        51.5459404, -0.0553962),
    '372, Green Lanes, Harringay, London Borough of Haringey, London, Greater London, England, N4 1DP, UK': (
        51.5743843, -0.09779315),
    "Park Plaza Victoria, 239, Vauxhall Bridge Road, St. James's, Victoria, City of Westminster, London, Greater London, England, SW1V 1EJ, UK": (
        51.4940587, -0.141620558984279),
    'Paul Smith, 223, Rue Saint-Honoré, Vendôme, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.865906, 2.3298418),
    'Le Relais Montmartre, Rue Constance, Grandes-Carrières, 18e, Paris, Île-de-France, France métropolitaine, 75018, France': (
        48.88545145, 2.33358040722013),
    'Holiday Inn, De Boelelaan, Zuideramstel, Amsterdam, Zuid, Amsterdam, Noord-Holland, Nederland, 1183, Nederland': (
        52.335192, 4.88852930006399),
    "St James's Hotel and Club, Park Place, St. James's, Mayfair, City of Westminster, London, Greater London, England, SW1A 1NN, UK": (
        51.5061183, -0.140342051354168),
    '21, Rue Félicien David, Auteuil, 16e, Paris, Île-de-France, France métropolitaine, 75015, France': (
        48.8493305, 2.2742708),
    "The Wellington, Rochester Row, St. James's, Pimlico, City of Westminster, London, Greater London, England, SW1, UK": (
        51.49448605, -0.13625655969888),
    'Hôtel Okko, 2, Rue du Colonel Pierre Avia, Javel, 15e, Paris, Île-de-France, France métropolitaine, 75015, France': (
        48.83271975, 2.27811899446183),
    'de Brakke Grond, Nesplein, Burgwallen-Oude Zijde, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1017, Nederland': (
        52.37104605, 4.89389713193508),
    '15, Rue de la Grande Chaumière, ND-des-Champs, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.8421083, 2.3304115),
    'Holiday Inn, 1/A, Via Ugo Bassi, Zona Farini, Isola, Milano, MI, LOM, 20159, Italia': (45.4887269, 9.1830526),
    'Starhotel Echo, 4, Viale Andrea Doria, Centrale, Municipio 2, Milano, MI, LOM, 20124, Italia': (
        45.4847135, 9.20727321109367),
    'Platine, Impasse S/15, Javel, 15e, Paris, Île-de-France, France métropolitaine, 75015, France': (
        48.8473814, 2.2833183),
    "Royal Mail, Park Lane, St. James's, Mayfair, City of Westminster, London, Greater London, England, SW3 4, UK": (
        51.5059438, -0.1512696),
    'Chesterton Road, Ladbroke Grove, Silchester Estate, North Kensington, Royal Borough of Kensington and Chelsea, London, Greater London, England, W10 5LU, UK': (
        51.5197913, -0.2114937),
    "9, Rue d'Argenson, Europe, 8e, Paris, Île-de-France, France métropolitaine, 75008, France": (
        48.8747343, 2.3167562),
    'Hôtel Alexander, Avenue Victor Hugo, Porte-Dauphine, 16e, Paris, Île-de-France, France métropolitaine, 75116, France': (
        48.8688648, 2.28279306452219),
    'Renaissance Amsterdam, Engelsesteeg, Burgwallen-Nieuwe Zijde, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1017, Nederland': (
        52.3780269, 4.8944036),
    'Novotel Paris Bercy, Rue de Bercy, 12e Arrondissement (urbain), Bercy, 12e, Paris, Île-de-France, France métropolitaine, 75012, France': (
        48.8388012, 2.3804572),
    'Best Western Opera Batignolles, Rue Dulong, Batignolles, 17e, Paris, Île-de-France, France métropolitaine, 75017, France': (
        48.88706855, 2.31435500224383),
    'Hôtel Westminster, Rue de la Paix, Gaillon, 1er, Paris, Île-de-France, France métropolitaine, 75002, France': (
        48.8693831, 2.3310566),
    'NH Carlton Amsterdam, 4, Vijzelstraat, Grachtengordel, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1017 HK, Nederland': (
        52.3664381, 4.892926),
    'SE11 26, Glasshouse Walk, Vauxhall, London Borough of Lambeth, London, Greater London, England, SE11, UK': (
        51.4886551, -0.1206258),
    'Hôtel Effeil-Blomet, 78, Rue Blomet, Necker, 15e, Paris, Île-de-France, France métropolitaine, 75015, France': (
        48.8416773, 2.30238705537826),
    '8, Rue Saint-Placide, ND-des-Champs, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.8498511, 2.3243899),
    'Salpêtrière, 13e, Paris, Île-de-France, France métropolitaine, 75013, France': (48.8424033, 2.3675868),
    '6, Via Senigallia, Bruzzano, Milano, MI, LOM, 20095, Italia': (45.5332007, 9.17113743185806),
    'The Chamberlain, 130-135, Minories, London, Greater London, England, EC3N 1NU, UK': (51.5121747, -0.0757376),
    "Holiday Inn Kings Cross, 1, King's Cross Road, Finsbury, London Borough of Islington, London, Greater London, England, WC1X 9HX, UK": (
        51.52625635, -0.113520681988214),
    'Villa Opéra Drouot, Rue Geoffroy Marie, Fg-Montmartre, 9e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.87321885, 2.3435781166738),
    'Silken Concordia, Avinguda del Paral·lel, el Poble-sec, Sants-Montjuïc, Barcelona, BCN, CAT, 08014, España': (
        41.374792, 2.161013),
    'Hotel Eurostars Vienna, 34-36, Ottakringer Straße, KG Hernals, Ottakring, Wien, 1170, Österreich': (
        48.2149769, 16.3365593),
    "Ca' Granda - Hotel Corte del Naviglio, Via Lodovico il Moro, Restocco Maroni, Milano, MI, LOM, 20144, Italia": (
        45.4435054, 9.1377147365944),
    'Streetkitchen, Eerste Constantijn Huygensstraat, Helmersbuurt, Amsterdam, West, Amsterdam, Noord-Holland, Nederland, 1053, Nederland': (
        52.3649706, 4.8734655),
    'Exact Change, Plaça dels Països Catalans, Sants, Sants-Montjuïc, Barcelona, BCN, CAT, 08014, España': (
        41.3794844, 2.1408159),
    'Legend Hotel by Elegancia, 151, Rue de Rennes, ND-des-Champs, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.8453963, 2.3255943),
    'Strand Palace Hotel, Exeter Street, St Clement Danes, Covent Garden, City of Westminster, London, Greater London, England, WC2E 7HA, UK': (
        51.5110762, -0.120932899130503),
    '5, Getreidemarkt, KG Mariahilf, Mariahilf, Wien, 1060, Österreich': (48.20045385, 16.3644713204448),
    'Lycée polyvalent privé Saint-Nicolas, Rue de Vaugirard, ND-des-Champs, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.84680515, 2.32524802076847),
    'Coq Hôtel, Rue Édouard Manet, Salpêtrière, 13e, Paris, Île-de-France, France métropolitaine, 75013, France': (
        48.83288365, 2.35729602219344),
    "Intercontinental London Park Lane, 17B, Curzon Street, St. James's, Mayfair, City of Westminster, London, Greater London, England, W1J 5HX, UK": (
        51.5038255, -0.150461623430574),
    '23D, Pieter de Hoochstraat, Museumkwartier, Amsterdam, Zuid, Amsterdam, Noord-Holland, Nederland, 1071ED, Nederland': (
        52.3560928, 4.885806),
    'Hôtel Malte Opéra - Astotel, Rue de Richelieu, Palais Royal, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.86720635, 2.33744821251946),
    "M by Montcalm Shoreditch, 151-157, City Road, Saint Luke's, London Borough of Islington, London, Greater London, England, EC1V 1JH, UK": (
        51.5278321, -0.0889557029276858),
    'UNA hotel Cusani, 13, Via Cusani, Castello, Municipio 1, Milano, MI, LOM, 20121, Italia': (45.4685226, 9.1833684),
    '33, Rue Cambon, Vendôme, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (48.8682642, 2.3268144),
    "17, Rue de l'Arcade, Madeleine, 8e, Paris, Île-de-France, France métropolitaine, 75008, France": (
        48.8721274, 2.3237134),
    'Hôtel Plaza Élysées, Boulevard Haussmann, Quartier du Faubourg-du-Roule, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.874647, 2.3057595),
    '40, Rue Liancourt, Petit-Montrouge, 14e, Paris, Île-de-France, France métropolitaine, 75014, France': (
        48.83472625, 2.3255319499698),
    'Hotel Capricorno, 3-4, Schwedenplatz, Stubenviertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.21109275, 16.3789326892857),
    '6, Rue Gustave Flaubert, Plaine-Monceau, 17e, Paris, Île-de-France, France métropolitaine, 75017, France': (
        48.8815451, 2.2992992),
    'Skandium, Egerton Gardens, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW3 4, UK': (
        51.4963963, -0.1689272),
    'W Barcelona, 1, Passeig Mare Nostrum, la Barceloneta, Ciutat Vella, Barcelona, BCN, CAT, 08039, España': (
        41.3687878, 2.19012463419563),
    'Hotel Maison Moschino, 12, Viale Monte Grappa, Municipio 1, Milano, MI, LOM, 20124, Italia': (
        45.48104575, 9.1900015075436),
    'Hotel Bristol, 1, Kärntner Ring, Kärntner Viertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.2027033, 16.3701848617386),
    'Hotel Rubens, 21, Via Pietro Rubens, Molinazzo, Milano, MI, LOM, 20148, Italia': (45.46711165, 9.14301144695151),
    "Buddha Bar Hotel Paris, 4, Rue d'Anjou, Madeleine, 8e, Paris, Île-de-France, France métropolitaine, 75008, France": (
        48.8694993, 2.3206396),
    '12, Rue Jean Goujon, Champs-Élysées, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8664557, 2.3085305),
    'Madison Hotel, Via Leopoldo Gasparotto, Centrale, Municipio 2, Milano, MI, LOM, 20124, Italia': (
        45.4881943, 9.2015953),
    'CER el Cle, Carrer dels Arcs, el Gòtic, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (41.3845837, 2.174319),
    "Le Lumière, 1, Rue Scribe, Chaussée-d'Antin, 9e, Paris, Île-de-France, France métropolitaine, 75009, France": (
        48.8704636, 2.3297136),
    'Best Western Hotel Mozart, Via Giuseppe Mussi, Zona Sempione, Bullona, Milano, MI, LOM, 20154, Italia': (
        45.48340325, 9.16661771273842),
    "44, Welbeck Street, St. James's, Marylebone, City of Westminster, London, Greater London, England, W1G 8ED, UK": (
        51.5182588, -0.149853799999999),
    "Tophams Hotel, 24-32, Ebury Street, St. James's, Victoria, City of Westminster, London, Greater London, England, SW3 4, UK": (
        51.49575535, -0.147778632853489),
    'Meissl & Schadn, 10-12, Schubertring, Kärntner Viertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.20226, 16.3749365),
    '117, Rue Lauriston, Chaillot, 16e, Paris, Île-de-France, France métropolitaine, 75116, France': (
        48.8663766, 2.2867453),
    "647, Gran Via de les Corts Catalanes, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08003, España": (
        41.3927014, 2.1722123),
    "Grosvenor House Hotel, 90, Park Lane, St. James's, Mayfair, City of Westminster, London, Greater London, England, W1K 7TN, UK": (
        51.5095847, -0.15505774779728),
    'Up on The Roof, 4, Rue Danton, Monnaie, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.8528186, 2.3422724),
    'MK2 Parnasse, Rue Jules Chaplain, ND-des-Champs, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.8427585, 2.3305253),
    'Hôtel de Banville, 166, Boulevard Berthier, Plaine-Monceau, 17e, Paris, Île-de-France, France métropolitaine, 75017, France': (
        48.8864077, 2.2949505),
    'The Piccadilly London West End Hotel, 65-73, Shaftesbury Avenue, Chinatown, City of Westminster, London, Greater London, England, WC2H 8DP, UK': (
        51.51222415, -0.13181159069796),
    "142, 146, Carrer de Balmes, l'Antiga Esquerra de l'Eixample, Eixample, Barcelona, BCN, CAT, 08023, España": (
        41.3940183, 2.15699181721875),
    'Radisson Blu Edwardian Bloomsbury Street Hotel, 9, Bloomsbury Street, Holborn, St Giles, London Borough of Camden, London, Greater London, England, WC1B 3QD, UK': (
        51.5174732, -0.127706112347417),
    'Burgundy Paris, Rue Duphot, Vendôme, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.8679659, 2.3258303),
    'Park Inn, 16-18, Wagramer Straße, KG Kaisermühlen, Donaustadt, Neukagran, Wien, 1220, Österreich': (
        48.2340936, 16.4209871159201),
    'Western Marble Arch Synagogue, 32, Great Cumberland Place, Marylebone, City of Westminster, London, Greater London, England, W1H 7TP, UK': (
        51.5149476, -0.158958129837622),
    "Ipo's Coffee Gallery, 29, Piet Heinkade, Amsterdam, Oost, Amsterdam, Noord-Holland, Nederland, 1019 BR, Nederland": (
        52.3778708, 4.9141862),
    'The Nadler, 10, Carlisle Street, Soho, City of Westminster, London, Greater London, England, W1D 3BS, UK': (
        51.51476665, -0.134070373233372),
    'École maternelle et primaire Madame, Rue Honoré Chevalier, Odéon, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.84907885, 2.3314175612149),
    'Ibis Milano Ca Granda, Via Val Cismon, Pratocentenaro, Milano, MI, LOM, 20124, Italia': (
        45.5064946, 9.19685371708968),
    'Pestana Chelsea Bridge Hotel & Spa, 354, Queenstown Road, Nine Elms, London Borough of Wandsworth, London, Greater London, England, SW8 4AE, UK': (
        51.48154045, -0.148169012878151),
    '25hours Hotel, 1-3, Lerchenfelder Straße, Buchfeld, KG Josefstadt, Josefstadt, Wien, 1070, Österreich': (
        48.2064573, 16.3546387999155),
    'Mettez, Rue Chauveau-Lagarde, Madeleine, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8715797, 2.3225222),
    'Hôtel Bercy Gare de Lyon, Rue de Charenton, 12e Arrondissement (urbain), Bercy, 12e, Paris, Île-de-France, France métropolitaine, 75012, France': (
        48.8393596, 2.3892373),
    '15, Franz-Josefs-Kai, Stubenviertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.2113426, 16.377647),
    "Casa D'Oro Luciani, 32, Ratschkygasse, Untermeidling, KG Meidling, Meidling, Kabelwerk, Wien, 1120, Österreich": (
        48.1777589, 16.3243440917763),
    'Chloé, 253, Rue Saint-Honoré, Vendôme, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.8671519, 2.3268748),
    'Unknown, Carrer del Regomir, el Gòtic, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (41.3811385, 2.1795401),
    '75, Oudeschans, Nieuwmarktbuurt, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1011KW, Nederland': (
        52.3703206, 4.9031481),
    '9, Rue Magellan, Champs-Élysées, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8703215, 2.2998367),
    "Plaça d'Espanya, Gran Via de les Corts Catalanes, Hostafrancs, Eixample, Barcelona, BCN, CAT, 08014, España": (
        41.3750291, 2.14913234977835),
    "115, 117, Carrer de Balmes, l'Antiga Esquerra de l'Eixample, Eixample, Barcelona, BCN, CAT, 08014, España": (
        41.39209465, 2.15847602853627),
    "5, Place de l'Odéon, Odéon, 6e, Paris, Île-de-France, France métropolitaine, 75006, France": (48.8497667, 2.33922),
    "Astra, Rue de Caumartin, Chaussée-d'Antin, 9e, Paris, Île-de-France, France métropolitaine, 75009, France": (
        48.87182765, 2.32788571483759),
    "Hôtel d'Orsay, 93, Rue de Lille, St-Germain-des-Prés, 6e, Paris, Île-de-France, France métropolitaine, 75006, France": (
        48.8603935, 2.3231363),
    "Holiday Inn Mayfair, 3, Berkeley Street, St. James's, Mayfair, City of Westminster, London, Greater London, England, W1J 8NE, UK": (
        51.5077103, -0.142416472500238),
    '27-29, Wiedner Hauptstraße, Freihausviertel, KG Wieden, Wieden, Wien, 1040, Österreich': (48.1953087, 16.3673067),
    'Hôtel Stendhal Paris Place Vendôme MGallery by Sofitel, Rue Danielle Casanova, Gaillon, 1er, Paris, Île-de-France, France métropolitaine, 75002, France': (
        48.86813385, 2.33133732623676),
    'Mercadona, Travessera de les Corts, la Maternitat i Sant Ramon, les Corts, Barcelona, BCN, CAT, 08014, España': (
        41.381252, 2.1267921),
    'breizh, Rue Grégoire de Tours, Monnaie, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.8533204, 2.3379667),
    '34, Rue Jean Mermoz, Madeleine, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8717259, 2.3122686),
    'Hôtel La Comtesse by Elegancia, 29, Avenue de Tourville, École-Militaire, 7e, Paris, Île-de-France, France métropolitaine, 75007, France': (
        48.8539009, 2.307242),
    "178, Carrer de Mallorca, l'Antiga Esquerra de l'Eixample, Eixample, Barcelona, BCN, CAT, 08014, España": (
        41.3890368, 2.15667109540584),
    "Cavendish, 81-84, Jermyn Street, St. James's, Mayfair, City of Westminster, London, Greater London, England, SW1Y 6JF, UK": (
        51.50781625, -0.13780200914142),
    'Hotel Capitol, 6, Via Domenico Cimarosa, Porta Vercellina, Milano, MI, LOM, 20145, Italia': (
        45.4663201, 9.1587332),
    '3, Weihburggasse, Kärntner Viertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.2071275, 16.3722924),
    "Four Seasons Hotel, Park Lane, Hamilton Mews, St. James's, Belgravia, City of Westminster, London, Greater London, England, W1J 7DR, UK": (
        51.504433, -0.149785887003609),
    'Hotel Colon, Avinguda de la Catedral, el Gòtic, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (
        41.3850146, 2.1758364),
    '8, Rue Laferrière, Nouvelle Athènes, St-Georges, 9e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.8785609, 2.3384118),
    'Regency Hotel, 19, Nottingham Place, Marylebone, City of Westminster, London, Greater London, England, W1U 5LQ, UK': (
        51.52151495, -0.153422321768982),
    "6, Plaça d'Urquinaona, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08010, España": (
        41.38969525, 2.17196526800052),
    'Hilton London Wembley, Lakeside Way, Preston, London Borough of Brent, London, Greater London, England, HA9 0BU, UK': (
        51.55731545, -0.28282454699406),
    '15, Rue Gît-le-Coeur, Monnaie, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.8535751, 2.3425458),
    'Hotel Abba, Carrer de Numància, les Corts, Barcelona, BCN, CAT, 08014, España': (41.3825674, 2.1400415),
    'Fox @ Excel, Western Gateway, Canning Town, Newham, London, Greater London, England, E12, UK': (
        51.5088147, 0.0255735),
    'Belle et Zen, Rue René Boulanger, Porte-St-Martin, 10e, Paris, Île-de-France, France métropolitaine, 75010, France': (
        48.8684134, 2.3610677),
    'Hotel Magna Pars Suites, Via Vincenzo Forcella, Zona Tortona, Municipio 6, Milano, MI, LOM, 20136, Italia': (
        45.4525437, 9.1670327),
    "Brown's Hotel, 30, Albemarle Street, St. James's, Mayfair, City of Westminster, London, Greater London, England, W1S 4BP, UK": (
        51.50907805, -0.142169748566165),
    'Hotel Spadari, 11, Via Spadari, Cordusio, Municipio 1, Milano, MI, LOM, 20123, Italia': (45.4635796, 9.1869623),
    'Hotel am Konzerthaus, 35-37, Am Heumarkt, Botschaftsviertel, KG Landstraße, Landstraße, Wien, 1030, Österreich': (
        48.1996448, 16.3773488),
    'The College Hotel, 1, Roelof Hartstraat, Oud-Zuid, Amsterdam, Zuid, Amsterdam, Noord-Holland, Nederland, 1071VE, Nederland': (
        52.3527763, 4.8836858),
    'Café Americain, Leidseplein, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1017, Nederland': (
        52.3638967, 4.8813718),
    'London Bridge Hotel, London Bridge Street, Borough, London Borough of Southwark, London, Greater London, England, SE15, UK': (
        51.5051397, -0.0880618296057679),
    'Acca Palace, 9, Via Giovanni Nicotera, Affori, Milano, MI, LOM, 20161, Italia': (45.5105117, 9.1745698),
    "Hôtel Banke, Rue de la Fayette, Chaussée-d'Antin, 9e, Paris, Île-de-France, France métropolitaine, 75009, France": (
        48.8736554, 2.3360245),
    'London Marriott Hotel Maida Vale, Plaza Parade, South Hampstead, London Borough of Camden, London, Greater London, England, NW6 5RP, UK': (
        51.5357268, -0.190416129949063),
    '13, Sonnwendgasse, Sonnwendviertel, KG Favoriten, Favoriten, Wien, 1100, Österreich': (
        48.18291045, 16.3778165381006),
    'E115, Montague Street, Holborn, Bloomsbury, London Borough of Camden, London, Greater London, England, WC1B 5BH, UK': (
        51.5202894, -0.1261195),
    'Jocs Mallart, Carrer de Jaume I, el Gòtic, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (
        41.3836253, 2.1782236),
    'Best Western Elysées Paris Monceau, Rue de Constantinople, Europe, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8803508, 2.3196013),
    '20, Rue du Colisée, Quartier du Faubourg-du-Roule, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8710024, 2.3091653),
    'Ristorante Settimo Cielo, 3, Singerstraße, Kärntner Viertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.2078671, 16.3723947),
    '143, Avenue de Malakoff, Chaillot, 16e, Paris, Île-de-France, France métropolitaine, 75116, France': (
        48.875555, 2.2836747),
    "373, Avinguda Diagonal, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08023, España": (
        41.3964326, 2.16115023809723),
    '13, Rue Saint-Sulpice, Odéon, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.8514592, 2.3374911),
    'Di@rdamo, Eslarngasse, Fasanviertel, KG Landstraße, Landstraße, Wien, 1030, Österreich': (48.1963605, 16.3958386),
    '5, Rue de Ponthieu, Quartier du Faubourg-du-Roule, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8701324, 2.3111491),
    "Mercure Blanqui Place d'Italie, Rue du Père Guérin, Cité florale, Maison-Blanche, 13e, Paris, Île-de-France, France métropolitaine, 75013, France": (
        48.8302035, 2.35299461628129),
    'Hotel Enterprise, Corso Sempione, Zona Sempione, Portello, Milano, MI, LOM, 20148, Italia': (
        45.4867899, 9.1573812),
    'Les Jardins du Marais, Rue Amelot, St-Ambroise, 11e, Paris, Île-de-France, France métropolitaine, 75011, France': (
        48.8605485, 2.3680184),
    '15, Gower Street, Holborn, Bloomsbury, London Borough of Camden, London, Greater London, England, WC1E 6BT, UK': (
        51.52034735, -0.130519281631806),
    '14, West Halkin Street, Belgravia, City of Westminster, London, Greater London, England, SW3 4, UK': (
        51.49906655, -0.156237668330559),
    "DoubleTree by Hilton Hotel London - Victoria, 2, Bridge Place, St. James's, Victoria, City of Westminster, London, Greater London, England, SW1V 1QA, UK": (
        51.49391735, -0.143290327422053),
    'Conservatorium, Van Baerlestraat, Museumkwartier, Amsterdam, Zuid, Amsterdam, Noord-Holland, Nederland, 1053, Nederland': (
        52.3587108, 4.87855020026744),
    "Queen's Gate Hotel, 31-34, Queen's Gate, Brompton, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW7 5JA, UK": (
        51.49817255, -0.180079316574893),
    'Stazione Centrale M2 M3, Piazza Quattro Novembre, Centrale, Municipio 2, Milano, MI, LOM, 20124, Italia': (
        45.4868663, 9.2020524),
    '71-1, Chasséstraat, De Baarsjes, Amsterdam, West, Amsterdam, Noord-Holland, Nederland, 1057JA, Nederland': (
        52.3696298, 4.8612785),
    'Famdeburguer, Carrer de Riego, Sants, Sants-Montjuïc, Barcelona, BCN, CAT, 08014, España': (41.377233, 2.1384492),
    'Four Seasons Hotel, Gloucester Place, Marylebone, City of Westminster, London, Greater London, England, NW1 6DX, UK': (
        51.5241093, -0.1608709),
    "550, Gran Via de les Corts Catalanes, la Nova Esquerra de l'Eixample, Eixample, Barcelona, BCN, CAT, 08014, España": (
        41.3830816, 2.16056949587517),
    'One Aldwych, 1, Aldwych, St Clement Danes, Covent Garden, City of Westminster, London, Greater London, England, WC2B 4BZ, UK': (
        51.51176615, -0.11939404976184),
    '9, Petersplatz, Widmerviertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (48.2097285, 16.3704271),
    'Hotel Café Royal, Glasshouse Street, Soho, City of Westminster, London, Greater London, England, W1B 5AR, UK': (
        51.51018365, -0.135712940362751),
    '2, Rue Duperré, Quartier Saint-Georges, St-Georges, 9e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.8821499, 2.3367452),
    '1, Daungasse, Buchfeld, KG Josefstadt, Josefstadt, Wien, 1080, Österreich': (48.21335105, 16.3471604567262),
    "The Chesterfield Hotel, 35, Charles Street, St. James's, Mayfair, City of Westminster, London, Greater London, England, W1J 5EB, UK": (
        51.50768235, -0.146999479166664),
    '5, Rue du Mont Thabor, Vendôme, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.8654306, 2.3292701),
    "272, Carrer de Còrsega, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08008, España": (
        41.39537865, 2.15950999134717),
    'The Ring, 8, Kärntner Ring, Kärntner Viertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.2016507, 16.3710087829938),
    'La croix de Malte, Rue de Malte, Folie-Méricourt, 11e, Paris, Île-de-France, France métropolitaine, 75011, France': (
        48.8636313, 2.3690033),
    '16, Rue de Sèze, Madeleine, 9e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8705268, 2.3263724),
    'Andaz Hotel, Prinsengracht, Negen Straatjes, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1017, Nederland': (
        52.3678418, 4.8829317),
    '20, NDSM-plein, NDSM, Amsterdam, Noord, Amsterdam, Noord-Holland, Nederland, 1033WB, Nederland': (
        52.4004147, 4.8933075),
    'Zu den drei großen Kronen, Kirchberggasse, KG Neubau, Neubau, Wien, 1070, Österreich': (
        48.20373545, 16.3560146979069),
    'Louvre Montana, Rue Saint-Roch, Palais Royal, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.864469, 2.3318128),
    "Excelsior Hotel Gallia, Piazza Duca d'Aosta, Centrale, Municipio 2, Milano, MI, LOM, 20124, Italia": (
        45.4860073, 9.20205388103135),
    'Apollohal, Apollolaan, Oud-Zuid, Amsterdam, Zuid, Amsterdam, Noord-Holland, Nederland, 1017, Nederland': (
        52.3484817, 4.88427057201087),
    'Hotel dei Cavalieri, 1, Piazza Giuseppe Missori, Bottonuto, Municipio 1, Milano, MI, LOM, 20123, Italia': (
        45.4608911, 9.1888069),
    "Subway, 4, Berners Street, St. James's, Fitzrovia, City of Westminster, London, Greater London, England, W1T 3LE, UK": (
        51.5165038, -0.1360625),
    'Hilton Garden Inn Vienna South, 5, Hertha-Firnberg-Straße, Triesterviertel, KG Inzersdorf Stadt, Favoriten, Wien, 1100, Österreich': (
        48.166765, 16.3450386),
    "Georgian House Hotel, 35-39, St George's Drive, St. James's, Pimlico, City of Westminster, London, Greater London, England, SW1V 1PH, UK": (
        51.490612, -0.143831156933076),
    '10-16, Hietzinger Hauptstraße, KG Hietzing, Hietzing, Wien, 1130, Österreich': (48.1866691, 16.3023705),
    '7, Place Boulnois, Ternes, 17e, Paris, Île-de-France, France métropolitaine, 75017, France': (
        48.8793621, 2.295847),
    "Restaurant Pau Claris 190, 190, Carrer de Pau Claris, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08037, España": (
        41.3966517, 2.1622492),
    'Rosewood London, 252, High Holborn, Holborn, St Giles, London Borough of Camden, London, Greater London, England, WC1V 7EN, UK': (
        51.51735555, -0.117567313292327),
    'Hotel de Lille, 40, Rue de Lille, St-Germain-des-Prés, 6e, Paris, Île-de-France, France métropolitaine, 75007, France': (
        48.8585295, 2.3299131),
    "Saint-Pétersbourg, Rue de Caumartin, Chaussée-d'Antin, 9e, Paris, Île-de-France, France métropolitaine, 75009, France": (
        48.8721186, 2.3280405),
    "46, Passeig de Gràcia, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08003, España": (
        41.39194845, 2.16605441939301),
    "3, Rue de l'Abbé de l'Épée, Val-de-Grâce, 5e, Paris, Île-de-France, France métropolitaine, 75005, France": (
        48.8430547, 2.3422878),
    '35, Avenue Hoche, Quartier du Faubourg-du-Roule, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8758743, 2.3005281),
    'Armani Building, Via Alessandro Manzoni, Borgonuovo, Municipio 1, Milano, MI, LOM, 20121, Italia': (
        45.47057115, 9.19295148860007),
    'Park Hyatt Milano, 1, Via Tommaso Grossi, Scala, Municipio 1, Milano, MI, LOM, 20121, Italia': (
        45.4655528, 9.1889231),
    '65, Rue des Saints-Pères, St-Germain-des-Prés, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.853396, 2.3298408),
    '4, Carrer de les Magdalenes, el Gòtic, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (
        41.3859443, 2.1751397050895),
    'Thistle Hyde Park, Lancaster Gate, Paddington, City of Westminster, London, Greater London, England, W2 3LG, UK': (
        51.51116595, -0.180875420413342),
    'Place Vendôme, Vendôme, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.8674634, 2.32942811682519),
    "Hilton London Green Park, Half Moon Street, St. James's, Mayfair, City of Westminster, London, Greater London, England, W1J 7BN, UK": (
        51.5064449, -0.1456241),
    '15, Rue de Bassano, Chaillot, 16e, Paris, Île-de-France, France métropolitaine, 75116, France': (
        48.8690031, 2.2972085),
    '103-109, Carrer de Casp, el Fort Pienc, Eixample, Barcelona, BCN, CAT, 08013, España': (
        41.39619175, 2.17931180062477),
    '14, Via Santa Radegonda, Duomo, Municipio 1, Milano, MI, LOM, 20121, Italia': (45.4656962, 9.1916929),
    '40, Via Laietana, el Gòtic, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (41.386099, 2.17640041372549),
    'Holland Gardens, Holland Road, Silchester Estate, Royal Borough of Kensington and Chelsea, London, Greater London, England, W14 8HN, UK': (
        51.4988266, -0.2090005),
    "Hôtel Opéra Marigny, Rue de l'Arcade, Madeleine, 8e, Paris, Île-de-France, France métropolitaine, 75008, France": (
        48.87175825, 2.32349071300578),
    '6, Köllnerhofgasse, Stubenviertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (48.2105491, 16.376052),
    "181, Carrer de Mallorca, l'Antiga Esquerra de l'Eixample, Eixample, Barcelona, BCN, CAT, 08014, España": (
        41.3896178, 2.15624255711864),
    'Mercure Paris Opera Grands Boulevards, Rue des Petites Écuries, Porte-St-Denis, 10e, Paris, Île-de-France, France métropolitaine, 75010, France': (
        48.8740857, 2.35021204716738),
    "The Grange Rochester Hotel, Vane Street, St. James's, Victoria, City of Westminster, London, Greater London, England, SW1, UK": (
        51.4942188, -0.136533878857181),
    "Acevi Villaroel, Carrer de Villarroel, l'Antiga Esquerra de l'Eixample, Eixample, Barcelona, BCN, CAT, 08014, España": (
        41.38541425, 2.15677613651317),
    'Hôtel Mercure, Rue de la Fédération, Grenelle, 15e, Paris, Île-de-France, France métropolitaine, 75015, France': (
        48.8547898, 2.29231931416315),
    'Westin Palace, 20, Piazza della Repubblica, Porta Nuova, Milano, MI, LOM, 20124, Italia': (
        45.4787674, 9.19929891487337),
    'Me London, 336-337, Strand, St Clement Danes, Covent Garden, City of Westminster, London, Greater London, England, WC2R 1ES, UK': (
        51.51173865, -0.118558253972165),
    'Waldorf Astoria Amsterdam, 542-556, Herengracht, Grachtengordel, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1017CG, Nederland': (
        52.3646205, 4.89693309784715),
    'Hotel Miramar Barcelona, Carretera de Miramar, Montjuïc, Sants-Montjuïc, Barcelona, BCN, CAT, 08038, España': (
        41.3700759, 2.17133805414879),
    'Maison Borella, 8, Alzaia Naviglio Grande, Zona Navigli, Municipio 6, Milano, MI, LOM, 20144, Italia': (
        45.4521255, 9.175853),
    '20 bis, Rue de la Gaîté, Montparnasse, 14e, Paris, Île-de-France, France métropolitaine, 75014, France': (
        48.8397286, 2.3235027),
    'Best Western Blue Sqare Hotel, Krijn Breurstraat, Slotermeer, Amsterdam, Nieuw-West, Amsterdam, Noord-Holland, Nederland, 1063, Nederland': (
        52.37861155, 4.82091323010651),
    'Club Quarters, 24, Ludgate Hill, Temple, London, Greater London, England, EC4, UK': (51.5138704, -0.1011565),
    'The Crosse Keys, 7/12, Gracechurch Street, London, Greater London, England, EC3V 0DR, UK': (51.5126631, -0.084714),
    "Ten Manchester Street, 10, Manchester Street, St. James's, Marylebone, City of Westminster, London, Greater London, England, W1U 4DG, UK": (
        51.5186459, -0.153776403705635),
    'Pierre Gagnaire, 6, Rue Balzac, Quartier du Faubourg-du-Roule, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8733364, 2.3004153),
    '11, Rue Godot de Mauroy, Vendôme, 9e, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.8709285, 2.3268483),
    'BP Oude Haagseweg, Oude Haagseweg, Slotervaart, Amsterdam, Nieuw-West, Amsterdam, Noord-Holland, Nederland, 1066, Nederland': (
        52.3374762, 4.8181272),
    'Barclays, Old Brompton Road, Brompton, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW7, UK': (
        51.4923437, -0.1780663),
    'Steigenberger Hotel Herrenhof, 10, Herrengasse, Schottenviertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.2098594, 16.3662660214102),
    "Majestic Hotel & Spa, 3, Passatge dels Camps Elisis, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08003, España": (
        41.3937039, 2.16418040967696),
    'Hôtel ibis Styles Paris Gare Saint-Lazare, 9, Rue de Constantinople, Europe, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8796982, 2.3209703),
    '4, Rue de la Comète, Gros-Caillou, 7e, Paris, Île-de-France, France métropolitaine, 75007, France': (
        48.8595504, 2.3088684),
    'Style Hotel, 1, Via delle Erbe, Brera, Municipio 1, Milano, MI, LOM, 20121, Italia': (45.4709058, 9.1841599),
    "The Connaught, Adam's Row, St. James's, Mayfair, City of Westminster, London, Greater London, England, SW3 4, UK": (
        51.51018605, -0.149779503904675),
    'Les Fondus de la Raclette, 209, Boulevard Raspail, Montparnasse, 14e, Paris, Île-de-France, France métropolitaine, 75014, France': (
        48.8410868, 2.3302507),
    "4, Boulevard Raspail, St-Thomas-d'Aquin, 7e, Paris, Île-de-France, France métropolitaine, 75007, France": (
        48.8552934, 2.325538),
    "644, Gran Via de les Corts Catalanes, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08003, España": (
        41.3901392, 2.1696502),
    '1, Avenue Carnot, Ternes, 17e, Paris, Île-de-France, France métropolitaine, 75017, France': (48.8747777, 2.293732),
    'Chelsea Harbour, Thames Avenue, Chelsea Harbour, Sands End, London Borough of Hammersmith and Fulham, London, Greater London, England, SW10 0UX, UK': (
        51.47536985, -0.181046742926716),
    "2, Rue d'Artois, Quartier du Faubourg-du-Roule, 8e, Paris, Île-de-France, France métropolitaine, 75008, France": (
        48.8722763, 2.308991),
    '22, Rue de la Parcheminerie, Îlot Saint-Séverin, Sorbonne, 5e, Paris, Île-de-France, France métropolitaine, 75005, France': (
        48.8518075, 2.3447847),
    'Hotel Melià Il Duca, 13, Piazza della Repubblica, Porta Nuova, Milano, MI, LOM, 20124, Italia': (
        45.479418, 9.1961835),
    '23, Gower Street, Holborn, Bloomsbury, London Borough of Camden, London, Greater London, England, WC1E 6BT, UK': (
        51.52056685, -0.130773518368212),
    'Officine Panerai, 3/5, Rue de la Paix, Gaillon, 1er, Paris, Île-de-France, France métropolitaine, 75002, France': (
        48.8688082, 2.3305268),
    'Il Capriccio, Viale Andrea Doria, Zona Buenos Aires, Municipio 3, Milano, MI, LOM, 20124, Italia': (
        45.4853972, 9.2116928),
    'Russell Court, Coram Street, Holborn, Bloomsbury, London Borough of Camden, London, Greater London, England, WC1N 1HB, UK': (
        51.5237404, -0.126367293348624),
    'Lansbury Hotel, 117, Poplar High Street, Poplar, London Borough of Tower Hamlets, London, Greater London, England, E14 0AS, UK': (
        51.5091914, -0.0157041630000005),
    'World Trade Center Barcelona, Moll de Barcelona, el Raval, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (
        41.3714013, 2.18233997400114),
    'DoubleTree by Hilton Hotel London - Marble Arch, 4, Bryanston Street, Marylebone, City of Westminster, London, Greater London, England, W1H 7BY, UK': (
        51.5146111, -0.1566998),
    'Trafalgar Square / Charing Cross Station, Strand, St Clement Danes, Covent Garden, City of Westminster, London, Greater London, England, WC2, UK': (
        51.5082824, -0.1262415),
    'Hotel Manin, 7, Via Daniele Manin, Porta Nuova, Milano, MI, LOM, 20121, Italia': (45.4740024, 9.1960177),
    'Hilton London Angel Islington, 53, Upper Street, Islington, London Borough of Islington, London, Greater London, England, N1 0UY, UK': (
        51.53596525, -0.104814345821145),
    "Shepherd's Bush Market, Brook Green, London Borough of Hammersmith and Fulham, London, Greater London, England, W12 8DG, UK": (
        51.5054194, -0.2262459),
    'Charlotte Street Hotel, 15-17, Charlotte Street, Holborn, London Borough of Camden, London, Greater London, England, W1T 1RJ, UK': (
        51.5183675, -0.135027890609857),
    'Cristal, 9, Rue Washington, Quartier du Faubourg-du-Roule, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.872633, 2.3021016), 'Centrale, Via Roberto Lepetit, Centrale, Municipio 2, Milano, MI, LOM, 20124, Italia': (
        45.484057, 9.20551649645382),
    'Hotel Pullman Barcelona Skipper, 10, Carrer de Trelawny, la Barceloneta, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (
        41.3858137, 2.19500408206622),
    'Falcon Wharf, 34, Lombard Road, Battersea, London Borough of Wandsworth, London, Greater London, England, SW11 3, UK': (
        51.4703493, -0.177955339932134),
    'Corvinus, 57-59, Mariahilfer Straße, Ratzenstadl, KG Mariahilf, Mariahilf, Wien, 1060, Österreich': (
        48.1990376, 16.3524748),
    'Hôtel Hor, Rue La Fayette, St-Vincent-de-Paul, 10e, Paris, Île-de-France, France métropolitaine, 75010, France': (
        48.8792713, 2.35767157548591),
    'Novotel London Tower Bridge, Pepys Street, London, Greater London, England, EC3, UK': (
        51.5105749, -0.0775135076963129),
    'Marriott Rive Gauche, Boulevard Saint-Jacques, Montsouris, Parc-Montsouris, 14e, Paris, Île-de-France, France métropolitaine, 75014, France': (
        48.83165665, 2.33986031814801),
    '64, Avenue Marceau, Champs-Élysées, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8705873, 2.2980109),
    'The Montague on the Gardens, 15, Montague Street, Holborn, Bloomsbury, London Borough of Camden, London, Greater London, England, WC1B 5BJ, UK': (
        51.52013845, -0.125523852546695),
    'Rainers Hotel, 184, Gudrunstraße, KG Favoriten, Favoriten, Wien, 1100, Österreich': (48.1799879, 16.3625354645315),
    "Hyde Park Corner Screen, Knightsbridge, St. James's, Belgravia, City of Westminster, London, Greater London, England, SW3 4, UK": (
        51.503227, -0.152299201033497),
    'Hotel Gallitzinberg, 32, Johann-Staud-Straße, KG Ottakring, Ottakring, Wien, 1160, Österreich': (
        48.21452095, 16.284588479368),
    'Quadrilatero della Moda, Via Gesù, Quadrilatero della Moda, Municipio 1, Milano, MI, LOM, 20121, Italia': (
        45.46952695, 9.19531484904891),
    '2, Rue Saint-Sulpice, Odéon, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.8515839, 2.3381366),
    'the guest house, Führichgasse, Kärntner Viertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.2051419, 16.3690801),
    '23, Wallgasse, Obere Windmühle, KG Mariahilf, Mariahilf, Wien, 1060, Österreich': (48.1919228, 16.3391422876577),
    '9, Via Poliziano, Zona Sempione, Municipio 8, Milano, MI, LOM, 20154, Italia': (45.4835821, 9.1648393),
    "L'Hôtel du Collectionneur, 51-57, Rue de Courcelles, Quartier du Faubourg-du-Roule, 8e, Paris, Île-de-France, France métropolitaine, 75008, France": (
        48.8769651, 2.3069884),
    'Bupa, Barter Street, Holborn, St Giles, London Borough of Camden, London, Greater London, England, WC1A 2LX, UK': (
        51.5177702, -0.123200550016404),
    '48-50, Upper Richmond Road, Southfields, London Borough of Wandsworth, London, Greater London, England, SW19, UK': (
        51.45727705, -0.20561188958587),
    '5-7, Harmoniegasse, Thurygrund II, KG Alsergrund, Alsergrund, Wien, 1090, Österreich': (48.2198924, 16.3599121),
    'BNP Paribas, Rue Sainte-Cécile, Fg-Montmartre, 9e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.87326805, 2.3461591199112),
    'Novotel Pari Gare Montparnasse, Rue du Cotentin, Necker, 15e, Paris, Île-de-France, France métropolitaine, 75015, France': (
        48.8384924, 2.3151043),
    '57, Drayton Gardens, Brompton, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW10, UK': (
        51.48887125, -0.180981102621912),
    "214, 216, Carrer Aragó, l'Antiga Esquerra de l'Eixample, Eixample, Barcelona, BCN, CAT, 08014, España": (
        41.3881911, 2.16011040533937),
    "Pierre Herme, 39, Avenue de l'Opéra, Gaillon, 1er, Paris, Île-de-France, France métropolitaine, 75002, France": (
        48.8683415, 2.3330811),
    'Capital Hotel, Basil Street, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW3 4, UK': (
        51.5001038, -0.1614634),
    'Casino BCN, Carrer de la Marina, la Vila Olímpica del Poblenou, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (
        41.38656195, 2.19706652243787),
    "64, Rue de l'Arbre Sec, Quartier des Halles, Les Halles, 1er, Paris, Île-de-France, France métropolitaine, 75001, France": (
        48.86127, 2.3426083),
    "Durrants, 26-32, George Street, St. James's, Marylebone, City of Westminster, London, Greater London, England, W1H 5BJ, UK": (
        51.51800395, -0.153202387354534),
    'Hotel Melià Barcelona, 46, 50, Avinguda de Sarrià, les Corts, Barcelona, BCN, CAT, 08014, España': (
        41.3910379, 2.14181022336509),
    'Holiday Inn, Rue de Penthièvre, Madeleine, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8730086, 2.31615198104313),
    'Crowne Plaza : The City, 19, New Bridge Street, Temple, London, Greater London, England, EC4V 6DB, UK': (
        51.5122778, -0.104631820474838),
    'Hôtel Mercure Paris 19 Philharmonie La Villette, 216, Avenue Jean Jaurès, Amérique, 19e, Paris, Île-de-France, France métropolitaine, 75019, France': (
        48.8888774, 2.3943052),
    "160 - Avda. d'Eduard Maristany 1, Passeig del Taulat, el Besòs i el Maresme, Sant Martí, Barcelona, BCN, CAT, 08020, España": (
        41.4110327, 2.2193857),
    "Église Saint-Thomas d'Aquin, Rue Montalembert, St-Thomas-d'Aquin, 7e, Paris, Île-de-France, France métropolitaine, 75007, France": (
        48.85639865, 2.32763588182037),
    'London Fenchurch Street, Fenchurch Place, London, Greater London, England, EC3M 4AJ, UK': (
        51.511328, -0.0776270747760119),
    'Hôtel Royal Garden, Rue du Faubourg Saint-Honoré, Quartier du Faubourg-du-Roule, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8757133, 2.3039016),
    'St Pancras International Station, Euston Road, Holborn, Bloomsbury, London Borough of Camden, London, Greater London, England, N1C 4QP, UK': (
        51.5318585, -0.126604089443774),
    'MK2 Bastille, Boulevard Richard Lenoir, St-Ambroise, 11e, Paris, Île-de-France, France métropolitaine, 75011, France': (
        48.8545349, 2.3691603),
    "Dukes Hotel, 35-36, St. James's Place, St. James's, Mayfair, City of Westminster, London, Greater London, England, SW1A 1NY, UK": (
        51.50543905, -0.139376755572466),
    '15, Delflandlaan, Slotervaart, Amsterdam, Nieuw-West, Amsterdam, Noord-Holland, Nederland, 1062EA, Nederland': (
        52.3511228, 4.8411696),
    'Sheraton Belgravia, Pont Street, Belgravia, City of Westminster, London, Greater London, England, SW3 4, UK': (
        51.4973611, -0.1562075),
    'Amedia Hotel, 155, Landstraßer Hauptstraße, St. Marx, KG Landstraße, Landstraße, Wien, 1030, Österreich': (
        48.19240805, 16.3996777361596),
    '10, Roemer Visscherstraat, Vondelbuurt, Amsterdam, West, Amsterdam, Noord-Holland, Nederland, 1054EX, Nederland': (
        52.3617577, 4.8780052),
    '2, Avenue des Portugais, Chaillot, 16e, Paris, Île-de-France, France métropolitaine, 75116, France': (
        48.8712417, 2.2937726),
    "Hôtel Pont Royal, Rue Montalembert, St-Thomas-d'Aquin, 7e, Paris, Île-de-France, France métropolitaine, 75007, France": (
        48.8565619, 2.3273421),
    'Kensington House Hotel, Prince of Wales Terrace, South Kensington, Royal Borough of Kensington and Chelsea, London, Greater London, England, W8 5PQ, UK': (
        51.5012251, -0.185987968258427),
    'Park Plaza Riverbank, 18, Albert Embankment, Vauxhall, London Borough of Lambeth, London, Greater London, England, SE1 7TJ, UK': (
        51.4914309, -0.121428799236551),
    '16-18, Carrer del Rec Comtal, Sant Pere, Santa Caterina i la Ribera, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (
        41.38961975, 2.18011790647399),
    "Eccleston Square Hotel, 37, Eccleston Square, St. James's, Pimlico, City of Westminster, London, Greater London, England, SW1V 1PH, UK": (
        51.49111665, -0.144918469039126),
    'Arion Cityhotel, 1, Hintschiggasse, Siedlung Wienerberg-Süd, KG Inzersdorf Stadt, Favoriten, Wien, 1100, Österreich': (
        48.1586487, 16.3451357529265),
    '15, Rue Jacob, St-Germain-des-Prés, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.8550868, 2.3350785),
    'Hôtel Pullman Montparnasse, Rue Vercingétorix, Plaisance, 14e, Paris, Île-de-France, France métropolitaine, 75014, France': (
        48.83841655, 2.32087268495146),
    'Le Marianne Hotel, 11, Rue Paul Baudry, Quartier du Faubourg-du-Roule, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8725879, 2.3076104),
    "Rathbone Hotel, 30, Rathbone Street, St. James's, Fitzrovia, City of Westminster, London, Greater London, England, W1T 1LB, UK": (
        51.518658, -0.135551346663266),
    'Tulip Inn, Loosdrechtdreef, K-buurt, Amsterdam, Zuidoost, Amsterdam, Noord-Holland, Nederland, 1107, Nederland': (
        52.3152302, 4.9960537),
    'Hôtel Marriott, Promenade des Champs-Élysées, Quartier du Faubourg-du-Roule, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8710747, 2.3050358),
    'Hotel Claris, 271, Carrer de València, la Sagrada Família, Eixample, Barcelona, BCN, CAT, 08003, España': (
        41.39455845, 2.16523030504046),
    '1, Rue Sainte-Opportune, Quartier des Halles, Les Halles, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.859827, 2.3471265),
    '34, Rue Viala, Grenelle, 15e, Paris, Île-de-France, France métropolitaine, 75015, France': (48.8501315, 2.2890804),
    'Lorenteggio, Via Lorenteggio, Lorenteggio, Milano, MI, LOM, 20147, Italia': (45.4436687, 9.1160489),
    "Sherborne Court, Marloes Road, Earl's Court, Royal Borough of Kensington and Chelsea, London, Greater London, England, W8 5LL, UK": (
        51.4950967, -0.192459985960196),
    'Lycée Français Charles de Gaulle, Queensberry Way, Brompton, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW7, UK': (
        51.4947404, -0.176427545775193),
    '3, Boulevard Montmartre, Fg-Montmartre, 2e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.8714007, 2.3426398),
    'Rosenberger Markt-Restaurant, 2, Maysedergasse, Kärntner Viertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.2043299, 16.3701683),
    'Hotel Boltzmann, 8, Boltzmanngasse, Thurygrund II, KG Alsergrund, Alsergrund, Wien, 1090, Österreich': (
        48.22166245, 16.3567466023973),
    'Parking Clichy-Montmartre, Rue Caulaincourt, Grandes-Carrières, 18e, Paris, Île-de-France, France métropolitaine, 75018, France': (
        48.885116, 2.32984727888303),
    'Imperial Road, Sands End, London Borough of Hammersmith and Fulham, London, Greater London, England, SW6 2AX, UK': (
        51.4753529, -0.1875762),
    'Hotel Square Louvois, 12, Rue de Louvois, Vivienne, 2e, Paris, Île-de-France, France métropolitaine, 75002, France': (
        48.8684167, 2.3367966),
    "Bar Prima Donna, Via dell'Orso, Brera, Municipio 1, Milano, MI, LOM, 20121, Italia": (45.4690021, 9.1867651),
    '7, Rue Casimir Delavigne, Odéon, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.850179, 2.3391975),
    'Bistro One Ninety, 189, Bremner Road, South Kensington, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW7 2ER, UK': (
        51.50015205, -0.179650078828298),
    'Novotel London Wembley, Fulton Road, Preston, London Borough of Brent, London, Greater London, England, HA9 9JR, UK': (
        51.5611124, -0.2790191),
    "30, Carrer de Balmes, l'Antiga Esquerra de l'Eixample, Eixample, Barcelona, BCN, CAT, 08003, España": (
        41.38815125, 2.16457832940713),
    'Glynne Court Hotel, 41, Great Cumberland Place, Marylebone, City of Westminster, London, Greater London, England, W1, UK': (
        51.5157145, -0.1602317),
    'MiniHotel Tiziano, 6, Via Tiziano, San Pietro, Municipio 8, Milano, MI, LOM, 20145, Italia': (
        45.4706456, 9.1561429),
    '8b, Avenue de la Sœur Rosalie, Croulebarbe, 13e, Paris, Île-de-France, France métropolitaine, 75013, France': (
        48.832094, 2.3536674),
    "Hôtel d'Espinoy et Pavillon de la Reine, Place des Vosges, Archives, 4e, Paris, Île-de-France, France métropolitaine, 75003, France": (
        48.8562799, 2.36596432726581),
    'Okura Hotel, Amstelkade, Scheldebuurt, Amsterdam, Zuid, Amsterdam, Noord-Holland, Nederland, 1017, Nederland': (
        52.34865715, 4.89363602414552),
    '50, Schepenbergweg, Amstel III, Amsterdam, Zuidoost, Amsterdam, Noord-Holland, Nederland, 1105 AT, Nederland': (
        52.2924563, 4.94444462848837),
    '10b, Rue Gabriel Laumain, Porte-St-Denis, 10e, Paris, Île-de-France, France métropolitaine, 75010, France': (
        48.8734447, 2.3484747),
    'The Collonade, 2, Warrington Crescent, Maida Vale, City of Westminster, London, Greater London, England, W9 1ER, UK': (
        51.52429365, -0.184608262932694),
    "El Cau Encantat, Carrer d'Arenys, la Teixonera, Horta-Guinardó, Barcelona, BCN, CAT, 08035, España": (
        41.4228354, 2.1460447),
    'The Leonard Hotel, 15, Seymour Street, Marylebone, City of Westminster, London, Greater London, England, W1H 7JW, UK': (
        51.51462555, -0.157783635907469),
    '3, Rue Auguste Maquet, Auteuil, 16e, Paris, Île-de-France, France métropolitaine, 92130, France': (
        48.8396734, 2.2662762),
    'Hotel Franklin Roosevelt, 18, Rue Clément Marot, Champs-Élysées, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8677851, 2.3032087),
    'Best Western Plus Epping Forest, 30, Oak Hill, Hale End, Chingford, London Borough of Waltham Forest, London, Greater London, England, IG8 9NY, UK': (
        51.6032893, 0.0108502),
    "Hôtel Sofitel Le Faubourg, Rue Boissy d'Anglas, Madeleine, 8e, Paris, Île-de-France, France métropolitaine, 75008, France": (
        48.8684048, 2.3213802),
    "Hotel Eurostars Gaudí, Carrer del Consell de Cent, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08013, España": (
        41.4006467, 2.1787045),
    'Pullman London St Pancras, 100-110, Euston Road, Holborn, Bloomsbury, London Borough of Camden, London, Greater London, England, NW1 2AJ, UK': (
        51.5284827, -0.128331118092792),
    '20, Rue Marbeuf, Champs-Élysées, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8684839, 2.3035927),
    'Hôtel Élysées Mermoz, 30, Rue Jean Mermoz, Madeleine, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8715442, 2.3121315),
    'Premier Inn, 15A, Great Suffolk Street, Southwark, London Borough of Southwark, London, Greater London, England, SE15, UK': (
        51.50505805, -0.100900342703508),
    'Hotel Grums, Carrer de Palaudàries, el Raval, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (
        41.3729061, 2.1720069),
    'Aloft, 1, Sandstone Lane, Silvertown, Newham, London, Greater London, England, E16 1FR, UK': (
        51.50846285, 0.03522969202474),
    'Novotel, 40, Marsh Wall, Isle of Dogs, London Borough of Tower Hamlets, London, Greater London, England, E14 9TP, UK': (
        51.50120225, -0.0233764758607864),
    "L'Hôtel, Rue des Beaux-Arts, St-Germain-des-Prés, 6e, Paris, Île-de-France, France métropolitaine, 75006, France": (
        48.856323, 2.3352294),
    "Lords (closed), Lodge Road, St. John's Wood, City of Westminster, London, Greater London, England, NW8 7JT, UK": (
        51.5292954, -0.168220138151121),
    '148, Keizersgracht, Grachtengordel, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1015CX, Nederland': (
        52.3762724, 4.8863122),
    'The Levante Parliament, 9, Auerspergstraße, Buchfeld, KG Josefstadt, Josefstadt, Wien, 1080, Österreich': (
        48.20834305, 16.3547858170368),
    'Chiswick Moran Hotel, 626, Chiswick High Road, London Borough of Hounslow, London, Greater London, England, W4 5RY, UK': (
        51.4924503, -0.278344043016742),
    "Taj 51 Buckingham Gate Suites and Residences, Buckingham Gate, St. James's, Victoria, City of Westminster, London, Greater London, England, SW1E 6AX, UK": (
        51.4985107, -0.137935899892195),
    'The Buckingham, 39, Bedford Place, Holborn, Bloomsbury, London Borough of Camden, London, Greater London, England, WC1A 2PJ, UK': (
        51.5196094, -0.1239586),
    'Hôtel Paris Le Marquis Eiffel, 15, Rue Dupleix, Grenelle, 15e, Paris, Île-de-France, France métropolitaine, 75015, France': (
        48.85161995, 2.2978601877862),
    'Turin Hotel, Carrer del Pintor Fortuny, el Raval, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (
        41.3830791, 2.1701799),
    '99, Rue de Rome, Madeleine, 8e, Paris, Île-de-France, France métropolitaine, 75017, France': (
        48.8837483, 2.3186268),
    "Arai, 30, Carrer d'Avinyó, el Gòtic, Ciutat Vella, Barcelona, BCN, CAT, 08003, España": (
        41.38076145, 2.17731260695819),
    'Justin James Hotel, 43, Worple Road, South Wimbledon, Merton, London, Greater London, England, SW19 4JZ, UK': (
        51.42028225, -0.211245485250161),
    'Crowne Plaza Kensington, Cromwell Road, South Kensington, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW7 4DL, UK': (
        51.4950962, -0.1837631),
    'Amorino, Rue Budé, Îles, 4e, Paris, Île-de-France, France métropolitaine, 75004, France': (48.852026, 2.3557283),
    '6, Papagenogasse, KG Mariahilf, Mariahilf, Wien, 1060, Österreich': (48.2000268, 16.3641783),
    '49, Avenue Marceau, Champs-Élysées, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8691745, 2.2982565),
    "Apartments La casa de les Lletres, 6, Plaça d'Antonio López, el Gòtic, Ciutat Vella, Barcelona, BCN, CAT, 08002, España": (
        41.381132, 2.1813053),
    'Courtyard by Marriott Wien Messe, 4, Trabrennstraße, Pratercottage, KG Leopoldstadt, Leopoldstadt, Wien, 1020, Österreich': (
        48.21301945, 16.413430967791),
    '3, Rue Louis Codet, Gros-Caillou, 7e, Paris, Île-de-France, France métropolitaine, 75007, France': (
        48.8549684, 2.3085008),
    "Hotel Ramada, 27, Via Stamira D'Ancona, Turro, Milano, MI, LOM, 20127, Italia": (45.5017734, 9.22769248663537),
    '300, Viale Fulvio Testi, Bicocca, Milano, MI, LOM, 20095, Italia': (45.52664255, 9.21313726551312),
    'DoubleTree by Hilton Hotel London - West End, 92, Southampton Row, Holborn, St Giles, London Borough of Camden, London, Greater London, England, WC1B 4BH, UK': (
        51.5201101, -0.12213),
    'Corendon Vitality Hotel Amsterdam, 7, Aletta Jacobslaan, Slotervaart, Amsterdam, Nieuw-West, Amsterdam, Noord-Holland, Nederland, 1066 BP, Nederland': (
        52.346558, 4.8307726813105),
    'Le Général Hôtel, Rue Rampon, Folie-Méricourt, 11e, Paris, Île-de-France, France métropolitaine, 75011, France': (
        48.866247, 2.3669),
    'The Lobby, 2, Fizeaustraat, Oost-Watergraafsmeer, Amsterdam, Oost, Amsterdam, Noord-Holland, Nederland, 1097SC, Nederland': (
        52.3453343, 4.9255508),
    '110, Viale Certosa, Boldinasco, Milano, MI, LOM, 20148, Italia': (45.4950166, 9.1413609),
    'The Clarendon, 34, Bedford Place, Holborn, Bloomsbury, London Borough of Camden, London, Greater London, England, WC1A 2PJ, UK': (
        51.5198344, -0.1242027),
    "The Athenaeum Hotel, 116, Piccadilly, St. James's, Mayfair, City of Westminster, London, Greater London, England, W1J 7BJ, UK": (
        51.5047391, -0.147556122872102),
    'Uptown Palace, 10, Via Santa Sofia, Porta Lodovica, Milano, MI, LOM, 20122, Italia': (45.4574898, 9.1919471),
    'Hôtel Victor Hugo, Rue Copernic, Chaillot, 16e, Paris, Île-de-France, France métropolitaine, 75116, France': (
        48.8691051, 2.2891789),
    "The Stafford, St. James's Place, St. James's, Mayfair, City of Westminster, London, Greater London, England, SW1A 1NN, UK": (
        51.50586975, -0.140145189466598),
    "Queen's Gate School, 131-133, Queen's Gate, Brompton, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW7 5LE, UK": (
        51.494538, -0.178388978701822),
    'The Hoxton, 81, Great Eastern Street, Shoreditch, London Borough of Hackney, London, Greater London, England, EC2V 7HH, UK': (
        51.52549775, -0.0829090433999737),
    'Hotel St. George, 9, Viale Tunisia, Lazzaretto, Municipio 3, Milano, MI, LOM, 20124, Italia': (
        45.4771542, 9.2054184),
    "Telepizza, Carrer de Viladomat, Project Area Hospital Clinic, la Nova Esquerra de l'Eixample, Eixample, Barcelona, BCN, CAT, 08014, España": (
        41.384492, 2.1511307),
    'Tranvia Milano-Saronno-Tradate, Via Varesina, Quartiere Varesina, Municipio 8, Milano, MI, LOM, 20148, Italia': (
        45.5011737, 9.141302),
    "22-25, Finsbury Square, Saint Luke's, London Borough of Islington, London, Greater London, England, EC2V 7HH, UK": (
        51.521806, -0.0855284491359048),
    'Pearle, 55-57, Simmeringer Hauptstraße, KG Simmering, Simmering, Wien, 1110, Österreich': (48.1789891, 16.4115676),
    'Hotel Rathaus, 13, Lange Gasse, Buchfeld, KG Josefstadt, Josefstadt, Wien, 1080, Österreich': (
        48.2074903, 16.3524684256843),
    'Hotel InterContinental, 28, Johannesgasse, KG Innere Stadt, Innere Stadt, Wien, 1037, Österreich': (
        48.2017622, 16.3789991383557),
    "Conrad London St. James, Tothill Street, St. James's, Millbank, City of Westminster, London, Greater London, England, SW1, UK": (
        51.4993247, -0.132386882590175),
    'Hotel Mediolanum, 1, Via Mauro Macchi, Centrale, Municipio 2, Milano, MI, LOM, 20124, Italia': (
        45.4813891, 9.20398),
    'JUFA Wien, 50-54, Mautner-Markhof-Gasse, KG Simmering, Simmering, Wien, 1110, Österreich': (
        48.1757004, 16.4203272049185),
    'Hôtel Best Western Ducs de Bourgogne, Rue du Pont Neuf, Quartier des Halles, Les Halles, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.8603405, 2.344133),
    'Via dei Fontanili, Morivione, Municipio 5, Milano, MI, LOM, 20141, Italia': (45.4399641, 9.1933029),
    "Shangri-La Hotel, 10, Avenue d'Iéna, Chaillot, 16e, Paris, Île-de-France, France métropolitaine, 75116, France": (
        48.8637194, 2.2934262),
    'De Hallen, Hannie Dankbaarpassage, Oud-West, Amsterdam, West, Amsterdam, Noord-Holland, Nederland, 1053, Nederland': (
        52.36701545, 4.86815680523511),
    'La Gare, 20, Via Giovanni Battista Pirelli, Centro Direzionale, Municipio 2, Milano, MI, LOM, 20124, Italia': (
        45.4842102, 9.1988135),
    "4, Rue d'Alger, Vendôme, 1er, Paris, Île-de-France, France métropolitaine, 75001, France": (48.8648677, 2.3295324),
    'International Hotel, 163, Marsh Wall, Isle of Dogs, London Borough of Tower Hamlets, London, Greater London, England, E14 9SJ, UK': (
        51.50175725, -0.0234075418772731),
    'Radisson Edwardian Grafton Hotel, 130, Tottenham Court Road, Holborn, Somers Town, London Borough of Camden, London, Greater London, England, W1T 5AY, UK': (
        51.52402985, -0.138016612056741),
    "Room Mate Anna Hotel, 271, Carrer Aragó, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08007, España": (
        41.39297085, 2.16533821002218),
    'Kiko, 3, Corso Buenos Aires, Zona Buenos Aires, Porta Venezia, Milano, MI, LOM, 20129, Italia': (
        45.4757694, 9.206051),
    'The Hub, 10, Via privata Polonia, Musocco, Milano, MI, LOM, 20148, Italia': (45.51385215, 9.11944945),
    '4, Maria-Theresien-Straße, KG Alsergrund, Alsergrund, Wien, 1010, Österreich': (48.2147675, 16.3626634),
    'Embassy Suites by Hilton Houston Downtown, 1515, Dallas Street, Houston, Harris County, Texas, 77010, United States of America': (
        29.75302945, -95.3613309036377),
    '10, Rue de Bruxelles, Quartier Saint-Georges, St-Georges, 9e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.8835768, 2.331458),
    "Crivi's Hotel, Via Carlo Crivelli, Quadronno, Municipio 1, Milano, MI, LOM, 20123, Italia": (45.4529655, 9.195951),
    'Cedar House, 39-41, Nottingham Place, Marylebone, City of Westminster, London, Greater London, England, W1U 5EW, UK': (
        51.5221747, -0.153512070907241),
    'Le Lavoisier, Rue Lavoisier, Madeleine, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8737103, 2.3202018922734),
    '3, Rue du 8 Mai 1945, Porte-St-Martin, 10e, Paris, Île-de-France, France métropolitaine, 75010, France': (
        48.8759305, 2.35895),
    'Ayre Hotel Rosellón, 390, Carrer del Rosselló, la Sagrada Família, Eixample, Barcelona, BCN, CAT, 08025, España': (
        41.4047213, 2.1728228),
    '221, Van Leijenberghlaan, Buitenveldert, Amsterdam, Zuid, Amsterdam, Noord-Holland, Nederland, 1082GG, Nederland': (
        52.3266692, 4.8800358),
    'Gucci, Pavilion Road, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW3 4, UK': (
        51.5000865, -0.160244617002379),
    'Palazzo Segreti, 8/B, Via San Tomaso, Cordusio, Municipio 1, Milano, MI, LOM, 20121, Italia': (
        45.4672077, 9.1841975),
    'Mandarin Oriental Hyde Park, 66, Knightsbridge, Belgravia, City of Westminster, London, Greater London, England, SW1X 7LA, UK': (
        51.50221365, -0.159986053670699),
    'TownHouse Duomo Milano, 2, Via Silvio Pellico, Duomo, Municipio 1, Milano, MI, LOM, 20121, Italia': (
        45.4649695, 9.1893218),
    'The Rose Court Hotel, 35, Great Cumberland Place, Marylebone, City of Westminster, London, Greater London, England, W1H 7DS, UK': (
        51.5151886, -0.1600185),
    'NH Machiavelli, 5, Via Lazzaretto, Lazzaretto, Porta Nuova, Milano, MI, LOM, 20124, Italia': (
        45.477635, 9.2015517),
    'Crowne Plaza, George Gershwinlaan, Zuideramstel, Amsterdam, Zuid, Amsterdam, Noord-Holland, Nederland, 1183, Nederland': (
        52.33572335, 4.87453125226577),
    'Novotel, Thrale Street, Borough, London Borough of Southwark, London, Greater London, England, SE15, UK': (
        51.50536515, -0.0949974415920117),
    'Hôtel Montaigne, 6, Avenue Montaigne, Champs-Élysées, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.865467, 2.30389626687229),
    "Idol Hotel, 16, Rue d'Edimbourg, Europe, 8e, Paris, Île-de-France, France métropolitaine, 75008, France": (
        48.8795063, 2.3203278),
    '1, Aspernbrückengasse, Afrikanerviertel, KG Leopoldstadt, Leopoldstadt, Wien, 1020, Österreich': (
        48.2133555, 16.3831675),
    "The Boltons Hotel by Best Western, 19-21, Penywern Road, Earl's Court, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW5 9AD, UK": (
        51.49072495, -0.193438016044401),
    "May Fair Hotel, Stratton Street, St. James's, Mayfair, City of Westminster, London, Greater London, England, W1J 8LT, UK": (
        51.50831975, -0.144084508924745),
    "The Belgrave, Belgrave Road, St. James's, Pimlico, City of Westminster, London, Greater London, England, SW1V 2BG, UK": (
        51.4901136, -0.138092326533369),
    '10, Rotensterngasse, Afrikanerviertel, KG Leopoldstadt, Leopoldstadt, Wien, 1020, Österreich': (
        48.21756945, 16.3821155918154),
    'Graben, 3, Dorotheergasse, Kärntner Viertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.207904, 16.3700585),
    'The Victoria, 451, Queensbridge Road, South Hornsey, Shacklewell, London Borough of Hackney, London, Greater London, England, E10, UK': (
        51.54571365, -0.0701003989693799),
    '3, Rue Christine, Monnaie, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.8544372, 2.3400012),
    "Petit palace BCN, 21, Carrer de Roger de Llúria, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08003, España": (
        41.3909966, 2.1714195),
    'Hôtel Rochester, Rue La Boétie, Quartier du Faubourg-du-Roule, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8723468, 2.3092947),
    'The Drayton Court Hotel, 2, The Avenue, West Ealing, Hanwell, London Borough of Ealing, London, Greater London, England, W13 8PH, UK': (
        51.5142404, -0.3192305),
    '97, Rue Lauriston, Chaillot, 16e, Paris, Île-de-France, France métropolitaine, 75116, France': (
        48.8672448, 2.2879213),
    'Mandarin Oriental, 9, Via Andegari, Scala, Municipio 1, Milano, MI, LOM, 20121, Italia': (45.4694631, 9.1909801),
    'Pharmacie Cavanna, Avenue Victor Hugo, Chaillot, 16e, Paris, Île-de-France, France métropolitaine, 75116, France': (
        48.8729379, 2.2926546),
    '8, Carrer de Santaló, Galvany, Sant Gervasi - Galvany, Sarrià - Sant Gervasi, Barcelona, BCN, CAT, 08023, España': (
        41.3949879, 2.14699942287031),
    '46, Noorderstraat, Rivierenbuurt, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1017TV, Nederland': (
        52.3611838, 4.8936467), 'South Place Hotel, Wilson Street, London, Greater London, England, EC2V 7HH, UK': (
        51.5192835, -0.0862869748693607),
    'Edifici Apolo, Avinguda del Paral·lel, el Raval, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (
        41.37446145, 2.17025009082587),
    'Punto SMA, 11, Via Michelangelo Buonarroti, San Pietro, Municipio 7, Milano, MI, LOM, 20145, Italia': (
        45.4682535, 9.1549911),
    'Arc hotel Irla, Carrer de Calvet, Galvany, Sant Gervasi - Galvany, Sarrià - Sant Gervasi, Barcelona, BCN, CAT, 08014, España': (
        41.3947875, 2.1434626),
    '14, Tiefer Graben, Schottenviertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.2121783, 16.368031),
    'Fielding, 4, Broad Court, St Clement Danes, Covent Garden, City of Westminster, London, Greater London, England, WC2B 5QZ, UK': (
        51.51391835, -0.12201703721997),
    '294, Spuistraat, Burgwallen-Nieuwe Zijde, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1012VX, Nederland': (
        52.3696497, 4.8887363),
    'Royal Garden Hotel, 2-24, Kensington High Street, South Kensington, Royal Borough of Kensington and Chelsea, London, Greater London, England, W8 4PT, UK': (
        51.5027775, -0.18803845416935),
    '33, Place de la Madeleine, Madeleine, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8710308, 2.3247804),
    'Société Générale, Boulevard Brune, Plaisance, 14e, Paris, Île-de-France, France métropolitaine, 75014, France': (
        48.8274443, 2.3054531),
    'Caixa Galicia, la Rambla, el Gòtic, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (41.3826477, 2.1716377),
    'Timhotel Opera Grands Magasins, 35, Rue La Bruyère, Nouvelle Athènes, St-Georges, 9e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.8794957, 2.3334918),
    'Sunflower, Piazzale Lugano, Derganino, Municipio 9, Milano, MI, LOM, 20121, Italia': (45.4988155, 9.1662016),
    '3, Hollandstraße, Karmeliterviertel, KG Leopoldstadt, Leopoldstadt, Wien, 1020, Österreich': (
        48.21523485, 16.3761052010066),
    '22, Bina Gardens, South Kensington, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW5, UK': (
        51.49161485, -0.183339278036971),
    "Alimara Barcelona Hotel, 126, Carrer de Berruguete, la Vall d'Hebron, Horta-Guinardó, Barcelona, BCN, CAT, 08035, España": (
        41.4339651, 2.1474969),
    '2, Rue Hector Malot, 12e Arrondissement (urbain), Quinze-Vingts, 12e, Paris, Île-de-France, France métropolitaine, 75012, France': (
        48.845301, 2.3752606),
    'Mercure, Rue de la Sorbonne, Sorbonne, 5e, Paris, Île-de-France, France métropolitaine, 75005, France': (
        48.8493373, 2.3431508),
    'NH Danube City, 21, Wagramer Straße, KG Kaisermühlen, Donaustadt, Neukagran, Wien, 1220, Österreich': (
        48.2354451, 16.4218808647994),
    "Yamamay, 1, Piazza Duca d'Aosta, Centrale, Municipio 2, Milano, MI, LOM, 20124, Italia": (45.4859708, 9.2042731),
    'Landhaus Fuhrgassl-Huber, 24, Rathstraße, KG Neustift am Walde, Döbling, Wien, 1190, Österreich': (
        48.2509984, 16.3049884825794),
    'Hôtel Washington Opéra, Passage de Beaujolais, Palais Royal, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.8662429, 2.33734701405024),
    '11, Rue de Trévise, Fg-Montmartre, 9e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.8732734, 2.3450666),
    "Next, New Bond Street, St. James's, Mayfair, City of Westminster, London, Greater London, England, W1S 1PY, UK": (
        51.51439595, -0.146400624256994),
    'Whitechapel Hotel, 49 - 53, New Road, Whitechapel, London Borough of Tower Hamlets, London, Greater London, England, SE15, UK': (
        51.5161218, -0.062467287105263),
    '102, Avenue de Villiers, Plaine-Monceau, 17e, Paris, Île-de-France, France métropolitaine, 75017, France': (
        48.8847739, 2.2996919), '40, Via Mac Mahon, Ghisolfa, Milano, MI, LOM, 20148, Italia': (45.4911556, 9.1618327),
    '19, 25, Carrer de Loreto, les Corts, Barcelona, BCN, CAT, 08014, España': (41.3898563, 2.14167307053956),
    '54, Rue Pierre Charron, Champs-Élysées, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8690608, 2.302639),
    'Lalit London, 181, Tooley Street, Bermondsey, London Borough of Southwark, London, Greater London, England, SE1 2JR, UK': (
        51.5033408, -0.0781845364613226),
    'Hotel Medinaceli, 8, Plaça del Duc de Medinaceli, el Gòtic, Ciutat Vella, Barcelona, BCN, CAT, 08002, España': (
        41.3780797, 2.17857837850096),
    "Le Péra, 17, Rue de Caumartin, Chaussée-d'Antin, 9e, Paris, Île-de-France, France métropolitaine, 75009, France": (
        48.8713093, 2.32778580320911),
    "6, Prince's Square, Bayswater, City of Westminster, London, Greater London, England, W2 4NP, UK": (
        51.5127307, -0.192635191466428),
    'Hôtel Mathis Élysées, Rue de Ponthieu, Quartier du Faubourg-du-Roule, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8700445, 2.3113231),
    'Citizen M, 40, Trinity Square, Spitalfields, London Borough of Tower Hamlets, London, Greater London, England, EC3N 4DJ, UK': (
        51.5102108, -0.0764426253637532),
    'Osteria Italiana, 22, Via Napo Torriani, Centrale, Municipio 2, Milano, MI, LOM, 20124, Italia': (
        45.4829357, 9.2033473),
    '5b, Rue Massenet, Muette, 16e, Paris, Île-de-France, France métropolitaine, 75116, France': (
        48.8583226, 2.2795113),
    "Hotel ibis Styles London Kensington, 15-25, Hogarth Road, Earl's Court, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW5 0QJ, UK": (
        51.4937469, -0.1917517),
    'The Rembrandt, 11, Thurloe Place, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW3 4, UK': (
        51.49585025, -0.170339950366452),
    "Hôtel Pavillon Opéra, Rue de l'Échiquier, Porte-St-Denis, 10e, Paris, Île-de-France, France métropolitaine, 75010, France": (
        48.8719164, 2.34928914568674),
    "H10 Casanova, 559, Gran Via de les Corts Catalanes, l'Antiga Esquerra de l'Eixample, Eixample, Barcelona, BCN, CAT, 08014, España": (
        41.38424795, 2.16074314026278),
    'The Blakemore, 25-31, Leinster Gardens, Bayswater, City of Westminster, London, Greater London, England, W2 3WA, UK': (
        51.5128624, -0.1837817),
    'Portman Towers, Marylebone, City of Westminster, London, Greater London, England, W1H 2LA, UK': (
        51.5163275, -0.158049926196663),
    'Ace Hotel London Shoreditch, 100, Shoreditch High Street, Shoreditch, London Borough of Hackney, London, Greater London, England, E1 6JQ, UK': (
        51.52565355, -0.077219882040521),
    '4, Breughelstraat, Apollobuurt, Amsterdam, Zuid, Amsterdam, Noord-Holland, Nederland, 1077LC, Nederland': (
        52.3503211, 4.8770356),
    'Herbal Hill Gardens, 9, Herbal Hill, Clerkenwell, London Borough of Islington, London, Greater London, England, EC1N 7TS, UK': (
        51.5223961, -0.107855352264553),
    'Hotel Husa Arenas, Carrer del Capità Arenas, Sarrià, les Corts, Barcelona, BCN, CAT, 08014, España': (
        41.3904809, 2.1262671),
    '4, Rue La Boétie, Madeleine, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8745027, 2.3187887),
    "20, Lexham Gardens, Earl's Court, Royal Borough of Kensington and Chelsea, London, Greater London, England, W8 5JJ, UK": (
        51.4954392, -0.189274148805216),
    '9, Rue de la Michodière, Gaillon, 2e, Paris, Île-de-France, France métropolitaine, 75002, France': (
        48.8695969, 2.3346522),
    '78, Avenue Marceau, Champs-Élysées, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8718785, 2.2970381),
    "Hotel Pulitzer, Carrer de Bergara, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08003, España": (
        41.3860387, 2.1682944),
    'Hôtel Opera Richepanse, 14, Rue du Chevalier de Saint-George, Vendôme, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.8687107, 2.3252026), '68, Viale Certosa, Cagnola, Milano, MI, LOM, 20148, Italia': (45.4921109, 9.1476366),
    'AC Hotel Milano, 2, Via Enrico Tazzoli, Porta Volta, Municipio 9, Milano, MI, LOM, 20154, Italia': (
        45.4852345, 9.1831159),
    "Glam Hotel, 4, Piazza Duca d'Aosta, Centrale, Municipio 2, Milano, MI, LOM, 20124, Italia": (
        45.4837974, 9.2034286), 'Apex London Wall Hotel, Great Swan Alley, London, Greater London, England, SE15, UK': (
        51.51606385, -0.0880113319396703),
    'Kursaal Diana, Viale Piave, Zona Risorgimento, Porta Venezia, Milano, MI, LOM, 20124, Italia': (
        45.4738417, 9.20672496421788),
    'H10 London Waterloo, Dodson Street, Southwark, London Borough of Southwark, London, Greater London, England, SE15, UK': (
        51.4987966, -0.106307642467936),
    'iH-Hotels Milano, Corso Buenos Aires, Zona Buenos Aires, Municipio 3, Milano, MI, LOM, 20124, Italia': (
        45.4794625, 9.209768),
    "Holiday Inn London Regents Park, Great Titchfield Street, St. James's, Fitzrovia, City of Westminster, London, Greater London, England, W1, UK": (
        51.52254685, -0.1427356021928),
    "45 Park Lane, 45, Park Lane, St. James's, Mayfair, City of Westminster, London, Greater London, England, W1K 1PN, UK": (
        51.50629145, -0.151539413180209),
    '12, Stadhouderskade, Vondelbuurt, Amsterdam, West, Amsterdam, Noord-Holland, Nederland, 1054ES, Nederland': (
        52.3625488, 4.8801249),
    'Hôtel Belloy Saint-Germain, Rue Racine, Sorbonne, 6e, Paris, Île-de-France, France métropolitaine, 75005, France': (
        48.8503717, 2.3422419),
    'Hôtel Élysées Régencia, Rue Jean Giraudoux, Chaillot, 16e, Paris, Île-de-France, France métropolitaine, 75116, France': (
        48.8686655, 2.2984695),
    'Frenchie Covent Garden, 16, Henrietta Street, St Clement Danes, Covent Garden, City of Westminster, London, Greater London, England, WC2E 8QH, UK': (
        51.5108399, -0.1238856),
    '2, Albert Cuypstraat, Oude Pijp, Amsterdam, Zuid, Amsterdam, Noord-Holland, Nederland, 1072CT, Nederland': (
        52.3545, 4.887468),
    'Carlton Hotel Baglioni, 5, Via Senato, Quadrilatero della Moda, Porta Venezia, Milano, MI, LOM, 20121, Italia': (
        45.4692053, 9.1984661),
    'Hotel Mercure Josefshof Wien Am Rathaus, 4-6, Josefsgasse, Buchfeld, KG Josefstadt, Josefstadt, Wien, 1080, Österreich': (
        48.2087606, 16.3538784160808),
    'Gartenbauhochhaus, 12, Parkring, Stubenviertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.20554045, 16.3779376),
    'Clikò, Via Giorgio Vasari, Municipio 4, Milano, MI, LOM, 20141, Italia': (45.4521021, 9.2054417),
    "Grupotel Gran Vía 678, 678, Gran Via de les Corts Catalanes, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08003, España": (
        41.3924679, 2.1727493),
    'Cannizaro Park Hotel, 20, West Side Common, Cottenham Park, Merton, London, Greater London, England, SW19 4UE, UK': (
        51.4243544, -0.229367618143712),
    "Alexandra Barcelona Hotel, Curio Collection by Hilton, 251, Carrer de Mallorca, l'Antiga Esquerra de l'Eixample, Eixample, Barcelona, BCN, CAT, 08008, España": (
        41.3932503, 2.16146932090517),
    '71, Rue de Charonne, Ste-Marguerite, 11e, Paris, Île-de-France, France métropolitaine, 75011, France': (
        48.8536835, 2.3805829),
    'Sallés Hotel Pere IV, 128-130, Carrer de Pallars, el Parc i la Llacuna del Poblenou, Sant Martí, Barcelona, BCN, CAT, 08018, España': (
        41.39685695, 2.1924358969028),
    "Marriott Hotel Regent's Park, Adelaide Road, Swiss Cottage, Belsize Park, London Borough of Camden, London, Greater London, England, NW3 3SG, UK": (
        51.5421531, -0.170289770094315),
    '26, Neubaugürtel, Lerchenfeld, KG Neubau, Neubau, Wien, 1070, Österreich': (48.1995668, 16.3387471),
    'The Westin Paris, Rue de Castiglione, Vendôme, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.8657785, 2.3274056),
    "Great St Helen's Hotel, Great St Helen's, London, Greater London, England, SE15, UK": (51.5148858, -0.0825103),
    'Brediusbad, 306, Spaarndammerdijk, Westerpark, Amsterdam, West, Amsterdam, Noord-Holland, Nederland, 1013ZX, Nederland': (
        52.3924717, 4.8683383),
    'Cavendish, 73-75, Gower Street, Holborn, Bloomsbury, London Borough of Camden, London, Greater London, England, WC1E 6BT, UK': (
        51.5220103, -0.13243040767148),
    'The Soho Hotel, 4, Richmond Mews, Soho, City of Westminster, London, Greater London, England, W1D 3BD, UK': (
        51.5140175, -0.133770111389909),
    'TC Forex, 40, Carrer Nou de la Rambla, el Raval, Ciutat Vella, Barcelona, BCN, CAT, 08001, España': (
        41.3780003, 2.1730467),
    "Sanderson Hotel, Berners Street, St. James's, Fitzrovia, City of Westminster, London, Greater London, England, W1T 3NG, UK": (
        51.517479, -0.137138),
    "Central Basin, St Katharine's Way, St.George in the East, London Borough of Tower Hamlets, London, Greater London, England, SE15, UK": (
        51.5068099, -0.0716807823419543),
    'Greenwich Court, Cameron Place, Dorian Estate, Whitechapel, London Borough of Tower Hamlets, London, Greater London, England, SE15, UK': (
        51.5154193, -0.0572562525665398),
    'Prince de Galles, Avenue George V, Quartier du Faubourg-du-Roule, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8691274, 2.3007665),
    'Anema e Cozze, Via Pietro Orseolo, Zona Tortona, Porta Genova, Milano, MI, LOM, 20136, Italia': (
        45.4567534, 9.1686062),
    'Hotel NH, 7, Stadhouderskade, Vondelbuurt, Amsterdam, West, Amsterdam, Noord-Holland, Nederland, 1054ES, Nederland': (
        52.3630852, 4.8794581),
    '29, Rue Jacob, St-Germain-des-Prés, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.8553785, 2.3341636),
    "Hôtel France d'Antin, Rue d'Antin, Gaillon, 2e, Paris, Île-de-France, France métropolitaine, 75002, France": (
        48.8692604, 2.3339332),
    'Hotel Inglaterra, Carrer de Pelai, el Raval, Eixample, Barcelona, BCN, CAT, 08003, España': (
        41.3856916, 2.1659374),
    'Terraza Gran Hotel Central, Carrer de Mercaders, Sant Pere, Santa Caterina i la Ribera, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (
        41.385131, 2.1778655),
    'Am Spiegeln, 30, Johann-Hörbiger-Gasse, Sauberg, KG Mauer, Liesing, Wien, 1230, Österreich': (
        48.1536737, 16.2825532422816),
    'Ibis, 49, Blackfriars Road, Southwark, London Borough of Southwark, London, Greater London, England, SE1 8NZ, UK': (
        51.50492405, -0.105131463079574),
    'Jumeirah Lowndes Hotel, Halkin Arcade, Belgravia, City of Westminster, London, Greater London, England, SW3 4, UK': (
        51.49927605, -0.157684619351145),
    'Hotel de la Ville, 6, Via Ulrico Hoepli, Duomo, Municipio 1, Milano, MI, LOM, 20121, Italia': (
        45.4659559, 9.1922395),
    'Majestic Hotel - Spa, 30, Rue La Pérouse, Chaillot, 16e, Paris, Île-de-France, France métropolitaine, 75116, France': (
        48.8704132, 2.2938813),
    'The Mitre Hotel, Roan Street, Greenwich, London, Greater London, England, SE10 9JY, UK': (
        51.4801319, -0.00972446400693972),
    "Disney Store, 350-352, Oxford Street, St. James's, Mayfair, City of Westminster, London, Greater London, England, W1C 1JH, UK": (
        51.5146644, -0.1483051),
    "11, Rue d'Astorg, Madeleine, 8e, Paris, Île-de-France, France métropolitaine, 75008, France": (
        48.8728414, 2.3193943),
    'Burger King, Plaça de Joaquim Xirau i Palau, el Gòtic, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (
        41.3782575, 2.176255),
    '10, Rue de Bellechasse, Faubourg Saint-Germain, 7e, Paris, Île-de-France, France métropolitaine, 75007, France': (
        48.8595394, 2.3240289),
    'Albert Heijn, 226, Nieuwezijds Voorburgwal, Burgwallen-Nieuwe Zijde, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1012 RR, Nederland': (
        52.3727974, 4.8901573),
    'Marriott, Oxford Street, Mayfair, City of Westminster, London, Greater London, England, W1C 1LX, UK': (
        51.51319895, -0.157917083192888),
    'Zona Buenos Aires, Piazza Lima, Zona Buenos Aires, Municipio 3, Milano, MI, LOM, 20124, Italia': (
        45.4805218, 9.2113776912077),
    "16, Avenue de l'Opéra, Palais Royal, 1er, Paris, Île-de-France, France métropolitaine, 75001, France": (
        48.8654554, 2.3347522),
    '153, Via Palmanova, Crescenzago, Milano, MI, LOM, 20132, Italia': (45.5045486, 9.2464296),
    '36, Rue de Saint-Quentin, St-Vincent-de-Paul, 10e, Paris, Île-de-France, France métropolitaine, 75010, France': (
        48.8793124, 2.3559676),
    'Straf Bar, 3, Via San Raffaele, Duomo, Municipio 1, Milano, MI, LOM, 20121, Italia': (45.4652438, 9.1912639),
    "iH Hotel Milano Gioia, 10/D, Via della Giustizia, Cassina de' Pomm, Greco, Milano, MI, LOM, 20125, Italia": (
        45.4995245, 9.2061485),
    '22, Rue de Chateaubriand, Quartier du Faubourg-du-Roule, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8739942, 2.3001501),
    'The Imperial Riding School Vienna, 60, Ungargasse, Fasanviertel, KG Landstraße, Landstraße, Wien, 1030, Österreich': (
        48.19666075, 16.3864637389727),
    "62, Passeig de Gràcia, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08003, España": (
        41.39307265, 2.16468280214985),
    "The Kensington Quarter, 34-44, Barkston Gardens, Earl's Court, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW5 0EW, UK": (
        51.4919826, -0.1917036),
    "Opéra Garnier, Rue Gluck, Chaussée-d'Antin, 9e, Paris, Île-de-France, France métropolitaine, 75009, France": (
        48.87203085, 2.3317901855896),
    'W14 13, Lakeside Road, Brook Green, London Borough of Hammersmith and Fulham, London, Greater London, England, W14, UK': (
        51.5014591, -0.2175079),
    'Hôtel Le Walt, 37, Avenue de la Motte-Picquet, Gros-Caillou, 7e, Paris, Île-de-France, France métropolitaine, 75007, France': (
        48.8547458, 2.3065559),
    'La Villa Haussmann, 132, Boulevard Haussmann, Europe, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8752929, 2.3167096),
    'Hotel Leonardo, 6,8, Matrosengasse, Obere Windmühle, KG Mariahilf, Mariahilf, Wien, 1060, Österreich': (
        48.1945261, 16.3402647),
    'Bermudadreieck, Seitenstettengasse, Bermudadreieck, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.2116939, 16.3747088525205),
    'cent111onze, 111, Carrer del Pintor Fortuny, el Raval, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (
        41.383726, 2.1709656),
    '1, Audley Road, Acton, London Borough of Ealing, London, Greater London, England, W13, UK': (
        51.5210758, -0.291042402499844),
    "31, Ronda de la Universitat, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08003, España": (
        41.3871802, 2.16715930280123),
    "The Grosvenor, 101, Buckingham Palace Road, St. James's, Victoria, City of Westminster, London, Greater London, England, SW1W 0RP, UK": (
        51.49559815, -0.145218494250906),
    'Hôtel Crayon Rouge, Rue Coquillière, Quartier des Halles, Les Halles, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.8645288, 2.3405105),
    "Jardins de Carme Biada, Carrer de Roger de Llúria, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08023, España": (
        41.39833965, 2.16286649078859),
    "43, Rue de l'Abbé Grégoire, ND-des-Champs, 6e, Paris, Île-de-France, France métropolitaine, 75006, France": (
        48.8471473, 2.3259309),
    "17, Passatge de la Concepció, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08023, España": (
        41.3941771, 2.15979195551684),
    'NH Milano Grand Hotel Verdi, 6, Via Melchiorre Gioia, Varesine, Municipio 9, Milano, MI, LOM, 20124, Italia': (
        45.4813987, 9.19188206176094),
    'Hotel Berna, 18, Via Napo Torriani, Centrale, Municipio 2, Milano, MI, LOM, 20124, Italia': (
        45.4826665, 9.2034273),
    'Römischer Kaiser, 16, Annagasse, Kärntner Viertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.2040742, 16.3725344),
    '21, Naritaweg, Sloterdijk, Amsterdam, Westpoort, Amsterdam, Noord-Holland, Nederland, 1043BP, Nederland': (
        52.3874133, 4.8349673),
    "The Mandeville, Hinde Mews, St. James's, Marylebone, City of Westminster, London, Greater London, England, W1U 2NQ, UK": (
        51.51649265, -0.150945407633889),
    'Chiesa di San Raffaele, Galleria Ciro Fontana, Duomo, Municipio 1, Milano, MI, LOM, 20121, Italia': (
        45.4654104, 9.19156343833827),
    'Ham Yard Hotel, 1, Ham Yard, Soho, City of Westminster, London, Greater London, England, W1D 7DT, UK': (
        51.511163, -0.134909),
    'Hôtel Victoires Opéra, Rue Montorgueil, Quartier des Halles, Les Halles, 2e, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.8649114, 2.3469659),
    "La Ville d'Argentan, Rue d'Amsterdam, Quartier Saint-Georges, St-Georges, 9e, Paris, Île-de-France, France métropolitaine, 75009, France": (
        48.875912, 2.326979),
    "The Langham, Cavendish Place, St. James's, Fitzrovia, City of Westminster, London, Greater London, England, W1S 1PY, UK": (
        51.51756265, -0.143823863672016),
    '7, Rue Rennequin, Plaine-Monceau, 17e, Paris, Île-de-France, France métropolitaine, 75017, France': (
        48.8809055, 2.2989994),
    'Hilton Vienna Danube Waterfront, 269, Handelskai, Stuwerviertel, KG Leopoldstadt, Leopoldstadt, Wien, 1020, Österreich': (
        48.21406405, 16.4217091790491),
    '13, Via Enrico Stendhal, Zona Tortona, Municipio 6, Milano, MI, LOM, 20145, Italia': (45.451352, 9.160436),
    '7, Annagasse, Kärntner Viertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (48.20418, 16.3726583),
    '33, Via Carlo Goldoni, Zona Risorgimento, Acquabella, Milano, MI, LOM, 20129, Italia': (45.4693272, 9.2142549),
    "Le Comptoir du Relais, 9, Carrefour de l'Odéon, Odéon, 6e, Paris, Île-de-France, France métropolitaine, 75006, France": (
        48.8519626, 2.3388319),
    'Hôtel de la cité Rougemont, Cité Rougemont, Fg-Montmartre, 9e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.8720938, 2.3452475),
    '21, Wurzbachgasse, Nibelungenviertel, KG Fünfhaus, Rudolfsheim-Fünfhaus, Wien, 1150, Österreich': (
        48.2038097, 16.3356545),
    'Holiday Inn, Rue de Lyon, 12e Arrondissement (urbain), Quinze-Vingts, 12e, Paris, Île-de-France, France métropolitaine, 75012, France': (
        48.8467471, 2.3717077),
    "St George's Hotel, Linden Avenue, Alperton, London Borough of Brent, London, Greater London, England, HA9 8BB, UK": (
        51.55530435, -0.286451163958426),
    'Königin von Ungarn, 10, Schulerstraße, Stubenviertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.20814125, 16.375199590625),
    '19, Place du Panthéon, Sorbonne, 5e, Paris, Île-de-France, France métropolitaine, 75005, France': (
        48.8457641, 2.3448572),
    '45, Rue des Acacias, Ternes, 17e, Paris, Île-de-France, France métropolitaine, 75017, France': (
        48.8778081, 2.2932308),
    "The Trafalgar St. James London, Curio Collection by Hilton, 2, Spring Gardens, St. James's, Covent Garden, City of Westminster, London, Greater London, England, SW1A 2TS, UK": (
        51.5073487, -0.129427460109434),
    '7, Rilkeplatz, Freihausviertel, KG Wieden, Wieden, Wien, 1040, Österreich': (48.1978161, 16.367095),
    '38, Cleveland Square, Paddington, City of Westminster, London, Greater London, England, W2 6DA, UK': (
        51.5137298, -0.183418040746102),
    '42, Rue Vineuse, Muette, 16e, Paris, Île-de-France, France métropolitaine, 75116, France': (48.861311, 2.28628),
    'Paris Arc de Triomphe, Avenue des Ternes, Ternes, 17e, Paris, Île-de-France, France métropolitaine, 75017, France': (
        48.87816505, 2.29488265071702),
    '21, Leeuwendalersweg, Bos en Lommer, Amsterdam, West, Amsterdam, Noord-Holland, Nederland, 1055JE, Nederland': (
        52.3793024, 4.8457427),
    'Catedral, Carrer dels Sagristans, el Gòtic, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (
        41.3848367, 2.17524),
    "2, Avenue de l'Opéra, Palais Royal, 1er, Paris, Île-de-France, France métropolitaine, 75001, France": (
        48.8640984, 2.3353359),
    'Carnaval des Affaires, Boulevard Poissonnière, Fg-Montmartre, 2e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.8715556, 2.3439258),
    '5&33, 5, Martelaarsgracht, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1017, Nederland': (
        52.377864, 4.8969716),
    'Centre de secours Saint-Honoré, Rue Sainte-Anne, Palais Royal, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.86567685, 2.33547133291899),
    "Hôtel des Champs Élysée, Rue d'Artois, Quartier du Faubourg-du-Roule, 8e, Paris, Île-de-France, France métropolitaine, 75008, France": (
        48.8723588, 2.3088888),
    'Gelderlandplein, Zuideramstel, Amsterdam, Zuid, Amsterdam, Noord-Holland, Nederland, 1183, Nederland': (
        52.33122245, 4.87748610640909),
    'Imperial, 16, Kärntner Ring, Kärntner Viertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.2010498, 16.3728336778046),
    'Regina, Rue de Mazagran, Porte-St-Denis, 2e, Paris, Île-de-France, France métropolitaine, 75010, France': (
        48.87089315, 2.35173060021771),
    'Andreas Ensemble, Andreasplein, Slotervaart, Amsterdam, Nieuw-West, Amsterdam, Noord-Holland, Nederland, 1055, Nederland': (
        52.35741335, 4.84525286756623),
    'Anderson Hotel, 20, Piazza Luigi di Savoia, Centrale, Municipio 2, Milano, MI, LOM, 20124, Italia': (
        45.4852888, 9.20704562901713),
    '14, Arlandaweg, Sloterdijk, Amsterdam, Westpoort, Amsterdam, Noord-Holland, Nederland, 1043EW, Nederland': (
        52.3856225, 4.8344433),
    '4, Rue Lécluse, Batignolles, 17e, Paris, Île-de-France, France métropolitaine, 75017, France': (
        48.8835896, 2.3257422),
    'London Guards Hotel, 36 - 37, Lancaster Mews, Paddington, City of Westminster, London, Greater London, England, W2 3NA, UK': (
        51.512593, -0.1802574),
    'Hotel Casa Fuster, 132, Passeig de Gràcia, la Vila de Gràcia, Gràcia, Barcelona, BCN, CAT, 08008, España': (
        41.39817415, 2.15818940348883),
    'Barceló Antenea Mar, Passeig de Garcia Fària, Diagonal Mar i el Front Marítim del Poblenou, Sant Martí, Barcelona, BCN, CAT, 08020, España': (
        41.4023874, 2.2117838),
    "Monument Hotel, 75, Passeig de Gràcia, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08008, España": (
        41.39373455, 2.16211172458678),
    '19-21, Craven Hill, Paddington, City of Westminster, London, Greater London, England, W2 3DU, UK': (
        51.5124148, -0.18202885431066),
    'California Hotel, Belgrove Street, Holborn, London Borough of Camden, London, Greater London, England, WC1X 8BB, UK': (
        51.5295045, -0.123438),
    '13, Rue Jean Giraudoux, Chaillot, 16e, Paris, Île-de-France, France métropolitaine, 75116, France': (
        48.8689199, 2.2975411),
    "Carlton's, Boulevard de Rochechouart, Rochechouart, 9e, Paris, Île-de-France, France métropolitaine, 75009, France": (
        48.88194565, 2.34097657852622),
    '20142, Via Spezia, Quartiere Stadera, Chiesa Rossa, Milano, MI, LOM, 20136, Italia': (
        45.4409958, 9.17289963929102),
    'Yayami, Rue Richard Lenoir, Roquette, 11e, Paris, Île-de-France, France métropolitaine, 75011, France': (
        48.8571385, 2.3806468),
    'Hotel Felice Casati, Via Casati, Lazzaretto, Porta Nuova, Milano, MI, LOM, 20124, Italia': (45.4785666, 9.2042002),
    'Mahatna, 23, Rue Vignon, Vendôme, 9e, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.8716728, 2.3262544),
    'Hôtel duo, 11, Rue du Temple, Beaubourg, St-Merri, 3e, Paris, Île-de-France, France métropolitaine, 75004, France': (
        48.8580936, 2.3529258),
    '49, Vijzelstraat, Grachtengordel, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1017HE, Nederland': (
        52.3657859, 4.8932578),
    "Rda. Sant Pere - Pl. Urquinaona, Ronda de Sant Pere, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08003, España": (
        41.3896951, 2.1746222),
    'Milestone Hotel, Kensington Road, South Kensington, Royal Borough of Kensington and Chelsea, London, Greater London, England, W8 5PE, UK': (
        51.50195985, -0.186663181955496),
    'UBI Banco di Brescia, Viale Monza, Municipio 2, Milano, MI, LOM, 20132, Italia': (45.5007084, 9.2208548),
    'Villa Panthéon, Rue des Écoles, Sorbonne, 5e, Paris, Île-de-France, France métropolitaine, 75005, France': (
        48.8488721, 2.3470349),
    'Ayre Hotel Gran Via, 322-324, Gran Via de les Corts Catalanes, la Font de la Guatlla, Sants-Montjuïc, Barcelona, BCN, CAT, 08014, España': (
        41.373363, 2.1473387),
    'Room Mate Giulia Hotel, 4, Via Silvio Pellico, Duomo, Municipio 1, Milano, MI, LOM, 20121, Italia': (
        45.4651444, 9.1893365),
    "Mercure, 1a, Lexham Gardens, Earl's Court, Royal Borough of Kensington and Chelsea, London, Greater London, England, W8 5JJ, UK": (
        51.49490645, -0.190616494193546),
    'NH Hotel Galaxy, Distelkade, Disteldorp, Amsterdam, Noord, Amsterdam, Noord-Holland, Nederland, 1021, Nederland': (
        52.39237485, 4.91055226374636),
    'Arora Ballroom, Blackwall Tunnel, Blackwall, London Borough of Tower Hamlets, London, Greater London, England, E14 9SA, UK': (
        51.50270385, -0.000148334196176833),
    '5, Rue de Naples, Europe, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (48.8798058, 2.3205891),
    'Bilton Towers, Great Cumberland Place, Marylebone, City of Westminster, London, Greater London, England, W1, UK': (
        51.5147925, -0.159951360892572),
    "Les Finestres de Llúria, Carrer de Roger de Llúria, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08003, España": (
        41.3936321, 2.1684591),
    'Romana Residence Hotel, 64, Corso di Porta Romana, Municipio 1, Milano, MI, LOM, 20122, Italia': (
        45.4571983, 9.1937535),
    'strandhotel alte donau, An der oberen Alten Donau, KG Kagran, Donaustadt, Neukagran, Wien, 1220, Österreich': (
        48.2391259, 16.4289979261772),
    'Simply Rooms and Suites Kensington, 21, Avonmore Road, West Kensington, London Borough of Hammersmith and Fulham, London, Greater London, England, W14 8RT, UK': (
        51.4944913, -0.207066974999998),
    '13, Rue Jules César, 12e Arrondissement (urbain), Quinze-Vingts, 12e, Paris, Île-de-France, France métropolitaine, 75012, France': (
        48.8489727, 2.3698005),
    'Eitljörg, Filmteichstraße, Siedlung Südost, KG Oberlaa Stadt, Favoriten, Stierofen, Wien, 1100, Österreich': (
        48.15118895, 16.4064883719126),
    'The Hyde Park Premier, 14-16, Craven Hill, Paddington, City of Westminster, London, Greater London, England, W2 3DU, UK': (
        51.5132285, -0.1806004),
    'W11 19, Stanley Gardens, Silchester Estate, Notting Hill, Royal Borough of Kensington and Chelsea, London, Greater London, England, W11 2ND, UK': (
        51.5125034, -0.203206),
    '132, Hietzinger Hauptstraße, KG Ober St. Veit, Hietzing, Wien, 1130, Österreich': (48.1878461, 16.2728296152556),
    '3, Boulevard Saint-Michel, Sorbonne, 5e, Paris, Île-de-France, France métropolitaine, 75005, France': (
        48.852843, 2.3440704),
    '30, Rue Pernety, Plaisance, 14e, Paris, Île-de-France, France métropolitaine, 75014, France': (
        48.83345, 2.3190508),
    'Ambassade Hotel, 341, Herengracht, Negen Straatjes, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1016AZ, Nederland': (
        52.3693735, 4.887183),
    'Schubert Bar, 11, Schubertring, Kärntner Viertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.2017055, 16.3754187),
    'AC Barcelona, Passeig del Taulat, Diagonal Mar i el Front Marítim del Poblenou, Sant Martí, Barcelona, BCN, CAT, 08020, España': (
        41.4101986, 2.21884492298088),
    'The Beauchamp, 24-27, Bedford Place, Holborn, Bloomsbury, London Borough of Camden, London, Greater London, England, WC1B 5JH, UK': (
        51.5203735, -0.1248357),
    'Hotel Vincci Condal Mar, 138, Carrer Cristobal de Moura, la Catalana, Sant Adrià de Besòs, BCN, CAT, 08019, España': (
        41.4114921, 2.211856),
    "SB Icaria Barcelona, Avinguda d'Icària, la Vila Olímpica del Poblenou, Sant Martí, Barcelona, BCN, CAT, 08003, España": (
        41.3936323, 2.1994114),
    'Étoile Saint-Honoré, Rue du Faubourg Saint-Honoré, Quartier du Faubourg-du-Roule, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8756281, 2.3041375),
    'Tesco Express, Baker Street, Marylebone, City of Westminster, London, Greater London, England, W1U 6RJ, UK': (
        51.5209709, -0.156710756952406),
    'Hôtel Le Littré, Rue Littré, ND-des-Champs, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.8454273, 2.3241304),
    '4, Rue de Valois, Palais Royal, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.8631129, 2.3377752),
    'Hotel & Palais Strudlhof, Strudlhofgasse, Thurygrund II, KG Alsergrund, Alsergrund, Wien, 1090, Österreich': (
        48.2218441, 16.3570980693834),
    "267, Carrer del Consell de Cent, l'Antiga Esquerra de l'Eixample, Eixample, Barcelona, BCN, CAT, 08014, España": (
        41.38734205, 2.16037573224724),
    '41, Cleveland Square, Paddington, City of Westminster, London, Greater London, England, W2 6DA, UK': (
        51.51390265, -0.182891429512397),
    'Atala, 10, Rue de Chateaubriand, Quartier du Faubourg-du-Roule, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8733993, 2.3023131),
    '34, Rue de Buci, St-Germain-des-Prés, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.8534652, 2.3360798),
    'Hotel Le Chat Noir, 68, Boulevard de Clichy, Grandes-Carrières, 18e, Paris, Île-de-France, France métropolitaine, 75018, France': (
        48.8835582, 2.3341029),
    "Hôtel La Tour d'Auvergne, Rue de la Tour d'Auvergne, Rochechouart, 9e, Paris, Île-de-France, France métropolitaine, 75009, France": (
        48.8789211, 2.3448903),
    '29, Bond Street, West Ealing, Perivale, London Borough of Ealing, London, Greater London, England, W13, UK': (
        51.5121913, -0.305677057420473),
    '2, Boulevard Garibaldi, Necker, 15e, Paris, Île-de-France, France métropolitaine, 75015, France': (
        48.8475239, 2.30223),
    '17, Rathausstraße, KG Alsergrund, Alsergrund, Wien, 1010, Österreich': (48.2132776, 16.3568541),
    'SW7 15, Harrington Gardens, South Kensington, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW7 4LT, UK': (
        51.4928411, -0.1845542),
    '519, Herengracht, Grachtengordel, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1017BV, Nederland': (
        52.3653633, 4.8932037),
    'Ferrovia Milano-Mortara, Via Mario Pagano, Zona Pagano, Porta Vercellina, Milano, MI, LOM, 20145, Italia': (
        45.4676699, 9.1596583),
    '230, Mile End Road, Stepney, London Borough of Tower Hamlets, London, Greater London, England, E10, UK': (
        51.52154775, -0.04689818686485),
    'Shop, Rue du Faubourg Poissonnière, Porte-St-Denis, 9e, Paris, Île-de-France, France métropolitaine, 75010, France': (
        48.8776775, 2.3492392),
    'Room Mate Aitana Hotel, 6, IJdok, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1013MM, Nederland': (
        52.38468495, 4.89410932980969),
    'The Kooples sport, 97, Avenue des Champs-Élysées, Champs-Élysées, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8712822, 2.30139861596342),
    'Shell, Bingle Road, Rosslyn, Harris County, Texas, 77092, United States of America': (
        29.8370615, -95.4887079713318),
    '4, Bognergasse, Widmerviertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (48.2102811, 16.3682838),
    "The Wellesley, 11, Knightsbridge, St. James's, Belgravia, City of Westminster, London, Greater London, England, SW3 4, UK": (
        51.502305, -0.153795801977688),
    '36, Rue Saint-Marc, Vivienne, 2e, Paris, Île-de-France, France métropolitaine, 75002, France': (
        48.8708032, 2.3382303),
    'Apex Temple Court Hotel, 1-2, Serjeants Inn Courtyard, Temple, London, Greater London, England, EC4Y 1LL, UK': (
        51.5138157, -0.1089001),
    'Barceló Milan, 55, Via Giorgio Stephenson, Musocco, Milano, MI, LOM, 20157, Italia': (45.51159, 9.124219),
    '35, Rue Jean Goujon, Champs-Élysées, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8652585, 2.3044797),
    'Austria Trend Hotel Savoyen, 16, Rennweg, Botschaftsviertel, KG Landstraße, Landstraße, Wien, 1030, Österreich': (
        48.19453625, 16.3846192988296),
    'Hotel de Filosoof, 6, Anna van den Vondelstraat, Oud-West, Amsterdam, West, Amsterdam, Noord-Holland, Nederland, 1054 GZ, Nederland': (
        52.3607582, 4.8695022),
    'Viena, la Rambla, el Gòtic, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (41.3842121, 2.1706668),
    "St Paul's Hotel, Hammersmith Road, Brook Green, London Borough of Hammersmith and Fulham, London, Greater London, England, W6 7BY, UK": (
        51.493543, -0.215281),
    '8-10, Sonnenhofgasse, KG Margarethen, Margareten, Wien, 1050, Österreich': (48.1914879, 16.3546443),
    'Le Meurice, Rue de Rivoli, Vendôme, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.8652754, 2.3282212),
    'Hotel Brunelleschi, 12, Via Flavio Baracchini, Bottonuto, Municipio 1, Milano, MI, LOM, 20123, Italia': (
        45.4611333, 9.1911546),
    "Le relais du Louvre, Rue des Prêtres Saint-Germain l'Auxerrois, St-Germain-l'Auxerrois, 1er, Paris, Île-de-France, France métropolitaine, 75001, France": (
        48.8592501, 2.3409933),
    'Hotel Margareten Wien, 142, Margaretengürtel, KG Margarethen, Margareten, Wien, 1050, Österreich': (
        48.1867527, 16.3439838),
    '7, Rue Gît-le-Coeur, Monnaie, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.8539545, 2.3429117),
    '7 Bis, Rue Bélidor, Ternes, 17e, Paris, Île-de-France, France métropolitaine, 75017, France': (
        48.8802219, 2.2859422),
    'Windsor Hotel, 2, Via Galileo Galilei, Varesine, Porta Nuova, Milano, MI, LOM, 20124, Italia': (
        45.4795392, 9.195209),
    '8, Rue Jean Goujon, Champs-Élysées, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.866596, 2.309069),
    '14, Rue Stanislas, ND-des-Champs, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.8437978, 2.3281335),
    '78-80, Mariahilfer Straße, Obere Windmühle, KG Mariahilf, Mariahilf, Wien, 1070, Österreich': (
        48.1980909, 16.3482901289726),
    'Hotel Cavour, 21, Via Fatebenefratelli, Borgonuovo, Porta Nuova, Milano, MI, LOM, 20121, Italia': (
        45.4726283, 9.194509),
    'Hôtel Powers, 52, Rue François 1er, Champs-Élysées, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8691472, 2.3031344),
    "58, Carrer d'Enric Granados, l'Antiga Esquerra de l'Eixample, Eixample, Barcelona, BCN, CAT, 08023, España": (
        41.39195645, 2.15733699400743),
    'Tesla Supercharger, Upper Berkeley Street, Marylebone, City of Westminster, London, Greater London, England, W1H 7QZ, UK': (
        51.5157251, -0.157401), 'Palazzo Clerici, Via Clerici, Cordusio, Municipio 1, Milano, MI, LOM, 20121, Italia': (
        45.4667744, 9.18718778308071),
    'Hôtel Bachaumont, Rue Bachaumont, Mail, 2e, Paris, Île-de-France, France métropolitaine, 75002, France': (
        48.86624815, 2.34505184584852),
    'Hotel Atenea, 209, Carrer de Joan Güell, les Corts, Barcelona, BCN, CAT, 08028, España': (
        41.38617175, 2.12881689660116),
    'DoubleTree by Hilton Hotel London - Ealing, 2-8, Hanger Lane, Acton, London Borough of Ealing, London, Greater London, England, W5 3HN, UK': (
        51.51151365, -0.290603949383685),
    'Hilton London Bankside, 2-8, Great Suffolk Street, Southwark, London Borough of Southwark, London, Greater London, England, SE1 0UG, UK': (
        51.50558795, -0.101643012281146),
    '7, Rue Paul Albert, Château Rouge, Clignancourt, 18e, Paris, Île-de-France, France métropolitaine, 75018, France': (
        48.8866775, 2.3450117),
    'Le Meridien, Opernring, Kärntner Viertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.2026339, 16.3663656139251),
    'Ramada Encore, 11, Grieshofgasse, KG Meidling, Meidling, Kabelwerk, Wien, 1120, Österreich': (
        48.18275045, 16.3327818502924),
    'Leonidas, Rue Pergolèse, Chaillot, 16e, Paris, Île-de-France, France métropolitaine, 75116, France': (
        48.8757441, 2.2863651),
    'Park Plaza Westminster Bridge, Westminster Bridge Road, Lambeth, London Borough of Lambeth, London, Greater London, England, SE15, UK': (
        51.5008932, -0.116538002891655),
    'Catalonia Atenas, 151, Avinguda Meridiana, Navas, Sant Martí, Barcelona, BCN, CAT, 08030, España': (
        41.4110737, 2.1865397),
    '717-O, Prinsengracht, Grachtengordel, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1017JW, Nederland': (
        52.3647911, 4.8853408),
    '34, Rue de Moscou, Europe, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8813648, 2.3234883),
    'Mercure Paris Alesia, 185, Boulevard Brune, Petit-Montrouge, 14e, Paris, Île-de-France, France métropolitaine, 75014, France': (
        48.82382715, 2.32411667082365),
    'Hyatt Regency Amsterdam, 104, Sarphatistraat, Weesperbuurt, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1018GV, Nederland': (
        52.3617812, 4.9117415),
    '123, Boulevard de Sébastopol, Sentier, Bonne-Nouvelle, 2e, Paris, Île-de-France, France métropolitaine, 75002, France': (
        48.8676341, 2.3530937),
    'Courthouse, 19-21, Great Marlborough Street, Soho, City of Westminster, London, Greater London, England, W1F 7HH, UK': (
        51.5143154, -0.1394202),
    'Hotel Bosei, 7b, Gutheil-Schoder-Gasse, KG Inzersdorf Stadt, Favoriten, Wien, 1100, Österreich': (
        48.1630617, 16.3403469589497),
    "2, Rue Édouard VII, Chaussée-d'Antin, 9e, Paris, Île-de-France, France métropolitaine, 75009, France": (
        48.8704448, 2.3292245),
    '8, Piazza Ventiquattro Maggio, Zona Navigli, Porta Ticinese, Milano, MI, LOM, 20123, Italia': (
        45.4531429, 9.1791381),
    'Jardins de Joan Fuster i Ortells, Passeig del Taulat, Diagonal Mar i el Front Marítim del Poblenou, Sant Martí, Barcelona, BCN, CAT, 08020, España': (
        41.4019271, 2.21025697586851),
    '4, Rue Cadet, Fg-Montmartre, 9e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.8743143, 2.3425777),
    'Holiday Inn Brent Cross, Tilling Road, Clitterhouse Estate, Brent Cross, London Borough of Barnet, London, Greater London, England, NW2 1LP, UK': (
        51.57293305, -0.222652645354774),
    "Hotel Sercotel Abbot, Avinguda de Roma, la Nova Esquerra de l'Eixample, Eixample, Barcelona, BCN, CAT, 08014, España": (
        41.3815341, 2.1449734),
    'Brent Street / Green Lane, Brent Street, Hendon, London Borough of Barnet, London, Greater London, England, NW4 2EX, UK': (
        51.5834342, -0.2164),
    'Golden Tulip Amsterdam West, 1, Molenwerf, Bos en Lommer, Amsterdam, West, Amsterdam, Noord-Holland, Nederland, 1055, Nederland': (
        52.3854025, 4.8469012),
    '1, Pelzgasse, Nibelungenviertel, KG Fünfhaus, Rudolfsheim-Fünfhaus, Wien, 1150, Österreich': (
        48.1979912, 16.3364036),
    "2, Rue d'Amboise, Vivienne, 2e, Paris, Île-de-France, France métropolitaine, 75002, France": (
        48.8709859, 2.3393994),
    'Scheepvaarthuis, Buiten Bantammerstraat, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1017, Nederland': (
        52.37430235, 4.90413325401224),
    'Champs-Élysées Plaza, Rue de Berri, Quartier du Faubourg-du-Roule, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8737055, 2.3062317),
    'Holiday Inn, Rue Gager-Gabillot, Necker, 15e, Paris, Île-de-France, France métropolitaine, 75015, France': (
        48.837696, 2.3062844),
    '10, Rue Chénier, Sentier, Bonne-Nouvelle, 2e, Paris, Île-de-France, France métropolitaine, 75002, France': (
        48.8694524, 2.3514427),
    "700, Gran Via de les Corts Catalanes, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08003, España": (
        41.393611, 2.1742789),
    'Holiday Inn, Jamestown Road, Chalk Farm, London Borough of Camden, London, Greater London, England, NW1 7DJ, UK': (
        51.5403595, -0.146078),
    'Best Western Montmartre Sacré Coeur, 66, Boulevard Barbès, Château Rouge, Clignancourt, 18e, Paris, Île-de-France, France métropolitaine, 75018, France': (
        48.88863345, 2.34989527692308),
    "Millennium Bailey's Hotel\u200e, Gloucester Road, South Kensington, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW7 4SS, UK": (
        51.4938416, -0.182444849359753),
    "L'Antoine, Rue de Charonne, 12e Arrondissement (urbain), Quinze-Vingts, 11e, Paris, Île-de-France, France métropolitaine, 75012, France": (
        48.8524194, 2.3743229),
    'Holliday Inn, Avenue du Maine, Montparnasse, 14e, Paris, Île-de-France, France métropolitaine, 75014, France': (
        48.8383119, 2.3229285),
    'Capri by Fraser Barcelona, el Parc i la Llacuna del Poblenou, Sant Martí, Barcelona, BCN, CAT, 08003, España': (
        41.3975377, 2.18905814364859),
    "255, Carrer de Còrsega, l'Antiga Esquerra de l'Eixample, Eixample, Barcelona, BCN, CAT, 08014, España": (
        41.3931725, 2.15442820554273),
    '159, Cromwell Road, South Kensington, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW7 4DT, UK': (
        51.4944872, -0.190931002868853),
    'Relay, Gare RER - Gare de Lyon, 12e Arrondissement (urbain), Quinze-Vingts, 12e, Paris, Île-de-France, France métropolitaine, 75012, France': (
        48.84422015, 2.37311516416309),
    "Hôtel d'Aubusson, Rue Dauphine, Monnaie, 6e, Paris, Île-de-France, France métropolitaine, 75006, France": (
        48.8547614, 2.3395044),
    'The Toren, 164, Keizersgracht, Grachtengordel, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1015CZ, Nederland': (
        52.3758754, 4.8859642),
    "Le Méridien Piccadilly, Piccadilly, St. James's, Mayfair, City of Westminster, London, Greater London, England, W1J 0LA, UK": (
        51.50939405, -0.136592945561144),
    'Starhotels Business Palace, Via Carlo Boncompagni, Corvetto, Milano, MI, LOM, 20141, Italia': (
        45.4378379, 9.23090764942086),
    'Bilderberg Garden Hotel, Apollolaan, Oud-Zuid, Amsterdam, Zuid, Amsterdam, Noord-Holland, Nederland, 1053, Nederland': (
        52.3510598, 4.87412223913864),
    "14, Rue de Saint-Simon, St-Thomas-d'Aquin, 7e, Paris, Île-de-France, France métropolitaine, 75007, France": (
        48.856042, 2.3236727),
    '40, Pembridge Road, Notting Hill, Royal Borough of Kensington and Chelsea, London, Greater London, England, W11 3HN, UK': (
        51.51010745, -0.19713987161859),
    '2, Uraniastraße, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (48.2110789, 16.3838512),
    '9, Rue Frochot, Quartier Saint-Georges, St-Georges, 9e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.8816183, 2.3372802),
    "Gail's, Bayley Street, Holborn, Bloomsbury, London Borough of Camden, London, Greater London, England, WC1B 3HA, UK": (
        51.51884675, -0.131954815797174),
    'The Wesley, 81-103, Euston Street, Holborn, Somers Town, London Borough of Camden, London, Greater London, England, NW1 2EZ, UK': (
        51.52670505, -0.135861242396159),
    'Westminster Bridge House, Westminster Bridge Road, Lambeth, London Borough of Lambeth, London, Greater London, England, SE15, UK': (
        51.49898965, -0.113216593414291),
    'Mirage, 104, Viale Certosa, Boldinasco, Milano, MI, LOM, 20148, Italia': (45.4946406, 9.1419987),
    "L'Espace Harmattan, Rue des Écoles, Sorbonne, 5e, Paris, Île-de-France, France métropolitaine, 75005, France": (
        48.84832605, 2.34904966323378),
    "The Three Tuns, 1, Portman Mews South, St. James's, Mayfair, City of Westminster, London, Greater London, England, W1H 6DZ, UK": (
        51.514523, -0.155939718565824),
    '14, Rue Joseph de Maistre, Grandes-Carrières, 18e, Paris, Île-de-France, France métropolitaine, 75018, France': (
        48.8865453, 2.332909),
    '15, Rotenturmstraße, Stubenviertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.210273, 16.3741112),
    'Jolly, Largo Augusto, Verziere, Municipio 1, Milano, MI, LOM, 20121, Italia': (45.46309, 9.1977928),
    'Courtyard Vienna Schönbrunn, 38-40, Schönbrunner Schlossstraße, Obermeidling, KG Meidling, Meidling, Kabelwerk, Wien, 1120, Österreich': (
        48.18479885, 16.3210324647348),
    "La Muscleria, 290, Carrer de Mallorca, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08003, España": (
        41.3964732, 2.1662651),
    "The Dorchester, 53, Park Lane, St. James's, Mayfair, City of Westminster, London, Greater London, England, W1K 1QA, UK": (
        51.5072956, -0.152363447244274),
    '8, Rue Frédéric Bastiat, Quartier du Faubourg-du-Roule, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.872861, 2.3073078),
    '2, Landstraßer Hauptstraße, Botschaftsviertel, KG Landstraße, Landstraße, Wien, 1030, Österreich': (
        48.2062114, 16.3833716),
    'W6 29D, Goldhawk Road, London Borough of Hammersmith and Fulham, London, Greater London, England, W6 0SA, UK': (
        51.4940442, -0.2450531),
    'Botschaft der Vereinigten Staaten (Konsularabteilung), 12a, Parkring, Stubenviertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.2050846, 16.3772704),
    "Dean's Bar, Cosmo Place, Holborn, Bloomsbury, London Borough of Camden, London, Greater London, England, WC1N 3AH, UK": (
        51.5209138, -0.1231538),
    '4, Rue du Docteur Laurent, Cité florale, Maison-Blanche, 13e, Paris, Île-de-France, France métropolitaine, 75013, France': (
        48.8251623, 2.3571022),
    'Carrer del Putget, el Putget, el Putget i Farró, Sarrià - Sant Gervasi, Barcelona, BCN, CAT, 08023, España': (
        41.4066603, 2.1440589),
    '74, Jan Luijkenstraat, Museumkwartier, Amsterdam, Zuid, Amsterdam, Noord-Holland, Nederland, 1071CT, Nederland': (
        52.3596283, 4.8802463),
    'Schild, 97-99, Neustift am Walde, KG Neustift am Walde, Döbling, Wien, 1190, Österreich': (
        48.2512422, 16.2986766241969),
    'King Mokinba Hotel, 19, Corso Magenta, Municipio 1, Milano, MI, LOM, 20133, Italia': (45.4656506, 9.1778515),
    'idea hotel milano san siro, Via Gaetano Airaghi, Quinto Romano, Milano, MI, LOM, 20019, Italia': (
        45.4716369, 9.0779012),
    "Hotel Avenida Palace, 605-607, Gran Via de les Corts Catalanes, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08003, España": (
        41.3890433, 2.1673446),
    'Hôtel Dacia, Boulevard Saint-Michel, Sorbonne, 6e, Paris, Île-de-France, France métropolitaine, 75005, France': (
        48.8492256, 2.3422373),
    'Holiday Inn Vienna City, 53, Margaretenstraße, Nikolsdorf, KG Margarethen, Margareten, Wien, 1050, Österreich': (
        48.1935645, 16.361588),
    "Haymarket Hotel, Suffolk Place, St. James's, Covent Garden, City of Westminster, London, Greater London, England, SW1Y 4HX, UK": (
        51.5082841, -0.131150385942764),
    'NH Grand Hotel Krasnapolsky, 9, Dam, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1012JS, Nederland': (
        52.3727291, 4.8943846),
    "2, Rue Scribe, Chaussée-d'Antin, 9e, Paris, Île-de-France, France métropolitaine, 75009, France": (
        48.8707377, 2.3302414),
    'Amstel Hotel, Prof. Tulpplein, Rivierenbuurt, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1017, Nederland': (
        52.36001025, 4.90508928822191),
    '94, Boulevard Richard Lenoir, St-Ambroise, 11e, Paris, Île-de-France, France métropolitaine, 75011, France': (
        48.86291, 2.37232),
    'Quality Maîtrise Hotel, 53-57, Kilburn High Road, South Hampstead, London Borough of Camden, London, Greater London, England, NW6 5SB, UK': (
        51.53649985, -0.192024756968721),
    'Solid 1A, IJburglaan, IJburg, Amsterdam, Oost, Amsterdam, Noord-Holland, Nederland, 1024, Nederland': (
        52.35937455, 4.98833397626796),
    'Greenwich Novotel, Greenwich High Road, Greenwich, London, Greater London, England, SE10 8JL, UK': (
        51.47784935, -0.013755863341121),
    "Generalitat de Catalunya. Departament Agricultura, Gran Via de les Corts Catalanes (lateral mar), la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08003, España": (
        41.3874243, 2.16627152036766),
    'Palazzo del Monte di Pietà, Via Monte di Pietà, Scala, Municipio 1, Milano, MI, LOM, 20121, Italia': (
        45.46955095, 9.18957145780543),
    'Grand Hotel Et De Milan, 29, Via Alessandro Manzoni, Borgonuovo, Municipio 1, Milano, MI, LOM, 20121, Italia': (
        45.4699226, 9.1924982),
    'Hotel Nasco, 69, Corso Sempione, Zona Sempione, Municipio 8, Milano, MI, LOM, 20149, Italia': (
        45.4847404, 9.1596392),
    'London Marriott Hotel West India Quay, 22, Hertsmere Road, Poplar, London Borough of Tower Hamlets, London, Greater London, England, E14 4ED, UK': (
        51.50736435, -0.0210665046211476),
    '17, Rue Amélie, Gros-Caillou, 7e, Paris, Île-de-France, France métropolitaine, 75007, France': (
        48.8584862, 2.3077182),
    '59, Carrer de Nicaragua, les Corts, Barcelona, BCN, CAT, 08014, España': (41.38321425, 2.14071798814109),
    '66, 68, Carrer de Deu i Mata, les Corts, Barcelona, BCN, CAT, 08014, España': (41.3884136, 2.13609884123839),
    'The Crown Moran Hotel, Yew Grove, Cricklewood, London Borough of Brent, London, Greater London, England, NW2 3AB, UK': (
        51.556173, -0.214180567177221),
    "L'Illa Diagonal, 557, Avinguda Diagonal, les Corts, Barcelona, BCN, CAT, 08014, España": (
        41.389584, 2.13501142898845),
    'Hôtel de Neuville, 3, Rue Verniquet, Plaine-Monceau, 17e, Paris, Île-de-France, France métropolitaine, 75017, France': (
        48.886898, 2.300469),
    'Hôtel Lleo, 22, 24, Carrer de Pelai, el Raval, Eixample, Barcelona, BCN, CAT, 08001, España': (
        41.385617, 2.1669838),
    '11, Passage du Clos Bruneau, Sorbonne, 5e, Paris, Île-de-France, France métropolitaine, 75005, France': (
        48.8485619, 2.3479376),
    '18, Rue du Cirque, Madeleine, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8709971, 2.3153969),
    'citizenM, 6, Holywell Lane, Shoreditch, London Borough of Hackney, London, Greater London, England, EC2V 7HH, UK': (
        51.52426315, -0.0787145603152297),
    'Hôtel Saint-Dominique, Rue Saint-Dominique, Gros-Caillou, 7e, Paris, Île-de-France, France métropolitaine, 75007, France': (
        48.8599286, 2.308788),
    'Sofitel Vienna Stephansdom, Praterstraße, Karmeliterviertel, KG Leopoldstadt, Leopoldstadt, Wien, 1020, Österreich': (
        48.21295685, 16.3799138167908),
    'Bridges, Oudezijds Voorburgwal, Burgwallen-Oude Zijde, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1017, Nederland': (
        52.3709275, 4.895255),
    'Institut Français, Cromwell Mews, Brompton, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW7, UK': (
        51.4944053, -0.1749475),
    'Melia Milano, 19, Via Masaccio, Tre Torri, Milano, MI, LOM, 20148, Italia': (45.4791849, 9.1458654),
    "base2stay, Morton Mews, Earl's Court, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW5 0PG, UK": (
        51.4931293, -0.190616317221044),
    'Hotel Ambassador, 22, Kärntner Straße, Kärntner Viertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.2057281, 16.3710897),
    'Lambeth Palace, Lambeth Road, Lambeth, London Borough of Lambeth, London, Greater London, England, SE1, UK': (
        51.4948535, -0.1189516),
    'Novotel Porte de la Chapelle, 1, Impasse Marteau, La Chapelle, 18e, Paris, Île-de-France, France métropolitaine, 75018, France': (
        48.901704, 2.3596074),
    '66, Boulevard de Grenelle, Grenelle, 15e, Paris, Île-de-France, France métropolitaine, 75015, France': (
        48.8504659, 2.2928097),
    '217 - Rector Ubach 24, 24, Carrer del Rector Ubach, Galvany, Sant Gervasi - Galvany, Sarrià - Sant Gervasi, Barcelona, BCN, CAT, 08006, España': (
        41.3984153, 2.1440139),
    '203, High Holborn, Holborn, St Giles, London Borough of Camden, London, Greater London, England, WC1V 7BD, UK': (
        51.5170405, -0.122292042172978),
    '21, Montague Street, Holborn, Bloomsbury, London Borough of Camden, London, Greater London, England, WC1B 5BH, UK': (
        51.51984705, -0.125187258646979),
    'CitizenM, 30, Prinses Irenestraat, Zuideramstel, Amsterdam, Zuid, Amsterdam, Noord-Holland, Nederland, 1077WX, Nederland': (
        52.34194195, 4.87597212187505),
    'AC Marriott Victoria Suites, Carrer de Josep M. de Segarra, Pedralbes, les Corts, Barcelona, BCN, CAT, 08014, España': (
        41.3893464, 2.1212331),
    'The Westbridge Hotel, 335-337, High Street, Mill Meads, Newham, London, Greater London, England, E10, UK': (
        51.53738355, -0.00237431619328176),
    "104, Carrer de Balmes, l'Antiga Esquerra de l'Eixample, Eixample, Barcelona, BCN, CAT, 08014, España": (
        41.39165965, 2.15921836378423),
    'Hotel Monsieur, 62, Rue des Mathurins, Madeleine, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8735214, 2.3216484),
    "Casa Camper Barcelona, Carrer d'Elisabets, el Raval, Ciutat Vella, Barcelona, BCN, CAT, 08003, España": (
        41.3832308, 2.1685776),
    'Mercure Notre-Dame, Rue du Sommerard, Sorbonne, 5e, Paris, Île-de-France, France métropolitaine, 75005, France': (
        48.85035495, 2.34503709682687),
    "Moonlight, 9, Knaresborough Place, Earl's Court, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW5 0TP, UK": (
        51.49392265, -0.19113021504854),
    'Abbey Street, Tower Bridge Road, Walworth, London Borough of Southwark, London, Greater London, England, SE17, UK': (
        51.4990415, -0.0792265),
    '4, Kleine Stadtgutgasse, Jägerzeile, KG Leopoldstadt, Leopoldstadt, Wien, 1020, Österreich': (
        48.21855325, 16.3882183631371),
    'Villa Montparnasse, Rue Boulard, Montparnasse, 14e, Paris, Île-de-France, France métropolitaine, 75014, France': (
        48.8348854, 2.3296013),
    'Hôtel Vernet, 25, Rue Vernet, Champs-Élysées, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.871859, 2.29784787426002),
    'Ontario Tower, 4, Fairmont Avenue, Blackwall, London Borough of Tower Hamlets, London, Greater London, England, E14 9JD, UK': (
        51.50680735, -0.00460798593575214),
    'Hotel Attica 21, 10, Carrer de Provençals, Diagonal Mar i el Front Marítim del Poblenou, Sant Martí, Barcelona, BCN, CAT, 08019, España': (
        41.4051323, 2.2118586),
    'Pharmacie des Arts, Rue Victor Massé, Quartier Saint-Georges, St-Georges, 9e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.8808537, 2.3375391),
    'Golden Tours, 156, Cromwell Road, South Kensington, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW7 4EF, UK': (
        51.4947682, -0.1883974),
    'Hotel Silken Diagonal Barcelona, 205, Avinguda Diagonal, el Parc i la Llacuna del Poblenou, Sant Martí, Barcelona, BCN, CAT, 08018, España': (
        41.40362725, 2.19027432971146),
    'Radisson Blu Edwardian Vanderbilt Hotel, Cromwell Road, South Kensington, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW7 4EN, UK': (
        51.4952842, -0.1816667),
    'Hôtel Napoléon, Avenue de Friedland, Quartier du Faubourg-du-Roule, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.87433955, 2.29811282706478),
    'Hotel Novotel Barcelona City, 201, Avinguda Diagonal, el Parc i la Llacuna del Poblenou, Sant Martí, Barcelona, BCN, CAT, 08018, España': (
        41.40379165, 2.19123412999803),
    '21, Avenue de la Grande Armée, Chaillot, 16e, Paris, Île-de-France, France métropolitaine, 75017, France': (
        48.8748025, 2.2907235),
    'Arenberg, Stubenring, Stubenviertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.2106871, 16.3822517),
    '2, Grünangergasse, Stubenviertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (48.2079673, 16.3756382),
    'Les bols de Jean, 2, Rue de Choiseul, Gaillon, 2e, Paris, Île-de-France, France métropolitaine, 75002, France': (
        48.86901, 2.3368741),
    'Gran Hotel Torre Catalunya, 2-4, Avinguda de Roma, Hostafrancs, Eixample, Barcelona, BCN, CAT, 08014, España': (
        41.37965105, 2.14249778242236),
    '9, Rue Pierre Chausson, Porte-St-Martin, 10e, Paris, Île-de-France, France métropolitaine, 75010, France': (
        48.8708286, 2.3605968),
    '2, Boulevard Edgar Quinet, Montparnasse, 14e, Paris, Île-de-France, France métropolitaine, 75014, France': (
        48.8396173, 2.3300518),
    '7, Rotensterngasse, Afrikanerviertel, KG Leopoldstadt, Leopoldstadt, Wien, 1020, Österreich': (
        48.2179153, 16.3820546),
    "The Rookery, 12, Peter's Lane, Clerkenwell, London Borough of Islington, London, Greater London, England, EC1M 6DS, UK": (
        51.5203205, -0.102404853611485),
    '1 Bis, Avenue Mac-Mahon, Ternes, 17e, Paris, Île-de-France, France métropolitaine, 75017, France': (
        48.8753599, 2.2945219),
    'Hôtel Le Derby Alma, 8, Avenue Rapp, Gros-Caillou, 7e, Paris, Île-de-France, France métropolitaine, 75007, France': (
        48.8604399, 2.3007825),
    'Kaiserhof, 10, Frankenberggasse, Freihausviertel, KG Wieden, Wieden, Wien, 1040, Österreich': (
        48.19758595, 16.3686251965092),
    'Admiral Hotel, 16, Via Domodossola, Tre Torri, Milano, MI, LOM, 20145, Italia': (45.4804653, 9.159961),
    'A Galceran Marquet, Plaça del Duc de Medinaceli, el Gòtic, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (
        41.37832885, 2.17897395536744),
    'Wellington House, Savoy Street, St Clement Danes, Covent Garden, City of Westminster, London, Greater London, England, WC2E 7ED, UK': (
        51.5109605, -0.119406069092318),
    '3, Rue Rouget de Lisle, Vendôme, 1er, Paris, Île-de-France, France métropolitaine, 75001, France': (
        48.8660934, 2.3261969),
    "Club Quarters, 61, Lincoln's Inn Fields, St Clement Danes, City of Westminster, London, Greater London, England, WC2A 3JW, UK": (
        51.5159928, -0.118633054112798),
    '12, Rue Saint-Didier, Chaillot, 16e, Paris, Île-de-France, France métropolitaine, 75116, France': (
        48.8662359, 2.2881094),
    'Hotel Baviera, 7, Via Panfilo Castaldi, Porta Nuova, Milano, MI, LOM, 20124, Italia': (45.4782733, 9.1998607),
    "The Grange, St Paul's, 10, Godliman Street, Temple, London, Greater London, England, EC4V 5AJ, UK": (
        51.5126951, -0.09968697322609),
    '4, Rue Mousset-Robert, 12e Arrondissement (urbain), Bel-Air, 12e, Paris, Île-de-France, France métropolitaine, 75012, France': (
        48.8430291, 2.4049143),
    'Hotel Sacher, 4, Philharmonikerstraße, Kärntner Viertel, KG Innere Stadt, Innere Stadt, Wien, 1010, Österreich': (
        48.2038797, 16.3698061),
    'Hôtel Mercedes, Rue Brémontier, Plaine-Monceau, 17e, Paris, Île-de-France, France métropolitaine, 75017, France': (
        48.88489175, 2.30344767927052),
    'Allsop Arms, Gloucester Place, Marylebone, City of Westminster, London, Greater London, England, NW1 5AL, UK': (
        51.5224752, -0.1601586),
    'Austria Trend Hotel Park Royal Palace Vienna, 8, Schlossallee, KG Penzing, Penzing, Wien, 1140, Österreich': (
        48.1914089, 16.3163732059113),
    'Novotel, Via Mecenate, Taliedo, Milano, MI, LOM, 20138, Italia': (45.44850155, 9.25699199645669),
    'Altstadt, 41, Kirchengasse, Lerchenfeld, KG Neubau, Neubau, Wien, 1070, Österreich': (48.2048176, 16.3513395),
    '123, Apollolaan, Oud-Zuid, Amsterdam, Zuid, Amsterdam, Noord-Holland, Nederland, 1077AP, Nederland': (
        52.350423, 4.8756401),
    'Timhôtel Best Western Tour Eiffel Invalides, Boulevard de la Tour Maubourg, Invalides, 7e, Paris, Île-de-France, France métropolitaine, 75007, France': (
        48.8604075, 2.3104739),
    'Austria Trend Hotel Anatol, 26, Webgasse, Obere Windmühle, KG Mariahilf, Mariahilf, Wien, 1060, Österreich': (
        48.1945648, 16.3463061),
    '80, Carrer de la Diputació, Hostafrancs, Eixample, Barcelona, BCN, CAT, 08015, España': (
        41.38023985, 2.15389522231899),
    'Hôtel Saint-Paul Rive Gauche, Rue Monsieur le Prince, Odéon, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.8496648, 2.3402192),
    'H10 Marina Barcelona, 64-68, Avinguda del Bogatell, la Vila Olímpica del Poblenou, Sant Martí, Barcelona, BCN, CAT, 08005, España': (
        41.39312545, 2.1927294259987),
    '46, Rue de Trévise, Fg-Montmartre, 9e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.876072, 2.3456393),
    "Olivia Plaza Hotel, 19, Plaça de Catalunya, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08002, España": (
        41.3862014, 2.1711443),
    'Radisson Blu Hotel, Via Villapizzone, Quartiere Varesina, Municipio 8, Milano, MI, LOM, 20148, Italia': (
        45.5006951, 9.1443732),
    '568, Avinguda Diagonal, Galvany, Sant Gervasi - Galvany, Eixample, Barcelona, BCN, CAT, 08014, España': (
        41.3944954, 2.15011956170213),
    "668-664, Gran Via de les Corts Catalanes, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08003, España": (
        41.3915757, 2.1715558),
    'Mercure, Avenue Émile Zola, Javel, 15e, Paris, Île-de-France, France métropolitaine, 75015, France': (
        48.8460064, 2.27886814882443),
    'Residencia San Marius, 507, Carrer de Muntaner, la Bonanova, Sant Gervasi - la Bonanova, Sarrià - Sant Gervasi, Barcelona, BCN, CAT, 08022, España': (
        41.4034727, 2.1370155),
    'The Five Fields, 8-9, Blacklands Terrace, Chelsea, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW3 4, UK': (
        51.4917272, -0.1612738),
    'HUNter 486, Great Cumberland Place, Marylebone, City of Westminster, London, Greater London, England, W1, UK': (
        51.5160445, -0.1600494),
    'Au Manoir Saint-Germain des Prés, Boulevard Saint-Germain, St-Germain-des-Prés, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.8537719, 2.3323137),
    'De Roode Leeuw, Damrak, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1017, Nederland': (
        52.3737497, 4.8935952),
    'R.Kipling Hôtel, Rue Blanche, Nouvelle Athènes, St-Georges, 9e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.882049, 2.3316649),
    "570, 572, Gran Via de les Corts Catalanes, la Nova Esquerra de l'Eixample, Eixample, Barcelona, BCN, CAT, 08014, España": (
        41.3839818, 2.16193381794574),
    '5, Rue de Marivaux, Vivienne, 9e, Paris, Île-de-France, France métropolitaine, 75002, France': (
        48.8707723, 2.337358),
    '19, Nieuwezijds Kolk, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1012PV, Nederland': (
        52.3761449, 4.8944788),
    'Le Week-end, Rue de Castellane, Madeleine, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8722237, 2.3257923),
    'Threadneedles Hotel, Finch Lane, London, Greater London, England, SE15, UK': (51.5139494, -0.0855837740046841),
    'Milano Watttredici, 13, Via Giacomo Watt, San Cristoforo, Milano, MI, LOM, 20143, Italia': (
        45.4438329, 9.15299577592918),
    '1, Cité Pigalle, Quartier Saint-Georges, St-Georges, 9e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.8800822, 2.3343323),
    "Hotel HC Gotik, Ronda de Sant Pere, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08003, España": (
        41.3885941, 2.1712563),
    "Theobald's Road, Southampton Row, Holborn, St Giles, London Borough of Camden, London, Greater London, England, WC1A 2QP, UK": (
        51.5196285, -0.1217622),
    'Primark, King Street, Brook Green, London Borough of Hammersmith and Fulham, London, Greater London, England, W6 0QB, UK': (
        51.4926371, -0.2288907),
    'INK Hotel Amsterdam, 67, Nieuwezijds Voorburgwal, Amsterdam, Centrum, Amsterdam, Noord-Holland, Nederland, 1012 RE, Nederland': (
        52.3755009, 4.8929456),
    'County Hall, Belvedere Road, Lambeth, London Borough of Lambeth, London, Greater London, England, SE1, UK': (
        51.5019685, -0.118739137124634),
    'Orbis Wharf, Bridges Court, Battersea, London Borough of Wandsworth, London, Greater London, England, SW11 3BE, UK': (
        51.46875555, -0.179062050091132),
    'Mercure - Paris Bastille, Passage Brûlon, 12e Arrondissement (urbain), Quinze-Vingts, 12e, Paris, Île-de-France, France métropolitaine, 75012, France': (
        48.8495823, 2.37987752579365),
    '20, Via Senato, Porta Nuova, Milano, MI, LOM, 20121, Italia': (45.4713488, 9.1964833),
    "61, Rue de l'Arcade, Madeleine, 8e, Paris, Île-de-France, France métropolitaine, 75008, France": (
        48.874788, 2.3245207),
    "BT, Wrights Lane, Earl's Court, Royal Borough of Kensington and Chelsea, London, Greater London, England, W8 5RY, UK": (
        51.500037, -0.1928928),
    'Villa Eugénie, Rue Dulong, Batignolles, 17e, Paris, Île-de-France, France métropolitaine, 75017, France': (
        48.8871081, 2.31421829182425),
    'Hotel Major, 2, Viale Isonzo, Morivione, Municipio 5, Milano, MI, LOM, 20141, Italia': (45.4471825, 9.2091529),
    "Eurostar Anglí, 60, Carrer d'Anglí, Sarrià, Sarrià - Sant Gervasi, Barcelona, BCN, CAT, 08023, España": (
        41.4031218, 2.1231758),
    "Hotel Catalonia Plaça Catalunya, Carrer de Bergara, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08003, España": (
        41.3863262, 2.1681968),
    '88b, Avenue Kléber, Chaillot, 16e, Paris, Île-de-France, France métropolitaine, 75116, France': (
        48.8663691, 2.2893915),
    '21, Boulevard de Clichy, Quartier Saint-Georges, St-Georges, 9e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.8824023, 2.3365571),
    'Hôtel Ares Eiffel, 7, Rue du Général de Larminat, Grenelle, 15e, Paris, Île-de-France, France métropolitaine, 75015, France': (
        48.85033305, 2.29820863434364),
    'Das Triest, 12, Wiedner Hauptstraße, Freihausviertel, KG Wieden, Wieden, Wien, 1040, Österreich': (
        48.197381, 16.3673237),
    'TIM, Galleria Vittorio Emanuele II, Duomo, Municipio 1, Milano, MI, LOM, 20121, Italia': (45.4657222, 9.189537),
    'Hotel 4 Barcelona, 164, Carrer del Doctor Trueta, el Poblenou, Sant Martí, Barcelona, BCN, CAT, 08005, España': (
        41.3959516, 2.2009182),
    '8, Rue de Sévigné, Archives, 4e, Paris, Île-de-France, France métropolitaine, 75003, France': (
        48.8555141, 2.362089),
    "The Goring, Victoria Square, St. James's, Victoria, City of Westminster, London, Greater London, England, SW3 4, UK": (
        51.4976151, -0.145530365546592),
    'DoubleTree by Hilton London Greenwich, Catherine Grove, Greenwich, London, Greater London, England, SE10 8BB, UK': (
        51.4744806, -0.0195694843570206),
    "Henry Wood House, 3-6, Langham Place, St. James's, Fitzrovia, City of Westminster, London, Greater London, England, W1S 1PY, UK": (
        51.5178649, -0.142385278668694),
    '214, High Street, Acton, London Borough of Ealing, London, Greater London, England, W3 9NX, UK': (
        51.50789205, -0.272998440846877),
    'Caprabo, Avinguda de la República Argentina, el Putget, el Putget i Farró, Gràcia, Barcelona, BCN, CAT, 08023, España': (
        41.4086067, 2.1472424),
    "Zenit Borrell, 208, Carrer del Comte Borrell, la Nova Esquerra de l'Eixample, Eixample, Barcelona, BCN, CAT, 08029, España": (
        41.3860496, 2.15156243953423),
    '187, Hernalser Hauptstraße, Frauenfeld, KG Dornbach, Hernals, Wien, 1170, Österreich': (48.2238693, 16.3138979),
    'Royal Crescent, Holland Park Avenue, Silchester Estate, Notting Hill, Royal Borough of Kensington and Chelsea, London, Greater London, England, W12 8LG, UK': (
        51.505288, -0.213831),
    'Arkadenhof, 5, Viriotgasse, Thurygrund II, KG Alsergrund, Alsergrund, Wien, 1090, Österreich': (
        48.23074035, 16.3552375883364),
    'Mercure Paris Monty Opéra, Rue de Montyon, Fg-Montmartre, 9e, Paris, Île-de-France, France métropolitaine, 75009, France': (
        48.872991, 2.34453531381517),
    'Mareuil, Rue de Malte, Folie-Méricourt, 11e, Paris, Île-de-France, France métropolitaine, 75011, France': (
        48.8659977, 2.3674507),
    "Grange Fitzrovia Hotel, 20-28, Bolsover Street, St. James's, Fitzrovia, City of Westminster, London, Greater London, England, W1W 5NB, UK": (
        51.5217661, -0.142537517199615),
    'Hotel Russell, Russell Square, Holborn, Bloomsbury, London Borough of Camden, London, Greater London, England, WC1H 0LH, UK': (
        51.52263415, -0.125013902180308),
    "Royal Trafalgar Hotel, Whitcomb Street, St. James's, Covent Garden, City of Westminster, London, Greater London, England, WC2H 7HA, UK": (
        51.50906175, -0.13014018150664),
    'Boundary, Redchurch Street, Shoreditch, London Borough of Hackney, London, Greater London, England, EC2V 7HH, UK': (
        51.5245692, -0.0762861876170896),
    'Draycott Hotel, Cadogan Gardens, Chelsea, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW3 4, UK': (
        51.4929221, -0.1597612),
    "Ajuntament de Barcelona - Oficina d'Atenció Ciutadana (OAC) del Districte d'Horta - Guinardó, 387, Carrer de Lepant, el Baix Guinardó, Eixample, Barcelona, BCN, CAT, 08025, España": (
        41.40966665, 2.1694534434017), 'Via Feltre, Rottole, Milano, MI, LOM, 20132, Italia': (45.4911496, 9.2389302),
    "55, 's-Gravesandestraat, Oosterparkbuurt, Amsterdam, Oost, Amsterdam, Noord-Holland, Nederland, 1092AA, Nederland": (
        52.3605937, 4.9159528),
    '17, Mariahilfer Straße, Untere Windmühle, KG Mariahilf, Mariahilf, Wien, 1060, Österreich': (
        48.2009216, 16.3592147),
    '9, Rue Duhesme, Grandes-Carrières, 18e, Paris, Île-de-France, France métropolitaine, 75018, France': (
        48.8906098, 2.3375975),
    '1, Rue du Général Blaise, St-Ambroise, 11e, Paris, Île-de-France, France métropolitaine, 75011, France': (
        48.8610334, 2.3789124),
    'Hôtel Amarante Champs-Élysées, Rue Vernet, Champs-Élysées, 8e, Paris, Île-de-France, France métropolitaine, 75008, France': (
        48.8717742, 2.2984126),
    '10, Rue Cognacq-Jay, Gros-Caillou, 7e, Paris, Île-de-France, France métropolitaine, 75007, France': (
        48.8618611, 2.3040832),
    'Starbucks, la Rambla, el Gòtic, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (41.3834216, 2.1712242),
    "Casa Garriga Nogués, 250, Carrer de la Diputació, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08013, España": (
        41.3887399, 2.16540411065737),
    'Barcelona, Carrer de Jaume I, el Gòtic, Ciutat Vella, Barcelona, BCN, CAT, 08003, España': (41.3831378, 2.1778061),
    'Hotel Hermitage, Via Aristotile Fioravanti, Chinatown, Municipio 8, Milano, MI, LOM, 20121, Italia': (
        45.4823565, 9.175709),
    "Hôtel Mercure Paris Opéra Garnier, 4, Rue de l'Isly, Chaussée-d'Antin, 9e, Paris, Île-de-France, France métropolitaine, 75008, France": (
        48.8748982, 2.3260331),
    'Red Rooster, 45, Curtain Road, Shoreditch, London Borough of Hackney, London, Greater London, England, EC2A 3PT, UK': (
        51.5237301, -0.0805482),
    'Zetland Arms, 2, Bute Street, Brompton, Royal Borough of Kensington and Chelsea, London, Greater London, England, SW7 3EX, UK': (
        51.49339975, -0.175895507830002),
    "HCC St. Moritz, 264, Carrer de la Diputació, la Dreta de l'Eixample, Eixample, Barcelona, BCN, CAT, 08007, España": (
        41.391097, 2.1682549),
    '2, Rue Perronet, St-Germain-des-Prés, 6e, Paris, Île-de-France, France métropolitaine, 75006, France': (
        48.8552243, 2.3305859)}

df = pd.DataFrame(diction_with_address.values(), index=diction_with_address.keys(), columns=['Latitude', 'Longitude'])

df['Address'] = df.index
df_with_lon_lat_address = df.reset_index(drop=True)

