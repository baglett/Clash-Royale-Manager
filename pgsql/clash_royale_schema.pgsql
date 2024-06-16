-- clash_royale.clan_member definition

-- Drop table if it exists
-- DROP TABLE IF EXISTS clash_royale.clan_member;

CREATE TABLE clash_royale.clan_member (
    id serial4 NOT NULL,
    tag varchar(20) NOT NULL,
    name varchar(100) NOT NULL,
    role varchar(50) NOT NULL,
    trophies int4 NOT NULL,
    best_trophies int4 NOT NULL,
    exp_level int4 NOT NULL,
    wins int4 NOT NULL,
    losses int4 NOT NULL,
    battle_count int4 NOT NULL,
    three_crown_wins int4 NOT NULL,
    challenge_cards_won int4 NOT NULL,
    challenge_max_wins int4 NOT NULL,
    tournament_cards_won int4 NOT NULL,
    tournament_battle_count int4 NOT NULL,
    donations int4 NOT NULL,
    donations_received int4 NOT NULL,
    total_donations int4 NOT NULL,
    war_day_wins int4 NOT NULL,
    clan_cards_collected int4 NOT NULL,
    current_season_trophies int4 NOT NULL,
    current_season_best_trophies int4 NOT NULL,
    previous_season_id varchar(10) NOT NULL,
    previous_season_trophies int4 NOT NULL,
    previous_season_best_trophies int4 NOT NULL,
    best_season_id varchar(10) NOT NULL,
    best_season_trophies int4 NOT NULL,
    star_points int4 NOT NULL,
    exp_points int4 NOT NULL,
    legacy_trophy_road_high_score int4 NOT NULL,
    current_path_of_legend_league int4 NOT NULL,
    current_path_of_legend_trophies int4 NOT NULL,
    current_path_of_legend_rank int4 NULL,
    last_path_of_legend_league int4 NOT NULL,
    last_path_of_legend_trophies int4 NOT NULL,
    last_path_of_legend_rank int4 NULL,
    best_path_of_legend_league int4 NOT NULL,
    best_path_of_legend_trophies int4 NOT NULL,
    best_path_of_legend_rank int4 NULL,
    total_exp_points int4 NOT NULL,
    last_seen timestamptz NOT NULL,
    join_date timestamptz NOT NULL,
    created_at timestamptz DEFAULT CURRENT_TIMESTAMP NULL,
    updated_at timestamptz DEFAULT CURRENT_TIMESTAMP NULL,
    CONSTRAINT clan_member_pkey PRIMARY KEY (id),
    CONSTRAINT clan_member_tag_key UNIQUE (tag)
);

CREATE INDEX idx_clan_member_donations ON clash_royale.clan_member USING btree (donations);
CREATE INDEX idx_clan_member_join_date ON clash_royale.clan_member USING btree (join_date);
CREATE INDEX idx_clan_member_last_seen ON clash_royale.clan_member USING btree (last_seen);
CREATE INDEX idx_clan_member_name ON clash_royale.clan_member USING btree (name);
CREATE INDEX idx_clan_member_role ON clash_royale.clan_member USING btree (role);
CREATE INDEX idx_clan_member_tag ON clash_royale.clan_member USING btree (tag);
CREATE INDEX idx_clan_member_trophies ON clash_royale.clan_member USING btree (trophies);
CREATE INDEX idx_clan_member_best_trophies ON clash_royale.clan_member USING btree (best_trophies);
CREATE INDEX idx_clan_member_exp_level ON clash_royale.clan_member USING btree (exp_level);
CREATE INDEX idx_clan_member_wins ON clash_royale.clan_member USING btree (wins);
CREATE INDEX idx_clan_member_losses ON clash_royale.clan_member USING btree (losses);
CREATE INDEX idx_clan_member_battle_count ON clash_royale.clan_member USING btree (battle_count);
CREATE INDEX idx_clan_member_three_crown_wins ON clash_royale.clan_member USING btree (three_crown_wins);
CREATE INDEX idx_clan_member_challenge_cards_won ON clash_royale.clan_member USING btree (challenge_cards_won);
CREATE INDEX idx_clan_member_challenge_max_wins ON clash_royale.clan_member USING btree (challenge_max_wins);
CREATE INDEX idx_clan_member_tournament_cards_won ON clash_royale.clan_member USING btree (tournament_cards_won);
CREATE INDEX idx_clan_member_tournament_battle_count ON clash_royale.clan_member USING btree (tournament_battle_count);
CREATE INDEX idx_clan_member_donations_received ON clash_royale.clan_member USING btree (donations_received);
CREATE INDEX idx_clan_member_total_donations ON clash_royale.clan_member USING btree (total_donations);
CREATE INDEX idx_clan_member_war_day_wins ON clash_royale.clan_member USING btree (war_day_wins);
CREATE INDEX idx_clan_member_clan_cards_collected ON clash_royale.clan_member USING btree (clan_cards_collected);
CREATE INDEX idx_clan_member_current_season_trophies ON clash_royale.clan_member USING btree (current_season_trophies);
CREATE INDEX idx_clan_member_current_season_best_trophies ON clash_royale.clan_member USING btree (current_season_best_trophies);
CREATE INDEX idx_clan_member_previous_season_id ON clash_royale.clan_member USING btree (previous_season_id);
CREATE INDEX idx_clan_member_previous_season_trophies ON clash_royale.clan_member USING btree (previous_season_trophies);
CREATE INDEX idx_clan_member_previous_season_best_trophies ON clash_royale.clan_member USING btree (previous_season_best_trophies);
CREATE INDEX idx_clan_member_best_season_id ON clash_royale.clan_member USING btree (best_season_id);
CREATE INDEX idx_clan_member_best_season_trophies ON clash_royale.clan_member USING btree (best_season_trophies);
CREATE INDEX idx_clan_member_star_points ON clash_royale.clan_member USING btree (star_points);
CREATE INDEX idx_clan_member_exp_points ON clash_royale.clan_member USING btree (exp_points);
CREATE INDEX idx_clan_member_legacy_trophy_road_high_score ON clash_royale.clan_member USING btree (legacy_trophy_road_high_score);
CREATE INDEX idx_clan_member_current_path_of_legend_league ON clash_royale.clan_member USING btree (current_path_of_legend_league);
CREATE INDEX idx_clan_member_current_path_of_legend_trophies ON clash_royale.clan_member USING btree (current_path_of_legend_trophies);
CREATE INDEX idx_clan_member_current_path_of_legend_rank ON clash_royale.clan_member USING btree (current_path_of_legend_rank);
CREATE INDEX idx_clan_member_last_path_of_legend_league ON clash_royale.clan_member USING btree (last_path_of_legend_league);
CREATE INDEX idx_clan_member_last_path_of_legend_trophies ON clash_royale.clan_member USING btree (last_path_of_legend_trophies);
CREATE INDEX idx_clan_member_last_path_of_legend_rank ON clash_royale.clan_member USING btree (last_path_of_legend_rank);
CREATE INDEX idx_clan_member_best_path_of_legend_league ON clash_royale.clan_member USING btree (best_path_of_legend_league);
CREATE INDEX idx_clan_member_best_path_of_legend_trophies ON clash_royale.clan_member USING btree (best_path_of_legend_trophies);
CREATE INDEX idx_clan_member_best_path_of_legend_rank ON clash_royale.clan_member USING btree (best_path_of_legend_rank);
CREATE INDEX idx_clan_member_total_exp_points ON clash_royale.clan_member USING btree (total_exp_points);