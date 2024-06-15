from pgsql_helper import PgSQLHelper
from models import ClanMember
from typing import List, Optional
from datetime import datetime, timezone
import json
import urllib.request
from jwt_utils import get_request
import os

class ClashPgSQLHelper:
    def __init__(self):
        self.db_helper = PgSQLHelper()
        self.db_helper.connect()
        self.baseUrl = "https://api.clashroyale.com/v1"
        self.clan_tag = os.getenv('CLAN_TAG')

    def create_clan_member(self, clan_member: ClanMember) -> None:
        query = """
        INSERT INTO clash_royale.clan_member (tag, name, role, trophies, donations, last_seen, join_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            clan_member.tag, clan_member.name, clan_member.role, 
            clan_member.trophies, clan_member.donations, 
            clan_member.last_seen, clan_member.join_date
        )
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
        SET name = %s, role = %s, trophies = %s, donations = %s, 
            last_seen = %s, join_date = %s, updated_at = CURRENT_TIMESTAMP
        WHERE tag = %s;
        """
        params = (
            clan_member.name, clan_member.role, clan_member.trophies, 
            clan_member.donations, clan_member.last_seen, 
            clan_member.join_date, clan_member.tag
        )
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
        clan_data = self.get_clan_info()
        for member in clan_data['memberList']:
            clan_member = ClanMember(
                tag=member['tag'],
                name=member['name'],
                role=member['role'],
                trophies=member['trophies'],
                donations=member['donations'],
                last_seen=datetime.strptime(member['lastSeen'][:-5], "%Y%m%dT%H%M%S").replace(tzinfo=timezone.utc),
                join_date=datetime.now(timezone.utc)  # Assuming join_date is now, update if you have the correct data
            )
            existing_member = self.read_clan_member(clan_member.tag)
            if existing_member:
                self.update_clan_member(clan_member)
            else:
                self.create_clan_member(clan_member)

    def get_clan_info(self):
        endpoint = f"/clans/%23{self.clan_tag}"
        request = get_request(endpoint, self.baseUrl)
        
        # Debugging: Print the request URL and headers
        print(f"Request URL: {request.full_url}")
        print(f"Request Headers: {request.headers}")

        response = urllib.request.urlopen(request).read().decode("utf-8")
        data = json.loads(response)
        return data

    def __del__(self):
        self.db_helper.disconnect()

# Example usage:
if __name__ == "__main__":
    clash_helper = ClashPgSQLHelper()

    # Fetch and update clan members from the API
    clash_helper.fetch_and_update_clan_members()

    # List all clan members
    members = clash_helper.list_clan_members()