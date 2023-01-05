

--
-- Base de données : Proj531
--

-- --------------------------------------------------------

--
-- Structure de la table Historique
--

CREATE TABLE Historique (
  idHisto int(11) NOT NULL,
  score int(11) DEFAULT NULL,
  mode int(11) DEFAULT NULL
) ;

-- --------------------------------------------------------

--
-- Structure de la table Question
--

CREATE TABLE Question (
  idQuestion int(11) NOT NULL,
  question text DEFAULT NULL,
  reponse1 text DEFAULT NULL,
  reponse2 text DEFAULT NULL,
  bonneReponse text DEFAULT NULL
) ;

-- --------------------------------------------------------

--
-- Structure de la table quizz
--

CREATE TABLE quizz (
  idQuizz int(11) NOT NULL,
  nom varchar(50) DEFAULT NULL,
  theme varchar(50) DEFAULT NULL
) ;

-- --------------------------------------------------------

--
-- Structure de la table Utilisateur
--

CREATE TABLE Utilisateur (
  idUtilisateur int(11) NOT NULL,
  nom varchar(50) DEFAULT NULL,
  mdp varchar(50) DEFAULT NULL,
  isAdmin tinyint(1) DEFAULT NULL
) ;

--
-- Déchargement des données de la table Utilisateur
--

INSERT INTO Utilisateur (idUtilisateur, nom, mdp, isAdmin) VALUES
(1, 'Alexis', '1234', 1),
(2, 'Arthur', '1234', 1),
(3, 'Andres', '1234', 1),
(4, 'Carlyne', '1234', 1);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table Historique
--
ALTER TABLE Historique
  ADD PRIMARY KEY (idHisto);

--
-- Index pour la table Question
--
ALTER TABLE Question
  ADD PRIMARY KEY (idQuestion);

--
-- Index pour la table quizz
--
ALTER TABLE quizz
  ADD PRIMARY KEY (idQuizz);

--
-- Index pour la table Utilisateur
--
ALTER TABLE Utilisateur
  ADD PRIMARY KEY (idUtilisateur);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table Historique
--
ALTER TABLE Historique
  MODIFY idHisto int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table Question
--
ALTER TABLE Question
  MODIFY idQuestion int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table quizz
--
ALTER TABLE quizz
  MODIFY idQuizz int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table Utilisateur
--
ALTER TABLE Utilisateur
  MODIFY idUtilisateur int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
