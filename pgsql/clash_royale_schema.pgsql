CREATE TABLE clan_member (
    id SERIAL PRIMARY KEY,
    tag VARCHAR(20) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    role VARCHAR(50) NOT NULL,
    trophies INTEGER NOT NULL,
    donations INTEGER NOT NULL,
    last_seen TIMESTAMP WITH TIME ZONE NOT NULL,
    join_date TIMESTAMP WITH TIME ZONE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_clan_member_tag ON clan_member (tag);
CREATE INDEX idx_clan_member_name ON clan_member (name);
CREATE INDEX idx_clan_member_role ON clan_member (role);
CREATE INDEX idx_clan_member_trophies ON clan_member (trophies);
CREATE INDEX idx_clan_member_donations ON clan_member (donations);
CREATE INDEX idx_clan_member_last_seen ON clan_member (last_seen);
CREATE INDEX idx_clan_member_join_date ON clan_member (join_date);