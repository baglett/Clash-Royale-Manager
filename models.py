from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ClanMember(BaseModel):
    tag: str = Field(..., max_length=20)
    name: str = Field(..., max_length=100)
    role: str = Field(..., max_length=50)
    trophies: int
    best_trophies: int
    exp_level: int
    wins: int
    losses: int
    battle_count: int
    three_crown_wins: int
    challenge_cards_won: int
    challenge_max_wins: int
    tournament_cards_won: int
    tournament_battle_count: int
    donations: int
    donations_received: int
    total_donations: int
    war_day_wins: int
    clan_cards_collected: int
    current_season_trophies: int
    current_season_best_trophies: int
    previous_season_id: str = Field(..., max_length=10)
    previous_season_trophies: int
    previous_season_best_trophies: int
    best_season_id: str = Field(..., max_length=10)
    best_season_trophies: int
    star_points: int
    exp_points: int
    legacy_trophy_road_high_score: int
    current_path_of_legend_league: int
    current_path_of_legend_trophies: int
    current_path_of_legend_rank: Optional[int] = None
    last_path_of_legend_league: int
    last_path_of_legend_trophies: int
    last_path_of_legend_rank: Optional[int] = None
    best_path_of_legend_league: int
    best_path_of_legend_trophies: int
    best_path_of_legend_rank: Optional[int] = None
    total_exp_points: int
    last_seen: datetime
    join_date: datetime
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None