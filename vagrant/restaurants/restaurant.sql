-- Table definitions for the restaurant menus project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP DATABASE IF EXISTS restaurantmenus;
CREATE DATABASE restaurantmenus;
\c restaurantmenus;

-- Extra Credit -> Multiple Tournaments
-- Could add other columns, like rules, location, prize pool
/*
CREATE TABLE tournaments (
    tourn_id serial PRIMARY KEY
);


CREATE TABLE players (
    player serial PRIMARY KEY,
    name varchar(40) NOT NULL
);


CREATE TABLE matches (
    match serial PRIMARY KEY,
    tourn_id integer REFERENCES tournaments(tourn_id) ,
    winner_id integer REFERENCES players(player) ON DELETE CASCADE,
    loser_id integer REFERENCES players(player) ON DELETE CASCADE
);


CREATE TABLE tournament_players (
    tourn_id integer references tournaments(tourn_id) ON DELETE CASCADE,
    player integer references players(player) ON DELETE CASCADE,
    matches_won integer DEFAULT 0,
    matches_played integer DEFAULT 0,
    PRIMARY KEY(tourn_id, player)
);


CREATE VIEW matches_played AS
    SELECT
        matches.tourn_id AS tournament,
        players.player AS player_id,
        players.name AS player_name,
        count (*) as played
    FROM matches, players
    WHERE
        players.player = matches.winner_id
    OR
        players.player = matches.loser_id
    GROUP BY matches.tourn_id, players.player;


CREATE VIEW matches_won AS
    SELECT
        matches.tourn_id AS tournament,
        players.player AS player_id,
        players.name AS player_name,
        count(*) as wins
    FROM matches, players
    WHERE
        players.player = matches.winner_id
    GROUP BY matches.tourn_id, players.player;


CREATE VIEW standings AS
    SELECT
        mp.tournament,
        mp.player_id,
        mp.player_name,
        COALESCE(mw.wins,0) as wins,
        mp.played
    FROM
        matches_played mp
    LEFT JOIN
        matches_won mw
    ON
        mp.player_id = mw.player_id OR wins=0
    ORDER BY mp.tournament, wins desc;

CREATE TYPE tournament_pairing AS
(
    p1_id integer,
    p1_name text,
    p2_id integer,
    p2_name text
);


CREATE TYPE player_info AS
(
    id integer,
    name text,
    won integer,
    played integer
);

-- Returns the Standings of a Tournament using it's id
CREATE OR REPLACE FUNCTION playerStandings(tournament_id int) RETURNS
    setof player_info AS
$BODY$
DECLARE
    r record;
    result player_info;
BEGIN
    FOR r IN
        SELECT
            tp.player as player,
            p.name as name,
            tp.matches_won as won,
            tp.matches_played as played
    FROM
        tournament_players tp,
        players p
    WHERE tp.tourn_id=tournament_id AND p.player=tp.player
    ORDER BY tp.matches_won desc LOOP
        result.id = r.player;
        result.name = CAST(r.name AS text);
        result.won = r.won;
        result.played = r.played;
        RETURN NEXT result;
    END LOOP;
    RETURN;
END;
$BODY$
LANGUAGE plpgsql;


-- Creates a pairing of two players.
-- idx is the row # in the in the Player Standings that belongs to the
-- the first of the two players being matched up
CREATE OR REPLACE FUNCTION createPair(tournament int, idx int) RETURNS tournament_pairing AS
$BODY$
DECLARE
    result tournament_pairing;
BEGIN
    SELECT p1.id, p1.name, p2.id, p2.name
    INTO result
    FROM
        ( SELECT id, name FROM playerStandings(tournament) LIMIT 1 OFFSET idx) as p1,
        ( SELECT id, name FROM playerStandings(tournament) LIMIT 1 OFFSET idx + 1) as p2;

    RETURN result;
END;
$BODY$
LANGUAGE plpgsql;


-- Assuming there is an even number of players, generate the Swiss Pairings
CREATE OR REPLACE FUNCTION swissPairings(tournament int) RETURNS setof tournament_pairing AS
$BODY$
DECLARE
    i int := 0;
    numPlayers int := (SELECT COUNT(*) FROM playerStandings(tournament)) - 1;
    result tournament_pairing;
BEGIN
    FOR i IN 0 .. numPlayers BY 2 LOOP
        SELECT p1_id, p1_name, p2_id, p2_name
        INTO result
        FROM createPair(tournament, i);

        RETURN NEXT result;
    END LOOP;
    RETURN;
END;
$BODY$
LANGUAGE plpgsql;


-- Delete all Tournaments from the database.
CREATE OR REPLACE FUNCTION deleteTournaments() RETURNS void AS
$$
DECLARE
    t int;
BEGIN
    FOR t IN (SELECT tourn_id FROM tournaments) LOOP
        DELETE FROM tournament_players WHERE tourn_id=t;
    END LOOP;
END;
$$
LANGUAGE plpgsql;


-- Delete a specific tournament, by it's id.
CREATE OR REPLACE FUNCTION deleteTournament(tournament int) RETURNS void AS
$$
BEGIN
    DELETE FROM tournament_players WHERE tourn_id=tournament;
END;
$$
LANGUAGE plpgsql;


-- Report a Tournament Match given a tournament id, a winner's id and loser's id.
CREATE OR REPLACE FUNCTION reportMatch(tournament int, winner int, loser int) RETURNS void AS
$$
BEGIN
    -- Update the Winner's Record
    UPDATE tournament_players
    SET matches_won = matches_won+1, matches_played = matches_played+1
    WHERE (player = winner AND tourn_id = tournament);

    -- Update the Loser's Record
    UPDATE tournament_players
    SET matches_played = matches_played+1
    WHERE (player = loser AND tourn_id = tournament);

    -- Now add the Results to the Match table
    INSERT INTO matches(tourn_id, winner_id, loser_id)
    VALUES (tournament, winner, loser);
END;
$$
LANGUAGE plpgsql;


-- Create a new Tournament and return it's id.
CREATE OR REPLACE FUNCTION createTournament() RETURNS int AS
$$
DECLARE
    t_id int;
BEGIN
    INSERT INTO tournaments(tourn_id) VALUES(DEFAULT) RETURNING tourn_id INTO t_id;
    RETURN t_id;
END;
$$
LANGUAGE plpgsql;

-- Create a player, adds a Player, but does not place them into a tournament
-- with a record.
CREATE OR REPLACE FUNCTION createPlayer(player_name text) RETURNS int AS
$$
DECLARE
    player_id int;
BEGIN
    INSERT INTO players(name) VALUES(player_name) RETURNING player INTO player_id;
    RETURN player_id;
END;
$$
LANGUAGE plpgsql;


-- Registers a player (player_id) for a tournament (tournament_id).
CREATE OR REPLACE FUNCTION registerPlayer(player_id int, tournament_id int) RETURNS void AS
$$
BEGIN
    INSERT INTO tournament_players(tourn_id, player) VALUES(tournament_id, player_id);
END;
$$
LANGUAGE plpgsql;
*/