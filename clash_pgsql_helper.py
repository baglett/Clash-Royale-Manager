import os
import json
from datetime import datetime, timezone
from typing import List, Optional
from models import ClanMember
from pgsql_helper import PgSQLHelper
from clash_royale_api import get_clan_info, get_player_details

class ClashPgSQLHelper:
    def __init__(self):
        self.db_helper = PgSQLHelper()
        self.db_helper.connect()

    def create_clan_member(self, clan_member: ClanMember) -> None:
        query = """
        INSERT INTO clash_royale.clan_member (
            tag, name, role, trophies, best_trophies, exp_level, wins, losses, battle_count, 
            three_crown_wins, challenge_cards_won, challenge_max_wins, tournament_cards_won, 
            tournament_battle_count, donations, donations_received, total_donations, war_day_wins, 
            clan_cards_collected, current_season_trophies, current_season_best_trophies, 
            previous_season_id, previous_season_trophies, previous_season_best_trophies, 
            best_season_id, best_season_trophies, star_points, exp_points, legacy_trophy_road_high_score, 
            current_path_of_legend_league, current_path_of_legend_trophies, current_path_of_legend_rank, 
            last_path_of_legend_league, last_path_of_legend_trophies, last_path_of_legend_rank, 
            best_path_of_legend_league, best_path_of_legend_trophies, best_path_of_legend_rank, 
            total_exp_points, last_seen, join_date
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            clan_member.tag, clan_member.name, clan_member.role, clan_member.trophies, clan_member.best_trophies,
            clan_member.exp_level, clan_member.wins, clan_member.losses, clan_member.battle_count,
            clan_member.three_crown_wins, clan_member.challenge_cards_won, clan_member.challenge_max_wins,
            clan_member.tournament_cards_won, clan_member.tournament_battle_count, clan_member.donations,
            clan_member.donations_received, clan_member.total_donations, clan_member.war_day_wins,
            clan_member.clan_cards_collected, clan_member.current_season_trophies, clan_member.current_season_best_trophies,
            clan_member.previous_season_id, clan_member.previous_season_trophies, clan_member.previous_season_best_trophies,
            clan_member.best_season_id, clan_member.best_season_trophies, clan_member.star_points, clan_member.exp_points,
            clan_member.legacy_trophy_road_high_score, clan_member.current_path_of_legend_league, clan_member.current_path_of_legend_trophies,
            clan_member.current_path_of_legend_rank, clan_member.last_path_of_legend_league, clan_member.last_path_of_legend_trophies,
            clan_member.last_path_of_legend_rank, clan_member.best_path_of_legend_league, clan_member.best_path_of_legend_trophies,
            clan_member.best_path_of_legend_rank, clan_member.total_exp_points, 
            clan_member.last_seen.isoformat(), clan_member.join_date.isoformat()
        )
        
        # Debugging: Print the query and parameters
        print(query)
        print(params)
        self.db_helper.execute_query(query, params)

    def read_clan_member(self, tag: str) -> Optional[ClanMember]:
        query = "SELECT * FROM clash_royale.clan_member WHERE tag = %s;"
        params = (tag,)
        result = self.db_helper.fetch_query(query, params)
        if result:
            return ClanMember(**result[0])
        return None

    def update_clan_member(self, clan_member: ClanMember) -> None:
        query = """
        UPDATE clash_royale.clan_member
        SET name = %s, role = %s, trophies = %s, best_trophies = %s, exp_level = %s, wins = %s, 
            losses = %s, battle_count = %s, three_crown_wins = %s, challenge_cards_won = %s, 
            challenge_max_wins = %s, tournament_cards_won = %s, tournament_battle_count = %s, 
            donations = %s, donations_received = %s, total_donations = %s, war_day_wins = %s, 
            clan_cards_collected = %s, current_season_trophies = %s, current_season_best_trophies = %s, 
            previous_season_id = %s, previous_season_trophies = %s, previous_season_best_trophies = %s, 
            best_season_id = %s, best_season_trophies = %s, star_points = %s, exp_points = %s, 
            legacy_trophy_road_high_score = %s, current_path_of_legend_league = %s, 
            current_path_of_legend_trophies = %s, current_path_of_legend_rank = %s, 
            last_path_of_legend_league = %s, last_path_of_legend_trophies = %s, 
            last_path_of_legend_rank = %s, best_path_of_legend_league = %s, 
            best_path_of_legend_trophies = %s, best_path_of_legend_rank = %s, total_exp_points = %s, 
            last_seen = %s, join_date = %s, updated_at = CURRENT_TIMESTAMP
        WHERE tag = %s;
        """
        params = (
            clan_member.name, clan_member.role, clan_member.trophies, clan_member.best_trophies, clan_member.exp_level,
            clan_member.wins, clan_member.losses, clan_member.battle_count, clan_member.three_crown_wins,
            clan_member.challenge_cards_won, clan_member.challenge_max_wins, clan_member.tournament_cards_won,
            clan_member.tournament_battle_count, clan_member.donations, clan_member.donations_received,
            clan_member.total_donations, clan_member.war_day_wins, clan_member.clan_cards_collected,
            clan_member.current_season_trophies, clan_member.current_season_best_trophies, clan_member.previous_season_id,
            clan_member.previous_season_trophies, clan_member.previous_season_best_trophies, clan_member.best_season_id,
            clan_member.best_season_trophies, clan_member.star_points, clan_member.exp_points, clan_member.legacy_trophy_road_high_score,
            clan_member.current_path_of_legend_league, clan_member.current_path_of_legend_trophies, clan_member.current_path_of_legend_rank,
            clan_member.last_path_of_legend_league, clan_member.last_path_of_legend_trophies, clan_member.last_path_of_legend_rank,
            clan_member.best_path_of_legend_league, clan_member.best_path_of_legend_trophies, clan_member.best_path_of_legend_rank,
            clan_member.total_exp_points, clan_member.last_seen.isoformat(), clan_member.join_date.isoformat(), clan_member.tag
        )
        
        # Debugging: Print the query and parameters
        print(query)
        print(params)
        self.db_helper.execute_query(query, params)

    def delete_clan_member(self, tag: str) -> None:
        query = "DELETE FROM clash_royale.clan_member WHERE tag = %s;"
        params = (tag,)
        self.db_helper.execute_query(query, params)

    def list_clan_members(self) -> List[ClanMember]:
        query = "SELECT * FROM clash_royale.clan_member;"
        results = self.db_helper.fetch_query(query)
        return [ClanMember(**result) for result in results] if results else []

    def get_clan_member_tags(self) -> List[str]:
        query = "SELECT tag FROM clash_royale.clan_member;"
        results = self.db_helper.fetch_query(query)
        return [result['tag'] for result in results] if results else []

    def fetch_and_update_clan_members(self):
        clan_data = get_clan_info()
        for member in clan_data['memberList']:
            player_details = get_player_details(member['tag'][1:])  # Remove the '#' character from the tag
            league_statistics = player_details.get('leagueStatistics', {})
            current_season = league_statistics.get('currentSeason', {})
            previous_season = league_statistics.get('previousSeason', {})
            best_season = league_statistics.get('bestSeason', {})

            current_path_of_legend = player_details.get('currentPathOfLegendSeasonResult') or {}
            last_path_of_legend = player_details.get('lastPathOfLegendSeasonResult') or {}
            best_path_of_legend = player_details.get('bestPathOfLegendSeasonResult') or {}

            clan_member = ClanMember(
                tag=member['tag'],
                name=member['name'],
                role=member['role'],
                trophies=member['trophies'],
                best_trophies=player_details.get('bestTrophies', 0),
                exp_level=player_details['expLevel'],
                wins=player_details['wins'],
                losses=player_details['losses'],
                battle_count=player_details['battleCount'],
                three_crown_wins=player_details['threeCrownWins'],
                challenge_cards_won=player_details['challengeCardsWon'],
                challenge_max_wins=player_details['challengeMaxWins'],
                tournament_cards_won=player_details['tournamentCardsWon'],
                tournament_battle_count=player_details['tournamentBattleCount'],
                donations=member['donations'],
                donations_received=player_details['donationsReceived'],
                total_donations=player_details['totalDonations'],
                war_day_wins=player_details['warDayWins'],
                clan_cards_collected=player_details['clanCardsCollected'],
                current_season_trophies=current_season.get('trophies', 0),
                current_season_best_trophies=current_season.get('bestTrophies', 0),
                previous_season_id=previous_season.get('id', 'N/A'),
                previous_season_trophies=previous_season.get('trophies', 0),
                previous_season_best_trophies=previous_season.get('bestTrophies', 0),
                best_season_id=best_season.get('id', 'N/A'),
                best_season_trophies=best_season.get('trophies', 0),
                star_points=player_details['starPoints'],
                exp_points=player_details['expPoints'],
                legacy_trophy_road_high_score=player_details['legacyTrophyRoadHighScore'],
                current_path_of_legend_league=current_path_of_legend.get('leagueNumber', 0),
                current_path_of_legend_trophies=current_path_of_legend.get('trophies', 0),
                current_path_of_legend_rank=current_path_of_legend.get('rank'),
                last_path_of_legend_league=last_path_of_legend.get('leagueNumber', 0),
                last_path_of_legend_trophies=last_path_of_legend.get('trophies', 0),
                last_path_of_legend_rank=last_path_of_legend.get('rank'),
                best_path_of_legend_league=best_path_of_legend.get('leagueNumber', 0),
                best_path_of_legend_trophies=best_path_of_legend.get('trophies', 0),
                best_path_of_legend_rank=best_path_of_legend.get('rank'),
                total_exp_points=player_details['totalExpPoints'],
                last_seen=datetime.strptime(member['lastSeen'][:-5], "%Y%m%dT%H%M%S").replace(tzinfo=timezone.utc),
                join_date=datetime.now(timezone.utc)  # Assuming join_date is now, update if you have the correct data
            )
            existing_member = self.read_clan_member(clan_member.tag)
            if existing_member:
                self.update_clan_member(clan_member)
            else:
                self.create_clan_member(clan_member)

    def __del__(self):
        self.db_helper.disconnect()

def default_serializer(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

# Example usage:
if __name__ == "__main__":
    import sys
    # Set the console encoding to UTF-8
    sys.stdout.reconfigure(encoding='utf-8')
    
    clash_helper = ClashPgSQLHelper()

    # Fetch and update clan members from the API
    clash_helper.fetch_and_update_clan_members()

    # List all clan members
    members = clash_helper.list_clan_members()
    # Print members with graceful handling of encoding errors
    for member in members:
        print(json.dumps(member.dict(), ensure_ascii=False, default=default_serializer), flush=True)