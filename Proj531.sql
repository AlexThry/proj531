

--
-- Base de données : Proj531
--

-- --------------------------------------------------------

--
-- Structure de la table Historique
--

CREATE TABLE Historique (
  idHisto int(11) PRIMARY KEY AUTO_INCREMENT NOT NULL,
  score int(11) DEFAULT NULL,
  mode int(11) DEFAULT NULL
) ;

-- --------------------------------------------------------

--
-- Structure de la table Question
--

CREATE TABLE Question (
  idQuestion int(11) PRIMARY KEY AUTO_INCREMENT NOT NULL,
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
  idQuizz int(11) PRIMARY KEY AUTO_INCREMENT NOT NULL,
  nom varchar(50) DEFAULT NULL,
  theme varchar(50) DEFAULT NULL
) ;

-- --------------------------------------------------------

--
-- Structure de la table Utilisateur
--

CREATE TABLE Utilisateur (
  idUtilisateur int(11) PRIMARY KEY AUTO_INCREMENT NOT NULL,
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


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
